var videos = require('../../app/controllers/video.server.controller'),
	passport = require('passport');

module.exports = function(app) {
	app.route('/video').get(videos.list);
	app.route('/upload').post(videos.uploads);	
	app.route('/video/single/:url').get(videos.single);				
};