var express = require("express")
var bodyParser = require('body-parser')


var app = express()
var server = require('http').createServer(app);
var port = 8080

app.use(bodyParser());


server.listen(port)
console.log(0, "Server Started On Port " + port)


app.post('/', function(req, res){
	consle.log(1, "Request for /")
	//Handle input from the pi
});


app.use('/', express.static(__dirname + "/public/"))
