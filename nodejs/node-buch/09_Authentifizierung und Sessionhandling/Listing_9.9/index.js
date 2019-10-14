const express = require('express');
const morgan = require('morgan');
const bodyParser = require('body-parser');
const { ensureLoggedIn } = require('connect-ensure-login');
const movieRouter = require('./movie');
const auth = require('./auth');

const app = express();

app.set('view engine', 'pug');

app.use(express.static('public'));

app.use(bodyParser.urlencoded({ extended: false }));

auth(app);

app.get('/', (request, response) => response.redirect('/movie'));

app.use(morgan('common', { immediate: true }));

app.use('/movie', ensureLoggedIn('/login.html'), movieRouter);

app.listen(8080, () => {
  console.log('Server is listening to http://localhost:8080');
});
