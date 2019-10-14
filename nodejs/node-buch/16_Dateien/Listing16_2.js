const fs = require('fs/promises');

(async () => {
  try {
    const data = await fs.readFile('./input.txt', 'utf-8');
    console.log(data);
  } catch (e) {
    console.error(e);
  }
})();
