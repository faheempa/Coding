from tkinter import *
from tkinter import ttk
from sql_functions import *

table_name = "student"
attributes = "name text, dept text, year integer"
db = create_db("database")
cur = get_cur(db)
create_table(cur, table_name, attributes)

try:
    student_list = [
        ("soorej", "cs", 7),
        ("faheem", "cs", 5),
        ("soorej", "cs", 7),
        ("faheem", "cs", 5),
        ("soorej", "cs", 7),
        ("faheem", "cs", 5),
        ("soorej", "cs", 7),
        ("faheem", "cs", 5),
        ("faheem", "cs", 5),
        ("soorej", "cs", 7),
    ]
    insert_into_table(cur, table_name, student_list)
    data = select_from_table(cur, table_name, rtn=True)

    window = Tk()
    window.title("NAME")
    window.geometry("850x850")
    window.config(background="white")

    frm = Frame(window)
    frm.pack()

    tv = ttk.Treeview(frm, columns=(1, 2, 3, 4), show="headings")
    tv.pack()
    tv.heading(1, text="ID")
    tv.column(1, width=100)
    tv.heading(2, text="Name")
    tv.column(2, width=500)
    tv.heading(3, text="Dept")
    tv.column(3, width=100)
    tv.heading(4, text="Age")
    tv.column(4, width=100)

    for d in data:
        tv.insert("", "end", values=d)

    window.mainloop()


except Exception as e:
    print(e)
finally:
    drop_table(cur, table_name)
    db.commit()
    db.close()
