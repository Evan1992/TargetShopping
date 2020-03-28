var mongoose = require("mongoose")
var passportLocalMongoose = require("passport-local-mongoose");

// This is not defining a table like relational database
// This is defining a pattern
var ProductSchema = new mongoose.Schema({
	name:  String,
	img:   String,
	price: Number
});

// add in some methods to the user
// ProductSchema.plugin(passportLocalMongoose);
module.exports = mongoose.model("Product", ProductSchema)