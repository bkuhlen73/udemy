const fs = require('fs');
const filename = 'config.json';

function configParser(env) {
  return new Promise((resolve, reject) => {
    fs.readFile(filename, 'utf-8', (err, content) => {
      const config = JSON.parse(content);
      if (config.hasOwnProperty(env)) {
        resolve(config[env]);
      } else {
        reject(`Section ${env} does not exist`);
      }
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
