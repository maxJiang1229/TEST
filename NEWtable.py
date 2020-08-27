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


    sqlstudy = "SELECT * FROM study where StudyID = 4800"

    sqlobser = "SELECT * FROM observation where ObsID = 37102 "

    sql = "SELECT * FROM doseresp where ObsID = 37102 "

    cur.execute(sqlstudy)
    result1 = cur.fetchall()

    cur.execute(sqlobser)
    result2 = cur.fetchall()

    cur.execute(sql)
    results = cur.fetchall()



    list1 = []
    for row in result1:
        Species = row[2]
        Strain = row[3]
        Sex = row[4]
        Exposure_Time = row[5]
        Experiment_Time = row[7]
        Route = row[9]

        list1.append(row[2])
        list1.append(row[3])
        list1.append(row[4])
        list1.append(row[5])
        list1.append(row[7])
        list1.append(row[9])





        print ('Species:%s, Strain:%s, Sex:%s, Exposure_Time:%s, Experiment_Time:%s,Route:%s'%(Species, Strain, Sex, Exposure_Time, Experiment_Time,Route))

        #print (list1)


    for row in result2:
        TumourType = row[2]
        TumourSite = row[3]
        TD50_Gold = row[7]
        TD50_Lhasa = row[8]

        list1.append(row[2])
        list1.append(row[3])
        list1.append(row[7])
        list1.append(row[8])

        #print (list1)



        print ('TumourType:%s, TumourSite:%s, TD50_Gold:%s, TD50_Lhasa:%s'%(TumourType, TumourSite, TD50_Gold, TD50_Lhasa))




    Dose = []
    WithTumours = []
    for row in results:
        DoseRespID = row[0]
        ObsID = row[1]
        Dose.append(row[2])
        DoseUnit = row[3]
        TotalAnimals = row[4]
        WithTumours.append(row[5])


        #print ('DoseRespID:%s, ObsID:%s, Dose:%s, DoseUnit:%s, TotalAnimals:%s,WithTumours:%s'%(DoseRespID, ObsID, Dose, DoseUnit, TotalAnimals,WithTumours))

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

