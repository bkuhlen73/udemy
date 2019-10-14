function testBufferToString(test) {
  const myBuffer = Buffer.from('Hello World');

  const result = myBuffer.toString();

  test.equal(result, 'Hello World');

  test.done();
}

module.exports = { testBufferToString };
