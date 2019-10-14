const fs = require('fs');

fs.stat('./input.txt', (err, stat) => {
  if (err) {
    console.error(err);
  }
  console.log(stat);
});

fs.access('./input.txt', fs.R_OK, err => {
  if (!err) {
    console.log('file is readable');
  }
});
