const wc = require('./word-count');
const sentence = 'Wo viel Licht ist, ist auch viel Schatten.';
const wordCount = wc(sentence);
console.log(sentence);
for (var i in wordCount) {
  console.log(wordCount[i] + ' x ' + i);
}
