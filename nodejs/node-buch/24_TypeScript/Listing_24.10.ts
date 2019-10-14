let age: number | string;

age = 42; // ok
age = '42'; // ok
age = true; // fehler

if (age.isInteger()) {
} // fehler, isInteger existiert nur für number

const items: (number | string)[] = [];
items.push(1); // ok
items.push('Hello'); // ok
items.push(true); // fehler
