import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="75694590094",database="mydb")
mycurs = mydb.cursor()
print(mycurs)

#mycurs.execute("create database class")
#mycurs.execute("SHOW DATABASES")
#mycurs.execute("create table users(name varchar(50),email varchar(50),password varchar(50))")
#sql="insert into users (name,email,password) values(%s,%s,%s)"

#mycurs.execute(sql,val)
#mycurs.execute("show tables");
#for db in mycurs:
    #print(db)
#mycurs.execute("show tables");
mycurs.execute("select * from users")
#for x in mycurs:
    #print(x)
