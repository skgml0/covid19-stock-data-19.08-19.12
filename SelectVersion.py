import pymysql

connection = pymysql.connect(host='localhost', port=3306, db='INVESTAR',
    user='root', passwd='2355', autocommit=True)

cursor = connection.cursor()
cursor.execute("SELECT VERSION();")
result = cursor.fetchone()

print ("NAHEE MariaDB version : {}".format(result))

connection.close()