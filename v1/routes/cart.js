var express 	= require("express"),
	router		= express.Router(),
	cart		= require("../models/cart"),
	User		= require("../models/users"),
	middleware  = require("../middleware/index")

// if not login, redirect to login page
router.get("/cart", function(req, res){
	res.render("login")
})

// show router
router.get("/cart/:id", middleware.isLoggedIn, function(req, res){
	User.findOne({username:"Wu"}).populate("Product").exec(function(err, foundUser){
		if(err){
			console.log(err);
		}else{
			console.log(foundUser);
			res.render("cart/show",{foundUser:foundUser});
		}
	})
})

// handle myAccount update router
// router.get("/user/:id/edit", function(req, res){
// 	User.findById(req.params.id, function(err, ){
		
// 	})
// 	res.render("user/edit");
// })

module.exports = router;
