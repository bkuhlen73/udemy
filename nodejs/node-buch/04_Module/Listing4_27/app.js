require('./my-module');
delete require.cache[require.resolve('./my-module')];
require('./my-module');
