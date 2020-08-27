import PySimpleGUI as sg
import pymysql
import matplotlib.pyplot as plt


def connect(chemname):
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

        Join = "select StudyID from chemident inner join study on chemident.ChemID=study.ChemID"


        join3table = "	SELECT study.Species, observation.TumourType, doseresp.Dose, doseresp.WithTumours FROM study INNER JOIN observation ON study.StudyID=observation.StudyID INNER JOIN doseresp ON observation.ObsID=doseresp.ObsID"
        cur.execute(join3table)
        join3t = cur.fetchall()

        StudyID1 = "SELECT StudyID FROM study where Strain = 'Alpk:APfSD' "
        cur.execute(StudyID1)
        resultID1 = cur.fetchall()
        ChemID1 = []
        for row in resultID1:
            ChemID1.append(row[0])
        print (ChemID1)

        cur.execute(Join)
        joinId = cur.fetchall()


        ChemCAS = "SELECT ChemID FROM chemident where chemident.Value = '"+ chemname + "'"


        cur.execute(ChemCAS)
        resultcas = cur.fetchall()

        Species = []
        TumourType = []
        Dose = []
        WithTumours = []
        for row in join3t:
            Species.append(row[0])
            TumourType.append(row[1])
            Dose.append(row[2])
            WithTumours.append(row[3])

        print ('Species:%s' % (Species))
        print (' TumourType:%s' % (TumourType))
        print ('Dose:%s' % (Dose))
        print ('WithTumours:%s' % (WithTumours))


        for row in resultcas:
            ChemID = row[0]
            print ('ChemID:%s' % (ChemID))

        Study = []
        for row in joinId:
            Study.append(row[0])
        # print ('Study:%s' % (Study))

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











    except pymysql.Error as e:
        print ("Connection failed" + str(e))
        db.rollback()

    db.close()


sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Enter something on Row 2'), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break

    searchId = values[0]

    print (type(searchId))

    connect(searchId)

    print('You entered ', values[0])

window.close()
