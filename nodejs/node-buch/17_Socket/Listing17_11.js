const net = require('net');
const fs = require('fs');

net
  .createServer(socket => {
    let file = '';

    socket.on('readable', () => {
      file += socket.read();
    });

    socket.on('end', () => {
      const input = Buffer.from(file, 'base64');
      fs.writeFile('dest.jpg', input, () => {});
    });
  })
  .listen(8080, '127.0.0.1');
