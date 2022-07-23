import mysql.connector

conn=mysql.connector.connect(user='root',password='P@assw0rd',host='127.0.0.1',database='info')

cursor=conn.cursor()

cursor.execute("DROP table if exists ABOUT")

sql=""" Create table ABOUT(
    id int  PRIMARY KEY NOT NULL AUTO_INCREMENT,
    Username char(20) NOT NULL,
    Password char(20) NOT NULL,
    Contact char(20) NOT NULL) AUTO_INCREMENT=1"""

cursor.execute(sql)

sql1 = "INSERT INTO ABOUT(Username,Password,Contact) VALUES ('admin','admin','9034215678')"
try:
    cursor.execute(sql1)
    conn.commit()
except:
    conn.rollback()
    print('not valid')
