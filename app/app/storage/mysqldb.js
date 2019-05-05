var mysql = require('mysql')

var con = mysql.createConnection({

    host: "localhost",
    user: "myDB",
    password: "hunchbackofPersistentStorage"
})

con.connect(function(err) {
    if(err) throw err;
    console.log(connected)
});

