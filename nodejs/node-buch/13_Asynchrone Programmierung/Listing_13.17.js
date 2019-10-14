function asyncOperation(resolve, value, time) {
  return new Promise((res, rej) => {
    setTimeout(() => (resolve ? res(value) : rej(value)), time);
  });
}

Promise.race([
  asyncOperation(true, 'First', 100),
  asyncOperation(true, 'Second', 50),
  asyncOperation(true, 'Third', 75),
]).then(value => {
  console.log(value);
});
