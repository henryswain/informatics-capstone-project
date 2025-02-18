import pymysql
def application(environ, start_response):
    status = '200 OK'

    output = '<html><head><title>Job Display</title></head>\n'

    output += '''<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <div class="container">'''

    output += '''<script>
    const url = 'https://webdev.divms.uiowa.edu/webdev/cs3910/henryswain/informatics-capstone-project/job.wsgi?'

    function LinkToJob(jobID) {
        const searchParams = new URLSearchParams({Job_ID: jobID});
        console.log(searchParams);

        const queryString = searchParams.toString();
        console.log(queryString);

        window.location.href = url + queryString;
    }
    </script>'''

    # connect
    dbcnx = pymysql.connect(host="webdev.divms.uiowa.edu",port=3306,user="henryswain",passwd="AgRZXxndJYXOIStHrDqk",db="cs3910_henryswain")
   
    sqlquery="""SELECT Job_ID, Civil_Service_Title, `Full-Time/Part-Time_indicator`, Salary_Range_From, Salary_Range_To, Salary_Frequency, Work_Location FROM nyc_jobs LIMIT 10;"""
   
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
       output %= row[1]
       output += '<div class="card-body">\n'
       output += f'<p class="card-text">{row[2]}</p>\n'
       output += f'<p class="card-text">${row[3]}-{row[4]}</p>\n'
       output += f'<p class="card-text">{row[6]}</p>\n'

       <!-- output %= row[2] -->
       <!-- output += '<p class="card-text">%s</p>\n' -->
       <!-- output %= row[3] -->
       <!-- output += '<p class="card-text">%s</p>\n'
       output %= row[4] -->
       <!-- output += '<button class="btn-primary" id="button_%s"'
       output %= row[0]
       output += 'onclick=LinkToJob(%s)>Learn More</button>'
       output %= row[0] -->
       output += f'<button class="btn-primary" id="button_{row[0]}" onclick="LinkToJob({row[0]})">Learn More</button>'
       output += "</div>\n</div>"

    output += "</div>"
    output += "</body></html>\n"
    cursor.close ()
    dbcnx.close ()

    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output))),
                        ('Access-Control-Allow-Origin', '*'),
                        ('Access-Control-Allow-Methods', 'GET'),
                        ('Access-Control-Allow-Headers', 'Content-Type')]

    start_response(status, response_headers)
    output2 = output.encode('utf-8')
    return [output2]

