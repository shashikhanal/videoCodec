process.env.NODE_ENV = process.env.NODE_ENV || 'development';

var config = require('./config/config'), //development.js->mongo and social media conf
	mongoose = require('./config/mongoose'), //connect mongoose
	express = require('./config/express'), //express and routes conf  
	passport = require('./config/passport'); //social media req

var db = mongoose(),
	app = express(),
	passport = passport();

app.listen(config.port);
module.exports = app;
console.log(process.env.NODE_ENV + ' server running at http://localhost:' + config.port);