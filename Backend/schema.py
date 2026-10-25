import sqlite3
sqliteConnection = sqlite3.connect('db.db')
cursor = sqliteConnection.cursor()


table = '''CREATE TABLE IF NOT EXISTS EVENTS (
            EID INTEGER PRIMARY KEY,
            Name text NOT NULL,
            Type text CHECK(Type = "Social" OR Type = "Professional" OR Type = "Volunteering"),
            Description text NOT NULL,
            Date DATETIME NOT NULL,
            FormLink text,
            Food text CHECK(Food = 'Y' OR Food = 'N'),
            Merch text CHECK(Merch = 'Y' OR Merch = 'N')
        );'''
cursor.execute(table)    

"""
curr = '''INSERT INTO EVENTS(EID, Name, Type, Description, Date, Food, Merch)
          Values(67, "Arduino Workshop", "Professional", "Arduino Stuff", "10-25-26", "N", "N")
       '''
cursor.execute(curr)
cursor.execute("SELECT * FROM EVENTS")
x = cursor.fetchall()
print(x)
"""