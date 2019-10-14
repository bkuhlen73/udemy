function getName(connections, socket) {
  let name;
  for (const key in connections) {
    if (socket === connections[key]) {
      name = key;
    }
  }
  return name;
}

function init(io) {
  const connections = {};

  io.sockets.on('connection', socket => {
    socket.on('msg', message => {
      const name = getName(connections, socket);

      const msg = {
        name,
        msg: message.msg,
      };

      socket.emit('msg', msg);
      socket.broadcast.emit('msg', msg);
    });

    socket.on('join', function(message) {
      const name = getName(connections, socket);

      connections[message.name] = socket;

      var msg = { names: Object.keys(connections) };

      socket.emit('join', msg);
      socket.broadcast.emit('join', msg);
    });
  });

  return {
    logout(user) {
      connections[user].broadcast.emit('msg', msg);
      connections[user].close();
      delete connections[user];

      var msg = JSON.stringify({
        type: 'join',
        names: Object.keys(connections),
      });
    },
  };
}

module.exports = init;
