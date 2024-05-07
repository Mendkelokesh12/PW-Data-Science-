import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("insert into test2.test_table values(123,'Lokesh',234.5,245,'Mendke')")
mycursor.execute("insert into test2.test_table values(124,'Lokesh',234.5,245,'Mendke')")
mycursor.execute("insert into test2.test_table values(125,'Lokesh',234.5,245,'Mendke')")
mycursor.execute("insert into test2.test_table values(126,'Lokesh',234.5,245,'Mendke')")
mycursor.execute("insert into test2.test_table values(127,'Lokesh',234.5,245,'Mendke')")
mydb.commit()
mydb.close()