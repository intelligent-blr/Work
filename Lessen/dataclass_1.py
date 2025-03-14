from typing import Any


class Coordinates:
    __slots__ = ("longitude", "latitude") 

    longitude: float
    latitude: float

    def __init__(self, longitude: float, latitude: float) -> None:
        self.longitude = longitude
        self.latitude = latitude

    def __repr__(self) -> str:
        return f"Coordinates(longitude={self.longitude}, latitude={self.latitude})"

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Coordinates):
            return self.longitude == other.longitude and self.latitude == other.latitude
        return False


def get_gps_coordinates() -> Coordinates:
    return Coordinates(10.0, 20.0)


coordinates1 = Coordinates(10.0, 20.0)
coordinates2 = Coordinates(101.0, 202.0)
print(coordinates2.latitude)  
print(coordinates2) 
print(coordinates1 == coordinates2)