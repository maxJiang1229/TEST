import PySimpleGUIQt as sg
#!/usr/bin/env python
# coding=utf-8
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
import pymysql
import matplotlib.pyplot as plt

#start connect db
DBHOST = '127.0.0.1'
DBUSER = 'max'
DBPASS = 'Jjy662500'
DBNAME = 'carcdb'

try:
    db = pymysql.connect( DBHOST, DBUSER, DBPASS, DBNAME)
    print("Connection succeeded")
    cur = db.cursor()

    #retrieve data

    sql = "SELECT * FROM doseresp where ObsID = 1160 "
    cur.execute(sql)
    results = cur.fetchall()

    Dose = []
    WithTumours = []
    for row in results:
        DoseRespID = row[0]
        ObsID = row[1]
        Dose.append(row[2])
        DoseUnit = row[3]
        TotalAnimals = row[4]
        WithTumours.append(row[5])


        print ('DoseRespID:%s, ObsID:%s, Dose:%s, DoseUnit:%s, TotalAnimals:%s,WithTumours:%s'%(DoseRespID, ObsID, Dose, DoseUnit, TotalAnimals,WithTumours))

    plt.figure()
    bar = plt.bar(Dose, WithTumours, width=0.8)
    plt.xlabel('Dose')
    plt.ylabel('WithTumours')
    #plt.title('test')



    for x, y in zip(Dose,WithTumours):
         plt.text(x, y+0.001, '%.0f' % y, ha='center', va='bottom')

    # 显示图表
    plt.show()




except pymysql.Error as e:
    print ("Connection failed" +str(e))
    db.rollback()

db.close()


#end connect db







# Design pattern 1 - First window does not remain active


# START OF MATPLOTLIB CODE
# fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
# t = np.arange(0, 3, .01)
# fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

fig = plt.figure()
bar = plt.bar(Dose, WithTumours, width=0.8)
plt.xlabel('Dose')
plt.ylabel('WithTumours')
plt.title('test')
for x, y in zip(Dose, WithTumours):
    plt.text(x, y + 0.001, '%.0f' % y, ha='center', va='bottom')

# ------------------------------- Beginning of Matplotlib helper code -----------------------
matplotlib.use('TkAgg')


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)


# define the window layout


layout1 = [[ sg.Text('Search ID'),],
          [sg.InputText(key='-INPUT-')],
          [sg.Button('OK'), sg.Button('Cancel')]
          ]

win1 = sg.Window('Search Information', layout1)

win2_active=False
while True:
    ev1, vals1 = win1.read(timeout=100)
    if ev1 == 'OK':
        print('You input', vals1['-INPUT-'])
    if ev1 == sg.WIN_CLOSED or ev1 == 'Cancel':
        break



    if ev1 == 'OK'  and not win2_active:
        win2_active = True
        win1.Hide()
        layout3 = plt.show()
        layout2 = [[sg.Text('Plot test')],
                   [sg.Canvas(key='-CANVAS-')],
                   [sg.Button('Exit')]]



        win2 = sg.Window('Matplotlib Single Graph', layout2, finalize=True, element_justification='center', font='Helvetica 18')

        draw_figure(win2['-CANVAS-'].TKCanvas, fig)

        while True:
            ev2, vals2 = win2.read()
            if ev2 == sg.WIN_CLOSED or ev2 == 'Exit':
                win2_active = False
                win2.close()
                break


