const net = require('net');

const client = net.connect({ port: 8080, host: '127.0.0.1' }, () => {
  client.end('Hello Server!');
});
