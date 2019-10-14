function withoutGroup(test) {
  const buffer = Buffer.from('Hello World');

  const result = buffer.toString();

  test.equals(result, 'Hello World');
  test.done();
}

const buffer = {
  setUp(callback) {
    this.buffer = Buffer.from('Hello World');
    callback();
  },

  toString(test) {
    const result = this.buffer.toString();

    test.equals(result, 'Hello World');
    test.done();
  },
};

const path = {
  normalize(test) {
    const path = '/tmp/../etc/';

    const result = require('path').normalize(path);

    test.equals(result, '/etc/');
    test.done();
  },
};

module.exports = {
  withoutGroup,
  buffer,
  path,
};
