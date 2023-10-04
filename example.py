def sum(a,b):
	return a+b

def subtract(a,b):
	return a-b

def test_sum():
	assert sum(2,3) == 5 # assert lets you verify IF (test) => TRUE
	assert sum('space','ship') == 'spaceship' # also test string sums
#pytest will search for test_functions and run them, returning outputs.

def test_subtract():
	assert subtract(2,3) == -1


