#mysql
import mysql.connector as pydo
from mysql.connector import errorcode
#from dotenv import load_dotenv

class App:
    
    def __init__(self):
        
        self.user='cron'
        self.pwd='password'
        self.db='app'
        self.cnx = None
        
        try:
            self.cnx = pydo.connect(user=self.user, password=self.pwd, database=self.db)

        except pydo.Error as err:
    
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
    

    def connect():
        pass

    def select(self):
        
        request = "select * from author where name LIKE %s"
        params = ("Steve%",)
        
        with self.cnx.cursor() as c:
            c.execute(request, params)
            resultats = c.fetchall()
            for r in resultats:
                print(r)



app=App()

        
app.select()
