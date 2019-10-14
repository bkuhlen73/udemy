const cluster = require('cluster');

if (cluster.isMaster) {
  cluster.setupMaster({ silent: true });

  setTimeout(cluster.disconnect, 2000);

  cluster.on('exit', function() {
    console.log('Worker wurden nach 2000ms beendet');
  });

  cluster.fork();
  cluster.fork();
}

if (cluster.isWorker) {
  const http = require('http');
  http
    .createServer((req, res) => {
      console.log('Worker ' + cluster.worker.id);
      res.end('Worker ' + cluster.worker.id);
    })
    .listen('8080');
}
