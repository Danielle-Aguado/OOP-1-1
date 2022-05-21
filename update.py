import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
                                r'DBQ=C:\Users\HanSel\Documents\Database1.accdb;')
    print("Database is Connected")

    Fullname = "Aguado, Danielle Ysabelle M."
    user_id = 10

    database = connection.cursor()
    database.execute('UPDATE Table1 SET Fullname=? WHERE id=?', (Fullname, user_id))
    connection.commit()

    Address = "Silang, Cavite"
    user_id = 10

    database = connection.cursor()
    database.execute('UPDATE Table1 SET Address=? WHERE id=?', (Address, user_id))
    connection.commit()

    Grade = 94
    user_id = 10

    database = connection.cursor()
    database.execute('UPDATE Table1 SET Grade=? WHERE id=?', (Grade, user_id))
    connection.commit()



    print("Database is updated")

except pyodbc.Error:
    print("Database is NOT connected")