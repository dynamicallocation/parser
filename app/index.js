var fs = require('fs')
var parser = require('xml2json')
var PouchDB = require('pouchdb')
var fileDB = new PouchDB('files')
var remoteCouch = new PouchDB('http://localhost:8000')
fs.readFile( '../corpus/parser/venv/Science/platelets/platelets3.xml', function(err, data) {

    var json = JSON.parse(parser.toJson(data, {reversible: true}));
    pop()
    syncDB()

});


var push = (content) => {


    var file = {

        _id: new Date().toISOString(),
        content: content,
    }

    fileDB.put(file).then(res => {
        console.log("Success",res)
    }).catch(err => {
        console.log("Failed",err)
    })
    

}

var pop = () => {

    fileDB.get("2019-04-15T22:20:59.977Z").then(res => {
        console.log("Got file:",res)
    }).catch(err => {
        console.log("Failed to get File:",err)
    })

}

var syncDB = () => {

    syncDom.setAttribute('data-sync-state', 'syncing');
    var opts = {live: true};
    fileDB.replicate.to(remoteCouch, opts, syncError);
    fileDB.replicate.from(remoteCouch, opts, syncError);
    

}

