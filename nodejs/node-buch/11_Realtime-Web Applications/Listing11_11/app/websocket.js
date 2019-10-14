const WSS = require('websocket').server;
const http = require('http');

function init() {
  const server = http.createServer();
  server.listen(8181);

  const wss = new WSS({
    httpServer: server,
    autoAcceptConnections: false,
  });

  const connections = [];

  wss.on('request', request => {
    const connection = request.accept('chat', request.origin);

    connections.push(connection);

    connection.on('message', message => {
      for (var i = 0; i < connections.length; i++) {
        if (connections[i] && connections[i].send) {
          connections[i].send(message.utf8Data);
        }
      }
    });
  });
}

module.exports = init;
