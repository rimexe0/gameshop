import pymysql

hostName = "localhost"
userName = "root"
userPassword = ""
databaseName = "gameshop"
databaseCharset = "utf8mb4"
cusrorType = pymysql.cursors.DictCursor


def connect():
    try:
        databaseConnection = pymysql.connect(host=hostName,

                                             user=userName,

                                             password=userPassword,

                                             db=databaseName,

                                             charset=databaseCharset,

                                             cursorclass=cusrorType)

        return databaseConnection
    except Exception as e:
        print("connection failed : {}".format(e))


def callStoredProcedure(query, args):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.callproc(query, args)
        data = cur.fetchall()
        if len(data) == 0:
            conn.commit()
        else:
            print('error: ', str(data[0]))
    except Exception as e:
        print("query failed : {}".format(e))
    finally:
        conn.close()


def returnStoredProcedure(query, args):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.callproc(query, args)
        data = cur.fetchall()
        return data
    except Exception as e:
        print("returning stored procedure failed : {}".format(e))
    finally:
        conn.close()


