const model = require('./model');
const view = require('./view');
const form = require('./form');

function listAction(request, response) {
  model.getAll(request.user.id).then(
    movies => {
      response.render(__dirname + '/views/list', { movies });
    },
    error => response.send(error),
  );
}

function deleteAction(request, response) {
  const id = parseInt(request.params.id, 10);
  model
    .delete(id, request.user.id)
    .then(
      () => response.redirect(request.baseUrl),
      error => response.send(error),
    );
}

function formAction(request, response) {
  const movie = { id: '', title: '', year: '', public: '' };

  if (request.params.id) {
    model
      .get(parseInt(request.params.id, 10), request.user.id)
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
    public: request.body.public === '1' ? 1 : 0,
  };
  model.save(movie, request.user.id).then(
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
