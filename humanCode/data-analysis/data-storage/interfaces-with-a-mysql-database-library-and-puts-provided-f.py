# This connects to a mysql server and saves the first and last name

import os, mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="test",
        passwd="test",
        database="FIRST_NAME"
)
mycursor = mydb.cursor()

def register_name():
    fname = input("Enter the first name: ")
    lname = input("Enter the last name: ")

    t = (fname, lname)
    sql = "insert into names (fname, lname) values (%s, %s)"
    mycursor.execute(sql, t)
    mydb.commit()

register_name()
