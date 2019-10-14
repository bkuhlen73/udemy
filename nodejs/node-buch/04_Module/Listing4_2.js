const fs = require('fs');

fs.readFile('input.txt', function(err, data) {
  console.log(data);
  console.log(data.toString());
});
