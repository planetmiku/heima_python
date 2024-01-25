from data_define import Record
from file_define import TextFileReader
from pymysql import Connection
path = 'txt数据.txt'
text_file_reader = TextFileReader(path)
text_data: list[Record] = text_file_reader.read_data()

conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    autocommit=True
)
print(conn.get_server_info())
cursor = conn.cursor()
conn.select_db('py_sql')
for line in text_data:
    sql = f"insert into orders values ('{line.order_date}','{line.order_id}',{line.money},'{line.province}');"
    cursor.execute(sql)

conn.close()