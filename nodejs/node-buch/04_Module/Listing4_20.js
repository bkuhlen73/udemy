module.exports = function(DEBUG) {
  return {
    options: {
      outputStyle: DEBUG ? 'expanded' : 'compressed',
      sourceMap: DEBUG,
      sourceMapEmbed: true,
    },
    files: {
      'style/style.css': 'style/style.scss',
    },
  };
};
