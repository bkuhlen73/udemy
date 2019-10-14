const dgram = require('dgram');
const socket = dgram.createSocket('udp6');
let count = 0;

socket.on('message', data => {
  console.log(`${count++}: ${data.toString()}`);

  if (count >= 1000) {
    socket.close();
  }
});

socket.on('close', () => {
  console.log(`received ${count} datagrams`);
});

socket.bind(8080, () => {
  console.log('server listening on localhost:8080');
});
