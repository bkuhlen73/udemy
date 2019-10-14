const assert = require('assert');
const asyncFunction = require('./asyncModule');

asyncFunction(true, 'Hello World').then(data => {
  assert.strictEqual(data, 'Hello World');
});
