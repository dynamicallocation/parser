
   
   function openDB(myData){

    const request = indexedDB.open("fileStorage",1)
    request.onsuccess = event => {

        db = event.target.result;

    };

  

    request.onupgradeneeded = function(event) {

    var db = event.target.result
    var id = new Date().toISOString()

    // Create an objectStore to hold information about our customers. We're
    // going to use "ssn" as our key path because it's guaranteed to be
    // unique - or at least that's what I was told during the kickoff meeting.
    var objectStore = db.createObjectStore("files", { keyPath: id });

    

    // Create an index to search customers by email. We want to ensure that
    // no two customers have the same email, so use a unique index.
    objectStore.createIndex("file", "file", { unique: true });

    // Use transaction oncomplete to make sure the objectStore creation is 
    // finished before adding data into it.
    objectStore.transaction.oncomplete = function(event) {
        // Store values in the newly created objectStore.
        var fileObjectStore = db.transaction("files", "readwrite").objectStore("files");

        fileObjectStore.add(myData)
    };

    };


}

module.exports = {open:openDB}




