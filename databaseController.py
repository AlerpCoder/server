import os, sys, sqlite3

connection = sqlite3.connect("./tempData.db")
cursor = connection.cursor()

#create database
cursor.execute('''create table if not exists running (date text, temperatur integer, humadity integer)''')
