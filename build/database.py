import sqlite3 as sq


def create_utable():
    conn = sq.connect("Autoscheduler.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
            Username TEXT NOT NULL UNIQUE,
	        U_Id INTEGER NOT NULL UNIQUE,
	        Password	TEXT NOT NULL,
	        Age	INTEGER NOT NULL CHECK("Age" > 0),
	        Email_Id	TEXT NOT NULL UNIQUE,
	        PRIMARY KEY(U_Id AUTOINCREMENT))''')
    conn.commit()
    conn.close()


def create_ttable():
    conn = sq.connect("Autoscheduler.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Tasks(
	Task_ID	INTEGER NOT NULL UNIQUE,
	Task Name	TEXT NOT NULL,
	Priority	INTEGER,
	U_Id	INTEGER NOT NULL,
	Status	TEXT NOT NULL,
	Days Remaining	INTEGER NOT NULL,
	FOREIGN KEY(U_Id) REFERENCES User(U_Id),
	PRIMARY KEY(Task_ID AUTOINCREMENT))''')
    conn.commit()
    conn.close()

# def fetchptasks():
#     conn=sq.connect("Autosceduler.db")
#     cursor=conn.cursor()
#     cursor.execute('select * FROM Tasks where Status= 'Pending' AND U_Id = ')
#     ptasks=cursor.fetchall()
#     conn.close()
#     return ptasks
    


# def fetchutasks():
    
    
    
    
    
# def fetchctasks():
create_ttable()
create_utable()