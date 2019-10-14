const net = require('net');

const client = net.connect('/tmp/nodejs.sock', () => {
  let count = 0;
  let number = 0;
  let interval = setInterval(() => {
    if (count < 100) {
      number = Math.ceil(Math.random() * 100);
      console.log(number);
      client.write(number.toString());
      count += 1;
    } else {
      clearInterval(interval);
      client.end();
    }
  }, 500);
});

client.on('readable', () => {
  console.log('subtotal: ' + client.read().toString());
});
