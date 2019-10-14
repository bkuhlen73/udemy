const model = require('./model');
const view = require('./view');
const form = require('./form');

function listAction(request, response) {
  model.getAll().then(
    movies => {
      response.render(__dirname + '/views/list', { movies });
    },
    error => response.send(error),
  );
}

function deleteAction(request, response) {
  const id = parseInt(request.params.id, 10);
  model
    .delete(id)
    .then(
      () => response.redirect(request.baseUrl),
      error => response.send(error),
    );
}

function formAction(request, response) {
  let movie = { id: '', title: '', year: '' };

  if (request.params.id) {
    model
      .get(parseInt(request.params.id, 10))
      .then(movie => response.send(form(movie)), error => response.send(error));
  } else {
    const body = form(movie);
    response.send(body);
  }
}

function saveAction(request, response) {
  const movie = {
    id: request.body.id,
    title: request.body.title,
    year: request.body.year,
  };
  model.save(movie).then(
    () => {
      response.redirect(request.baseUrl);
    },
    error => {
      response.send(error);
    },
  );
}

module.exports = {
  listAction,
  deleteAction,
  formAction,
  saveAction,
};
