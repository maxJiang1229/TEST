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

Dosee1 = []
WithTumourss1 = []
Dosee = []
WithTumourss = []
DoseT = []
WithTumoursT = []
DoseT1 = []
WithTumoursT1 = []
DoseT2 = []
WithTumoursT2 = []
DoseT3 = []
WithTumoursT3 = []
DoseT4 = []
WithTumoursT4 = []
printType = ''



def connectchemident(CAS, Species,Strain):

    #connectdatabase
    db = pymysql.connect(DBHOST, DBUSER, DBPASS, DBNAME)
    print("Connection succeeded")
    cur = db.cursor()


    #Find the ChemID corresponding to the specified cas in the chemident table
    ChemCAS = "SELECT ChemID FROM chemident where chemident.Value = '" + CAS + "'"
    cur.execute(ChemCAS)
    resultCAS = cur.fetchall()

    #get ChemID
    ChemID = []
    for row in resultCAS:
        ChemID = row[0]



    #sql statement. Select the corresponding studyid from the study table
    StudyID = "SELECT * FROM study where study.ChemID = '" + ChemID + "' and Species = '" + Species + "' and Strain = '" + Strain + "'"





    cur.execute(StudyID)
    resultsdID = cur.fetchall()

    Studyid = []
    Exposure_Time = []

    #Cyclic study information to the specified chemid
    for row in resultsdID:
        Studyid.append(row[1])
        #Sex = row[4]
        Exposure_Time.append(row[5])
        #Experiment_Time = row[7]


    #Determine whether cas exists
    if Studyid:
        print ('Studyid:%s' % (Studyid))
    else:
        print("CAS does not exist")
        return 0




    #Get some data
    show_stid = []
    for i in range(0,len(Exposure_Time)):
        if i + 1 < len(Exposure_Time):
            if Exposure_Time[i] == Exposure_Time[i + 1]:
                show_stid.append(Studyid[i])
                show_stid.append(Studyid[i+1])


    Obsid = []
    Tumourtype = []
    Tumoursite = []
    #Obtain obsid and type and location from the observation table
    for i in range(0, len(show_stid)):
        ObsID = "SELECT observation.ObsID, observation.TumourType, observation.TumourSite FROM observation where observation.StudyID = '" + str(show_stid[i]) + "'"
        cur.execute(ObsID)
        resultobsid = cur.fetchall()


        for row in resultobsid:
            Obsid.append(row[0])
            Tumourtype.append(row[1])
            Tumoursite.append(row[2])

    Obsid1 = "SELECT * FROM observation where observation.StudyID = 4802 "
    cur.execute(Obsid1)
    retobsid = cur.fetchall()

    TumourSite = []
    TumourType = []
    sameObsID = []
    recoid = []

    for row in retobsid:
        sameObsID.append(row[0])
        TumourType.append(row[2])
        TumourSite.append(row[3])

        for i in range(0, len(TumourType)):
            if i + 1 < len(TumourType):
                if TumourType[i] == TumourType[i + 1]:
                    recoid.append(sameObsID[i])
                    recoid.append(sameObsID[i + 1])
                    printType = TumourType[i]

        reid = list(set(recoid))

    datasameT1 = "SELECT * FROM doseresp where doseresp.ObsID = '" + str(reid[0]) + "' order by Dose "
    cur.execute(datasameT1)
    redata1 = cur.fetchall()

    for row1 in redata1:
        DoseT.append(row1[2])
        WithTumoursT.append(row1[5])

    print ('Dosee:%s, WithTumourss:%s' % (DoseT, WithTumoursT))

    datasameT2 = "SELECT * FROM doseresp where doseresp.ObsID = '" + str(reid[1]) + "' order by Dose "
    cur.execute(datasameT2)
    redata2 = cur.fetchall()

    for row1 in redata2:
        DoseT1.append(row1[2])
        WithTumoursT1.append(row1[5])

    print ('Dosee1:%s, WithTumourss1:%s' % (DoseT1, WithTumoursT1))

    datasameT3 = "SELECT * FROM doseresp where doseresp.ObsID = '" + str(reid[2]) + "' order by Dose "
    cur.execute(datasameT3)
    redata3 = cur.fetchall()

    for row1 in redata3:
        DoseT2.append(row1[2])
        WithTumoursT2.append(row1[5])

    print ('Dosee2:%s, WithTumourss2:%s' % (DoseT2, WithTumoursT2))

    datasameT4 = "SELECT * FROM doseresp where doseresp.ObsID = '" + str(reid[3]) + "' order by Dose "
    cur.execute(datasameT4)
    redata4 = cur.fetchall()

    for row1 in redata4:
        DoseT3.append(row1[2])
        WithTumoursT3.append(row1[5])

    print ('Dosee3:%s, WithTumourss3:%s' % (DoseT3, WithTumoursT3))



    print ('ObsID:%s, TumourType:%s, Tumoursite:%s' % (sameObsID, TumourType, TumourSite))


    #Get response information from doesresp table
    data1 = "SELECT * FROM doseresp where doseresp.ObsID = '" + str(Obsid[0]) + "' order by Dose "
    data2 = "SELECT * FROM doseresp where doseresp.ObsID = '" + str(Obsid[1]) + "' order by Dose "

    data3 = "SELECT * FROM doseresp where doseresp.ObsID = 37102 order by Dose "
    data4 = "SELECT * FROM doseresp where doseresp.ObsID = 37103 order by Dose "
    data5 = "SELECT * FROM doseresp where doseresp.ObsID = 42393 order by Dose "
    data6 = "SELECT * FROM doseresp where doseresp.ObsID = 46954 order by Dose "

    cur.execute(data1)
    resultdata1 = cur.fetchall()

    for row1 in resultdata1:
        Dosee.append(row1[2])
        WithTumourss.append(row1[5])

    print ('Dosee:%s, WithTumourss:%s' % (Dosee, WithTumourss))

    cur.execute(data2)
    resultdata2 = cur.fetchall()


    for row1 in resultdata2:
        Dosee1.append(row1[2])
        WithTumourss1.append(row1[5])

    print ('Dosee1:%s, WithTumourss1:%s' % (Dosee1, WithTumourss1))


    plt.plot(Dosee, WithTumourss, color='red', linewidth=2.0, linestyle='--', label=[Tumourtype[0]])
    plt.plot(Dosee1, WithTumourss1, color='blue', linewidth=2.0, linestyle='-.', label=[Tumourtype[1]])
    plt.legend()
    plt.xlabel('Dose')
    plt.ylabel('WithTumours')
    for x, y in zip(Dosee, WithTumourss):
        plt.text(x, y + 0.001, '%.0f' % y, ha='center', va='bottom')

    for x, y in zip(Dosee1, WithTumourss1):
        plt.text(x, y + 0.001, '%.0f' % y, ha='center', va='bottom')



    plt.figure()
    plt.plot(DoseT, WithTumoursT, color='red', linewidth=2.0, linestyle='--', label='Urinary bladder')
    plt.plot(DoseT1, WithTumoursT1, color='green', linewidth=2.0, linestyle='--', label='Uterus')
    plt.plot(DoseT2, WithTumoursT2, color='blue', linewidth=2.0, linestyle='--', label='Vagina')
    plt.plot(DoseT3, WithTumoursT3, color='black', linewidth=2.0, linestyle='--',label='Ovary')
    plt.legend()
    plt.xlabel('Dose')
    plt.ylabel('WithTumours')
    plt.title(printType)



    cur.execute(data3)
    resultdata3 = cur.fetchall()
    Dosee3 = []
    WithTumourss3 = []
    Dosee4 = []
    WithTumourss4 = []

    for row1 in resultdata3:
        Dosee3.append(row1[2])
        WithTumourss3.append(row1[5])

    print ('Dosee:%s, WithTumourss:%s' % (Dosee3, WithTumourss3))

    cur.execute(data4)
    resultdata4 = cur.fetchall()

    for row1 in resultdata4:
        Dosee4.append(row1[2])
        WithTumourss4.append(row1[5])

    cur.execute(data5)
    resultdata5 = cur.fetchall()
    Dosee5 = []
    WithTumourss5 = []
    Dosee6 = []
    WithTumourss6 = []

    for row1 in resultdata5:
        Dosee5.append(row1[2])
        WithTumourss5.append(row1[5])

    print ('Dosee:%s, WithTumourss:%s' % (Dosee5, WithTumourss5))

    cur.execute(data6)
    resultdata6 = cur.fetchall()

    for row1 in resultdata6:
        Dosee6.append(row1[2])
        WithTumourss6.append(row1[5])

    plt.figure()
    plt.plot(Dosee3, WithTumourss3, color='red', linewidth=2.0, linestyle='--', label='Adenoma- hepatocellular Female')
    plt.plot(Dosee5, WithTumourss5, color='red', linewidth=2.0, linestyle=':', label='Adenoma- hepatocellular Male')
    plt.plot(Dosee6, WithTumourss6, color='blue', linewidth=2.0, linestyle=':', label='Carcinoma- hepatocellular Male')
    plt.plot(Dosee4, WithTumourss4, color='blue', linewidth=2.0, linestyle='--',
             label='Carcinoma- hepatocellular Female')

    plt.legend()
    plt.xlabel('Dose')
    plt.ylabel('WithTumours')
    plt.show()


    db.close()





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

