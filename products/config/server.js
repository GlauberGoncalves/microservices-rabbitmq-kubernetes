const express = require('express');
const consign = require('consign');
const bodyParser = require('body-parser');
const app = express();

app.use(function(req, res, next){

	res.setHeader("Access-Control-Allow-Origin", "*");
	res.setHeader("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE");
	res.setHeader("Access-Control-Allow-Headers", "content-type");
	res.setHeader("Access-Control-Allow-Credentials", true);

	next();
});

app.use(bodyParser.urlencoded({extended: true}));

consign()		
	.then('app/controllers')
	.then('app/db.js')
	.into(app);

module.exports = app;