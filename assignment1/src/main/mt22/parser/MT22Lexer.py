# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u01c8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\61\7\61\u013d\n\61\f\61\16\61\u0140")
        buf.write("\13\61\3\61\5\61\u0143\n\61\3\61\6\61\u0146\n\61\r\61")
        buf.write("\16\61\u0147\7\61\u014a\n\61\f\61\16\61\u014d\13\61\3")
        buf.write("\61\5\61\u0150\n\61\3\62\3\62\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\5\64\u015d\n\64\3\64\3\64\3\64\3")
        buf.write("\64\5\64\u0163\n\64\3\65\3\65\6\65\u0167\n\65\r\65\16")
        buf.write("\65\u0168\3\66\3\66\5\66\u016d\n\66\3\66\3\66\7\66\u0171")
        buf.write("\n\66\f\66\16\66\u0174\13\66\3\67\3\67\7\67\u0178\n\67")
        buf.write("\f\67\16\67\u017b\13\67\38\38\38\38\78\u0181\n8\f8\16")
        buf.write("8\u0184\138\38\38\38\38\78\u018a\n8\f8\168\u018d\138\5")
        buf.write("8\u018f\n8\38\38\39\69\u0194\n9\r9\169\u0195\39\39\3:")
        buf.write("\3:\3:\3:\7:\u019e\n:\f:\16:\u01a1\13:\3:\3:\3:\3;\3;")
        buf.write("\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3?\3?\7?\u01b4\n?\f?\16")
        buf.write("?\u01b7\13?\3?\5?\u01ba\n?\3@\3@\3@\3A\3A\7A\u01c1\nA")
        buf.write("\fA\16A\u01c4\13A\3A\3A\3A\4\u0182\u01c2\2B\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\2e\2g\63i\2k\2m\64o\65q\66s\67u\2w\2")
        buf.write("y8{9}\2\177:\u0081\2\3\2\16\3\2\63;\3\2\62;\4\2GGgg\4")
        buf.write("\2--//\5\2C\\aac|\6\2\62;C\\aac|\4\2\f\f\17\17\5\2\13")
        buf.write("\f\17\17\"\"\6\2\f\f\17\17$$^^\n\2$$))^^ddhhppttvv\3\2")
        buf.write("$$\4\3\f\f\17\17\2\u01d3\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2g")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\2\177\3\2\2\2\3\u0083\3\2\2\2\5\u0086")
        buf.write("\3\2\2\2\7\u008e\3\2\2\2\t\u0092\3\2\2\2\13\u0097\3\2")
        buf.write("\2\2\r\u009d\3\2\2\2\17\u00a3\3\2\2\2\21\u00aa\3\2\2\2")
        buf.write("\23\u00ae\3\2\2\2\25\u00b7\3\2\2\2\27\u00ba\3\2\2\2\31")
        buf.write("\u00c3\3\2\2\2\33\u00c8\3\2\2\2\35\u00cb\3\2\2\2\37\u00d1")
        buf.write("\3\2\2\2!\u00d9\3\2\2\2#\u00e1\3\2\2\2%\u00e7\3\2\2\2")
        buf.write("\'\u00ee\3\2\2\2)\u00f4\3\2\2\2+\u00f9\3\2\2\2-\u00fe")
        buf.write("\3\2\2\2/\u0100\3\2\2\2\61\u0102\3\2\2\2\63\u0104\3\2")
        buf.write("\2\2\65\u0106\3\2\2\2\67\u0108\3\2\2\29\u010a\3\2\2\2")
        buf.write(";\u010d\3\2\2\2=\u0110\3\2\2\2?\u0113\3\2\2\2A\u0116\3")
        buf.write("\2\2\2C\u0118\3\2\2\2E\u011b\3\2\2\2G\u011d\3\2\2\2I\u0120")
        buf.write("\3\2\2\2K\u0123\3\2\2\2M\u0125\3\2\2\2O\u0127\3\2\2\2")
        buf.write("Q\u0129\3\2\2\2S\u012b\3\2\2\2U\u012d\3\2\2\2W\u012f\3")
        buf.write("\2\2\2Y\u0131\3\2\2\2[\u0133\3\2\2\2]\u0135\3\2\2\2_\u0137")
        buf.write("\3\2\2\2a\u014f\3\2\2\2c\u0151\3\2\2\2e\u0153\3\2\2\2")
        buf.write("g\u0162\3\2\2\2i\u0164\3\2\2\2k\u016a\3\2\2\2m\u0175\3")
        buf.write("\2\2\2o\u018e\3\2\2\2q\u0193\3\2\2\2s\u0199\3\2\2\2u\u01a5")
        buf.write("\3\2\2\2w\u01a7\3\2\2\2y\u01a9\3\2\2\2{\u01ac\3\2\2\2")
        buf.write("}\u01af\3\2\2\2\177\u01bb\3\2\2\2\u0081\u01be\3\2\2\2")
        buf.write("\u0083\u0084\7q\2\2\u0084\u0085\7h\2\2\u0085\4\3\2\2\2")
        buf.write("\u0086\u0087\7k\2\2\u0087\u0088\7p\2\2\u0088\u0089\7j")
        buf.write("\2\2\u0089\u008a\7g\2\2\u008a\u008b\7t\2\2\u008b\u008c")
        buf.write("\7k\2\2\u008c\u008d\7v\2\2\u008d\6\3\2\2\2\u008e\u008f")
        buf.write("\7q\2\2\u008f\u0090\7w\2\2\u0090\u0091\7v\2\2\u0091\b")
        buf.write("\3\2\2\2\u0092\u0093\7v\2\2\u0093\u0094\7t\2\2\u0094\u0095")
        buf.write("\7w\2\2\u0095\u0096\7g\2\2\u0096\n\3\2\2\2\u0097\u0098")
        buf.write("\7h\2\2\u0098\u0099\7c\2\2\u0099\u009a\7n\2\2\u009a\u009b")
        buf.write("\7u\2\2\u009b\u009c\7g\2\2\u009c\f\3\2\2\2\u009d\u009e")
        buf.write("\7d\2\2\u009e\u009f\7t\2\2\u009f\u00a0\7g\2\2\u00a0\u00a1")
        buf.write("\7c\2\2\u00a1\u00a2\7m\2\2\u00a2\16\3\2\2\2\u00a3\u00a4")
        buf.write("\7t\2\2\u00a4\u00a5\7g\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7")
        buf.write("\7w\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9\7p\2\2\u00a9\20")
        buf.write("\3\2\2\2\u00aa\u00ab\7h\2\2\u00ab\u00ac\7q\2\2\u00ac\u00ad")
        buf.write("\7t\2\2\u00ad\22\3\2\2\2\u00ae\u00af\7e\2\2\u00af\u00b0")
        buf.write("\7q\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2\7v\2\2\u00b2\u00b3")
        buf.write("\7k\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b5\7w\2\2\u00b5\u00b6")
        buf.write("\7g\2\2\u00b6\24\3\2\2\2\u00b7\u00b8\7f\2\2\u00b8\u00b9")
        buf.write("\7q\2\2\u00b9\26\3\2\2\2\u00ba\u00bb\7h\2\2\u00bb\u00bc")
        buf.write("\7w\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be\7e\2\2\u00be\u00bf")
        buf.write("\7v\2\2\u00bf\u00c0\7k\2\2\u00c0\u00c1\7q\2\2\u00c1\u00c2")
        buf.write("\7p\2\2\u00c2\30\3\2\2\2\u00c3\u00c4\7g\2\2\u00c4\u00c5")
        buf.write("\7n\2\2\u00c5\u00c6\7u\2\2\u00c6\u00c7\7g\2\2\u00c7\32")
        buf.write("\3\2\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca\7h\2\2\u00ca\34")
        buf.write("\3\2\2\2\u00cb\u00cc\7y\2\2\u00cc\u00cd\7j\2\2\u00cd\u00ce")
        buf.write("\7k\2\2\u00ce\u00cf\7n\2\2\u00cf\u00d0\7g\2\2\u00d0\36")
        buf.write("\3\2\2\2\u00d1\u00d2\7d\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4")
        buf.write("\7q\2\2\u00d4\u00d5\7n\2\2\u00d5\u00d6\7g\2\2\u00d6\u00d7")
        buf.write("\7c\2\2\u00d7\u00d8\7p\2\2\u00d8 \3\2\2\2\u00d9\u00da")
        buf.write("\7k\2\2\u00da\u00db\7p\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd")
        buf.write("\7g\2\2\u00dd\u00de\7i\2\2\u00de\u00df\7g\2\2\u00df\u00e0")
        buf.write("\7t\2\2\u00e0\"\3\2\2\2\u00e1\u00e2\7h\2\2\u00e2\u00e3")
        buf.write("\7n\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6")
        buf.write("\7v\2\2\u00e6$\3\2\2\2\u00e7\u00e8\7u\2\2\u00e8\u00e9")
        buf.write("\7v\2\2\u00e9\u00ea\7t\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec")
        buf.write("\7p\2\2\u00ec\u00ed\7i\2\2\u00ed&\3\2\2\2\u00ee\u00ef")
        buf.write("\7c\2\2\u00ef\u00f0\7t\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2")
        buf.write("\7c\2\2\u00f2\u00f3\7{\2\2\u00f3(\3\2\2\2\u00f4\u00f5")
        buf.write("\7x\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8")
        buf.write("\7f\2\2\u00f8*\3\2\2\2\u00f9\u00fa\7c\2\2\u00fa\u00fb")
        buf.write("\7w\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd\7q\2\2\u00fd,\3")
        buf.write("\2\2\2\u00fe\u00ff\7-\2\2\u00ff.\3\2\2\2\u0100\u0101\7")
        buf.write("/\2\2\u0101\60\3\2\2\2\u0102\u0103\7,\2\2\u0103\62\3\2")
        buf.write("\2\2\u0104\u0105\7\61\2\2\u0105\64\3\2\2\2\u0106\u0107")
        buf.write("\7\'\2\2\u0107\66\3\2\2\2\u0108\u0109\7#\2\2\u01098\3")
        buf.write("\2\2\2\u010a\u010b\7(\2\2\u010b\u010c\7(\2\2\u010c:\3")
        buf.write("\2\2\2\u010d\u010e\7~\2\2\u010e\u010f\7~\2\2\u010f<\3")
        buf.write("\2\2\2\u0110\u0111\7?\2\2\u0111\u0112\7?\2\2\u0112>\3")
        buf.write("\2\2\2\u0113\u0114\7#\2\2\u0114\u0115\7?\2\2\u0115@\3")
        buf.write("\2\2\2\u0116\u0117\7>\2\2\u0117B\3\2\2\2\u0118\u0119\7")
        buf.write(">\2\2\u0119\u011a\7?\2\2\u011aD\3\2\2\2\u011b\u011c\7")
        buf.write("@\2\2\u011cF\3\2\2\2\u011d\u011e\7@\2\2\u011e\u011f\7")
        buf.write("?\2\2\u011fH\3\2\2\2\u0120\u0121\7<\2\2\u0121\u0122\7")
        buf.write("<\2\2\u0122J\3\2\2\2\u0123\u0124\7*\2\2\u0124L\3\2\2\2")
        buf.write("\u0125\u0126\7+\2\2\u0126N\3\2\2\2\u0127\u0128\7]\2\2")
        buf.write("\u0128P\3\2\2\2\u0129\u012a\7_\2\2\u012aR\3\2\2\2\u012b")
        buf.write("\u012c\7\60\2\2\u012cT\3\2\2\2\u012d\u012e\7.\2\2\u012e")
        buf.write("V\3\2\2\2\u012f\u0130\7=\2\2\u0130X\3\2\2\2\u0131\u0132")
        buf.write("\7<\2\2\u0132Z\3\2\2\2\u0133\u0134\7}\2\2\u0134\\\3\2")
        buf.write("\2\2\u0135\u0136\7\177\2\2\u0136^\3\2\2\2\u0137\u0138")
        buf.write("\7?\2\2\u0138`\3\2\2\2\u0139\u0150\7\62\2\2\u013a\u013e")
        buf.write("\t\2\2\2\u013b\u013d\5e\63\2\u013c\u013b\3\2\2\2\u013d")
        buf.write("\u0140\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f\3\2\2\2")
        buf.write("\u013f\u014b\3\2\2\2\u0140\u013e\3\2\2\2\u0141\u0143\5")
        buf.write("c\62\2\u0142\u0141\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0145")
        buf.write("\3\2\2\2\u0144\u0146\5e\63\2\u0145\u0144\3\2\2\2\u0146")
        buf.write("\u0147\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0148\3\2\2\2")
        buf.write("\u0148\u014a\3\2\2\2\u0149\u0142\3\2\2\2\u014a\u014d\3")
        buf.write("\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014e")
        buf.write("\3\2\2\2\u014d\u014b\3\2\2\2\u014e\u0150\b\61\2\2\u014f")
        buf.write("\u0139\3\2\2\2\u014f\u013a\3\2\2\2\u0150b\3\2\2\2\u0151")
        buf.write("\u0152\7a\2\2\u0152d\3\2\2\2\u0153\u0154\t\3\2\2\u0154")
        buf.write("f\3\2\2\2\u0155\u0156\5a\61\2\u0156\u0157\5i\65\2\u0157")
        buf.write("\u0158\3\2\2\2\u0158\u0159\b\64\3\2\u0159\u0163\3\2\2")
        buf.write("\2\u015a\u015c\5a\61\2\u015b\u015d\5i\65\2\u015c\u015b")
        buf.write("\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015e\3\2\2\2\u015e")
        buf.write("\u015f\5k\66\2\u015f\u0160\3\2\2\2\u0160\u0161\b\64\4")
        buf.write("\2\u0161\u0163\3\2\2\2\u0162\u0155\3\2\2\2\u0162\u015a")
        buf.write("\3\2\2\2\u0163h\3\2\2\2\u0164\u0166\7\60\2\2\u0165\u0167")
        buf.write("\t\3\2\2\u0166\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168")
        buf.write("\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169j\3\2\2\2\u016a")
        buf.write("\u016c\t\4\2\2\u016b\u016d\t\5\2\2\u016c\u016b\3\2\2\2")
        buf.write("\u016c\u016d\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u0172\t")
        buf.write("\2\2\2\u016f\u0171\t\3\2\2\u0170\u016f\3\2\2\2\u0171\u0174")
        buf.write("\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173")
        buf.write("l\3\2\2\2\u0174\u0172\3\2\2\2\u0175\u0179\t\6\2\2\u0176")
        buf.write("\u0178\t\7\2\2\u0177\u0176\3\2\2\2\u0178\u017b\3\2\2\2")
        buf.write("\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017an\3\2\2")
        buf.write("\2\u017b\u0179\3\2\2\2\u017c\u017d\7\61\2\2\u017d\u017e")
        buf.write("\7,\2\2\u017e\u0182\3\2\2\2\u017f\u0181\13\2\2\2\u0180")
        buf.write("\u017f\3\2\2\2\u0181\u0184\3\2\2\2\u0182\u0183\3\2\2\2")
        buf.write("\u0182\u0180\3\2\2\2\u0183\u0185\3\2\2\2\u0184\u0182\3")
        buf.write("\2\2\2\u0185\u0186\7,\2\2\u0186\u018f\7\61\2\2\u0187\u018b")
        buf.write("\7^\2\2\u0188\u018a\n\b\2\2\u0189\u0188\3\2\2\2\u018a")
        buf.write("\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c\3\2\2\2")
        buf.write("\u018c\u018f\3\2\2\2\u018d\u018b\3\2\2\2\u018e\u017c\3")
        buf.write("\2\2\2\u018e\u0187\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0191")
        buf.write("\b8\5\2\u0191p\3\2\2\2\u0192\u0194\t\t\2\2\u0193\u0192")
        buf.write("\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0193\3\2\2\2\u0195")
        buf.write("\u0196\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0198\b9\5\2")
        buf.write("\u0198r\3\2\2\2\u0199\u019f\5w<\2\u019a\u019e\n\n\2\2")
        buf.write("\u019b\u019c\7^\2\2\u019c\u019e\5u;\2\u019d\u019a\3\2")
        buf.write("\2\2\u019d\u019b\3\2\2\2\u019e\u01a1\3\2\2\2\u019f\u019d")
        buf.write("\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a2\3\2\2\2\u01a1")
        buf.write("\u019f\3\2\2\2\u01a2\u01a3\5w<\2\u01a3\u01a4\b:\6\2\u01a4")
        buf.write("t\3\2\2\2\u01a5\u01a6\t\13\2\2\u01a6v\3\2\2\2\u01a7\u01a8")
        buf.write("\7$\2\2\u01a8x\3\2\2\2\u01a9\u01aa\13\2\2\2\u01aa\u01ab")
        buf.write("\b=\7\2\u01abz\3\2\2\2\u01ac\u01ad\5}?\2\u01ad\u01ae\b")
        buf.write(">\b\2\u01ae|\3\2\2\2\u01af\u01b5\5w<\2\u01b0\u01b4\n\f")
        buf.write("\2\2\u01b1\u01b2\7^\2\2\u01b2\u01b4\5u;\2\u01b3\u01b0")
        buf.write("\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5")
        buf.write("\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b9\3\2\2\2")
        buf.write("\u01b7\u01b5\3\2\2\2\u01b8\u01ba\t\r\2\2\u01b9\u01b8\3")
        buf.write("\2\2\2\u01ba~\3\2\2\2\u01bb\u01bc\5\u0081A\2\u01bc\u01bd")
        buf.write("\b@\t\2\u01bd\u0080\3\2\2\2\u01be\u01c2\5w<\2\u01bf\u01c1")
        buf.write("\13\2\2\2\u01c0\u01bf\3\2\2\2\u01c1\u01c4\3\2\2\2\u01c2")
        buf.write("\u01c3\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3\u01c5\3\2\2\2")
        buf.write("\u01c4\u01c2\3\2\2\2\u01c5\u01c6\7^\2\2\u01c6\u01c7\n")
        buf.write("\13\2\2\u01c7\u0082\3\2\2\2\30\2\u013e\u0142\u0147\u014b")
        buf.write("\u014f\u015c\u0162\u0168\u016c\u0172\u0179\u0182\u018b")
        buf.write("\u018e\u0195\u019d\u019f\u01b3\u01b5\u01b9\u01c2\n\3\61")
        buf.write("\2\3\64\3\3\64\4\b\2\2\3:\5\3=\6\3>\7\3@\b")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    OF = 1
    INHERIT = 2
    OUT = 3
    TRUE = 4
    FALSE = 5
    BREAK = 6
    RETURN = 7
    FOR = 8
    CONTINUE = 9
    DO = 10
    FUNCTION = 11
    ELSE = 12
    IF = 13
    WHILE = 14
    BOOL_TYP = 15
    INT_TYP = 16
    FLOAT_TYP = 17
    STRING_TYP = 18
    ARR_TYP = 19
    VOID_TYP = 20
    AUTO_TYP = 21
    PLUS = 22
    MINUS = 23
    MUL = 24
    DIV = 25
    MOD = 26
    NOT = 27
    AND = 28
    OR = 29
    D_EQ = 30
    NOT_EQ = 31
    LESS = 32
    LEQ = 33
    GREAT = 34
    GEQ = 35
    CONCAT = 36
    LB = 37
    RB = 38
    SLB = 39
    SRB = 40
    DOT = 41
    COMMA = 42
    SM = 43
    COlON = 44
    LCB = 45
    RCB = 46
    EQ = 47
    INTEGER = 48
    FLOAT = 49
    ID = 50
    CMT = 51
    WS = 52
    STRING = 53
    ERROR_CHAR = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'of'", "'inherit'", "'out'", "'true'", "'false'", "'break'", 
            "'return'", "'for'", "'continue'", "'do'", "'function'", "'else'", 
            "'if'", "'while'", "'boolean'", "'integer'", "'float'", "'string'", 
            "'array'", "'void'", "'auto'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", 
            "'>='", "'::'", "'('", "')'", "'['", "']'", "'.'", "','", "';'", 
            "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "OF", "INHERIT", "OUT", "TRUE", "FALSE", "BREAK", "RETURN", 
            "FOR", "CONTINUE", "DO", "FUNCTION", "ELSE", "IF", "WHILE", 
            "BOOL_TYP", "INT_TYP", "FLOAT_TYP", "STRING_TYP", "ARR_TYP", 
            "VOID_TYP", "AUTO_TYP", "PLUS", "MINUS", "MUL", "DIV", "MOD", 
            "NOT", "AND", "OR", "D_EQ", "NOT_EQ", "LESS", "LEQ", "GREAT", 
            "GEQ", "CONCAT", "LB", "RB", "SLB", "SRB", "DOT", "COMMA", "SM", 
            "COlON", "LCB", "RCB", "EQ", "INTEGER", "FLOAT", "ID", "CMT", 
            "WS", "STRING", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "OF", "INHERIT", "OUT", "TRUE", "FALSE", "BREAK", "RETURN", 
                  "FOR", "CONTINUE", "DO", "FUNCTION", "ELSE", "IF", "WHILE", 
                  "BOOL_TYP", "INT_TYP", "FLOAT_TYP", "STRING_TYP", "ARR_TYP", 
                  "VOID_TYP", "AUTO_TYP", "PLUS", "MINUS", "MUL", "DIV", 
                  "MOD", "NOT", "AND", "OR", "D_EQ", "NOT_EQ", "LESS", "LEQ", 
                  "GREAT", "GEQ", "CONCAT", "LB", "RB", "SLB", "SRB", "DOT", 
                  "COMMA", "SM", "COlON", "LCB", "RCB", "EQ", "INTEGER", 
                  "UNDER", "DIGIT", "FLOAT", "DEC", "EXP", "ID", "CMT", 
                  "WS", "STRING", "ESCAPE", "D_QUOTE", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "UNCLOSE_TOKEN", "ILLEGAL_ESCAPE", "ILLEGAL_TOKEN" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[47] = self.INTEGER_action 
            actions[50] = self.FLOAT_action 
            actions[56] = self.STRING_action 
            actions[59] = self.ERROR_CHAR_action 
            actions[60] = self.UNCLOSE_STRING_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTEGER_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def FLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

        if actionIndex == 2:
            self.text = self.text.replace('_','')
     

    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.text = self.text[1:]; raise UncloseString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            self.text = self.text[1:]; raise IllegalEscape(self.text)
     


