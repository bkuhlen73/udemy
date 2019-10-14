const fs = require('fs');
const EventEmitter = require('events');
const util = require('util');

class EventLogger extends EventEmitter {
  constructor(file, levels) {
    super();
    this.file = file;
    this.levels = levels;

    this.on('error', this.log.bind(this, 'ERR'));
    this.on('warning', this.log.bind(this, 'WARN'));
    this.on('info', this.log.bind(this, 'INFO'));
  }

  log(level, data) {
    if (this.levels.indexOf(level) > -1) {
      fs.open(this.file, 'a', (err, handle) => {
        var buffer = Buffer.from(
          util.format('%s (%s) %s\n', new Date(), level, data),
        );
        fs.write(
          handle,
          buffer,
          0,
          buffer.length,
          null,
          (err, written, buffer) => {
            fs.close(handle, () => {});
          },
        );
      });
    }
  }
}

var logger = new EventLogger('error.log', ['ERR', 'WARN']);

logger.emit('error', 'Something happened');
logger.emit('warning', 'Something else happened');
logger.emit('info', 'Not relevant');
