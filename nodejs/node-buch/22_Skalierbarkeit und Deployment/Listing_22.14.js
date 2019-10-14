module.exports = function(grunt) {
  require('load-grunt-tasks')(grunt);

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    nodeunit: {
      all: ['test/*_test.js'],
    },
    cssmin: {
      compress: {
        files: {
          'public/css/min.css': ['src/css/*.css'],
        },
      },
    },
  });
};
