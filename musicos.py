musicos=[]
def ingresarMusicos():
    for i in range(3):
        musicos.append(input("Ingrese el nombre de un musico: "))
def verificacion(musicos):
    return "Chris Martin" in musicos
ingresarMusicos()
resultado = lambda:print(verificacion(musicos))
resultado()