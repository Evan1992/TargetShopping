var mongoose = require("mongoose")
var passportLocalMongoose = require("passport-local-mongoose");

var CartSchema = new mongoose.Schema({
	name:  String,
	products: [
		{
			type:mongoose.Schema.Types.ObjectId,
			ref:"Product"
		}
	]
	
});

module.exports = mongoose.model("Cart", CartSchema)