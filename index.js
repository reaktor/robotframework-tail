'use strict';

const express = require('express');
const WebSocket = require('ws');
const SocketServer = WebSocket.Server;
const path = require('path');

const PORT = process.env.PORT || 3000;
const INDEX = path.join(__dirname, 'index.html');

const server = express();
server.use('/', express.static('public'));
server.listen(PORT, () => console.log(`Listening on ${ PORT }`));



const wss = new SocketServer({ server });

wss.on('connection', (ws) => {
  console.log('Client connected');
  ws.on('close', () => {
    console.log('Client disconnected');
  });
  ws.on("message", (data) => {
      console.log(data)
      wss.clients.forEach((client) => {
        if (client !== ws && client.readyState === WebSocket.OPEN) {
          client.send(data);
        };
      });
  });
});