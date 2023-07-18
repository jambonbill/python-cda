#mysql
import mysql.connector as pipo
from mysql.connector import errorcode

try:
    con=pipo.connect(
        host="localhost",
        user="cron",
        password="password",
        database="app"
    )

except pipo.Error as err:
    
    print("pipo pas content")
    
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)  

else:
    print(con)

    request = "select * from author where name LIKE %s"
    params = ("%",)
        
    with con.cursor() as c:
        c.execute(request, params)
        resultats = c.fetchall()
        dico={}
        for r in resultats:
            print(r)
            dico['id']='valiue'

        print(dico)