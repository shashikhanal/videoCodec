exports.render = function(req, res) {
    res.render('index', {
    	title: 'VIDEO CODEC',
    	user: req.user ? req.user.username : ''
    });
};