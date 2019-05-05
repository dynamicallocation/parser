var idb = require('idb')

if (!('indexedDB' in window)) {
    console.log("This browser does not support indexeddb")
    return;
}

var dbPromise = idb.openDB("filesystem",1, function(upgradeDb) {
    
    switch(upgradeDb.oldVersion){
        case 0:

        case 1:

        
    }
})

