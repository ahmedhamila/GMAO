
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


def Registration(*args):
    try:
            connection = mysql.connector.connect(host='localhost',
                                                database='gmao_db',
                                                user='root',
                                                password='')

            if connection.is_connected():
                sql = "INSERT INTO users(Matricule, Password, Role) VALUES(%s, %s, %s)"
                val = (args[0],args[4],args[3])
                cursor = connection.cursor()
                cursor.execute(sql,val)
                if args[3]=="Magasinier":
                    sql = "INSERT INTO magasinier(Matricule, Nom, Prenom) VALUES(%s, %s, %s)"
                    val = (args[0],args[1],args[2])
                    cursor = connection.cursor()
                    cursor.execute(sql,val)
                    connection.commit()
                if args[3]=="Responsable Production":
                    sql = "INSERT INTO responsable_production(Matricule, Nom, Prenom) VALUES(%s, %s, %s)"
                    val = (args[0],args[1],args[2])
                    cursor = connection.cursor()
                    cursor.execute(sql,val)
                    connection.commit()
                if args[3]=="Agent Maintenance":
                    sql = "INSERT INTO agent_maintenance(Matricule, Nom, Prenom,Specialite,Age,Sexe,NiveauEducation,ExperienceProfessionnelle) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
                    val = (args[0],args[1],args[2],args[5],args[6],args[7],args[8],args[9])
                    cursor = connection.cursor()
                    cursor.execute(sql,val)
                    connection.commit()
                if args[3]=="Responsable Maintenance":

                    query = """select * from chaine_production where RefChaine = %s """
                    cursor = connection.cursor()
                    cursor.execute(query,(args[5],))
                    record = cursor.fetchall()
                    if len(record) == 1 :
                        sql = "INSERT INTO responsable_maintenance(Matricule, Nom, Prenom, RefChaine) VALUES(%s, %s, %s, %s)"
                        val = (args[0],args[1],args[2],args[5])
                        cursor = connection.cursor()
                        cursor.execute(sql,val)
                        connection.commit()
                        return 1
                    else:
                        return 0
                if args[3]=="Responsable Chaine Production":
                    query = "select * from chaine_production where RefChaine = %s "
                    cursor = connection.cursor()
                    cursor.execute(query,(args[5],))
                    record = cursor.fetchall()
                    if len(record) == 1 :
                        sql = "INSERT INTO responsable_chaine_production(Matricule, Nom, Prenom, RefChaine) VALUES(%s, %s, %s, %s)"
                        val = (args[0],args[1],args[2],args[5])
                        cursor = connection.cursor()
                        cursor.execute(sql,val)
                        connection.commit()
                        return 1
                    else:
                        return 0
                
    except Error as e:
            print("Error while connecting to MySQL", e)
    finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")



