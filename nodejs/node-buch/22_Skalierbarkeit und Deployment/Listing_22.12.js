module.exports = function(grunt) {
  grunt.loadNpmTasks('grunt-contrib-nodeunit');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-jslint');

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
  });
};
