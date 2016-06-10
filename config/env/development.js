var port = 8080;

module.exports = {
	port: port,
	db: 'mongodb://localhost/video_codec',
	facebook: {
		clientID: '1535400743385418',
		clientSecret: 'f73a2e5bde8a020bfbaf0ea28554db46',
		callbackURL: 'http://localhost:'+ port +'/oauth/facebook/callback'
	},
	twitter: {
		clientID: 'wtmsGNlyNSds02UH4sPpr90KN',
		clientSecret: '3mfd5EYHhvkdcIDFH7tMT6SFLoKfSwnWkH9HdONqGxmuBYTQ78',
		callbackURL: 'http://localhost:'+ port +'/oauth/twitter/callback'
	}
};