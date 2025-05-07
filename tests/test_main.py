from src.main import add, subtract

def test_add():
	assert add(1,3) == 4
	assert add(-1,1) == 0

def test_subtract():

	assert subtract(3,2) == 1
	assert subtract(0,5) == -5



