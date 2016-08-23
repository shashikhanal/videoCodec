var mongoose = require('mongoose'),
	crypto = require('crypto'),
	Schema = mongoose.Schema,
	path = require('path');

var VideoSchema = new Schema({
    title:          { type: String },
    description:    { type: String },
    filename:       { type: String },
    
});
VideoSchema.virtual('uniqueId')
    .get(function() {
        return this.filename.replace(path.extname(this.filename), '');
    });


mongoose.model('Video', VideoSchema);