import PySimpleGUI as sg
import pymysql
import matplotlib.pyplot as plt



def connect(chemid):
    # start connect db
    DBHOST = '127.0.0.1'
    DBUSER = 'max'
    DBPASS = 'Jjy662500'
    DBNAME = 'carcdb'

    try:
        db = pymysql.connect(DBHOST, DBUSER, DBPASS, DBNAME)
        print("Connection succeeded")
        cur = db.cursor()

        # retrieve data

        StudyID = "SELECT StudyID FROM study where ChemID =" + chemid

        StudyID1 = "SELECT StudyID FROM study where Strain = 'Alpk:APfSD' "


        cur.execute(StudyID)
        resultID = cur.fetchall()
        cur.execute(StudyID1)
        resultID1 = cur.fetchall()


        # Dose = []
        # WithTumours = []
        # for row in results:
        #     DoseRespID = row[0]
        #     ObsID = row[1]
        #     Dose.append(row[2])
        #     DoseUnit = row[3]
        #     TotalAnimals = row[4]
        #     WithTumours.append(row[5])
        #
        #     print ('DoseRespID:%s, ObsID:%s, Dose:%s, DoseUnit:%s, TotalAnimals:%s,WithTumours:%s' % (
        #     DoseRespID, ObsID, Dose, DoseUnit, TotalAnimals, WithTumours))



        ChemID = []
        for row in resultID:
            ChemID.append(row[0])

        ChemID1 = []
        for row in resultID1:
            ChemID1.append(row[0])
        print (ChemID1)


        for i in ChemID:
            cid = str(i)

            obsIid = "SELECT ObsID FROM observation where StudyID =" + cid

            cur.execute(obsIid)
            resultsObsID = cur.fetchall()



            for row in resultsObsID:
                ObsID=row[0]
                print ('ObsID:%s' % (ObsID))

                # le = len(resultsObsID)
                #
                # print ('fgsfdg',type(le),le)


                barchart = "SELECT * FROM doseresp where ObsID =" + str(ObsID)
                cur.execute(barchart)
                resultsbar = cur.fetchall()

                Dose = []
                WithTumours = []
                for row in resultsbar:
                    Dose.append(row[2])
                    DoseUnit = row[3]
                    TotalAnimals = row[4]
                    WithTumours.append(row[5])
                    print ('Dose:%s, DoseUnit:%s, TotalAnimals:%s,WithTumours:%s' % (Dose, DoseUnit, TotalAnimals, WithTumours))





        plt.figure()
        bar = plt.bar(Dose, WithTumours, width=0.8)
        plt.xlabel('Dose')
        plt.ylabel('WithTumours')
        # plt.title('test')

        for x, y in zip(Dose, WithTumours):
            plt.text(x, y + 0.001, '%.0f' % y, ha='center', va='bottom')

        # 显示图表
        plt.show()




    except pymysql.Error as e:
        print ("Connection failed" + str(e))
        db.rollback()

    db.close()


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]


# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    searchId = values[0]

    connect(searchId)

    print('You entered ', values[0])

window.close()