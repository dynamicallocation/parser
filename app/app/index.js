
var fs = require('fs')
var db = require('../../DBStorage/fileDB/fileDB')
const express = require('express')
const bodyParser = require('body-parser')
const files = require('./js/fileStore')
var parser = require('xml2json')
var PouchDB = require('pouchdb')
var fileDB = new PouchDB('files')
var remoteCouch = new PouchDB('http://127.0.0.1:5984')
var dataFile;


fs.readFile( '../../corpus/parser/venv/Science/platelets/platelets7.xml', function(data,error){

        dataFile = data;

})

const app = express()
app.use(express.static('public'))
app.use(bodyParser.json())
app.post('/uploadFile', (req,res) => {

    files.uploadFile({

        file:dataFile,
        id: new Date().toISOString()

    }).then(() => res.sendStatus(200))

})

app.listen(7555, () => {

    console.log('Server running on http://localhost:7555')

})

