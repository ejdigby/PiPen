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
	console.log(req.body)
	//Handle input from the pi
});


app.use('/', express.static(__dirname + "/public/"))

io.on('connection', function(socket){
  console.log('a user connected');
  socket.emit('data', 1)
});


// io.on('connection', function (socket) {
// 	console.log("connection")

//   // // when the client emits 'new message', this listens and executes
//   // socket.on('new message', function (data) {
//   //   // we tell the client to execute 'new message'
//   //   socket.broadcast.emit('new message', {
//   //     username: socket.username,
//   //     message: data
//   //   });
//   // });

//   // // when the client emits 'add user', this listens and executes
//   // socket.on('add user', function (username) {
//   //   if (addedUser) return;

//   //   // we store the username in the socket session for this client
//   //   socket.username = username;
//   //   ++numUsers;
//   //   addedUser = true;
//   //   socket.emit('login', {
//   //     numUsers: numUsers
//   //   });
//   //   // echo globally (all clients) that a person has connected
//   //   socket.broadcast.emit('user joined', {
//   //     username: socket.username,
//   //     numUsers: numUsers
//   //   });
//   });