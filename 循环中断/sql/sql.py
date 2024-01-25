from pymysql import Connection

conn = Connection(
    host='localhost',
    port = 3306,
    user='root',
    password='root',

)
# print(conn.get_server_info())

cursor = conn.cursor()

conn.select_db('test1')

# cursor.execute("create table op(id int);")

# cursor.execute("select * from students limit 10") #
# result = cursor.fetchall()
# for i in result:
#     print(i)

cursor.execute("insert into students values (126,'试试',14,'女')")
conn.commit()
conn.close()