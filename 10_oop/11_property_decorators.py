class TeaLeaf:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else: # Here we are controlling the Error part also.
            raise ValueError("Tea leaf age must be between 1 and 5 years.")
        
leaf = TeaLeaf(2)
print(leaf.age)  # Accessing the age property
leaf.age = 4     # Setting the age property
print(leaf.age)