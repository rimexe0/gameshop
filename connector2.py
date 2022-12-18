import pyodbc

server = 'localhost'
database = 'gameshop'
username = 'root'
password = ''


def connect():
    try:
        conn = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)

        cursor = conn.cursor()
        cursor.execute('call select_all_users()')

        for i in cursor:
            print(i)

        return cursor
    except Exception as e:
        print("connection failed : {}".format(e))
