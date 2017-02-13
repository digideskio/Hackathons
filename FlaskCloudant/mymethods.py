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

def selectdb(srv):
   if (srv == "local"):
       couch = couchdb.Server("http://127.0.0.1:5984/")
   elif (srv =="remote"): 
       couch = couchdb.Server("https://c3eb2101-67.....mix.cloudant.com")   
   else:
       return "Database entry error" 
   return couch

