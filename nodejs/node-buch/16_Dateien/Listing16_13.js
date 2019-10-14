const fs = require('fs');

fs.stat('/usr/local/bin/node', (err, stat) => {
  console.log(`Size of the file "/usr/local/bin/node" is ${stat.size} Bytes`);
});
