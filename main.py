import tkinter as tk

# Create window
window1 = tk.Tk()
window1.title("login")
window1.geometry("500x300")
window1.configure(bg="lightblue")
studentsname=[]
studentsgrade=[]
studentsdep=[]
# Function
def check():
    if (a.get()=='') or (psw.get()==''):
        label3.config(text="Please fill all fields",fg="red")
    elif (a.get()=='admin') and (psw.get()=='1234') :
        label3.config(text="Welcome admin",fg="green")
        window2 = tk.Toplevel()
        window2.title("dashboard")
        window2.geometry("500x500")

        def add_student():
            window3 = tk.Toplevel()
            window3.title("add student")
            window3.geometry("500x300")
            
            # Function
            def save_B():
                if (dep.get()=='') or (grade.get()=='') or (name.get()==''):
                    label3.config(text="Please fill all fields",fg="red")
                elif float(grade.get()) < 0 or float(grade.get()) > 20:
                    label3.config(text="grade must be between 0 and 20",fg="red")
                else:
                    studentsname.append(name.get())
                    studentsgrade.append(float(grade.get()))
                    studentsdep.append(dep.get())
                window3.destroy()
                

            # Label
            label = tk.Label(window3, text="student name : ")
            label.pack(pady=10)
            name=tk.Entry(window3)
            name.pack(pady=10)

            label2 = tk.Label(window3, text="grade " )
            label2.pack(pady=10)
            grade=tk.Entry(window3)
            grade.pack(pady=10)
            label4 = tk.Label(window3, text="department " )
            label4.pack(pady=10)
            dep=tk.Entry(window3)
            dep.pack(pady=10)
            label3 = tk.Label(window1, text="" )
            label3.pack(pady=20)
            # Button
            save = tk.Button(window3, text="save", command=save_B)
            save.pack()
        def view_student():
            window4 = tk.Toplevel()
            window4.title("student List")
            window4.geometry("500x300")

            for i in range(0,len(studentsname)):
                tk.Label(window4, text=studentsname[i]).grid(row=i, column=0)
                tk.Label(window4, text=studentsgrade[i]).grid(row=i, column=1)
                tk.Label(window4, text=studentsdep[i]).grid(row=i, column=2)
        def statistics():
            
            window5 = tk.Toplevel()
            window5.title("statistics")
            window5.geometry("500x500")

            label = tk.Label(window5, text="number of students: ")
            label.pack(pady=10)
            label2 = tk.Label(window5, text=len(studentsname) )
            label2.pack(pady=10)

            label3 = tk.Label(window5, text="Highest grade " )
            label3.pack(pady=10)
            maxlabel = tk.Label(window5, text=str(max(studentsgrade)) )
            maxlabel.pack(pady=10)

            label4 = tk.Label(window5, text="lowest grade" )
            label4.pack(pady=10)
            minlabel = tk.Label(window5, text=str(min(studentsgrade)) )
            minlabel.pack(pady=10)

            label5 = tk.Label(window5, text="averge grade" )
            label5.pack(pady=10)
            avglabel = tk.Label(window5, text=str(sum(studentsgrade)/len(studentsname)))
            avglabel.pack(pady=10)

        def logout():
            window2.destroy()
            a.delete(0, tk.END)
            psw.delete(0, tk.END)
            label3.config(text= "")


        label0 = tk.Label(window2, text="Student Management System ")
        label0.pack(pady=10)

        add = tk.Button(window2, text="Add Student", command=add_student)
        add.pack()
        view = tk.Button(window2, text=" View Students", command=view_student)
        view.pack()
        stats = tk.Button(window2, text="Statistics", command=statistics)
        stats.pack()
        logout = tk.Button(window2, text="logout", command=logout)
        logout.pack()
    else  :
       label3.config(text="access denied",fg="red")

# Label
label0 = tk.Label(window1, text="Student Management System ")
label0.pack(pady=10)
label = tk.Label(window1, text="username: ",bg='pink')
label.pack(pady=10)
a=tk.Entry(window1,bg='yellow')
a.pack(pady=10)

label2 = tk.Label(window1, text="password" )
label2.pack(pady=10)
psw=tk.Entry(window1  ,show="*")
psw.pack(pady=10)
# Button
login = tk.Button(window1, text="login", command=check)
login.pack()
label3 = tk.Label(window1, text="",bg='light blue' )
label3.pack(pady=20)

# Run window
window1.mainloop()






