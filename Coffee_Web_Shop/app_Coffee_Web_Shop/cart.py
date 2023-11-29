class Cart():
    def __init__(self,request) :
        
        self.session = request.session

        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}


        self.cart = cart

    def add(self, product,product_qty):
        product_id = str(product.product_id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]= {'product':str(product.qty)}
 #           self.cart[product_id]= {'product':str(product.product_id),'qty':str(product_qty)}
        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def item(self):
        
        return self.cart