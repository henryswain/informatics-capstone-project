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
   
    sqlquery="""SELECT Job_ID, Civil_Service_Title, `Full-Time/Part-Time_indicator`, Salary_Range_From, Salary_Range_To, Salary_Frequency, Work_Location, Job_Description, Minimum_Qual_Requirements, Prefered_Skills, To_Apply FROM nyc_jobs LIMIT 10;"""
   
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
       if row[5] == "Hourly" and row[2] == "F":
           output += f'<p class="card-text">${row[3]}-{row[4]}/hr &#8226 Full-time</p>\n'
       elif row[5] == "Hourly" and row[2] == "P":
           output += f'<p class="card-text">${row[3]}-{row[4]}/hr &#8226 Part-time</p>\n'
       elif row[5] == "Annual" and row[2] == "F":
           output += f'<p class="card-text">${row[3]}-{row[4]}/yr &#8226 Full-time</p>\n'
       elif row[5] == "Annual" and row[2] == "P":
           output += f'<p class="card-text">${row[3]}-{row[4]}/yr &#8226 Part-time</p>\n'
       output += f'<p class="card-text">Location: {row[6]}</p>\n'
    #    output += f'<button class="btn btn-primary" id="button_{row[0]}" onclick="LinkToJob({row[0]})">Learn More</button>'
       output += f"""<!-- Button trigger modal -->
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" id="button_{row[0]}" data-bs-target="#exampleModal">
            Learn More
        </button>

        <!-- Modal -->
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="more information" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">{row[1]}</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <h5>Job Description</h5>
                <p>{row[7]}</p>
                <h5>Basic Qual Requirements</h5>
                <p>{row[8]}</p>
                <h5>Prefered Skills</h5>
                <p>{row[9]}</p>
                <h5>To Apply</h5>
                <p>{row[10]}</p>
            
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            </div>
            </div>
        </div>
        </div>'"""
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

