from django.shortcuts import render
from django.db import connection
import pandas as pd
from pathlib import Path
import os
from django.shortcuts import HttpResponse

html = """<style>
@import "https://fonts.googleapis.com/css?family=Montserrat:300,400,700";
.rwd-table {
  margin: 1em 0;
  min-width: 300px;
}
.rwd-table tr {
  border-top: 1px solid #ddd;
  border-bottom: 1px solid #ddd;
}
.rwd-table th {
  display: none;
}
.rwd-table td {
  display: block;
}
.rwd-table td:first-child {
  padding-top: .5em;
}
.rwd-table td:last-child {
  padding-bottom: .5em;
}
.rwd-table td:before {
  content: attr(data-th) ": ";
  font-weight: bold;
  width: 6.5em;
  display: inline-block;
}
@media (min-width: 480px) {
  .rwd-table td:before {
    display: none;
  }
}
.rwd-table th, .rwd-table td {
  text-align: left;
}
@media (min-width: 480px) {
  .rwd-table th, .rwd-table td {
    display: table-cell;
    padding: .25em .5em;
  }
  .rwd-table th:first-child, .rwd-table td:first-child {
    padding-left: 0;
  }
  .rwd-table th:last-child, .rwd-table td:last-child {
    padding-right: 0;
  }
}
 
 
h1 {
  font-weight: normal;
  letter-spacing: -1px;
  color: #34495E;
}
 
.rwd-table {
  background: #34495E;
  color: #fff;
  border-radius: .4em;
  overflow: hidden;
}
.rwd-table tr {
  border-color: #46637f;
}
.rwd-table th, .rwd-table td {
  margin: .5em 1em;
}
@media (min-width: 480px) {
  .rwd-table th, .rwd-table td {
    padding: 1em !important;
  }
}
.rwd-table th, .rwd-table td:before {
  color: #dd5;
}
</style>
<script>
  window.console = window.console || function(t) {};
</script>
<script>
  if (document.location.search.match(/type=embed/gi)) {
    window.parent.postMessage("resize", "*");
  }
</script>"""

def getdf(context, columns, data):
    for c in columns:
        context[c] = []
    for d in data:
        for i in range(len(columns)):
            context[columns[i]].append(d[i])
    BASE_DIR = Path(__file__).resolve().parent.parent
    df = pd.DataFrame.from_dict(context)
    df.to_csv(os.path.join(BASE_DIR,'use.csv'),index=False)
    df = pd.read_csv(os.path.join(BASE_DIR,'use.csv'))
    obj = df.to_html(os.path.join(BASE_DIR,"template\\data.html"))
    df.to_html(os.path.join(BASE_DIR,"template\\data.html"))
    with open(os.path.join(BASE_DIR,"template\\data.html")) as file:
        file = file.read()
    file = file.replace("<table ", "<table class='rwd-table'")
    with open(os.path.join(BASE_DIR,"template\\data.html"), "w") as file_to_write:
        file_to_write.write(html + file)
    # for c in context:
    #   if len(context[c])<=1:
    #     tmp = context[c]
    #     context[c] = tmp[0]
    return context

def writeinfile(string):
  with open('user.txt','w') as writer:
    writer.write(string)

def readfile():
  with open('user.txt','r') as reader:
    user = reader.read()
  return user 

