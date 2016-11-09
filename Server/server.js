var express = require("express")
var bodyParser = require('body-parser')


var app = express()
var server = require('http').createServer(app);
var port = 8080
var io = require('socket.io').listen(server);
app.use(bodyParser());


server.listen(port)
console.log(0, "Server Started On Port " + port)


app.post('/', function(req, res){
	console.log(1, "Request for /")
	//Handle input from the pi
	console.log(req.body)

	console.log(req.body.x)

	x = req.body.x
	y = req.body.y
	colour = req.body.colour	

	data = req.body
	io.emit('data', data)
	
});

app.use('/', express.static(__dirname + "/public/"))
