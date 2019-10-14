const assert = require('assert');

const myBuffer = Buffer.from('Hello World');

const result = myBuffer.toString();

assert.strictEqual(result, 'Hello Sun');
