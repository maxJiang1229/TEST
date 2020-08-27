# print ('ObsID:%s, TumourType:%s, Tumoursite:%s' % (Obsid, Tumourtype, Tumoursite))

# print ('StudyID:%s' % (Studyid))
# print ('Species:%s, Strain:%s, Sex:%s, Exposure_Time:%s, Experiment_Time:%s,Route:%s' % (
#   Species, Strain, Sex, Exposure_Time, Experiment_Time, Route))


import matplotlib
import pymysql
import matplotlib.pyplot as plt

try:
        DBHOST = '127.0.0.1'
        DBUSER = 'max'
        DBPASS = 'Jjy662500'
        DBNAME = 'carcdb'

        db = pymysql.connect(DBHOST, DBUSER, DBPASS, DBNAME)
        print("Connection succeeded")
        cur = db.cursor()

        # retrieve data

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
                        recoid.append(sameObsID[i+1])

            reid = list(set(recoid))

        print (len(reid))


        print (reid)
        data = []
        Dosee = []
        WithTumourss = []
        for i in range(0, len(reid)):
            if i + 1 < len(reid):
                data[i] = "SELECT * FROM doseresp where doseresp.ObsID = '" + str(reid[i]) + "' order by Dose "

                cur.execute(data[i])
                resultdata1 = cur.fetchall()
                for row1 in resultdata1:
                    Dosee.append(row1[2])
                    WithTumourss.append(row1[5])

                print ('Dosee:%s, WithTumourss:%s' % (Dosee, WithTumourss))

        data1 = "SELECT * FROM doseresp where doseresp.ObsID = '" + str(reid[0]) + "' order by Dose "
        data2 = "SELECT * FROM doseresp where doseresp.ObsID = '" + str(reid[1]) + "' order by Dose "

        cur.execute(data1)
        resultdata1 = cur.fetchall()

        for row1 in resultdata1:
            Dosee.append(row1[2])
            WithTumourss.append(row1[5])

        print ('Dosee:%s, WithTumourss:%s' % (Dosee, WithTumourss))

        print ('ObsID:%s, TumourType:%s, Tumoursite:%s' % (sameObsID, TumourType, TumourSite))


except pymysql.Error as e:
    print ("Connection failed" + str(e))
    db.rollback()

db.close()