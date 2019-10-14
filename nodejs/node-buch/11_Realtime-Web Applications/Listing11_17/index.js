const http = require('http');
const express = require('express');
const cookieSession = require('cookie-session');
const bodyParser = require('body-parser');
const router = require('./app');
const ws = require('./app/websocket');

const app = express();

const server = http.createServer(app);
server.listen(8080);
const io = require('socket.io').listen(server);

const websocket = ws(io);

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
