const socket = new WebSocket('ws://localhost:8181/');

socket.send('Hello Server');

socket.onmessage = msg => {
  console.log(msg.data);
};
