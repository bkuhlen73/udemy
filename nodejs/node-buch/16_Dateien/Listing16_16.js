const fs = require('fs');
const filename = 'input.txt';

fs.stat(filename, (err, stat) => {
  showPerms(err, stat);
  fs.chmod(filename, 0777, err => {
    fs.chown(filename, 0, 0, err => {
      fs.stat(filename, showPerms);
    });
  });
});

function showPerms(err, stat) {
  console.log('User: ' + stat.uid);
  console.log('Gruppe: ' + stat.gid);
  console.log('Permissions: ' + stat.mode.toString(8));
}
