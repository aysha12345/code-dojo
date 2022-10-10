from ex1 import largest_number, main

def test_largest_number():
    assert largest_number([50, 2, 1, 9]) == 95021
    assert largest_number([5, 50, 56]) == 56550
    assert largest_number([420, 42, 423]) == 42423420
    
def test_main():
    assert main("50, 2, 1, 9") == 95021
    assert main("23, 67, 2, 9") == 967232
    
