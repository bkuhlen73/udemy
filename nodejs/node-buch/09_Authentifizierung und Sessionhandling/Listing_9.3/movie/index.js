const Router = require('express').Router;
const {
  listAction,
  deleteAction,
  formAction,
  saveAction,
} = require('./controller');

const router = Router();

router.get('/', listAction);
router.get('/delete/:id', deleteAction);
router.get('/form/:id?', formAction);
router.post('/save', saveAction);

module.exports = router;
