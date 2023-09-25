
#FECHA 08/09/23 6:56 PM

print("Hello world, welcome to store")

#---------------------------------
prod = {"ICEBERG":100,"TOMATE":200,"POLLO":300,"PAN":400,"MAIZ":500}
#---------------------------------

while True:
    preg = int(input("Deseas comprar un articulo? SI=1 NO=2 :"))
    if preg==1:
        selec_artic = str(input("Selecciona el articulo: ").upper())
        if selec_artic in prod:
            selec = prod[selec_artic]
            print("Tu compra es: ",selec)  
        else:
            print("El articulo no se encuentra en venta")
    elif preg==2:
        print("Vuelva pronto") 
        break
