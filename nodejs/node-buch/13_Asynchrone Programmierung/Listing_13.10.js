const fork = require('child_process').fork;

if (process.argv[2] && process.argv[2] === 'child') {
  process.on('message', data => {
    console.log('in child process: ' + data);
  });
} else {
  const child = fork(process.argv[1], ['child']);

  for (let i = 0; i < 10; i += 1) {
    child.send(i);
  }
  child.disconnect();
}
