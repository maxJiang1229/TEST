#!/usr/bin/env python
import PySimpleGUI as sg
import random
import string
import pymysql
import matplotlib.pyplot as plt

"""
    Basic use of the Table Element
"""


def connect():
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

        sqlstudy = "SELECT * FROM study where StudyID = 26"

        sqlobser = "SELECT * FROM observation where ObsID = 5 "

        #sql = "SELECT * FROM doseresp where ObsID = 5 "

        cur.execute(sqlstudy)
        result1 = cur.fetchall()

        cur.execute(sqlobser)
        result2 = cur.fetchall()

        listcol = []

        for row in result1:
            Species = row[2]
            Strain = row[3]
            Sex = row[4]
            Exposure_Time = row[5]
            Experiment_Time = row[7]
            Route = row[9]

            listcol.append(row[2])
            listcol.append(row[3])
            listcol.append(row[4])
            listcol.append(row[5])
            listcol.append(row[7])
            listcol.append(row[9])

            print ('Species:%s, Strain:%s, Sex:%s, Exposure_Time:%s, Experiment_Time:%s,Route:%s' % (
            Species, Strain, Sex, Exposure_Time, Experiment_Time, Route))

        for row in result2:
            TumourType = row[2]
            TumourSite = row[3]
            TD50_Gold = row[7]
            TD50_Lhasa = row[8]

            listcol.append(row[2])
            listcol.append(row[3])
            listcol.append(row[7])
            listcol.append(row[8])

            print (listcol)

            print ('TumourType:%s, TumourSite:%s, TD50_Gold:%s, TD50_Lhasa:%s' % (
            TumourType, TumourSite, TD50_Gold, TD50_Lhasa))




    except pymysql.Error as e:
        print ("Connection failed" + str(e))
        db.rollback()

    db.close()

    return listcol

# ------ Some functions to help generate data for the table ------

listrow = ['Species', 'Strain', 'Sex', 'Exposure_Time', 'Experiment_Time', 'Route', 'TumourType', 'TumourSite', 'TD50_Gold', 'TD50_Lhasa']


def word():

    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    #return ','.join(listrow)
def number(max_val=1000):
    return random.randint(0, max_val)
    #return connect()



def wordrow():
    return connect()

data1 = wordrow()
print (data1)
print (type(data1))

def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [word() for __ in range(num_cols)]
    print (type(data[0]))
    for i in range(1, num_rows):
        data[i] = [word(), *[data1 for i in range(num_cols-1)]]
    return data

# ------ Make the Table Data ------
data = make_table(num_rows=2, num_cols=10)
heading = ['Species', 'Strain', 'Sex', 'Exposure_Time', 'Experiment_Time', 'Route', 'TumourType', 'TumourSite', 'TD50_Gold', 'TD50_Lhasa']


# ------ Window Layout ------
layout = [[sg.Table(values=data[1:][:],
                    headings=heading,
                    max_col_width=25,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=20,
                    key='-TABLE-',
                    row_height=35 )],
          [sg.Button('RETURN')]]

# ------ Create Window ------
window = sg.Window('The Table Element', layout )

# ------ Event Loop ------
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
window.close()