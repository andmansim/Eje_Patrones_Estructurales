
class Usuario:
    '''
    Esta clase se encarga de recoger el pedido actual y mirar si ha habido algún pedido anterior 
    con dicho usuario.
    '''
    def __init__(self, nombre, contrasenia):
        self.nombre = nombre
        self.contrasenia = contrasenia
        self.ordenes = []

    def pedido_actual(self, pizza):
        self.ordenes.append(pizza)

    def ultimo_pedido(self):
        if self.ordenes:
            return self.ordenes[-1]
        else:
            return None


