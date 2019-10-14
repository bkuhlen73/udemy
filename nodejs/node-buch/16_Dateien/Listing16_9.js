const fs = require('fs');
fs.open('/gibt-es-nicht.txt', 'r', (err, handle) => {
  if (err) throw err;
});
