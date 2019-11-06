import unittest
from ddt import  ddt, data, unpack


@ddt
class TestDdt(unittest.TestCase):

    @data([10,20],[10,10])
    @unpack
    def test_centos(self, a, b):
        print(a + b)

if __name__ =='__main__':
    unittest.main()