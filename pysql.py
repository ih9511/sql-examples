"""
MySQL Database with Python
"""

import pymysql
import sys

from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, session
from tkinter import *
from tkinter import messagebox

url_object = URL.create(
    drivername="mysql",
    username="root",
    password="",
    host="localhost",
    database="test",
    port=3306,
)

db_uri = "mysql://localhost:3306/test"

engine = create_engine(
    "mysql+mysqldb://"
    + "root"
    + "i"
    + ""
    + "@"
    + "localhost"
    + ":"
    + "3306"
    + "/"
    + "test",
    encoding="utf-8",
    echo=True,
    future=True,
)
result = engine.execute('select * from asdf;')

print(result)

sys.exit()
conn = engine.connect()
print(conn.execute("select + from ;"))
print(engine)

mysql_db = {"username": "root", "password": "", "host": "localhost", "port": 3306}
# print(URL(**mysql_db))

mysql = {"drivername": "mysql", "database": "localhost"}
# print(URL(**mysql))


# CRUD Class
class CRUD:

    def insertData():
        con, cur = None, None
        data1, data2, data3, data4 = "", "", "", ""
        sql = ""

        conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="1234",
            db="hanbitDB",
            charset="utf8",
        )
        cur = conn.cursor()

        data1 = edt1.get()
        data2 = edt2.get()
        data3 = edt3.get()
        data4 = edt4.get()

        try:
            sql = (
                "INSERT INTO userTable VALUES('"
                + data1
                + "', '"
                + data2
                + "', '"
                + data3
                + "', "
                + data4
                + ")"
            )
        except:
            messagebox.showerror("오류", "데이터 입력 오류가 발생함")
        else:
            messagebox.showinfo("성공", "데이터 입력 성공")
        conn.commit()
        conn.close()

    def selectData():
        strData1, strData2, strData3, strData4 = [], [], [], []
        conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="1234",
            db="hanbitDB",
            charset="utf8",
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM userTable")

        strData1.append("사용자ID")
        strData1.append("사용자이름")
        strData1.append("이메일")
        strData1.append("출생연도")

        strData1.append("-----------")
        strData1.append("-----------")
        strData1.append("-----------")
        strData1.append("-----------")

        while True:
            row = cur.fetchone()
            if row == None:
                break
            strData1.append(row[0])
            strData1.append(row[1])
            strData1.append(row[2])
            strData1.append(row[3])

        listData1.delete(0, listData1.size() - 1)
        listData2.delete(0, listData2.size() - 1)
        listData3.delete(0, listData3.size() - 1)
        listData4.delete(0, listData4.size() - 1)

        for item1, item2, item3, item4 in zip(strData1, strData2, strData3, strData4):
            listData1.insert(END, item1)
            listData2.insert(END, item2)
            listData3.insert(END, item3)
            listData4.insert(END, item4)

        conn.close()

    def updateData():
        pass

    def deleteData():
        pass


window = Tk()
window.geometry("600x300")
window.title("GUI 데이터 입력")

edtFrame = Frame(window)
edtFrame.pack()
listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

edt1 = Entry(edtFrame, width=10)
edt1.pack(side=LEFT, padx=10, pady=10)
edt2 = Entry(edtFrame, width=10)
edt2.pack(side=LEFT, padx=10, pady=10)
edt3 = Entry(edtFrame, width=10)
edt3.pack(side=LEFT, padx=10, pady=10)
edt4 = Entry(edtFrame, width=10)
edt4.pack(side=LEFT, padx=10, pady=10)

btnInsert = Button(edtFrame, text="입력", command=CRUD.insertData)
btnInsert.pack(side=LEFT, padx=10, pady=10)
btnSelect = Button(edtFrame, text="조회", command=CRUD.selectData)
btnSelect.pack(side=LEFT, padx=10, pady=10)

listData1 = Listbox(listFrame, bg="yellow")
listData1.pack(side=LEFT, fill=BOTH, expand=1)
listData2 = Listbox(listFrame, bg="yellow")
listData2.pack(side=LEFT, fill=BOTH, expand=1)
listData3 = Listbox(listFrame, bg="yellow")
listData3.pack(side=LEFT, fill=BOTH, expand=1)
listData4 = Listbox(listFrame, bg="yellow")
listData4.pack(side=LEFT, fill=BOTH, expand=1)

window.mainloop()
