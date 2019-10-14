const exec = require('child_process').exec;
const cmd = 'find /usr/local -iname "node"';

exec(cmd, (err, stdout, stderr) => {
  if (err) throw err;

  console.log(stdout);
});
