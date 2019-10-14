const net = require('net');
const fs = require('fs');

const server = net.createServer(conn => {
  conn.on('readable', data => {
    console.log(conn.read().toString());
  });

  conn.on('end', () => {
    console.log('connection ended');
  });
});

server.listen('/tmp/nodejs.sock', () => {
  fs.chmod('/tmp/nodejs.sock', 0700, () => {
    console.log('Server listening on /tmp/nodejs.sock');
  });
});
