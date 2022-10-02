
import mysql.connector
from mysql.connector import Error

def getBonApproListRM(matriculeRM):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """select * from bon_approvisionnement where matricule_RM = %s """
            cursor = connection.cursor()
            cursor.execute(query,(matriculeRM,))
            record = cursor.fetchall()
            print(record)
            if len(record) >= 1 :
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

def getBonApproList():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """select * from bon_approvisionnement """
            cursor = connection.cursor()
            cursor.execute(query)
            record = cursor.fetchall()
            print(record)
            if len(record) >= 1 :
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

def updateBonTravail(record):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """update bon_approvisionnement set Matricule_RM = %s,Matricule_M = %s,DateLiberation = %s,Description = %s"""
            cursor = connection.cursor()
            print("######################################•")
            print(query,record)
            print("######################################•")
            cursor.execute(query,record)
            record = cursor.fetchall()
            print(cursor.rowcount)
            connection.commit()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def getBonApproListMG(matriculeMG):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """select * from bon_approvisionnement where Matricule_M = %s """
            cursor = connection.cursor()
            cursor.execute(query,(matriculeMG,))
            record = cursor.fetchall()
            print(record)
            if len(record) >= 1 :
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
