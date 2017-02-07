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

    if(empty or pas != passwd):
        return -1
    else:
        query = str("SELECT role FROM logingui where name like \'" + (name) + "\'")
        role = -1
        cursor.execute(query)
        for n in cursor:
            role = n[0]
        return role

    cnx.commit()

    cursor.close()
    cnx.close()


def addEntry(name, string):
    if(string == ''):
        return False

    cnx = con.connect(user='root', password='vivek', host='localhost', database='login')
    cursor = cnx.cursor()

    query = "INSERT INTO entries(creator,format) VALUES(%s,%s)"

    args = (name, string)

    success = True

    try:
        cursor.execute(query, args)
        cnx.commit()
    except:
        success = False
    finally:
        cursor.close()
        cnx.close()
        return success


def delEntry(name, string):
    if(string == ''):
        return False

    cnx = con.connect(user='root', password='vivek', host='localhost', database='login')
    cursor = cnx.cursor()

    query = "DELETE FROM entries WHERE creator LIKE %s AND format LIKE %s"

    args = (name, string)

    success = True

    try:
        cursor.execute(query, args)
        cnx.commit()
    except:
        success = False
    finally:
        cursor.close()
        cnx.close()
        return success
