const fs = require('fs/promises');
const filename = 'config.json';

async function configParser(env) {
  const content = await fs.readFile(filename, 'utf-8');
  const config = JSON.parse(content);
  if (config.hasOwnProperty(env)) {
    return config[env];
  } else {
    throw new Error(`Section ${env} does not exist`);
  }
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
