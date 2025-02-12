import csv, pymysql
#This will connect you to database you need
#Make shure to add your correct information
#Check it worked before moving on
db=pymysql.connect(
  host = 'webdev.divms.uiowa.edu',
  user = '',
  passwd = '',
  db='')
#print ("connected")
#Create table (if doen't exist already)
#In this example has column Name and column gpa
create_SQL="""CREATE TABLE IF NOT EXISTS studentgpa (Name varchar(80), GPA DECIMAL(3,2));"""
#Below print can be used to check what command it tries to execute in next line
#print (create_SQL)
cur = db.cursor()
cur.execute(create_SQL)
db.commit()
cur.close()
#If you you got here table is created - check in dbdev
#print("Table created and exists")
#This will open file filename,csv
#It uses csvlibrary
with open('example.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # For every row with data - it skips first row with titles of columns
        # you can print row
        #print(row)
        #print(row['Name'])
        cur=db.cursor()
        # Next line creates sql string that represents
        # one insert sql command and current row data
        # Note row['Need to be one of the cilumn names'] will grab
        # value in current row for that column
        # %s is replaced with first parameter in parentheses - string
        # %f is replaced with second parameter - float
        sql = "INSERT INTO studentgpa VALUES ('%s', %f);" % (row['Name'], float(row['GPA']))
        # Below print can print sql command - check it legit before executing:)
        print(sql)
        cur.execute(sql)
        db.commit()
        cur.close()
db.close()