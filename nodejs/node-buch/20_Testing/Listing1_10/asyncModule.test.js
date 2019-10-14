const assert = require('assert');
const asyncFunction = require('./asyncModule');

(async () => {
  const data = await asyncFunction(true, 'Hello World');
  assert.strictEqual(data, 'Hello World');
})();
