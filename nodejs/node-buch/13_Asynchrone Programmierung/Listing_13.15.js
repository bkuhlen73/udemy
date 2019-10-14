function asyncOperation(resolve, value, time) {
  return new Promise((res, rej) => {
    setTimeout(() => (resolve ? res(value) : rej(value)), time);
  });
}

asyncOperation(true, 'Hello', 100)
  .then(data => {
    console.log(data + ' ');
    return asyncOperation(true, 'World', 200);
  })
  .then(data => {
    console.log(data);
    //return new Error();
    return '!';
  })
  .then(data => {
    console.log(data);
  })
  .catch(err => {
    console.log('myError: ', err);
  });