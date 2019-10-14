module.exports = function add(a, b) {
  if (typeof a !== 'number' || typeof b !== 'number') {
    throw new Error('Bitte nur Zahlen nutzen');
  }
  return a + b;
};
