const Router = require('express').Router;
const {
  listAction,
  deleteAction,
  formAction,
  saveAction,
  rateAction,
} = require('./controller');

const router = Router();

router.get('/', listAction);
router.get('/delete/:id', deleteAction);
router.get('/form/:id?', formAction);
router.post('/save', saveAction);
router.get('/rate/:movie/:rating', rateAction);

module.exports = router;
