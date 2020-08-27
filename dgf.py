#!/usr/bin/env python
import PySimpleGUI as sg

import matplotlib
import pymysql

matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


import matplotlib.pyplot as plt


#start connect db
DBHOST = '127.0.0.1'
DBUSER = 'max'
DBPASS = 'Jjy662500'
DBNAME = 'carcdb'

def connectchemident(CAS):
    db = pymysql.connect(DBHOST, DBUSER, DBPASS, DBNAME)
    print("Connection succeeded")
    cur = db.cursor()

    ChemCAS = "SELECT ChemID FROM chemident where chemident.Value = '" + CAS + "'"
    cur.execute(ChemCAS)
    resultCAS = cur.fetchall()

    ChemID = []
    for row in resultCAS:
        ChemID = row[0]
    if ChemID:
        print ('ChemCAS:%s' % (ChemID))
    else:
        print("CAS does not exist")
        return 0

    StudyID = "SELECT StudyID FROM study where study.ChemID = '" + ChemID + "'"

    cur.execute(StudyID)
    resultsdID = cur.fetchall()

    Studyid = []
    for row in resultsdID:
        Studyid.append(row[0])

    print ('StudyID:%s' % (Studyid))


try:
    db = pymysql.connect( DBHOST, DBUSER, DBPASS, DBNAME)
    print("Connection succeeded")
    cur = db.cursor()

    #retrieve data

    sql1 = "SELECT * FROM doseresp where ObsID = 37102"
    sql2 = "SELECT * FROM doseresp where ObsID = 37103"

    sqlstudy = "SELECT * FROM study where StudyID = 4800"

    sqlobser = "SELECT * FROM observation where ObsID = 37102 "
    sqlobser1 = "SELECT * FROM observation where ObsID = 37103 "



    cur.execute(sql1)
    result1 = cur.fetchall()
    cur.execute(sql2)
    result2 = cur.fetchall()

    cur.execute(sqlstudy)
    result3 = cur.fetchall()

    cur.execute(sqlobser)
    result4 = cur.fetchall()

    cur.execute(sqlobser1)
    result5 = cur.fetchall()




    Dose1 = []
    WithTumours1 = []
    for row1 in result1:
        DoseRespID1 = row1[0]
        ObsID1 = row1[1]
        Dose1.append(row1[2])
        DoseUnit1 = row1[3]
        TotalAnimals1 = row1[4]
        WithTumours1.append(row1[5])
        #print ('DoseRespID1:%s, ObsID1:%s, Dose1:%s, DoseUnit1:%s, TotalAnimals1:%s,WithTumours1:%s'%(DoseRespID1, ObsID1, Dose1, DoseUnit1, TotalAnimals1,WithTumours1))


    # layout1 = plt.figure()
    # bar = plt.bar(Dose1, WithTumours1, width=0.8)
    # plt.xlabel('Dose')
    # plt.ylabel('WithTumours')




    Dose2 = []
    WithTumours2 = []
    for row in result2:
        DoseRespID2 = row[0]
        ObsID2 = row[1]
        Dose2.append(row[2])
        DoseUnit2 = row[3]
        TotalAnimals2 = row[4]
        WithTumours2.append(row[5])

        #print ('DoseRespID:%s, ObsID:%s, Dose:%s, DoseUnit:%s, TotalAnimals:%s,WithTumours:%s' % (DoseRespID2, ObsID2, Dose2, DoseUnit2, TotalAnimals2, WithTumours2))

    layout2 = plt.figure()
    bar = plt.bar(Dose2, WithTumours2, width=0.8)
    plt.xlabel('Dose')
    plt.ylabel('WithTumours')
    plt.title('test')




    #plt.show()

    for x, y in zip(Dose1,WithTumours1):
         plt.text(x, y+0.001, '%.0f' % y, ha='center', va='bottom')

    print('finish')
    # 显示图表
    #plt.show()


    for row in result3:
        Species = row[2]
        Strain = row[3]
        Sex = row[4]
        Exposure_Time = row[5]
        Experiment_Time = row[7]
        Route = row[9]

        print ('Species:%s, Strain:%s, Sex:%s, Exposure_Time:%s, Experiment_Time:%s,Route:%s' % (
        Species, Strain, Sex, Exposure_Time, Experiment_Time, Route))

    for row in result4:
        TumourType = row[2]
        TumourSite = row[3]
        TD50_Gold = row[7]
        TD50_Lhasa = row[8]

        print ('TumourType:%s, TumourSite:%s, TD50_Gold:%s, TD50_Lhasa:%s' % (
        TumourType, TumourSite, TD50_Gold, TD50_Lhasa))

    for row in result5:
        TumourType = row[2]
        TumourSite = row[3]
        TD50_Gold = row[7]
        TD50_Lhasa = row[8]

        print ('TumourType:%s, TumourSite:%s, TD50_Gold:%s, TD50_Lhasa:%s' % (
        TumourType, TumourSite, TD50_Gold, TD50_Lhasa))



