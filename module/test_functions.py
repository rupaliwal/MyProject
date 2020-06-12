#Testing for Animal Type.
def test_animal_type():
    
    assert callable(animal_type)
    assert animal_type('dog') == True
    
test_animal_type()


# Testing for Animal Color.
def test_animal_col():
    
    assert callable(animal_col)
    assert isinstance(animal_col('gold'), bool)
    
test_animal_col()