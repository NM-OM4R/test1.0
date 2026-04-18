class Xbox:
    def __init__(self, modelo, almacenamiento, color, precio, encendido):
        self.__modelo = modelo 
        self.__almacenamiento = almacenamiento
        self.__color = color
        self.__precio = precio 
        self.__encendido = encendido
    
    def get_modelo(self):
        return self.__modelo
    def get_almacenamiento(self):
        return self.__almacenamiento
    def get_color(self):
        return self.__color
    def get_precio(self):
        return self.__precio
    def get_encendido(self):
        return self.__encendido
    
    

