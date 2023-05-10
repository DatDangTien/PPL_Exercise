import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    def test_simple_program250(self):
        """Simple program: int main() {} """
        input = """ fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
    def test_simple_program251(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))
    def test_simple_program252(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
            while (_xy >= 0) i = i + 1;
                a: boolean = true;
            do {
                b = !a;
            }
            while (b >= false); 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))
    def test_simple_program253(self):
        input = """x: integer = 65;
        a: array[23_3] of string = {"defd","dsfasd\\"adsf","dkf\\\\"};
        b: auto = 13_4;
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
            while (_xy >= 0) i = i + 1;
                a: boolean = true;
            do {
                b = !a;
            }
            while (b != false); 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))
    def test_simple_program254(self):
        input = """x: integer = 65;
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
            while (_xy >= 0) i = i + 1;
                a: boolean = true;
            do {
                b = !a;
            }
            while (b == false); 
            return _testreturn();
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))
    def test_simple_program255(self):
        input = """x: integer = 65;
        a: array[23_3] of string =  {"Kangxi", "Yongzheng", "Qianlong"};
        b: auto = 13_4;
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
            while (_xy >= 0) i = i + 1;
                a: boolean = true;
            do {
                b = !a;
            }
            while (b != false); 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))
    def test_simple_program256(self):
        input = """x: integer = 65;
        a: array[23_3] of auto =  {"Kangxi", 384_35, (234_24.3E4-10)};
        b: auto = 13_4;
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
            while (_xy >= 0) i = i + 1;
                a: boolean = true;
            do {
                b = !a;
            }
            while (b != false); 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))