const assert = require('assert');
const add = require('./add');

assert.throws(() => add('1', 2), Error);
