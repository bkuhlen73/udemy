process.on('unhandledRejection', function(e) {
  console.error(e);
});

function withPromise() {
  return Promise.reject('Whoops, an Error occured');
}

withPromise().then(function() {
  console.log('Promise resolved');
});
