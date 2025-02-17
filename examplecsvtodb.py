import csv, pymysql
#This will connect you to database you need
#Make shure to add your correct information
#Check it worked before moving on
db=pymysql.connect(
  host = 'webdev.divms.uiowa.edu',
  user = 'henryswain',
  passwd = 'AgRZXxndJYXOIStHrDqk',
  db='cs3910_henryswain')
#print ("connected")
#Create table (if doen't exist already)
create_SQL="""CREATE TABLE IF NOT EXISTS nyc_jobs (Job_ID VARCHAR(30), Civil_Service_Title VARCHAR(100), `Full-Time/Part-Time_indicator` VARCHAR(1), Salary_Range_From DECIMAL(10, 2), Salary_Range_To DECIMAL(10, 2), Salary_Frequency VARCHAR(20), Work_Location VARCHAR(200), Job_Description VARCHAR(15000), Minimum_Qual_Requirements VARCHAR(15000), Prefered_Skills VARCHAR(5000), To_Apply VARCHAR(10000));"""

cur = db.cursor()
cur.execute("""DROP TABLE IF EXISTS nyc_jobs;""")
cur.execute(create_SQL)

db.commit()
cur.close()

print("Starting to read CSV file...")

with open('./src/assets/Jobs_NYC_Postings.csv', newline='', encoding="utf-8") as csvfile:
  reader = csv.DictReader(csvfile)
  cur = db.cursor()
  row_count = 0
  def clean_text(text):
      # Remove non-ASCII characters
      return ''.join(char for char in text if ord(char) < 128)

  for row in reader:
    sql = "INSERT INTO nyc_jobs VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    print(repr(row['Salary Range From']))
    print(repr(row['Salary Range To']))

    values = (int(row['Job ID']), clean_text(row['Civil Service Title']), clean_text(row["Full-Time/Part-Time indicator"]), float(row["Salary Range From"]), float(row["Salary Range To"]), clean_text(row["Salary Frequency"]), clean_text(row["Work Location"]), clean_text(row["Job Description"]), clean_text(row["Minimum Qual Requirements"]), clean_text(row["Preferred Skills"]), clean_text(row["To Apply"]))
    try:
      # print(f"Attempting to insert Job ID: {row['Job ID']}, Agency: {row['Agency']}, Business Title: {row["Business Title"]}, Job Description: {row["Job Description"]}, Minimum Qual Requirements: {row['Minimum Qual Requirements']}, Preferred Skills: {row['Preferred Skills']}")
      cur.execute(sql, values)
      db.commit()
      row_count += 1
      if row_count % 100 == 0:  # Print progress every 100 rows
        print(f"Successfully inserted {row_count} rows...")
    except Exception as e:
      print(f"Error inserting row {row['Job ID']}: {str(e)}")
      continue
  print(f"Total rows processed: {row_count}")
cur.close()
db.close()
print("Database connection closed")
