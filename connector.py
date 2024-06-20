import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7569459094")
mycurs = mydb.cursor()
#mycurs.execute("create database mydb")
#mycurs.execute("SHOW DATABASES")
mycurs.execute("create table users(name varchar(50),email varchar(50),password varchar(50)")
mycurs.execute("show tables")
for db in mycurs:
    print(db)