var express		= require("express"),
	router		= express.Router(),
	User		= require("../models/users"),
	Product		= require("../models/products"),
	middleware	= require("../middleware/index")

// handle myAccount show router
router.get("/user/:id", function(req, res){
	User.findById(req.params.id, function(err, foundUser){
		if(err){
			res.redirect("/")
		}else{
			console.log(foundUser);
			res.render("user/show",{foundUser:foundUser});
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
