function asyncOperation(resolve, value, time) {
  return new Promise((res, rej) => {
    setTimeout(() => (resolve ? res(value) : rej(value)), time);
  });
}

console.log('here');

(async () => {
  const hello = await asyncOperation(true, 'Hello', 100);
  const world = await asyncOperation(true, 'World', 10000);
  console.log('some dummy text');
  try {
    await asyncOperation(true, '!', 100);
  } catch (e) {
    console.log(`${hello} ${world}${e}`);
  }
  console.log(`${hello} ${world}`);
})();

console.log('i am.');