comb_list = ['Cynomolgus monkey',  'Dog', 'Hamster', 'Mouse', 'Rat', 'Rhesus monkey', 'Syrian hamster', 'Tree shrew']

strain_list = ['Fischer 344', '(C3H x RIII)F1 (MTV+)', '(C57BL/6 x BALB/c)F1', 'A', 'A/He', 'ACI', 'ACI/n', 'AKR', 'Alderly Park', 'Alpk:APfSD',
               'B6AKF1', 'B6C3F1', 'B6C3F1/N', 'B6C3F2 br', 'B6C3F2 ph', 'BALB/c', 'BALB/cHe', 'BALB/cStCrlfC3Hf/Nctr', 'BD VI', 'Beagle', 'BR 46',
               'Buffalo', 'C.B. hooded', 'C3H (MTV+)', 'C3H/AnCum', 'C3H/FIB', 'C3H/He (MTV+)','C3H/HeN-MTV-/Nctr (MTV-)','C3H/St (MTV+)','C3HeB/FeJ',
               'C3HfB', 'C57BL', 'C57BL/10J', 'C57BL/6', 'C57BL/6N', 'C57BL/BVI', 'C57BL/He', 'C57L','C57L/He x 129/Rr x C3HeB/De x SWR/Ly','Cb/Sc',
               'CBA x C57BL', 'CBA/Cb/Se','CD1', 'CD-1 HaM/ICR', 'CF-1','CFLP','CFN','Cpb:Swiss random','Crj:BDF1','D2B6F1','DBA/2', 'Donryu','Fischer 344',
               'Fischer 344/DuCrj','Fischer 344/Jcl','Fischer 344/NTac', 'Fischer 344/Tox','FVB/N hemizygous', 'Ha/ICR', 'Harlan','Holtzman','HRA/Skh',
               'ICR','ICR/Jcl','Lewis','Long-Evans','Long-Evans BLU:(LE)','MMTV/NEU (Tg.Nk)','Monohybrid cross offspring of B6CF1','MRC Porton','NMRI',
               'Not specified','OF1','OFA','Osborne-Mendel','RIII (MTV+)','Slc-Wistar','Spartan','Sprague-Dawley','Swiss','Swiss Webster','Swiss/NIH',
               'TM','WAG','Wistar','Wistar Han','Wistar/LAC-P','Wistar-OSU',''
               ]


