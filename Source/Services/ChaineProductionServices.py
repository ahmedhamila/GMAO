import mysql.connector
from mysql.connector import Error


def getChaineProduction():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """select * from chaine_production """
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


def getResponsableChaineProduction(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """select * from responsable_chaine_production where Matricule=%s """
            cursor = connection.cursor()
            cursor.execute(query,(id))
            record = cursor.fetchall()
            print(record)
            if len(record) == 1 :
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
def addChaineProduction(record):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            
            query = """insert into chaine_production(RefChaine,NbEquipement) values (%s,%s) """
            print("######################################???")
            print(query,record)
            print("######################################???")
            cursor = connection.cursor()
            cursor.execute(query,record)
            print(cursor.rowcount)
            connection.commit()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")