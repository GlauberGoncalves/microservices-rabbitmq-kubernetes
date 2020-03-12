module.exports = app => {
    
    app.get('/products', (req, res) => {
        res.send(app.app.db)
    })

    app.get('/products/:id', (req, res) => {
        
        const { db } = app.app
        const { id } = req.params        

        const found = db.products.find( product => product.uuid == id)

        if(!found){
            res.send({})
        }
        res.send(found)
    })
}