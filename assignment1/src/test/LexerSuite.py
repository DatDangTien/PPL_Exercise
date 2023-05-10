import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))
    def test_lowercase_identifier11(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("0.483", "0.483,<EOF>", 111))
    def test_lowercase_identifier112(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1_70.4489E-09", "170.4489,E,-,0,9,<EOF>", 112))
    def test_lowercase_identifier113(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1_740.4489E-90", "1740.4489E-90,<EOF>", 113))
    def test_lowercase_identifier114(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1_234.567", "1234.567,<EOF>", 114))
    def test_lowercase_identifier151(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" """ , """He asked me: \"Where is John?\",<EOF>""", 151))
    def test_lowercase_identifier152(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\b asdfhj" """ , """He asked me: \"Where is John?\b asdfhj,<EOF>""", 152))
    def test_lowercase_identifier153(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?
        asdfhj" """ , """Unclosed String: He asked me: \"""", 153))
    def test_lowercase_identifier154(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\n asdfhj" """ , """He asked me: \"Where is John?\n asdfhj,<EOF>""", 154))
    def test_lowercase_identifier155(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\a asdfhj" """ , """Illegal Escape In String: He asked me: \"Where is John?\a""", 155))
    def test_lowercase_identifier156(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?"a asdfhj" """ , """Illegal Escape In String: He asked me: \"Where is John?\a""", 156))
    def test_lowercase_identifier157(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?"a asdfhj", 123 "abchdcld" """ , """Illegal Escape In String: He asked me: \"Where is John?\a""", 157))   
    def test_lowercase_identifier158(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(""" "He asked me: Where is John?
        asdfhj" """ , """Unclosed String: He asked me: \"""", 158))  
    def test_lowercase_identifier160(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(""" "Kangxi","abcd" """, """Kangxi,',',abcd""", 160)) 
    def test_lowercase_identifier159(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(""" {"Kangxi", "Yongzheng", "Qianlong"}""" , """Unclosed String: He asked me: \"""", 159))
    def test_lowercase_identifier161(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(""" {"defd","dsfasd\\"adsf","dkf\\\\"}""" , """Unclosed String: He asked me: \"""", 161))  
    def test_lowercase_identifier162(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(""" {"defd","dsfasd\\"adsf","dkf\\\\asdf"}""" , """Unclosed String: He asked me: \"""", 162))    
    
       