// all the middleware gose here
var middlewareObj = {};

middlewareObj.isLoggedIn = function (req, res, next){
	if(req.isAuthenticated()){
		return next();
	}
	// "error" is the key and "Please Login First" is the content to display
	req.flash("error", "You need to be logged in to do that");
	res.redirect("login");
};

module.exports = middlewareObj