function asyncOperation(resolve, value, time) {
  return new Promise((res, rej) => {
    setTimeout(() => (resolve ? res(value) : rej(value)), time);
  });
}

(async () => {
  const hello = await asyncOperation(true, 'Hello', 100);
  const world = await asyncOperation(true, 'World', 100);
  try {
    await asyncOperation(false, '!', 100);
  } catch (e) {
    console.log(`${hello} ${world}${e}`);
  }
})();
