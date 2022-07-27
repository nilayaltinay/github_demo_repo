import unittest


class MyTest(unittest.TestCase):

    def setUp(self):
        print("You have called setUp()")

    def test_func_1(self):
        pass

    def test_func_2(self):
        pass

    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])


    def tearDown(self):
        print("You have called tearDown()")

        
if __name__== "__main__":
    unittest.main()

