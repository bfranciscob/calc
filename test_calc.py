import pytest
from calc import soma

def test_soma():
	assert soma(1, 2) == 3
	#assert soma(1,"2") == 3
	#assert soma("1", "2") == 3
	#assert soma(-1, -2) == -3
	#assert soma(-1, 2) == 1
	#assert soma("x", 2) == None
	#assert soma(1, "y") == None
	#assert soma("x", "y") == None

