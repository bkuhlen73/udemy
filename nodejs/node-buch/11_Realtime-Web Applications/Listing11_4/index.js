const express = require('express');
const cookieSession = require('cookie-session');
const bodyParser = require('body-parser');

const app = express();

app.use(
  cookieSession({
    name: 'session',
    keys: ['key1', 'key2'],
  }),
);
app.use(bodyParser.urlencoded({ extended: false }));

app.set('views', __dirname + '/app/views');
app.set('view engine', 'pug');

app.get('/', (req, res) => {
  res.render('login');
});

app.listen(8080);
