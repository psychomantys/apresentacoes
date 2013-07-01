/*global module:false*/
/*jslint es5: true */
module.exports = function(grunt) {

	// Project configuration.
	grunt.initConfig({
	pkg: grunt.file.readJSON('package.json'),
	meta: {
		banner: '/*! <%= pkg.title || pkg.name %> - v<%= pkg.version %> - ' +
			'<%= grunt.template.today("yyyy-mm-dd") %>\n' +
			'<%= pkg.homepage ? " * " + pkg.homepage + "\\n" : "" %>' +
			' * Copyright (c) <%= grunt.template.today("yyyy") %> <%= pkg.author.name %>\n' +
			' * Licensed <%= _.pluck(pkg.licenses, "type").join(", ") %>\n */\n'
	},
	linter: {
		files: [ 'Gruntfile.js', 'package.json',
			'www/js/**/*.js', 'www/js/spec/**/*.js',
			'!www/thirdparty/**/*.js', '!www/js/**/*.min.js',
			'!www/thirdparty/'
		],
		globals: {
			jQuery: true,
			$: true,
			describe: true,
			it: true,
			xdescribe: true,
			xit: true,
			expect: true,
			define: true,
			require: true,
			requirejs: true
		}
	},
	watch: {
		files: ['<config:linter.files>', 'www/js/spec/**/*.js'],
		tasks: 'test'
	},
	uglify: {
		options: {
			mangle: false,
			banner: '<%= meta.banner %>'
		},sorvete_client: {
			files: {
				'www/js/<%= pkg.name %>.min.js': [ 'www/js/sorvete/**/*.js' ]
			}
		}
	}
	});

	grunt.loadNpmTasks('grunt-linter');
	grunt.loadNpmTasks('grunt-volo');

	// Default task
	grunt.registerTask('default', ['test_syntax','min_code','test_tdd']);
//	grunt.registerTask('test_tdd', ['jasmine']);

	// Custom tasks
	grunt.registerTask('test', ['test_syntax','test_tdd']);

	// Resolve and get deps.
	grunt.registerTask('get_deps', ['volo:install']);

	grunt.registerTask('test_syntax', ['linter']);
	grunt.registerTask('min_code', ['requirejs']);
};

