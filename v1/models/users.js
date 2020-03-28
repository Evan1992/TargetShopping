var mongoose = require("mongoose")
var passportLocalMongoose = require("passport-local-mongoose");
var product = require("./products")

var UserSchema = new mongoose.Schema({
	username: String,
	password: String,
	cart:[
		{
			type:mongoose.Schema.Types.ObjectId,
			ref:"Product"
		}
	]
});

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