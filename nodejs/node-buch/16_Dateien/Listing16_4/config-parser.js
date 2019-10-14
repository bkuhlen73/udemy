const fs = require('fs');
const filename = 'config.json';

function configParser(env) {
  return new Promise((resolve, reject) => {
    fs.open(filename, 'r', (err, handle) => {
      fs.stat(filename, (err, stats) => {
        const size = stats.size;
        const buffer = new Buffer.alloc(size);
        fs.read(handle, buffer, 0, size, 0, (err, bytes, content) => {
          fs.close(handle, err => {
            const config = JSON.parse(content);
            if (config.hasOwnProperty(env)) {
              resolve(config[env]);
            } else {
              reject(`Section ${env} does not exist`);
            }
          });
        });
      });
    });
  });
}

configParser('production').then(config => {
  console.log('Production: ', config);
});
configParser('development').then(config => {
  console.log('Development: ', config);
});
configParser('test').catch(e => {
  console.log(e);
});
