from abc import ABC,abstractmethod
class Animale(ABC):
    def __init__(self,type,color):
        self.__type = type
        self.__color = color
    @abstractmethod 
    def son(self):
        pass
    
class cat(Animale) :
    def __init__(self, type, color):
        super().__init__(type, color)
        
    def son(self):
        print("mew mew")
class dog(Animale):
    def __init__(self, type, color):
        super().__init__(type, color)
        
    def son(self):
        print("wolf wolf ")    