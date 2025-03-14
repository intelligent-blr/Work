# ПРИМЕР 1 - Использование Dict и Union
# Union[str, int] означает, что значения в словаре могут быть либо строками, либо числами.
# ----------------------
from typing import Dict, Union

def get_person_details(person: Dict[str, Union[str, int]]) -> str:
    return f"{person['name']}, {person['age']} years old"


print(get_person_details({"name": "Alice", "age": 25})) 



# ПРИМЕР 2 - Использование Any (любой тип)
# Any допускает любые значения, включая str, int, float, bool, None и т. д.
# ----------------------
from typing import Dict, Any

def get_person_details(person: Dict[str, Any]) -> str:
    return f"{person['name']}, {person['age']} years old"


print(get_person_details({"name": "Bob", "age": 30.5}))  



# ПРИМЕР 3 - Использование TypedDict (более строгая проверка типов)
# TypedDict позволяет точно определить, какие ключи и какие типы должны быть в словаре.
# ----------------------
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

def get_person_details(person: Person) -> str:
    return f"{person['name']}, {person['age']} years old"


print(get_person_details({"name": "Charlie", "age": 40})) 



# ПРИМЕР 4 - Использование Optional (если ключ может отсутствовать)
# Optional[int] означает, что age может быть int или None.
# ----------------------
from typing import Dict, Union, Optional

def get_person_details(person: Dict[str, Union[str, Optional[int]]]) -> str:
    age_value: Optional[int] = person.get("age")  # Может быть int или None
    age = str(age_value) if age_value is not None else "Unknown" 
    return f"{person['name']}, {age} years old"


print(get_person_details({"name": "David"}))   
print(get_person_details({"name": "Alice", "age": 30}))  
print(get_person_details({"name": "Bob", "age": None}))



### Перепишем без использвоания Optional
from typing import Dict, Union

def get_person_details(person: Dict[str, Union[str, int, None]]) -> str:
    age = person.get("age", "Unknown")
    return f"{person['name']}, {age} years old"


print(get_person_details({"name": "David"}))       
print(get_person_details({"name": "Alice", "age": 30}))
print(get_person_details({"name": "Bob", "age": None})) 
