

import sqlite3

#make connection to a new database
conn = sqlite3.connect('filename.db')

with conn:
    cur = conn.cursor()
    #create table SQL command with one primary key integer and one text column
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtfilenames( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT \
        )")
    conn.commit()
conn.close()

#New connection  to database for the search and add assignment
conn = sqlite3.connect('filename.db')

#list of filenames to search through for assignment
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#for loop to iterate through list and find files that end in '.txt', then add them to the database
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_txtfilenames (col_filename) VALUES (?)", (x,))
            print(x)
    conn.commit()
conn.close()
    
