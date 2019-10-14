const assert = require('assert');
const asyncFunction = require('./asyncModule');

assert.rejects(() => asyncFunction(false, 'Fail!'));
