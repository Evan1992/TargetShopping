var express 	= require("express"),
	router		= express.Router(),
	User		= require("../models/users"),
	middleware  = require("../middleware/index")

// if not login, redirect to login page
router.get("/cart", function(req, res){
	res.render("login")
})

// show router
// middleware.isLoggedIn to make sure the user is logged in
router.get("/cart/:id", middleware.isLoggedIn, function(req, res){
	User.findOne({username:"Wu"}).populate("cart").exec(function(err, foundUser){
		if(err){
			console.log(err);
		}else{
			console.log(foundUser);
			res.render("cart/show",{foundUser:foundUser});
		}
	})
})

// Story.
//   findOne({ title: 'Casino Royale' }).
//   populate('author').
//   exec(function (err, story) {
//     if (err) return handleError(err);
//     console.log('The author is %s', story.author.name);
//     // prints "The author is Ian Fleming"
//   });

// handle myAccount update router
// router.get("/user/:id/edit", function(req, res){
// 	User.findById(req.params.id, function(err, ){
		
// 	})
// 	res.render("user/edit");
// })

module.exports = router;
