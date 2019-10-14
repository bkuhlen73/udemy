const net = require('net');

const client = net.connect('/tmp/nodejs.sock', () => {
  console.log('connected to the server');
  client.write('Hello Server');
});
