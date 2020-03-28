var mongoose = require("mongoose"),
	Product  = require("./models/products")


var ProductSchema = new mongoose.Schema({
	name:  String,
	img:   String,
	price: Number
});

var data = [
	{
		name:"earpods",
		img:"https://images-na.ssl-images-amazon.com/images/I/71NTi82uBEL._SX342_.jpg",
		price:100
	},
	{
		name:"iPhone",
		img:"https://images-na.ssl-images-amazon.com/images/G/01/appcore/phone/AMZ_FamiyStripe_iPhone_7Plus._CB452028164_.png",
		price:1000
	},
	{
		name:"Mac",
		img:"https://images-na.ssl-images-amazon.com/images/I/71%2Bl4qh-8SL._SX342_.jpg",
		price: 2000
	}
]

function seedDB(){
	//Remove all products
	Product.remove({}, function(err){
		if(err){
			console.log(err);
		}
		console.log("removed all products!")
		// add products to database
		data.forEach(function(seed){
			Product.create(seed, function(err, product){
				if(err){
					console.log(err);
				}else{
					console.log("added a product");
				}
			});
		});
	});
}
 
module.exports = seedDB;