except pymysql.Error as e:
    print ("Connection failed" +str(e))
    db.rollback()




# plot with various axes scales
plt.figure(1)


# ObsID = 37102
plt.subplot(121)
plt.bar(Dose1, WithTumours1, width=0.8)
plt.xlabel('Dose')
plt.ylabel('WithTumours')
plt.title('ObsID = 37102')
for x, y in zip(Dose1, WithTumours1):
    plt.text(x, y + 0.001, '%.0f' % y, ha='center', va='bottom')


# ObsID = 37103
ax = plt.subplot(122)
plt.bar(Dose2, WithTumours2, width=0.8)
plt.xlabel('Dose')
ax.yaxis.tick_right()
plt.title('ObsID = 37103')
for x, y in zip(Dose2, WithTumours2):
    plt.text(x, y + 0.001, '%.0f' % y, ha='center', va='bottom')


fig = plt.gcf()  # if using Pyplot then get the figure from the plot
figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds


matplotlib.use('TkAgg')

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def delete_figure_agg(figure_agg):
    figure_agg.get_tk_widget().forget()
    plt.close('all')


# ------------------------------- Beginning of GUI CODE -------------------------------


layout1 = [[ sg.Text('Search ChemCAS')],[sg.InputText(key='-INPUT-')],
           [sg.Text('FEEDBACK', key='-OUTPUT-', size=(40,1))],
          [sg.Button('OK'), sg.Button('Reset'), sg.Button('Cancel')]
          ]

win1 = sg.Window('Search Information', layout1)
win2_active=False
while True:
    ev1, vals1 = win1.read(timeout=100)
    if ev1 == 'OK':
        print('You input', vals1['-INPUT-'])
    if ev1 == 'Reset':
        win1.FindElement("-INPUT-").Update("")
        win1.FindElement("-OUTPUT-").Update("FEEDBACK")
    if ev1 == sg.WIN_CLOSED or ev1 == 'Cancel':
        break



    # define the window layout
    if ev1 == 'OK' and not win2_active:
        get = connectchemident(vals1['-INPUT-'])
        if get == 0:
            win1.FindElement("-OUTPUT-").update('ChemCAS '+vals1['-INPUT-'] + ' does not exist')
        else:
            win2_active = True
            layout2 = [[sg.Text('Plot test', font='Any 18')],
                    [sg.Canvas(size=(figure_w, figure_h), key='canvas')],
                    # [sg.Button('More Infor', pad=((figure_w / 2, 0), 3))],
                    # [sg.Button('Exit', pad=((figure_w / 2, 0), 3))],
                    [sg.Button('Exit'), sg.Button('More Infor')]]

# create the form and show it without the plot
            win2 = sg.Window('Demo Application - Embedding Matplotlib In PySimpleGUI', layout2, finalize=True)

# add the plot to the window
            fig_canvas_agg = draw_figure(win2['canvas'].TKCanvas, fig)

            while True:
                ev2, vals2 = win2.read()
                if ev2 == sg.WIN_CLOSED or ev2 == 'Exit':
                    win2_active = False
                    win2.close()
                    break


db.close()