from sql_functions import *

table_name = "student"
attributes = "name text, dept text, sem integer, age integer, place text"
db = create_db("database")
cur = get_cur(db)
create_table(cur, table_name, attributes)

try:
    input_list = [
        ("soorej", "cs", 0, 21, "Kerala"),
        ("faheem", "cs", 1, 20, "TN"),
        ("alan", "mech", 2, 19, "Delhi")
    ]
    insert_into_table(cur, table_name, input_list)

    select_from_table(cur,table_name)
    print("-"*50)

    select_from_table(cur,table_name, id=False)
    print("-"*50)

    select_from_table(cur,table_name, condition="age>=20")
    print("-"*50)

    select_from_table(cur,table_name, condition="name like 'f%'")
    print("-"*50)

    select_from_table(cur,table_name, condition="age>=20 and name='faheem'")
    print("-"*50)

    select_from_table(cur,table_name, sort="name")
    print("-"*50)

    select_from_table(cur,table_name, sort="name", order="d")
    print("-"*50)

    select_from_table(cur,table_name, condition="age>=20", sort="name")
    print("-"*50)

    update_records(cur,table_name,set="sem=0")
    select_from_table(cur,table_name)
    print("-"*50)

    update_records(cur,table_name,set="sem=7",condition="rowid=1")
    update_records(cur,table_name,set="sem=3",condition="name like 'f%'")
    update_records(cur,table_name,set="sem=9",condition="sem<=0")
    select_from_table(cur,table_name)
    print("-"*50)

    delete_records(cur,table_name,condition="dept='mech'")
    select_from_table(cur,table_name)
    print("-"*50)

    records = select_from_table(cur,table_name,rtn=True, select="name,age", id=False)
    print(records)
    print("-"*50)

    select_from_table(cur,table_name, select="name")
    print("-"*50)

    select_from_table(cur,table_name, select="name,dept,age", id=False)
    print("-"*50)

    select_from_table(cur,table_name, select="name,dept,age", id=False, condition="age>20")
    print("-"*50)

except Exception as e:
    print(e)

finally:
    drop_table(cur, table_name)
    db.commit()
    db.close()
