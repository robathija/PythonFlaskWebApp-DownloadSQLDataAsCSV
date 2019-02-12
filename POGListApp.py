from flask import Flask, render_template, redirect, request, Response
from datetime import datetime
import pandas as pd
import pyodbc

#Define app
app = Flask(__name__)

#Db connection
dbconn = pyodbc.connect('Driver={SQL Server};Server=xxxx;Database=xx;uid=xx;pwd=xxxxx')

storelist = ['1','2','3']

#root    
@app.route("/")
def hello():
    return render_template('template.html',my_storelist = storelist)

#getCSV
@app.route("/getCSV/<store_id>")
def get_store_csv(store_id):
    selectquery = "EXEC yourSP" + " " + store_id
    data = pd.read_sql(selectquery, dbconn)
    table = data.to_csv(encoding='utf-8')
    return Response(
        table,mimetype="text/csv",headers={"Content-disposition":"attachment; filename=POGList_" + store_id + ".csv"})

app.run(debug=True)