#   Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
#   Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
           
    def square (self):
        S1 = 0.5 * abs((self.x2 - self.x1) * (self.y3 - self.y1) - (self.x3 - self.x1)*(self.y2 - self.y1)) 
        return S1
    def AB (self):
        return ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**.5
    def BC (self):
        return ((self.x3 - self.x2)**2 + (self.y3 - self.y2)**2)**.5
    def AC (self):
        return ((self.x3 - self.x1)**2 + (self.y3 - self.y1)**2)**.5
    def perimeter (self):
             
          P = self.AB() + self.BC() + self.AC()
          return P
    def hc (self):
          Hc = 2 * (self.square()) / (self.AB())
          return Hc
        
    def ha (self):
          Ha = 2 * (self.square()) / (self.BC())
          return Ha    
    
    def hb (self):
          Hb = 2 * (self.square()) / (self.AC())
          return Hb
            
        
print ("Треугольник")
tr1 = Triangle (1, 2, 3, 7, 4, 5)     
print ("Площадь треугольника ", tr1.square(), "см")
print ("Периметр треугольника", tr1.perimeter(), "см 2")
print ("Высота вершины С", tr1.hc ())
print ("Высота вершины A", tr1.ha ())    
print ("Высота вршины B", tr1.hb ())


print ()
print ("Трапеция")
# Задача-2: Написать Класс "Равнобочная трапеция", заданной\
# координатами 4-х точек.
class Trapezium:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
  # Предусмотреть в классе методы:

# вычисления: длины сторон, 
    def AB (self):
        return ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**.5
    def BC (self):
        return ((self.x3 - self.x2)**2 + (self.y3 - self.y2)**2)**.5

    def CD (self):
        return ((self.x4 - self.x3)**2 + (self.y4 - self.y3)**2)**.5
    def DA (self):
        return ((self.x4 - self.x1)**2 + (self.y4 - self.y1)**2)**.5

    
 #периметр,
    def perimeter (self):
        P = self.AB() + self.BC() + self.DA() + self.CD()
        return P
    def semi_p (self):
        P2 = self.perimeter()/2
        return P2
#площадь. 
    def square (self):
        S1 = ((self.semi_p() - self.AB()) * (self.semi_p() - self.BC())*(self.semi_p() - self.CD())*(self.semi_p() - self.DA()))**.5 
        return S1
# проверка, является ли фигура равнобочной трапецией;
    def check1 (self):
        if (self.x1 == self.x2 and self.x3 == self.x4) or (self.y1 == self.y4 and self.y2 == self.y3):
            
            if ((self.AB()) == (self.CD())) or ((self.BC()) == (self.DA())):
                print ("Фигура является равнобокой трапецией")
            else:    
                print ("Фигура является неравнобокой трапецией")
        else:
            print ("Фигура не явлется трапецией")       

trap1 = Trapezium (1, 2, 3, 7, 4, 5, 6, 2)     
print ("Длина стороны АВ ", trap1.AB(), "см")
print ("Длина стороны BC ", trap1.BC(), "см")
print ("Длина стороны CD ", trap1.CD(), "см")
print ("Длина стороны DA ", trap1.DA(), "см")
print ("Периметр фигуры", trap1.perimeter(), "см")
print ("Площадь фигуры ", trap1.square(), "см 2")
trap1.check1()

print()

trap2 = Trapezium (1, 1, 1, 3, 3, 0, 3, 4)     
print ("Длина стороны АВ ", trap1.AB(), "см")
print ("Длина стороны BC ", trap1.BC(), "см")
print ("Длина стороны CD ", trap1.CD(), "см")
print ("Длина стороны DA ", trap1.DA(), "см")
print ("Периметр фигуры", trap2.perimeter(), "см")
print ("Площадь фигуры ", trap2.square(), "см 2")
trap2.check1()

