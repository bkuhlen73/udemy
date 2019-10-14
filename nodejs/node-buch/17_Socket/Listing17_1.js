const net = require('net');

const server = net.createServer(conn => {
  conn.on('readable', data => {
    console.log(conn.read().toString());
  });

  conn.on('end', () => {
    console.log('connection ended');
  });
});

server.listen('/tmp/nodejs.sock', () => {
  console.log('Server listening on /tmp/nodejs.sock');
});
