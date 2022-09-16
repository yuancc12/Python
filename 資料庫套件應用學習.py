# -*- coding: utf-8 -*-
"""
Created on Tue May 31 15:31:27 2022

@author: User
"""
import sqlite3
def star(): 
    
        a=int(input("请输入需要的功能。1，顯示所有item,2,新增一筆item資料.3,依據rowid，修改一筆item資料的num.4,依據rowid，刪除一筆item資料.5, 離開程式"))
        if a==int(5):
           print("end")
        elif a==int(1):
           conn=sqlite3.connect(r"C:\Users\User\exquestion.db")
           cursor=conn.cursor()
           sql="select rowid,* from item;"
           cursor.execute(sql)
           result = cursor.fetchall()
           if result !=[]:
               print(result)
               conn.commit()
               conn.close()
               star()
           else:
               print("no any things")
               star()
        elif a==int(2):
           a=str(input("请输入题目"))
           b=int(input("请输入数字"))
           c=int(input("请输入類別（1为A，2为B)"))
           d=str(input("请输入截止日期"))
           if (c==int(1) or c==int(2)) and a!=" " and b!=" " and d!=" " and a!="" and b!="" and d!="":
               conn=sqlite3.connect(r"C:\Users\User\exquestion.db")
               cursor=conn.cursor()
               sql="insert into item(title,num,type,expireDay)values("+"'"+a+"'"+","+"'"+str(b)+"'"+","+"'"+str(c)+"'"+","+"'"+str(d)+"');"
               cursor.execute(sql)
               print("添加完成")
               conn.commit()
               conn.close()
               star()
           else:
               print("资料有误")
               star()
        elif a==int(3):
            a=str(input("请输入编号"))
            conn=sqlite3.connect(r"C:\Users\User\exquestion.db")
            cursor=conn.cursor()
            sql="select rowid,num from item;"
            cursor.execute(sql)
            result = cursor.fetchall()
            if result !=[]:
                b=int(input("请输入更改的数字"))
                sql = "update item set num="+"'"+str(b)+"'"+"where rowid="+"'"+a+"'"
                cursor.execute(sql)
                print('修改完成')
                conn.commit()
                conn.close()
                star()
            else:
                print("没有这资料")
                star()
        elif a==int(4):
            a=str(input("请输入编号"))
            conn=sqlite3.connect(r"C:\Users\User\exquestion.db")
            cursor=conn.cursor()
            sql="select rowid,title from item;"
            cursor.execute(sql)
            result = cursor.fetchall()
            if result !=[]:
                sql= "delete from item where rowid="+"'"+a+"'"
                cursor.execute(sql)
                print("已经删除完毕")
                conn.commit()
                conn.close()
                star()
            else:
                print("没有这资料")
                star()
    
star()