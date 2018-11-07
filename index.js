const WebSocketServer = require("ws").Server;
const http = require("http");
const express = require("express");
const app = express();
const port = process.env.PORT || 5000;

app.use(express.static(__dirname + "/"));

var server = http.createServer(app);
server.listen(port);

console.log("http server listening on %d", port);

var wss = new WebSocketServer({server: server, port: 2222});
console.log("websocket server created");

wss.on("connection", function(ws) {
  console.log("websocket connection open")
  ws.on("close", function() {
    console.log("websocket connection close")
  });
  ws.on("message", function(data) {
      console.log(data);
  })
});