const fs = require('fs');
fs.open('input.txt', 'wx+', (e, fd) => {
  if (e) throw e;
  console.log(fd);
});
