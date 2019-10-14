const dgram = require('dgram');
const socket = dgram.createSocket('udp6');

socket.on('message', data => {
  console.log(data.toString());
});

socket.bind(8080, () => {
  console.log('server listening on localhost:8080');
});
