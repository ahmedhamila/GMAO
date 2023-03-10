import mysql.connector
from mysql.connector import Error


def getMagasinier(matriculeMagasinier):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='gmao_db',
                                            user='root',
                                            password='')
        if connection.is_connected():
            query = """select * from magasinier where matricule = %s """
            cursor = connection.cursor()
            cursor.execute(query,(matriculeMagasinier,))
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
