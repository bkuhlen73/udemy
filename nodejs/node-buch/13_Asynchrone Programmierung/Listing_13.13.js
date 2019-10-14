const fs = require('fs');

function readFile(filename) {
  return new Promise((resolve, reject) => {
    fs.readFile(filename, 'utf-8', (err, data) => {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  });
}

readFile('input.txt').then(
  data => {
    console.log('Content of the file: ', data);
  },
  error => {
    console.log('An error occured: ', error.message);
  },
);
