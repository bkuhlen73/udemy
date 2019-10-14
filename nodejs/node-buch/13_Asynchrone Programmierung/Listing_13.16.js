function asyncOperation(resolve, value, time) {
  return new Promise((res, rej) => {
    setTimeout(() => (resolve ? res(value) : rej(value)), time);
  });
}

Promise.all([
  asyncOperation(true, 'World', 100),
  asyncOperation(true, 'Hello', 50),
]).then(values => {
  console.log(values.join(' '));
});