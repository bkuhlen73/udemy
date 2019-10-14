const fork = require('child_process').fork;

if (process.argv[2] && process.argv[2] === 'child') {
  console.log('Child Process');
} else {
  console.log('Parent Process');
  fork(process.argv[1], ['child']);
}
