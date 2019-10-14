const cluster = require('cluster');
const http = require('http');

if (cluster.isMaster) {
  cluster.fork();
  cluster.fork();

  cluster.on('listening', worker => {
    console.log(`Worker ${worker.id} ready and listening`);

    setTimeout(() => {
      worker.send('Hello Worker');
    }, 2000);
  });

  for (let i in cluster.workers) {
    cluster.workers[i].on(
      'message',
      function(i, msg) {
        console.log(`Worker ${i} said: ${msg}`);
      }.bind(this, i),
    );
  }
} else {
  http
    .createServer((req, res) => {
      res.end('Hello Client');
    })
    .listen('8080');

  cluster.worker.on('message', msg => {
    console.log(`Master said to Worker ${cluster.worker.id}: ${msg}`);
  });

  cluster.worker.send('Hello Master');
}
