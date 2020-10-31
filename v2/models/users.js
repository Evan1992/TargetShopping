var mongoose = require("mongoose")
var passportLocalMongoose = require("passport-local-mongoose");

var UserSchema = new mongoose.Schema({
	username: String,
	password: String,
	/*
	The relation between user and products is one-to-many, so we can use "Embedded Data" way to add products to the cart
	when user add a new product to the cart, add the new product to this list
	*/
	cart:[]
})

/* 
add some methods of passport-local-mongoose package 
to the user Schema.
- Hash and unhash the password
- serialize and deserialize user
*/
UserSchema.plugin(passportLocalMongoose);


// make the pattern be a model so that it has a bunch of methods like create, remove
// the collection is called "users", which is defined in mongoose.model("User", UserSchema)
// =============================================
// var User = mongoose.model("User", UserSchema)
// module.exports = User
// =============================================
module.exports = mongoose.model("User", UserSchema)