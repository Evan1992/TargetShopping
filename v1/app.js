var express    		= require("express"),
	app        		= express(),
	bodyParser 		= require("body-parser"),
	passport   		= require("passport"),
	LocalStrategy 	= require("passport-local"),
	flash      		= require("connect-flash"),
	mongoose   		= require("mongoose"),
	Product    		= require("./models/products"),
	User			= require("./models/users"),
	seedDB     		= require("./seeds")


// connect to the database
// if there is no database called "TargetShopping", it will create one automatically
mongoose.connect("mongodb://localhost/TargetShopping");

// with bodyParser, we can use the data from the form in view page through post
/* e.g. we can use the username and password from register page
to add a new user to database */
app.use(bodyParser.urlencoded({extended:true}));
// no necessary to add ".ejs" for ejs file after following setting
app.set("view engine", "ejs");

// Passport Configuration
app.use(require("express-session")({
	// secret can be anything at all
	// it is used to encode and decode the sessions
	secret:"Once again Rusty wins cutest dog!",
	resave: false,
	saveUnintialized: false
}));
app.use(passport.initialize());
app.use(passport.session());
// all the methods of User come from passport-local-mongoose
passport.use(new LocalStrategy(User.authenticate()));
/* deserializeUser is responsible for reading
the session that is encoded and decode it */
/* serializeUser is responsible for encoding it
and putting it back in the session */
// User.serializeUser(), this function is from passportLocalMongoose
passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());

seedDB();

// global middleware
// every res now have a parameter currentUser
app.use(function(req, res, next){
	res.locals.currentUser = req.user;
	next();
});

//=======================
//requiring routes
//=======================
var indexRoutes = require("./routes/index");
var userRoutes  = require("./routes/user");
var cartRoutes  = require("./routes/cart");
app.use(indexRoutes);
app.use(userRoutes);
app.use(cartRoutes);

// connect to server
app.listen(3000, function(){
	console.log("The server has started!")
})

