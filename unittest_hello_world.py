
import unittest


class MyTest(unittest.TestCase):

    def setUp(self):
        print("You have called setUp()")

    
    def test_split(self):
        s = 'hello World'
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split()

    def test_func_2(self):
        pass

    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertFalse(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)


    def tearDown(self):
        print("You have called tearDown()")

        
if __name__== "__main__":
    unittest.main()
