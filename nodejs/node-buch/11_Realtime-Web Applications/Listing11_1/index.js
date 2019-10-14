const express = require('express');

const app = express();

app.set('views', __dirname + '/app/views');
app.set('view engine', 'pug');

app.get('/', (req, res) => {
  res.render('login');
});

app.listen(8080);
