def saludos():
    print("hola")

saludos()


class automovil():
    def __init__(self,marca,parado):
        self.marca=marca
        self.parado=parado

    def quemarca(self):
        return self.marca

    def avanza(self):
        if self.parado=="si":
            return "esta parado"

micarro=automovil("jetta","si")
print(micarro.quemarca())
print(micarro.avanza())


print("que pedo puto")
