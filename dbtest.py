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



        cur.execute(StudyID)
        resultID = cur.fetchall()


        ChemID = []
        for row in resultID:
            ChemID.append(row[0])

        if ChemID:
            print (ChemID)
            print (len(ChemID))
        else:
            print("ID does not exist")

    except pymysql.Error as e:
        print ("Connection failed" + str(e))
        db.rollback()

    db.close()


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Text('id', key='-OUTPUT-')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

#
# chemid = vals1['-INPUT-']
#         StudyID = "SELECT StudyID FROM study where ChemID =" + chemid
#         cur.execute(StudyID)
#         resultID = cur.fetchall()
#
#         ChemID = []
#         for row in resultID:
#             ChemID.append(row[0])
#         if ChemID == "":
#             win1['-OUTPUT-'].update('does not exist')



# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == 'Ok':
        window.FindElement("-OUTPUT-").Update("fail")
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break



    searchId = values[0]

    connect(searchId)



    print('You entered ', values[0])

window.close()