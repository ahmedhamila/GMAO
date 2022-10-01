import mysql.connector
from mysql.connector import Error

def getEquipements():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = "select * from equipement "
            cursor = connection.cursor()
            cursor.execute(query)
            record = cursor.fetchall()
            print(record)
            if len(record) >0 :
                return True,record
            else :
                return False,False

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def getEquipement(code):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = "select * from equipement where Reference = %s"
            cursor = connection.cursor()
            cursor.execute(query,(code,))
            record = cursor.fetchall()
            print(record)
            if len(record) >0 :
                return True,record
            else :
                return False,False

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def deleteEquipement(ids):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """delete from equipement where Reference = %s"""
            for i in range(len(ids)-1):
                query+=" or Reference = %s"
            cursor = connection.cursor()
            print(query,tuple(ids))
            cursor.execute(query,tuple(ids))
            print(cursor.rowcount)
            connection.commit()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")