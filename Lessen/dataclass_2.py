from dataclasses import dataclass

@dataclass
class Coordinates:
    longitude: float
    latitude: float

coordinates1 = Coordinates(10.0, 20.0)
coordinates2 = Coordinates(101.0, 202.0)
print(coordinates2.latitude)  
print(coordinates2) 
print(coordinates1 == coordinates2)
