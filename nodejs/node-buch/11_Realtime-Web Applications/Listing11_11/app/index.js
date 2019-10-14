const Router = require('express').Router;
const checkAuth = require('./check-auth');

const router = Router();

router.get('/', (req, res) => {
  res.render('login');
});

router.post('/login', (req, res) => {
  const user = req.body.username;
  const pw = req.body.password;

  if (user === 'u1' && pw === 'test') {
    req.session.user = 'u1';
  } else if (user === 'u2' && pw === 'test') {
    req.session.user = 'u2';
  }

  res.redirect('/chat');
});

router.get('/chat', checkAuth, (req, res) => {
  res.render('chat', { user: req.session.user });
});

router.get('/logout', (req, res) => {
  delete req.session.user;
  res.redirect('/');
});

module.exports = router;
