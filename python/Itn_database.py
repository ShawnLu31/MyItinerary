import pymysql

db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "ncku2023",
    "db": "itinerary",
    "charset": "utf8"
}

table_name_list = ['attractions', 'hotels']

def insertData(table_name, data):
    with conn.cursor() as cursor:
        # command = "INSERT INTO attractions (place_id, name, cost)VALUES(%s, %s, %s)"
        # cursor.execute(command, ('ChIJbYl7d2F2bjQRnFdvyMBuZfI', '赤崁樓','50'))
        command = f"INSERT INTO {table_name} (place_id, name, cost)VALUES(%s, %s, %s)"
        for d in data:
            cursor.execute(command, (d['place_id'], d['place_name'], d['cost']))

        conn.commit()
    return

def getData(table_name):
    with conn.cursor() as cursor:
        command = f"SELECT * FROM {table_name}"
        cursor.execute(command)
        result = cursor.fetchall()
    return result

def updateData(table_name, col_name, value):
    if table_name == table_name_list[0]:
        # modify requirement
        with conn.cursor() as cursor:
            command = f"UPDATE {table_name} SET selected = %s WHERE name_requirement = %s"
            cursor.execute(command, (value, col_name))
            
    return

def deleteData():
    with conn.cursor() as cursor:
        # command = "DELETE FROM {} WHERE id = %s".format(table_name[1])
        # cursor.execute(command, (null))

        conn.commit()
    return


try:
    # 建立Connection物件
    conn = pymysql.connect(**db_settings)
    
except Exception as ex:
    print(ex)


