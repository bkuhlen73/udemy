const execFile = require('child_process').execFile;

execFile('./input.sh', (err, stdout, stderr) => {
  console.log(stdout);
});
