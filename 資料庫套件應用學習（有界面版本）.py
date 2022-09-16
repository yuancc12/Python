# -*- coding: utf-8 -*-
"""
Created on Tue May 31 22:00:01 2022

@author: User
"""

from tkinter import *
from tkinter import messagebox
from functools import partial
import sqlite3
window = Tk()
window.geometry('350x200')
window.title("资料库")
def star():
    def update(a,b,c,d,e,f,g,h,i):
                 def upload():#sq修改
                     if (txt3.get()==str(1) or txt3.get()==str(2)) and txt1.get()!="" and txt2.get()!="" and txt4.get!="":
                         conn=sqlite3.connect(r"C:\Users\User\exquestion.db")
                         sql1= "update item set title="+"'"+str(txt1.get())+"'"+"where rowid="+"'"+str(a)+"'"
                         sql2="update item set num="+"'"+str(txt2.get())+"'"+"where rowid="+"'"+str(a)+"'"
                         sql3="update item set type="+"'"+str(txt3.get())+"'"+"where rowid="+"'"+str(a)+"'"
                         sql4="update item set expireDay="+"'"+str(txt4.get())+"'"+"where rowid="+"'"+str(a)+"'"
                         
                         conn=sqlite3.connect(r"C:\Users\User\exquestion.db")
                         cursor=conn.cursor()
                         cursor.execute(sql1)
                         cursor.execute(sql2)
                         cursor.execute(sql3)
                         cursor.execute(sql4)
                         
                         conn.commit()
                         conn.close()
                         f.configure(text=txt1.get())
                         g.configure(text=txt2.get())
                         h.configure(text=txt3.get())
                         i.configure(text=txt4.get())
                         messagebox.showinfo("修改完成","已經修改完成")
                     else:
                         messagebox.showwarning('错误信息','请输入1=A 或者0=B')
                
                 top = Toplevel()
                 top.title("修改画面")
                 l1 = Label(top, text ="题目")
                 l1.grid(row = 0, column =1)
                 txt1= Entry(top,width=10)
                 txt1.insert(0,b)
                 txt1.grid(column=3, row=0)
                 l2 = Label(top, text ="数字")
                 l2.grid(row = 1, column =1)
                 txt2= Entry(top,width=10)
                 txt2.insert(0,c)
                 txt2.grid(column=3, row=1)
                 l3 = Label(top, text ="類別（1为A，2为B)")
                 l3.grid(row = 2, column =1)
                 txt3 = Entry(top,width=10)
                 txt3.insert(0,d)
                 txt3.grid(column=3, row=2)
                 l4 = Label(top, text ="截止日期")
                 l4.grid(row = 3, column =1)
                 txt4 = Entry(top,width=10)
                 txt4.insert(0,e)
                 txt4.grid(column=3, row=3)  
                 btn = Button(top,text='修改',command=upload)
                 btn.grid(column=5,row=5)
                 
    def delete(a,b,c,d,e,f):
        m = messagebox.askyesno('删除资讯', '确定删除编号'+str(a)+'吗？')
        if m==True:
            conn=sqlite3.connect(r"C:\Users\User\exquestion.db")
            sql= "delete from item where rowid="+"'"+str(a)+"'"
            cursor=conn.cursor()
            cursor.execute(sql)
            conn.commit()
            conn.close()
            for i in window.grid_slaves():
                if int(i.grid_info()["row"])>0:
                    i.destroy()
            star()
            
            
            
        
    def addnew():
        def register():
            conn=sqlite3.connect(r"C:\Users\User\exquestion.db")
            cursor=conn.cursor()
            sql="select rowid from item" 
            cursor.execute(sql)
            result = cursor.fetchall()
            if (txt3.get()==str(1) or txt3.get()==str(2)) and txt1.get()!="" and txt2.get()!="" and txt4.get!=""and txt1.get()!=" " and txt2.get()!=" " and txt4.get!=" ":
                if result==[]:
                   l11 = Label(window , text =1)
                   l11.grid(row = 1, column =0 )
                   l12 = Label(window , text =txt1.get())
                   l12.grid(row = 1, column =1)
                   l13 = Label(window , text =txt2.get())
                   l13.grid(row = 1, column =2)
                   l14 = Label(window , text =txt3.get())
                   l14.grid(row = 1, column =3)
                   l15 = Label(window , text =txt4.get())
                   l15.grid(row = 1, column =4)
                   btn1 = Button(window, text="修改",command=partial(update,l11.cget("text"),l12.cget("text"),l13.cget("text"),l14.cget("text"),l15.cget("text"),l12,l13,l14,l15))
                   btn1.grid(row=1,column=6)
                   btn2 = Button(window, text="删除",command=partial(delete,l11.cget("text"),l11,l12,l13,l14,btn1))
                   btn2.grid(row=1,column=7)
                   sql2="insert into item(title,num,type,expireDay)values("+"'"+txt1.get()+"'"+","+"'"+str(txt2.get())+"'"+","+"'"+str(txt3.get())+"'"+","+"'"+str(txt4.get())+"'"+");"
                   cursor.execute(sql2)
                   conn.commit()
                   conn.close()
                elif result!=[]:
                   o=[]
                   for i in result[-1]:
                    o=o+[i]
                    l11 = Label(window , text =o[0]+1)
                    l11.grid(row = o[0]+2, column =0 )
                    l12 = Label(window , text =txt1.get() )
                    l12.grid(row = o[0]+2, column =1)
                    l13 = Label(window , text =txt2.get() )
                    l13.grid(row = o[0]+2, column =2)
                    l14 = Label(window , text =txt3.get() )
                    l14.grid(row = o[0]+2, column =3)
                    l15 = Label(window , text =txt4.get())
                    l15.grid(row = o[0]+2, column =4)
                    btn1 = Button(window, text="修改",command=partial(update,l11.cget("text"),l12.cget("text"),l13.cget("text"),l14.cget("text"),l15.cget("text"),l12,l13,l14,l15))
                    btn1.grid(row=o[0]+2,column=6)
                    btn2 = Button(window, text="删除",command=partial(delete,l11.cget("text"),l11,l12,l13,l14,btn1))
                    btn2.grid(row=o[0]+2,column=7)
                    sql2="insert into item(title,num,type,expireDay)values("+"'"+txt1.get()+"'"+","+"'"+str(txt2.get())+"'"+","+"'"+str(txt3.get())+"'"+","+"'"+str(txt4.get())+"'"+");"
                    cursor.execute(sql2)
                    conn.commit()
                    conn.close()
            else:
                messagebox.showwarning('错误信息','请输入1=A 或者0=B')
         
        top = Toplevel()#添加账号
        top.title("新增資料")
        l11 = Label(top, text ="題目")
        l11.grid(row = 0, column =1)
        txt1= Entry(top,width=10)
        txt1.grid(column=3, row=0)
        l21 = Label(top, text ="數字")
        l21.grid(row = 1, column =1)
        txt2= Entry(top,width=10)
        txt2.grid(column=3, row=1)
        l31 = Label(top, text ="類別（1为A，2为B)")
        l31.grid(row = 2, column =1)
        txt3 = Entry(top,width=10)
        txt3.grid(column=3, row=2)
        l14 = Label(top, text ="截止日期")
        l14.grid(row = 3, column =1)
        txt4 = Entry(top,width=10)
        txt4.grid(column=3, row=3)    
        btn1 = Button(top,text='确定',command=register)
        btn1.grid(column=5,row=5)
      


    
    conn=sqlite3.connect(r"C:\Users\User\exquestion.db")
    cursor=conn.cursor()
    sql="select rowid,* from item" 
    cursor.execute(sql)
    result = cursor.fetchall()
    if result !=[]:
        a=1
        result2=[]
        for i in result:
            result2.append(list(i))
    
        for i in result2:
           l11 = Label(window , text =i[0])
           l11.grid(row = a+1, column =0 )
           l12 = Label(window , text =i[1])
           l12.grid(row = a+1, column =1)
           l13 = Label(window , text =i[2])
           l13.grid(row = a+1, column =2)
           l14 = Label(window , text =i[3])
           l14.grid(row = a+1, column =3)
           l15 = Label(window , text =i[4])
           l15.grid(row = a+1, column =4)
           btn1 = Button(window, text="修改",command=partial(update,l11.cget("text"),l12.cget("text"),l13.cget("text"),l14.cget("text"),l15.cget("text"),l12,l13,l14,l15))
           btn1.grid(row=a+1,column=6)
           btn2 = Button(window, text="删除",command=partial(delete,l11.cget("text"),l11,l12,l13,l14,btn1))
           btn2.grid(row=a+1,column=7)
           a=a+1
    btn = Button(window, text="新增",command=addnew)
    btn.grid(column=0, row=0)
    conn.commit()
    conn.close()

star()
window.mainloop()
