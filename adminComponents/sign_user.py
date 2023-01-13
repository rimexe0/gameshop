import gameshop.components.connector as connector


def login(username, password):
    args = [username, password]
    logon = connector.returnStoredProcedure("login_user", args)
    if len(logon) <= 0:
        print("wrong credentials")
    else:
        print("success")
        print(logon)
        return logon
