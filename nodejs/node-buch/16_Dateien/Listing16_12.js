const fs = require('fs');

class Explorer {
  constructor() {
    process.stdin.resume();
    process.stdin.setEncoding('utf8');
    process.stdin.on('data', this.dispatch.bind(this));
  }

  dispatch(chunk) {
    const result = chunk.match(/(\w*) (.*)/);
    let command = 'exit';
    let path = '';

    if (result !== null) {
      command = result[1];
      path = result[2];
    }

    switch (command) {
      case 'list':
        this.display(path);
        break;
      case 'change':
        process.chdir(path);
        this.listCurrent();
        break;
      case 'file':
        fs.writeFile(path, this.listCurrent.bind(this));
        break;
      case 'remove':
        fs.stat(path, (err, stat) => {
          if (stat.isFile()) {
            fs.unlink(path, this.listCurrent.bind(this));
          } else if (stat.isDirectory()) {
            fs.rmdir(path, this.listCurrent.bind(this));
          }
        });
        break;
      case 'directory':
        fs.mkdir(path, this.listCurrent.bind(this));
        break;
      case 'rename':
        var paths = path.split(' ');
        fs.rename(paths[0], paths[1], this.listCurrent.bind(this));
        break;
      default:
        process.exit();
        break;
    }
  }
  listCurrent() {
    this.dispatch('list ' + process.cwd());
  }

  display(path) {
    console.log(`Aktuelles Verzeichnis: ${process.cwd()}\n\n`);

    fs.readdir(path, (err, files) => {
      let result = '';

      for (let i = 0; i < files.length; i++) {
        result += files[i] + '\t';
        if ((i + 1) % 4 === 0) {
          result += '\n';
        }
      }

      let diff = process.stdout.rows - files.length;
      if (diff > 0) {
        for (let i = 0; i < diff; i++) {
          result += '\n';
        }
      }

      console.log(`${result}

Verfügbare Kommandos:
list, change, file, remove, directory, rename, exit
Ihre Eingabe: `);
    });
  }
}

var explorer = new Explorer();
explorer.listCurrent();
