const WSS = require('websocket').server;
const http = require('http');

function init() {
  const server = http.createServer();
  server.listen(8181);

  const wss = new WSS({
    httpServer: server,
    autoAcceptConnections: false,
  });

  const connections = {};

  wss.on('request', function(request) {
    const connection = request.accept('chat', request.origin);

    connection.on('message', message => {
      let name = '';

      for (var key in connections) {
        if (connection === connections[key]) {
          name = key;
        }
      }

      const data = JSON.parse(message.utf8Data);
      let msg;

      switch (data.type) {
        case 'join':
          connections[data.name] = connection;
          msg = JSON.stringify({
            type: 'join',
            names: Object.keys(connections),
          });
          break;
        case 'msg':
          msg = JSON.stringify({ type: 'msg', name, msg: data.msg });
          break;
      }

      for (const key in connections) {
        if (connections[key] && connections[key].send) {
          connections[key].send(msg);
        }
      }
    });
  });
}

module.exports = init;
