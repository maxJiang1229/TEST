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

    # sql = "SELECT * FROM study where ChemID = 1051 "
    # cur.execute(sql)
    # results = cur.fetchall()
    #
    # Species = []
    # Strain = []
    # Sex = []
    # Exposure_Time = []
    # StudyId = []
    # for row in results:
    #     StudyId.append(row[1])
    #     Species.append(row[2])
    #     Strain.append(row[3])
    #     Sex.append(row[4])
    #     Exposure_Time.append(row[5])
    #
    sql4798 = "SELECT * FROM observation where StudyID = 4798 "
    cur.execute(sql4798)
    results4798 = cur.fetchall()

    sql4799 = "SELECT * FROM observation where StudyID = 4799 "
    cur.execute(sql4799)
    results4799 = cur.fetchall()
    #
    # sql4800 = "SELECT * FROM observation where StudyID = 4800 "
    # cur.execute(sql4800)
    # results4800 = cur.fetchall()
    #
    # sql4801 = "SELECT * FROM observation where StudyID = 4801 "
    # cur.execute(sql4801)
    # results4801 = cur.fetchall()
    #
    # sql4802 = "SELECT * FROM observation where StudyID = 4802 "
    # cur.execute(sql4802)
    # results4802 = cur.fetchall()
    #
    # sql4803 = "SELECT * FROM observation where StudyID = 4803 "
    # cur.execute(sql4803)
    # results4803 = cur.fetchall()

    obsid1 = []
    tumourtpye1 = []
    tumoursit1 = []
    for row in results4798:
        obsid1.append(row[0])
        tumourtpye1.append(row[2])
        tumoursit1.append(row[3])

    print ('Dosee:%s, WithTumourss:%s' % (obsid1, tumourtpye1))

    obsid2 = []
    tumourtpye2 = []
    tumoursit2 = []
    for row in results4799:
        obsid2.append(row[0])
        tumourtpye2.append(row[2])
        tumoursit2.append(row[3])

    data1 = "SELECT * FROM doseresp where doseresp.ObsID = 46952 order by Dose "
    data2 = "SELECT * FROM doseresp where doseresp.ObsID = 46953 order by Dose "


    data3 = "SELECT * FROM doseresp where doseresp.ObsID = 37102 order by Dose "
    data4 = "SELECT * FROM doseresp where doseresp.ObsID = 37103 order by Dose "
    data5 = "SELECT * FROM doseresp where doseresp.ObsID = 42393 order by Dose "
    data6 = "SELECT * FROM doseresp where doseresp.ObsID = 46954 order by Dose "





    cur.execute(data1)
    resultdata1 = cur.fetchall()
    Dosee1 = []
    WithTumourss1 = []
    Dosee = []
    WithTumourss = []
    print (resultdata1)

    for row1 in resultdata1:
        Dosee.append(row1[2])
        WithTumourss.append(row1[5])

    print ('Dosee:%s, WithTumourss:%s' % (Dosee, WithTumourss))

    cur.execute(data2)
    resultdata2 = cur.fetchall()

    for row1 in resultdata2:
        Dosee1.append(row1[2])
        WithTumourss1.append(row1[5])


    plt.figure()
    plt.plot(Dosee, WithTumourss, color='red', linewidth=2.0, linestyle='--', label=tumourtpye1+["Female"])
    plt.plot(Dosee1, WithTumourss1, color='blue', linewidth=2.0, linestyle='-.', label=tumourtpye2+["Male"])
    plt.legend()
    plt.xlabel('Dose')
    plt.ylabel('WithTumours')
    # for x, y in zip(Dosee, WithTumourss):
    #     plt.text(x, y + 0.001, '%.0f' % y, ha='center', va='bottom')
    #
    # for x, y in zip(Dosee1, WithTumourss1):
    #     plt.text(x, y + 0.001, '%.0f' % y, ha='center', va='bottom')
    plt.show()
        #print ('Species:%s, Strain:%s, Sex:%s, Exposure_Time:%s'%(Species, Strain, Sex, Exposure_Time))
    # show = []
    # for i in range(0, len(Species)):
    #     if i + 1 < len(Species):
    #         if Species[i] == Species[i + 1]:
    #             if Strain[i] == Strain[i+1]:
    #                 if Sex[i] != Sex[i+1]:
    #                     if Exposure_Time[i] == Exposure_Time[i+1]:
    #                         show.append(StudyId[i])
    #                         show.append(StudyId[i+1])
    #                         break
    # print (show)

    # plt.figure()
    # bar = plt.bar(Dose, WithTumours, width=0.8)
    # plt.xlabel('Dose')
    # plt.ylabel('WithTumours')
    # #plt.title('test')
    #
    #
    #
    # for x, y in zip(Dose,WithTumours):
    #      plt.text(x, y+0.001, '%.0f' % y, ha='center', va='bottom')
    #
    # # 显示图表
    # plt.show()

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
    plt.plot(Dosee4, WithTumourss4, color='blue', linewidth=2.0, linestyle='--',label='Carcinoma- hepatocellular Female')

    plt.legend()
    plt.xlabel('Dose')
    plt.ylabel('WithTumours')
    # for x, y in zip(Dosee3, WithTumourss3):
    #     plt.text(x, y + 0.001, '%.0f' % y, ha='center', va='bottom')
    #
    # for x, y in zip(Dosee4, WithTumourss4):
    #     plt.text(x, y + 0.001, '%.0f' % y, ha='center', va='bottom')
    #
    # for x, y in zip(Dosee5, WithTumourss5):
    #     plt.text(x, y + 0.001, '%.0f' % y, ha='center', va='bottom')
    #
    # for x, y in zip(Dosee6, WithTumourss6):
    #     plt.text(x, y + 0.001, '%.0f' % y, ha='center', va='bottom')
    plt.show()

    data7 = "SELECT * FROM doseresp where doseresp.ObsID = 35930 order by Dose "
    data8 = "SELECT * FROM doseresp where doseresp.ObsID = 35931 order by Dose "
    data9 = "SELECT * FROM doseresp where doseresp.ObsID = 35932 order by Dose "
    data10 = "SELECT * FROM doseresp where doseresp.ObsID = 37104 order by Dose "

    cur.execute(data7)
    resultdata7 = cur.fetchall()
    cur.execute(data8)
    resultdata8 = cur.fetchall()
    cur.execute(data9)
    resultdata9 = cur.fetchall()
    cur.execute(data10)
    resultdata10 = cur.fetchall()
    Dosee7 = []
    WithTumourss7 = []
    Dosee8 = []
    WithTumourss8 = []
    Dosee9 = []
    WithTumourss9 = []
    Dosee10 = []
    WithTumourss10 = []

    for row1 in resultdata7:
        Dosee7.append(row1[2])
        WithTumourss7.append(row1[5])

    for row1 in resultdata8:
        Dosee8.append(row1[2])
        WithTumourss8.append(row1[5])

    for row1 in resultdata9:
        Dosee9.append(row1[2])
        WithTumourss9.append(row1[5])

    for row1 in resultdata10:
        Dosee10.append(row1[2])
        WithTumourss10.append(row1[5])

    plt.figure()
    plt.plot(Dosee7, WithTumourss7, color='red', linewidth=2.0, linestyle='--', label='Uterus')
    plt.plot(Dosee8, WithTumourss8, color='green', linewidth=2.0, linestyle='--', label='Vagina')
    plt.plot(Dosee9, WithTumourss9, color='blue', linewidth=2.0, linestyle='--', label='Ovary')
    plt.plot(Dosee10, WithTumourss10, color='black', linewidth=2.0, linestyle='--',label='Urinary bladder')

    plt.legend()
    plt.xlabel('Dose')
    plt.ylabel('WithTumours')
    plt.title('Sarcoma- reticulum cell; type A -- Female')
    # for x, y in zip(Dosee7, WithTumourss7):
    #     plt.text(x, y + 0.001, '%.0f' % y, ha='center', va='bottom')
    #
    # for x, y in zip(Dosee8, WithTumourss8):
    #     plt.text(x, y + 0.001, '%.0f' % y, ha='center', va='bottom')
    #
    # for x, y in zip(Dosee9, WithTumourss9):
    #     plt.text(x, y + 0.001, '%.0f' % y, ha='center', va='bottom')
    #
    # for x, y in zip(Dosee10, WithTumourss10):
    #     plt.text(x, y + 0.001, '%.0f' % y, ha='center', va='bottom')
    plt.show()


    plt.figure()
    plt.subplot(221)
    # plt.plot(Dosee7, WithTumourss7, color='red', linewidth=2.0, linestyle='--', label='Uterus')
    plt.bar(Dosee7, WithTumourss7, linewidth=2.0, label='Uterus')
    plt.xlabel('Dose')
    plt.ylabel('WithTumours')
    plt.legend()

    plt.subplot(222)
    # plt.plot(Dosee8, WithTumourss8, color='green', linewidth=2.0, linestyle='--', label='Vagina')
    plt.bar(Dosee8, WithTumourss8, linewidth=2.0, label='Vagina')
    plt.xlabel('Dose')
    plt.legend()

    plt.subplot(223)
    # plt.plot(Dosee9, WithTumourss9, color='blue', linewidth=2.0, linestyle='--', label='Ovary')
    plt.bar(Dosee9, WithTumourss9, linewidth=2.0, label='Ovary')
    plt.xlabel('Dose')
    plt.ylabel('WithTumours')
    plt.legend()

    plt.subplot(224)
    # plt.plot(Dosee10, WithTumourss10, color='black', linewidth=2.0, linestyle='--',label='Urinary bladder')
    plt.bar(Dosee10, WithTumourss10, linewidth=2.0, label='Urinary bladder')
    plt.legend()
    plt.xlabel('Dose')
    plt.show()



except pymysql.Error as e:
    print ("Connection failed" +str(e))
    db.rollback()

db.close()

#
# fig = plt.figure()
# bar = plt.bar(Dose, WithTumours, width=0.8)
# plt.xlabel('Dose')
# plt.ylabel('WithTumours')
# plt.title('test')
# for x, y in zip(Dose, WithTumours):
#     plt.text(x, y + 0.001, '%.0f' % y, ha='center', va='bottom')

