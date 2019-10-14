const { Service } = require('node-windows');
const service = new Service({
  name: 'Node.js Webserver',
  description: 'Webserver listening on port 80.',
  script: 'C:\\srv\\app\\index.js',
});

service.on('install', () => {
  service.start();
});

service.install();
