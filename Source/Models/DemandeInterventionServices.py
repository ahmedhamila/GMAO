import mysql.connector
from mysql.connector import Error


def getDemandeIntervention(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """select * from demande_intervention where id = %s """
            cursor = connection.cursor()
            cursor.execute(query,(id,))
            record = cursor.fetchall()
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

def updateDemandeIntervention(record):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """update demande_intervention set Matricule_RCP = %s,Matricule_RM = %s,CodeEquipement = %s,Section = %s,DateLiberation = %s,Motif = %s ,Description= %s where id = %s"""
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

def getDemandeInterventionList(matriculeRCP):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """select * from demande_intervention where matricule_RCP = %s """
            cursor = connection.cursor()
            cursor.execute(query,(matriculeRCP,))
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

def getDemandeInterventionListRM(matriculeRM):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """select * from demande_intervention where matricule_RM = %s """
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


def addDemandeIntervention(record):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """insert into demande_intervention(Matricule_RCP,Matricule_RM,CodeEquipement,Section,DateLiberation,Motif,Description) values (%s,%s,%s,%s,%s,%s,%s) """
            
            print("######################################•")
            print(query,record)
            print("######################################•")
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

def deleteDemandeIntervention(ids):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """delete from demande_intervention where Id = %s"""
            for i in range(len(ids)-1):
                query+=" or Id = %s"
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