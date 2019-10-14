const net = require('net');

net
  .createServer(socket => {
    socket.on('readable', () => {
      const data = socket.read();
      if (Buffer.isBuffer(data)) {
        console.log(data.toString());
      }
    });
  })
  .listen(8080, '127.0.0.1');
