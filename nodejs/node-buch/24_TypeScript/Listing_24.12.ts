function defaultParameters(a: number, b = 4): number {
  return a + b;
}

console.log(defaultParameters(2));

function optionalParameters(a: number, b?: number): number {
  return b !== undefined ? a + b : a;
}

console.log(optionalParameters(2));

function restParameters(a: number, ...more: number[]) {
  return more.reduce((prev, curr) => prev + curr, a);
}

console.log(restParameters(1, 2, 3));
