import mysql.connector as con
import configuration as cfg


def verifyUser(name, pas):
    cnx = con.connect(user=cfg.user, password=cfg.password, host=cfg.host, database=cfg.database)
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

    cnx = con.connect(user=cfg.user, password=cfg.password, host=cfg.host, database=cfg.database)
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

    cnx = con.connect(user=cfg.user, password=cfg.password, host=cfg.host, database=cfg.database)
    cursor = cnx.cursor()

    query = "DELETE FROM entries WHERE creator LIKE %s AND format LIKE %s"

    args = (name, string)

    success = True

    try:
        cursor.execute(query, args)
        cnx.commit()
    except Exception as e:
        print e
        success = False
    finally:
        cursor.close()
        cnx.close()
        return success


def getStrings(name):
    cnx = con.connect(user=cfg.user, password=cfg.password, host=cfg.host, database=cfg.database)
    cursor = cnx.cursor()

    query = str("SELECT format FROM entries WHERE creator LIKE \'" + (name) + "\'")

    cursor.execute(query)

    result = []
    for row in cursor:
        result.append(row[0])

    cnx.commit()

    cursor.close()
    cnx.close()

    return result


def getAdmins():
    cnx = con.connect(user=cfg.user, password=cfg.password, host=cfg.host, database=cfg.database)
    cursor = cnx.cursor()

    query = str("SELECT DISTINCT name FROM logingui WHERE role LIKE '1'")

    cursor.execute(query)

    result = []
    for row in cursor:
        result.append(row[0])

    cnx.commit()

    cursor.close()
    cnx.close()

    return result


def editEntry(name, ostr, nstr):
    cnx = con.connect(user=cfg.user, password=cfg.password, host=cfg.host, database=cfg.database)
    cursor = cnx.cursor()

    query = "UPDATE entries SET format=%s WHERE creator LIKE %s AND format LIKE %s"

    args = (nstr, name, ostr)

    success = True

    try:
        cursor.execute(query, args)
        cnx.commit()
    except Exception as e:
        print e
        success = False
    finally:
        cursor.close()
        cnx.close()
        return success
