import pymysql
def application(environ, start_response):
    status = '200 OK'

    output = '<html><head><title>Job Display</title></head>\n'

    query_string = environ.get('QUERY_STRING')
    
    params = dict(param.split('=') for param in query_string.split('&') if '=' in param)

    job_id = params.get('job_id')

    output += '''<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <div class="container">'''

    output += '''<script>
    const url = window.location.href;

    const searchParams = new URL(url).searchParams;

    const entries = new URLSearchParams(searchParams).entries();

    const array = Array.from(entries);
    console.log(array);
    </script>'''
    # ^^^ possibly (probably) unneeded

    # connect
    dbcnx = pymysql.connect(host="webdev.divms.uiowa.edu",port=3306,user="henryswain",passwd="AgRZXxndJYXOIStHrDqk",db="cs3910_henryswain")
   
    sqlquery=f"""SELECT Job_ID, Agency, Number_Of_Positions, Business_Title, Job_Description, Minimum_Qual_Requirements, Prefered_Skills FROM nyc_jobs WHERE Job_ID = {job_id};"""
   
    # create a database cursor
    cursor = dbcnx.cursor() 
   
    # execute SQL select 
    cursor.execute(sqlquery)

    # get the number of rows in the resultset
    numrows = int(cursor.rowcount)

    # get and display one row at a time
    for x in range(0,numrows):
       row = cursor.fetchone()
       output += '<div class="card"><h5 class="card-header">%s</h5>\n'
       output %= row[3]
       output += '<div class="card-body">\n'
       output += '<h5>Job Description</h5>'
       output += '<p class="card-text">%s</p>\n'
       output %= row[4]
       output += '<h5>Minimum Qual Requirements</h5>'
       output += '<p class="card-text">%s</p>\n'
       output %= row[5]
       output += '<h5>Prefered Skills</h5>'
       output += '<p class="card-text">%s</p>\n'
       output %= row[6]
       output += "</div>\n</div>"

    output += "</div>"
    output += "</body></html>\n"
    cursor.close ()
    dbcnx.close ()

    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]

    start_response(status, response_headers)
    output2 = output.encode('utf-8')
    return [output2]

