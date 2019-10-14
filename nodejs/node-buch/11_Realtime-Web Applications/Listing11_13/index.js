const express = require('express');
const cookieSession = require('cookie-session');
const bodyParser = require('body-parser');
const router = require('./app');
const ws = require('./app/websocket');

const websocket = ws();

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

app.use(router(websocket));

app.listen(8080);
