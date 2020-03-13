const app = require('./config/server');
const port = 3333;

app.listen(port, function(){
	console.log('Servidor online');
});