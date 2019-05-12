////////////////////////////////
//Setup//
////////////////////////////////

// Plugins
var gulp = require('./node_modules/gulp'),
    pjson = require('./package.json.js'),
    gutil = require('./node_modules/gulp-util'),
    sass = require('./node_modules/gulp-sass'),
    autoprefixer = require('./node_modules/gulp-autoprefixer'),
    cssnano = require('./node_modules/gulp-cssnano'),
    rename = require('./node_modules/gulp-rename'),
    del = require('./node_modules/del'),
    plumber = require('./node_modules/gulp-plumber'),
    pixrem = require('./node_modules/gulp-pixrem'),
    uglify = require('./node_modules/gulp-uglify'),
    imagemin = require('./node_modules/gulp-imagemin'),
    spawn = require('child_process').spawn,
    runSequence = require('./node_modules/run-sequence'),
    browserSync = require('./node_modules/browser-sync').create(),
    reload = browserSync.reload;


// Relative paths function
var pathsConfig = function(appName) {
    this.app = "./" + (appName || pjson.name);

    return {
        app: this.app,
        templates: this.app + '/templates',
        css: this.app + '/static/css',
        sass: this.app + '/static/sass',
        fonts: this.app + '/static/fonts',
        images: this.app + '/static/images',
        js: this.app + '/static/js'
    }
};

var paths = pathsConfig();

////////////////////////////////
//Tasks//
////////////////////////////////

// Javascript minification
gulp.task('scripts', function() {
    return gulp.src(paths.js + '/project.js')
        .pipe(plumber()) // Checks for errors
        .pipe(uglify()) // Minifies the js
        .pipe(rename({ suffix: '.min' }))
        .pipe(gulp.dest(paths.js));
});

// Image compression
gulp.task('imgCompression', function() {
    return gulp.src(paths.images + '/*')
        .pipe(imagemin()) // Compresses PNG, JPEG, GIF and SVG images
        .pipe(gulp.dest(paths.images))
});

// Run django server
gulp.task('runServer', function(cb) {
    var cmd = spawn('python', ['manage.py', 'runserver'], { stdio: 'inherit' });
    cmd.on('close', function(code) {
        console.log('runServer exited with code ' + code);
        cb(code);
    });
});

// Browser sync server for live reload
gulp.task('browserSync', function() {
    browserSync.init(
        [paths.css + "/*.css", paths.js + "*.js", paths.templates + '*.html'], {
            proxy: "localhost:8000"
        });
});

// Watch
gulp.task('watch', function() {

    gulp.watch(paths.sass + '/*.scss').on("change", reload);
    gulp.watch(paths.js + '/*.js', ['scripts']).on("change", reload);
    gulp.watch(paths.images + '/*', ['imgCompression']);
    gulp.watch(paths.templates + '/**/*.html').on("change", reload);

});

// Default task
gulp.task('default', function() {
    runSequence(['scripts', 'imgCompression'], ['runServer', 'browserSync', 'watch']);
});