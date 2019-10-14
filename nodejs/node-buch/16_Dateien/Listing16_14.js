const fs = require('fs');
const file = 'error.log';

const watcher = fs.watch('error.log', event => {
  console.log(`${file} has been ${event}d`);
  watcher.close();
});
