from tkinter import *
import mysql.connector
import time
import socket

class DB_Access:
    status = False
    def __init__(self):
        # connecting to the database
        self.db = mysql.connector.connect(host='localhost', user="root", password="Sruthi@hcl122", database="Network1")
        self.mycur = self.db.cursor()

    # destroy() in the code base is used to destroy the window
    def error_destroy(self):
        err.destroy()

    def succ_destroy(self):
        succ.destroy()
        root1.destroy()

    # error message pop-up box design
    def errorwin(self):
        global err
        err = Toplevel(root1)
        err.title("Error")
        err.geometry("300x300")
        Label(err, text="All fields are required...", fg="red", font="bold").pack()
        Label(err, text="").pack()
        Button(err, text="Ok", bg="light pink", width=8, height=1, command=self.error_destroy).pack()

    # success message pop-up box design
    def success(self):
        global succ
        succ = Toplevel(root1)
        succ.title("Success")
        succ.geometry("300x300")
        Label(succ, text="Registration successful...", fg="green", font="bold").pack()
        Label(succ, text="").pack()
        Button(succ, text="Ok", bg="light pink", width=8, height=1, command=self.succ_destroy).pack()

    def register_user(self):
        username_info = username.get()
        password_info = password.get()
        if username_info == "":
            self.errorwin()
        elif password_info == "":
            self.errorwin()
        else:
            Time = time.localtime()
            T = time.asctime(Time)
            ip=socket.gethostname()
            ipadd=socket.gethostbyname(ip)
            sql = "insert into DATA_TABLE values(%s,%s,%s,%s)"
            t = (username_info, password_info, T, ipadd)
            self.mycur.execute(sql, t)
            self.db.commit()
            Label(root1, text="").pack()
            #time.sleep(0.50)
            self.success()

    def registration(self):
        global root1
        root1 = Toplevel(root)
        root1.title("REGISTRATION PORTAL")
        root1.geometry("300x300")
        global username
        global password
        Label(root1, text="REGISTER YOUR ACCOUNT", bg="lavender", fg="black", font="algerian 14 underline",height=2, width=300).pack()
        username = StringVar()
        password = StringVar()
        Label(root1, text="").pack()
        Label(root1, text="USERNAME :", font="bold").pack()
        Entry(root1, textvariable=username).pack()
        Label(root1, text="").pack()
        Label(root1, text="PASSWORD :",font="bold").pack()
        Entry(root1, textvariable=password, show="*").pack()
        Label(root1, text="").pack()
        Button(root1, text="REGISTER", bg="light blue",height=1,width=18, command=self.register_user).pack()

    def login(self):
        global root2
        root2 = Toplevel(root)
        root2.title("LOG-IN PORTAL")
        root2.geometry("300x300")
        global username_varify
        global password_varify
        Label(root2, text="LOG-IN PORTAL", bg="lavender", fg="black", font="algerian 14 underline", height=2,width=300).pack()
        username_varify = StringVar()
        password_varify = StringVar()
        Label(root2, text="").pack()
        Label(root2, text="USERNAME :", font="bold").pack()
        Entry(root2, textvariable=username_varify).pack()
        Label(root2, text="").pack()
        Label(root2, text="PASSWORD :", font="bold").pack()
        Entry(root2, textvariable=password_varify, show="*").pack()
        Label(root2, text="").pack()
        Button(root2, text="LOG-IN", bg="light pink", height="1", width="15", command=self.login_varify).pack()
        Label(root2, text="")

    def logg_destroy(self):
        logg.destroy()
        root2.destroy()

    def fail_destroy(self):
        fail.destroy()

    def logged(self):
        global logg
        logg = Toplevel(root2)
        logg.title("WELCOME")
        logg.geometry("500x300")
        Label(logg, text="WELCOME {} ".format(username_varify.get()), fg="black", bg="lavender",font="algerian 14 underline",width=18, height=2).pack()
        Label(logg, text="").pack()
        Label(logg, text="YOUR DETAILS HAVE SAVED IN THE DATABASE SUCCESSFULLY.", bg="lavender",font="algerian",  height="2", width="60").pack()
        Label(logg, text="").pack()
        Button(logg, text="  OK  ", bg="violet",font="bold",  height="1", width="8", command=self.logg_destroy).pack()

    def failed(self):
        global fail
        fail = Toplevel(root2)
        fail.title("Invalid")
        fail.geometry("300x300")
        Label(fail, text="Invalid credentials...", fg="red", font="bold").pack()
        Label(fail, text="").pack()
        Button(fail, text="Ok", bg="light pink", width=8, height=1, command=self.fail_destroy).pack()

    def login_varify(self):
            user_varify = username_varify.get()
            pas_varify = password_varify.get()
            sql = "select * from DATA_TABLE where username = %s and password = %s"
            self.mycur.execute(sql, [(user_varify), (pas_varify)])
            results = self.mycur.fetchall()
            if results:
                for i in results:
                    self.logged()
                    self.status=True

                    break

            else:
                self.failed()
                self.status=False


    def main_screen(self):
        global root
        root = Tk()
        root.title("MAIN SCREEN")
        root.geometry("300x300")
        Label(root, text="WELCOME TO MAIN SCREEN", font="algerian 14 underline", bg="lavender", fg="black",height=2, width=700).pack()
        Label(root, text="").pack()
        Button(root, text="LOG-IN", width="8", height="1", bg="light pink", font="bold", command=self.login).pack()
        Label(root, text="").pack()
        Button(root, text="REGISTRATION", height="1", width="15", bg="light blue", font="bold",command=self.registration).pack()
        Label(root, text="").pack()
        Label(root, text="").pack()
        root.mainloop()

    def return_status(self):
        return self.status

DB = DB_Access()
#DB.main_screen()
#DB.return_status()

