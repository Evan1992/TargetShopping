// seperate routers with app.js
var express    	= require("express"),
	router     	= express.Router(),
	Product    	= require("../models/products"),
	User       	= require("../models/users"),
	passport   	= require("passport")

// Root Route
router.get("/", function(req, res){
	// get all products from DB
	Product.find({}, function(err, allProducts){
		if(err){
			console.log(err)
		}else{
			res.render("landing", {products:allProducts});
		}
	});
});

//======================
// AUTHENTICATION ROUTES
//======================
router.get("/login", function(req, res){
	res.render("login")
});

// handle login logic
// app.post("/login", middleware, callback)
// passport.use(new localStrategy(User.authenticate()));
router.post("/login", passport.authenticate("local", 
	{
		successRedirect: "/",
		failureRedirect: "login"
	}), function(req, res){
});

router.get("/logout", function(req, res){
	req.logout();
	res.redirect("/");
})


// show register form
router.get("/register", function(req, res){
	res.render("register");
});

// handle register logic
router.post("/register", function(req, res){
	/* do not pass password to user, because we have to 
	   hash the password instead of using it directly */
	var newUser = new User({username: req.body.username});
	// User.register is a function from passportLocalMongoose package
	User.register(newUser, req.body.password, function(err, user){
		if(err){
			console.log(err);
			// req.flash("error", err.message);
			return res.render("register")
		}
		// console.log("success");
		passport.authenticate("local")(req, res, function(){
			// console.log("success")
			// req.flash("success", "Welcome to YelpCamp " + user.username);
			res.redirect("/");
		});
	});
	res.redirect("/");
})

router.post("/addlink", function(req, res){
	var exec = require('child_process').exec;
	var cmd = 'python crawler/crawler.py ' + req.body.link;
	exec(cmd, function(err,stdout,stderr){
		if (err){
			console.log('Python error: '+stderr);
		} else {
			var dic = JSON.parse(stdout);
			
		}
	});
	// res.redirect("/");
})

// handle myAccount
// router.get("/user/:id", function(req, res){
// 	User.findById(req.params.id, function(err, foundUser){
// 		if(err){
// 			res.redirect("/")
// 		}else{
// 			res.render("user",{user:foundUser});
// 		}
// 	})
// })

module.exports = router;
