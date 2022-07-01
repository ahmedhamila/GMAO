
import mysql.connector
from mysql.connector import Error



def UserConnection(matricule, password):
    try:
            connection = mysql.connector.connect(host='localhost',
                                                database='gmao_db',
                                                user='root',
                                                password='')
            if connection.is_connected():
                query = """select * from users where matricule = %s and password = %s"""
                cursor = connection.cursor()
                cursor.execute(query,(matricule,password))
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
def UserList():
    try:
            connection = mysql.connector.connect(host='localhost',
                                                database='gmao_db',
                                                user='root',
                                                password='')
            if connection.is_connected():
                query = """select * from users"""
                cursor = connection.cursor()
                cursor.execute(query)
                record = cursor.fetchall()
                return record

    except Error as e:
            print("Error while connecting to MySQL", e)
    finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
def UserAdd(mat,passw,role):
    print(mat)
    print(passw)
    print(role)
    try:
            connection = mysql.connector.connect(host='localhost',
                                                database='gmao_db',
                                                user='root',
                                                password='')
            if connection.is_connected():
                sql = "INSERT INTO users(Matricule, Password, Role) VALUES(%s, %s, %s)"
                val = (mat,passw,role)
                cursor = connection.cursor()
                cursor.execute(sql,val)
                connection.commit()


    except Error as e:
            print("Error while connecting to MySQL", e)
    finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")