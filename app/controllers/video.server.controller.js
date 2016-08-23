var Video = require('mongoose').model('Video'),
passport = require('passport'),
path = require('path'),
fs = require('fs');

var User = require('../models/user.server.model');
exports.list = function(req, res) {
	res.render('upload', {
   title: 'VIDEO CODEC',
   user: req.user ? req.user.username : ''
 })};
  var randomID = function()
  {
    var text = "";
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    for( var i=0; i < 9; i++ )
      text += possible.charAt(Math.floor(Math.random() * possible.length));

    return text;
  };
  exports.single = function(req, res){
    var v_flag = false;
    

    try{
      d=fs.statSync('./app/uploads/min/'+ req.params.url + ".mkv");
    v_flag = true;
  }catch(e){
    console.log("error")
  }

  res.render('single', {
    vid_src: '/uploads/'+ req.params.url + ".mkv",
    vid_flag: v_flag
  });
}

exports.uploads = function(req, res) {
            // create an incoming form object
            var form = new formidable.IncomingForm();

      // specify that we want to allow the user to upload multiple files in a single request
      form.multiples = true;

      // store all uploads in the /uploads directory
      form.uploadDir = path.join(__dirname, '../uploads');

      // every time a file has been uploaded successfully,
      // rename it to it's orignal name
      var newID = randomID();
      form.on('file', function(field, file) {
        fs.rename(file.path, path.join(form.uploadDir, newID + ".mp4"));
      });

      // log any errors that occur
      form.on('error', function(err) {
        console.log('An error has occured: \n' + err);
        res.redirect('/video');
      });

      // once all the files have been uploaded, send a response to the client
      form.on('end', function() {
        var exec = require('child_process').exec;

var child = exec('/home/nishan/Documents/Temp/vco/app/uploads/script.sh '+newID+".mp4", function(error, stdout, stderr) {
  if (error) console.log(error);
  process.stdout.write(stdout);
  process.stderr.write(stderr);
});
        res.end(newID);
      });

      // parse the incoming request containing the form data
      form.parse(req);
      
    } 

