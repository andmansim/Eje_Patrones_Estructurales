precios_dict = {'Sin bebida': 0, 'Sin postre':0, 'agua':1.5, 'sopresa':3, 'vino_blaco':2.5, 'cerveza':2.5, 'zumo':1.5, 'leche':1.5, 
           'cafe': 2, 'infusion':1, 'licor':4, 'cava':4, 'batido':2, 'smoothie':2.25, 'granizado':2, 
           'te': 3, 'fanta':6, 'coca_cola':7, 'pepsi':5, 'yogurt':3, 'helado':6, 'tarta':9, 'fruta':1, 
           'galletas':3, 'postre_del_dia':6, 'flan':2, 'tarta_de_queso':8, 'tarta_de_chocolate':5, 
           'pizza': 15, 'barbacoa': 12, 'napolitana':13, 'cuatro_quesos':16, 'margarita':10, 
           'carbonara':16, 'cuatro_estaciones':18, 'especial':20, 'vegetal':15, 'hawaiana':15,}

datos =['Sin bebida', 'postre_del_dia']
for i in datos:
    for key in precios_dict:
        if key == i:
            print(precios_dict[key])
