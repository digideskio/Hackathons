# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, jsonify
import json
import requests
from flask import Flask, render_template, request, url_for
import couchdb, couchdb.mapping
from couchdb import Database,Server, Session
from couchdb.mapping import Document, TextField, IntegerField, DateTimeField
from datetime import datetime
import platform
from mymethods import selectdb 

app = Flask(__name__)

@app.route('/')
def Welcome():
    print ("Welcome.py")
    return app.send_static_file('index.html')

@app.route('/listdbs', methods = ['POST', 'GET'])
def listdbs():
   srv   = request.form['srv']
   couch=selectdb(srv)
   
   databases= "<h1>Databases1</h1><hr>" 
   server = couch
   for db in server:
      print (db) 
      databases=databases+" "+ db +"<br>"
   return databases   
#---------------------------------------------------	
#app.route('/api/createdbdlg')
def createdbdlg():
    print ("Createdbdlg")
    return app.send_static_file('index.html')
#----------------------------------------------------
@app.route('/createdb', methods = ['POST', 'GET'])
def createdb():
   db    = request.form['db']
   srv   = request.form['srv']
   print ("Database "+ db)   

   couch=selectdb(srv)
   
   print ("Creating database "+ db)
   rc = couch.create(db)
   	
   return "created database "+ db	
	
#---------------------------------------------------

@app.route('/dbinsert', methods=['GET','POST'])
def dbinsert():
    srv       = request.form['srv']	
    database  = request.form['database']
    id        = request.form['id']
    name      = request.form['name']
    age       = request.form['age']
    health    = request.form['health']
    
    couch=selectdb(srv)
	   
    db = couch[database]
    doc = ({'name': name,'age':age,'health': health})    
    db.save(doc)

    return "hit kom vi "+ srv +  " database " + database + " name: " + name + " age "+ age + " health: "+ health 	
	
#------------------------------------	
@app.route('/classprint', methods = ['POST'])
def classprint():
    srv       = request.form['srv']
    db = request.form['db']	
    print ("Classprint DB : "+ db)
	
    couch=selectdb(srv)
    db = couch[db]
    	
    record = "<h1>Records</h1><table><hr>"
    for id in db:
       #print (id)
       doc     = db[id]
       rid     = doc['_id']
       name    = doc['name']
       age     =  doc['age']
       health  = doc['health']
       rec = "<tr><td>Id: "+rid+"<td>Name: <td>"+name + "<td> Age: "+str(age)+"<td> Health: "+health+"</tr>"  
       record=record+rec 
    record=record+"</table>"
    print ("Classprint")
    return record 

@app.route('/jinja2')
def jinja2():
    print ("Jinja2")
    return render_template('template.html', my_string="Wheeeee!", my_list=['database1','database2','database3'])	
	
		
#------------------------------------------------
port = os.getenv('PORT', '5000')
print ("Welcome.py")
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
