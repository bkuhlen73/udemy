const net = require('net');

const writable = net.connect({ host: '127.0.0.1', port: 8181 }, () => {
  const readable = net.connect({ host: '127.0.0.1', port: 8080 }, () => {
    readable.pipe(writable);
  });
});
