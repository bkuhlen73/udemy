const fs = require('fs');

fs.stat('input.txt', (err, stat) => {
  console.log('User: ' + stat.uid);
  console.log('Gruppe: ' + stat.gid);
  console.log('Permissions: ' + stat.mode.toString(8));
});
