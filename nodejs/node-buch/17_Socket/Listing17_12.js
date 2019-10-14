const net = require('net');
const fs = require('fs');

fs.readFile('test.jpg', (err, data) => {
  const client = net.connect({ port: 8080, host: '127.0.0.1' }, () => {
    client.end(data.toString('base64'));
  });
});
