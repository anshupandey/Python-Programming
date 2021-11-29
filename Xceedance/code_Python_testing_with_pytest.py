
import code_python_sample_code_for_testing as cp

def test_add():
    assert cp.add(4,5)==9
    assert cp.add(4,-5)==-1
    assert cp.add(-4,9)==5
    
def test_multiply():
    assert cp.multiply(4,5)==20
    assert cp.multiply(4,-5)==-20
    assert cp.multiply(-4,9)==-36
    
def test_divide():
    assert cp.divide(4,2)==2
    assert cp.divide(4,-1)==-4
    assert cp.divide(-4,4)==-1

    