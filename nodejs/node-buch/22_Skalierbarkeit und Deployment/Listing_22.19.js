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
    uglify: {
      businessRoutines: {
        files: {
          'public/js/logic.min.js': ['src/js/*.js'],
        },
      },
    },
    jslint: {
      files: ['src/js/*.js'],
    },
    watch: {
      files: ['src/js/*.js'],
      tasks: ['jslint'],
    },
  });

  grunt.registerTask('default', ['nodeunit', 'cssmin', 'uglify', 'jslint']);
};
