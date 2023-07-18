
import mysql.connector
from mysql.connector import errorcode

class App:
    
    def __init__(self):
        self.user='cron'
        self.pwd='password'
        self.db='app'
        try:
            self.cnx = mysql.connector.connect(user=self.user, password=self.pwd, database=self.db)

        except mysql.connector.Error as err:
    
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)    

        finally:
            print("COOL")
            if self.cnx.is_connected():
                print("MySQL connection is ok !")
                #cursor.close()
                self.cnx.close()
                print("MySQL connection is closed")
        

    def connect():
        pass



app=App()

        

