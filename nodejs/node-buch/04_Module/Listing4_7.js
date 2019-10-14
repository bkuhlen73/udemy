let counter = 1;
const interval = setInterval(function() {
  console.log(`${counter} iteration`);
  if (counter++ > 2) {
    clearInterval(interval);
  }
}, 1000);
