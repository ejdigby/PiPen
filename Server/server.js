//Import Libraries and setup server
var express = require("express")
var bodyParser = require('body-parser')
var app = express()
var server = require('http').createServer(app);
var port = 8080
var io = require('socket.io').listen(server);
app.use(bodyParser());


//Listen on port 8080
server.listen(port)
console.log("Server Started On Port " + port)


//Define POST route for /
app.post('/', function(req, res){
	console.log(1, "Request for /")
	//Handle input from the pi

	//Define received data
	x = req.body.x
	y = req.body.y
	colour = req.body.colour	

	//Emit data to html
	data = req.body
	io.emit('data', data)
	res.end()
});

//Define GET route for /
app.use('/', express.static(__dirname + "/public/"))
