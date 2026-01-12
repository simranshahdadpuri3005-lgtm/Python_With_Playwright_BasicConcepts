import sqlite3  #sqlite3 is a package present in python
import _mysql_connector

#by using python we will copnnect to database
#playwright cannot handle databases hence python methods are used

def test_sqliteconnection():
    dataTables = sqlite3.connect(r"C:\Users\Owner\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db")
    #r in the poath name is for regular experession
    data = dataTables.cursor()
    data.execute("Select * from Album where AlbumId = 2")
    results = data.fetchall()
    print(results)

    #cursor is a function to execution. it provides forum for execution
    #execute command is used for specific sql query
    #fetall will give all the results of the query execution



