const childProcess = require('child_process');
const child1 = childProcess.fork('logic1.js');
const child2 = childProcess.fork('logic2.js');

let receivedChild1Response = false;
let receivedChild2Response = false;

function handleResults() {
  // wird nach child1 und child2 ausgeführt
}

child1.on('message', data => {
  receivedChild1Response = true;

  // logic to handle child1 result

  if (receivedChild1Response && receivedChild2Response) {
    // handle final results
    handleResults();
  }
});

child2.on('message', data => {
  receivedChild2Response = true;

  // logic to handle child2 result

  if (receivedChild1Response && receivedChild2Response) {
    // handle final results
    handleResults();
  }
});
