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
    
    def set_modelo(self, modelo):
        self.__modelo = modelo
    def set_almacenamiento(self, almacenamiento):
        self.__almacenamiento = almacenamiento
    def set_color(self, color):
        self.__color = color
    def set_precio(self, precio):
        self.__precio = precio
    def set_encendido(self, encendido):
        self.__encendido = encendido

    def encender(self):
        self.__encendido = True

    def apagar(self):
        self.__encendido = False
    
    def info(self):
        print('modelo:', self.__modelo)
        print('almacenamiento:', self.__almacenamiento)
        print('color:', self.__color)
        print('precio:', self.__precio)
        print('encendido', self.__encendido)
        
    
    
    

