import mysql.connector
from mysql.connector import Error


def getNotifications(matriculeRecepteur,type):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """select * from notification where Recepteur = %s and Type = %s """
            cursor = connection.cursor()
            cursor.execute(query,(matriculeRecepteur,type))
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

def getDemandeInterventionUntreated(matriculeRM):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """select * from demande_intervention where matricule_RM = %s and Status = %s"""
            cursor = connection.cursor()
            cursor.execute(query,(matriculeRM,"NonTraitee"))
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