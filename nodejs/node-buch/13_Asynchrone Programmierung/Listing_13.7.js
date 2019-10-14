const spawn = require('child_process').spawn;
const find = spawn('find', ['.', '-iname', 'node'], { cwd: '/usr/local' });
const grep = spawn('grep', ['bin']);

find.stdout.on('data', data => {
  grep.stdin.write(data);
});

find.on('exit', code => {
  grep.stdin.end();
});

grep.stdout.on('data', data => {
  console.log('' + data);
});
