var port = 8080;

module.exports = {
	port: port,
	db: 'mongodb://localhost/video_codec',
	facebook: {
		clientID: '1535400743385418',
		clientSecret: 'f73a2e5bde8a020bfbaf0ea28554db46',
		callbackURL: 'http://127.0.0.1:'+ port +'/oauth/facebook/callback'
	},
	twitter: {
		clientID: 'xZLuuDJWQfyicwgvZ0T1m5jPi',
		clientSecret: 'UEWlIw1vG0QfcqYG3taMH3rouUi1gZXJgsYaAFZOYriwhCmmQM',
		callbackURL: 'http://127.0.0.1:'+ port +'/oauth/twitter/callback'
	}
};