const net = require('net');

const server = net.createServer(conn => {
  let sum = 0;
  let count = 0;

  conn.on('readable', data => {
    sum += parseInt(conn.read().toString());
    count += 1;

    if (count >= 10) {
      count = 0;
      conn.write(sum.toString());
    }
  });
});

server.listen('/tmp/nodejs.sock', () => {
  console.log('Server listening on /tmp/nodejs.sock');
});
