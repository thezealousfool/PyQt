import mysql.connector as con

def verifyUser(name, pas):
    cnx = con.connect(user='root', password='vivek', host='localhost', database='login')
    cursor = cnx.cursor()

    query = str("SELECT password FROM logingui where name like \'" + (name) + "\'")

    cursor.execute(query)
    empty = cursor.rowcount == 0

    passwd = None
    if(empty):
        passwd = ''
    else:
        for n in cursor:
            passwd = n[0]

    if(empty):
        print("empty")

    if( empty or pas != passwd):
        return False
    else:
        return True
