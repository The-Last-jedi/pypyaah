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
	Task	TEXT NOT NULL,
	Priority	INTEGER,
	U_Id	INTEGER NOT NULL,
	Status	TEXT NOT NULL,
	Days	INTEGER NOT NULL,
	FOREIGN KEY(U_Id) REFERENCES User(U_Id),
	PRIMARY KEY(Task_ID AUTOINCREMENT))''')
    conn.commit()
    conn.close()

def fetchtasks():
    conn = sq.connect("Autoscheduler.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Tasks ORDER BY Days''')
    conn.commit()
    conn.close()

def fetchptasks():
    conn=sq.connect("Autoscheduler.db")
    cursor=conn.cursor()
    cursor.execute('''SELECT * FROM Tasks WHERE Status = 'Pending' AND Days<0 ''')
    ptasks=cursor.fetchall()
    conn.commit()
    conn.close()
    return ptasks


def fetchutasks():
	conn=sq.connect("Autoscheduler.db")
	cursor=conn.cursor()
	cursor.execute('''SELECT * FROM Tasks WHERE Status = 'Pending' AND Days>0 AND Days<7 ''')
	utasks=cursor.fetchall()
	conn.commit()
	conn.close()  
	return utasks
    
    
def fetchctasks():
	conn=sq.connect("Autoscheduler.db")
	cursor=conn.cursor()
	cursor.execute('''SELECT * FROM Tasks WHERE Status = 'Completed' ''')
	ctasks=cursor.fetchall()
	conn.commit()
	conn.close()
	return ctasks

def addtask(self,name,p,due):
    self.task_name = name
    self.task_priority = p
    self.task_due = due
    conn=sq.connect("Autoscheduler.db")
    cursor=conn.cursor()
    cursor.execute('''INSERT INTO Tasks(Task,Priority,Status,Days) VALUES(%s,%d,'Pending',%d)''',(self.task_name,self.task_priority,self.task_due))    
    conn.commit()
    conn.close()

def deltask(self,tid,uid):
    self.task_id = tid
    self.user_id = uid
    conn=sq.connect("Autoscheduler.db")
    cursor=conn.cursor()
    cursor.execute('''DELETE FROM Tasks WHERE Task_ID=%d AND U_Id=%d''',(self.task_id,self.user_id))
    conn.commit()
    conn.close()

def deluser(self,uid):
    self.user_id = uid
    conn=sq.connect("Autoscheduler.db")
    cursor=conn.cursor()
    cursor.execute('''DELETE FROM Users WHERE U_Id=%d''',(self.user_id))
    cursor.execute('''DELETE FROM Tasks WHERE U_Id=%d''',(self.user_id))
    conn.commit()
    conn.close()

def deluser(self,pwd,email,uid):
    self.user_id = uid
    self.pwd = pwd
    self.mail = email
    conn=sq.connect("Autoscheduler.db")
    cursor=conn.cursor()
    cursor.execute('''UPDATE Users SET Password=%s,Email_Id=%s WHERE U_Id=%d''',(self.pwd,self.mail,self.user_id))
    conn.commit()
    conn.close()   

create_ttable()
create_utable()
