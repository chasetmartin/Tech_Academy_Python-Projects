
import sqlite3

rosterValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Aknot', 'Mangalore', -5))

with sqlite3.connect(':memory:') as connection:
    c = connection.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Roster( \
        col_name TEXT, \
        col_species TEXT, \
        col_iq INT \
        )")
    c.executemany("INSERT INTO Roster VALUES(?,?,?)", rosterValues)
    c.execute("UPDATE Roster SET col_species=? WHERE col_name=?", ('Human', 'Korben Dallas'))
    c.execute("SELECT col_name, col_iq FROM Roster WHERE col_species == 'Human'")
    for row in c.fetchall():
        print(row)
