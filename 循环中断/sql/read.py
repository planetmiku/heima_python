from pymysql import Connection

conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    autocommit=True
)
print(conn.get_server_info())

conn.select_db('py_sql')

cursor = conn.cursor()

sql = 'select  * from orders;'

cursor.execute(sql)

data = cursor.fetchall()

with open('导出数据.txt','w',encoding='utf-8') as f:
    for list in data:
        writ_data = f"{{\"date\": \"{list[0]}\",\"order_id\": \"{list[1]}\",\"money\": {list[2]},\"province\": \"{list[3]}\"}}\n"
        f.write(writ_data)


conn.close()