const dgram = require('dgram');
const client = dgram.createSocket('udp6');
let count = 1;

const sendData = () => {
  const message = Buffer.from(Math.ceil(Math.random() * 100) + '');

  client.send(message, 0, message.length, 8080, (err, bytes) => {
    count += 1;

    if (count > 1000 || err) {
      client.close();
      clearInterval(interval);
    }
  });
};

const interval = setInterval(sendData, 1);
