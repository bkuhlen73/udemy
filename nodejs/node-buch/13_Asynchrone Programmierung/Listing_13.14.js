const http = require('http');

function doRequest(url) {
  return new Promise(function(resolve, reject) {
    const options = {
      hostname: url,
      port: 80,
      method: 'GET',
    };
    const req = http.request(options, res => {
      res.setEncoding('utf8');
      let data = '';
      res.on('data', chunk => (data += chunk));
      res.on('end', () => resolve(data));
      res.on('error', e => reject(e));
    });
    req.end();
  });
}

doRequest('www.google.de').then(
  function success(data) {
    console.log('data: ', data);
  },
  function failure(err) {
    console.log('error: ', err);
  },
);
