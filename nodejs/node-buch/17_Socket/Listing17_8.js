const net = require('net');

net
  .createServer(conn => {
    conn.write('Hello Client');
    conn.end();
  })
  .listen('\\\\.\\pipe\\node-pipe');
