enum Status {
  open,
  done,
}

const task = {
  title: 'get up',
  status: Status.done,
};

if (task.status === Status.done) {
  console.log('Erledigt');
}