layout1 = [[ sg.Text('Search ChemCAS ', size=(15, 1)),sg.InputText(key='-INPUT-', size=(27, 1))],
           [sg.Text('Species ', size=(15, 1)), sg.Combo(comb_list, size=(25, 1), key='-Species-')],
           [sg.Text('Strain ', size=(15, 1)), sg.Combo(strain_list, size=(25, 1), key='-Strain-')],
           [sg.Text('FEEDBACK', key='-OUTPUT-', size=(40,1))],
          [sg.Button('OK'), sg.Button('Reset'), sg.Button('Cancel')]
          ]

win1 = sg.Window('Search Information', layout1)
win2_active=False
while True:
    ev1, vals1 = win1.read(timeout=100)
    if ev1 == 'OK':
        print('You input', vals1['-INPUT-'], vals1['-Species-'],vals1['-Strain-'])
    if ev1 == 'Reset':
        win1.FindElement("-INPUT-").Update("")
        win1.FindElement("-OUTPUT-").Update("FEEDBACK")
    if ev1 == sg.WIN_CLOSED or ev1 == 'Cancel':
        break



    # define the window layout
    if ev1 == 'OK' and not win2_active:
        get = connectchemident(vals1['-INPUT-'],vals1['-Species-'],vals1['-Strain-'])
        if get == 0:
            win1.FindElement("-OUTPUT-").update('Not found')
        else:
            win2_active = True
            layout2 = [[sg.Text('The relationship between dose and withtumours', font='Any 18')],
                    [sg.Canvas(size=(figure_w, figure_h), key='canvas')],
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