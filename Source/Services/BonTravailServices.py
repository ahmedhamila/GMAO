
import mysql.connector
from mysql.connector import Error


def getBonTravail(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """select * from bon_travail where id = %s """
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
def updateBonTravail(record):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """update bon_travail set Matricule_RM = %s,Matricule_AM = %s,Description = %s,Section = %s,type = %s,CodeEquipement = %s,RefDIM = %s,Frequence = %s,Active = %s where id = %s"""
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
def getBonTravailListRM(matriculeRM):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """select * from bon_travail where matricule_RM = %s """
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
def getBonTravailListAM(matriculeAM):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """select * from bon_travail where matricule_AM = %s """
            cursor = connection.cursor()
            cursor.execute(query,(matriculeAM,))
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
def getBonTravailListAll():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """select * from bon_travail """
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


def addBonTravail(record):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """insert into bon_travail(Matricule_RM,Matricule_AM,Description,Section,DateLiberation,type,CodeEquipement,RefDIM,Frequence,Active) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """
            
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
def deleteBonTravail(ids):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """delete from bon_travail where Id = %s"""
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

def getBonTravailDemandeInter(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """select * from bon_travail where RefDIM = %s """
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