var express		= require("express"),
	router		= express.Router(),
	User		= require("../models/users"),
	Product		= require("../models/products"),
	middleware	= require("../middleware/index")

// add products to user
router.post("/user/:id", function(req, res){
	User.findById(req.params.id, function(err, foundUser){
		if(err){
			console.log(err);
			res.redirect("/")
		}else{
			Product.findById(req.body.productInCart, function(err, product){
				foundUser.cart.push(product);
				foundUser.save(function(err, data){
					if(err){
						console.log(err);
					}else{
						console.log(data);
					}
				})
			})
			res.redirect("/")
		}
	})
})

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
