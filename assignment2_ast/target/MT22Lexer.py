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
        buf.write("\u01c6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\2\3\2\7\2\u0084")
        buf.write("\n\2\f\2\16\2\u0087\13\2\3\2\3\2\3\2\3\2\7\2\u008d\n\2")
        buf.write("\f\2\16\2\u0090\13\2\5\2\u0092\n\2\3\2\3\2\3\3\6\3\u0097")
        buf.write("\n\3\r\3\16\3\u0098\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3")
        buf.write("$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3")
        buf.write("+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\63\7\63\u0156\n\63\f\63\16\63\u0159")
        buf.write("\13\63\3\63\5\63\u015c\n\63\3\63\6\63\u015f\n\63\r\63")
        buf.write("\16\63\u0160\7\63\u0163\n\63\f\63\16\63\u0166\13\63\3")
        buf.write("\63\5\63\u0169\n\63\3\64\3\64\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\5\66\u0176\n\66\3\66\3\66\3\66\3")
        buf.write("\66\5\66\u017c\n\66\3\67\3\67\6\67\u0180\n\67\r\67\16")
        buf.write("\67\u0181\38\38\58\u0186\n8\38\38\78\u018a\n8\f8\168\u018d")
        buf.write("\138\39\39\79\u0191\n9\f9\169\u0194\139\3:\3:\3:\3:\7")
        buf.write(":\u019a\n:\f:\16:\u019d\13:\3:\3:\3:\3;\3;\3<\3<\3=\3")
        buf.write("=\3=\3>\3>\3>\3>\7>\u01ad\n>\f>\16>\u01b0\13>\3>\5>\u01b3")
        buf.write("\n>\3>\3>\3>\3?\3?\3?\3?\7?\u01bc\n?\f?\16?\u01bf\13?")
        buf.write("\3?\3?\3?\3?\3?\3?\3\u0085\2@\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35")
        buf.write("9\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62")
        buf.write("c\63e\64g\2i\2k\65m\2o\2q\66s\67u\2w\2y8{9}:\3\2\16\4")
        buf.write("\2\f\f\17\17\5\2\13\f\17\17\"\"\3\2\63;\3\2\62;\4\2GG")
        buf.write("gg\4\2--//\5\2C\\aac|\6\2\62;C\\aac|\6\2\f\f\17\17$$^")
        buf.write("^\n\2$$))^^ddhhppttvv\4\2$$^^\4\3\f\f\17\17\2\u01d4\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2k\3")
        buf.write("\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}")
        buf.write("\3\2\2\2\3\u0091\3\2\2\2\5\u0096\3\2\2\2\7\u009c\3\2\2")
        buf.write("\2\t\u009f\3\2\2\2\13\u00a7\3\2\2\2\r\u00ab\3\2\2\2\17")
        buf.write("\u00b0\3\2\2\2\21\u00b6\3\2\2\2\23\u00bc\3\2\2\2\25\u00c3")
        buf.write("\3\2\2\2\27\u00c7\3\2\2\2\31\u00d0\3\2\2\2\33\u00d3\3")
        buf.write("\2\2\2\35\u00dc\3\2\2\2\37\u00e1\3\2\2\2!\u00e4\3\2\2")
        buf.write("\2#\u00ea\3\2\2\2%\u00f2\3\2\2\2\'\u00fa\3\2\2\2)\u0100")
        buf.write("\3\2\2\2+\u0107\3\2\2\2-\u010d\3\2\2\2/\u0112\3\2\2\2")
        buf.write("\61\u0117\3\2\2\2\63\u0119\3\2\2\2\65\u011b\3\2\2\2\67")
        buf.write("\u011d\3\2\2\29\u011f\3\2\2\2;\u0121\3\2\2\2=\u0123\3")
        buf.write("\2\2\2?\u0126\3\2\2\2A\u0129\3\2\2\2C\u012c\3\2\2\2E\u012f")
        buf.write("\3\2\2\2G\u0131\3\2\2\2I\u0134\3\2\2\2K\u0136\3\2\2\2")
        buf.write("M\u0139\3\2\2\2O\u013c\3\2\2\2Q\u013e\3\2\2\2S\u0140\3")
        buf.write("\2\2\2U\u0142\3\2\2\2W\u0144\3\2\2\2Y\u0146\3\2\2\2[\u0148")
        buf.write("\3\2\2\2]\u014a\3\2\2\2_\u014c\3\2\2\2a\u014e\3\2\2\2")
        buf.write("c\u0150\3\2\2\2e\u0168\3\2\2\2g\u016a\3\2\2\2i\u016c\3")
        buf.write("\2\2\2k\u017b\3\2\2\2m\u017d\3\2\2\2o\u0183\3\2\2\2q\u018e")
        buf.write("\3\2\2\2s\u0195\3\2\2\2u\u01a1\3\2\2\2w\u01a3\3\2\2\2")
        buf.write("y\u01a5\3\2\2\2{\u01a8\3\2\2\2}\u01b7\3\2\2\2\177\u0080")
        buf.write("\7\61\2\2\u0080\u0081\7,\2\2\u0081\u0085\3\2\2\2\u0082")
        buf.write("\u0084\13\2\2\2\u0083\u0082\3\2\2\2\u0084\u0087\3\2\2")
        buf.write("\2\u0085\u0086\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u0088")
        buf.write("\3\2\2\2\u0087\u0085\3\2\2\2\u0088\u0089\7,\2\2\u0089")
        buf.write("\u0092\7\61\2\2\u008a\u008e\7^\2\2\u008b\u008d\n\2\2\2")
        buf.write("\u008c\u008b\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c\3")
        buf.write("\2\2\2\u008e\u008f\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e")
        buf.write("\3\2\2\2\u0091\177\3\2\2\2\u0091\u008a\3\2\2\2\u0092\u0093")
        buf.write("\3\2\2\2\u0093\u0094\b\2\2\2\u0094\4\3\2\2\2\u0095\u0097")
        buf.write("\t\3\2\2\u0096\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098")
        buf.write("\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u009a\u009b\b\3\2\2\u009b\6\3\2\2\2\u009c\u009d\7q\2")
        buf.write("\2\u009d\u009e\7h\2\2\u009e\b\3\2\2\2\u009f\u00a0\7k\2")
        buf.write("\2\u00a0\u00a1\7p\2\2\u00a1\u00a2\7j\2\2\u00a2\u00a3\7")
        buf.write("g\2\2\u00a3\u00a4\7t\2\2\u00a4\u00a5\7k\2\2\u00a5\u00a6")
        buf.write("\7v\2\2\u00a6\n\3\2\2\2\u00a7\u00a8\7q\2\2\u00a8\u00a9")
        buf.write("\7w\2\2\u00a9\u00aa\7v\2\2\u00aa\f\3\2\2\2\u00ab\u00ac")
        buf.write("\7v\2\2\u00ac\u00ad\7t\2\2\u00ad\u00ae\7w\2\2\u00ae\u00af")
        buf.write("\7g\2\2\u00af\16\3\2\2\2\u00b0\u00b1\7h\2\2\u00b1\u00b2")
        buf.write("\7c\2\2\u00b2\u00b3\7n\2\2\u00b3\u00b4\7u\2\2\u00b4\u00b5")
        buf.write("\7g\2\2\u00b5\20\3\2\2\2\u00b6\u00b7\7d\2\2\u00b7\u00b8")
        buf.write("\7t\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb")
        buf.write("\7m\2\2\u00bb\22\3\2\2\2\u00bc\u00bd\7t\2\2\u00bd\u00be")
        buf.write("\7g\2\2\u00be\u00bf\7v\2\2\u00bf\u00c0\7w\2\2\u00c0\u00c1")
        buf.write("\7t\2\2\u00c1\u00c2\7p\2\2\u00c2\24\3\2\2\2\u00c3\u00c4")
        buf.write("\7h\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6\7t\2\2\u00c6\26")
        buf.write("\3\2\2\2\u00c7\u00c8\7e\2\2\u00c8\u00c9\7q\2\2\u00c9\u00ca")
        buf.write("\7p\2\2\u00ca\u00cb\7v\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd")
        buf.write("\7p\2\2\u00cd\u00ce\7w\2\2\u00ce\u00cf\7g\2\2\u00cf\30")
        buf.write("\3\2\2\2\u00d0\u00d1\7f\2\2\u00d1\u00d2\7q\2\2\u00d2\32")
        buf.write("\3\2\2\2\u00d3\u00d4\7h\2\2\u00d4\u00d5\7w\2\2\u00d5\u00d6")
        buf.write("\7p\2\2\u00d6\u00d7\7e\2\2\u00d7\u00d8\7v\2\2\u00d8\u00d9")
        buf.write("\7k\2\2\u00d9\u00da\7q\2\2\u00da\u00db\7p\2\2\u00db\34")
        buf.write("\3\2\2\2\u00dc\u00dd\7g\2\2\u00dd\u00de\7n\2\2\u00de\u00df")
        buf.write("\7u\2\2\u00df\u00e0\7g\2\2\u00e0\36\3\2\2\2\u00e1\u00e2")
        buf.write("\7k\2\2\u00e2\u00e3\7h\2\2\u00e3 \3\2\2\2\u00e4\u00e5")
        buf.write("\7y\2\2\u00e5\u00e6\7j\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8")
        buf.write("\7n\2\2\u00e8\u00e9\7g\2\2\u00e9\"\3\2\2\2\u00ea\u00eb")
        buf.write("\7d\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee")
        buf.write("\7n\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0\7c\2\2\u00f0\u00f1")
        buf.write("\7p\2\2\u00f1$\3\2\2\2\u00f2\u00f3\7k\2\2\u00f3\u00f4")
        buf.write("\7p\2\2\u00f4\u00f5\7v\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7")
        buf.write("\7i\2\2\u00f7\u00f8\7g\2\2\u00f8\u00f9\7t\2\2\u00f9&\3")
        buf.write("\2\2\2\u00fa\u00fb\7h\2\2\u00fb\u00fc\7n\2\2\u00fc\u00fd")
        buf.write("\7q\2\2\u00fd\u00fe\7c\2\2\u00fe\u00ff\7v\2\2\u00ff(\3")
        buf.write("\2\2\2\u0100\u0101\7u\2\2\u0101\u0102\7v\2\2\u0102\u0103")
        buf.write("\7t\2\2\u0103\u0104\7k\2\2\u0104\u0105\7p\2\2\u0105\u0106")
        buf.write("\7i\2\2\u0106*\3\2\2\2\u0107\u0108\7c\2\2\u0108\u0109")
        buf.write("\7t\2\2\u0109\u010a\7t\2\2\u010a\u010b\7c\2\2\u010b\u010c")
        buf.write("\7{\2\2\u010c,\3\2\2\2\u010d\u010e\7x\2\2\u010e\u010f")
        buf.write("\7q\2\2\u010f\u0110\7k\2\2\u0110\u0111\7f\2\2\u0111.\3")
        buf.write("\2\2\2\u0112\u0113\7c\2\2\u0113\u0114\7w\2\2\u0114\u0115")
        buf.write("\7v\2\2\u0115\u0116\7q\2\2\u0116\60\3\2\2\2\u0117\u0118")
        buf.write("\7-\2\2\u0118\62\3\2\2\2\u0119\u011a\7/\2\2\u011a\64\3")
        buf.write("\2\2\2\u011b\u011c\7,\2\2\u011c\66\3\2\2\2\u011d\u011e")
        buf.write("\7\61\2\2\u011e8\3\2\2\2\u011f\u0120\7\'\2\2\u0120:\3")
        buf.write("\2\2\2\u0121\u0122\7#\2\2\u0122<\3\2\2\2\u0123\u0124\7")
        buf.write("(\2\2\u0124\u0125\7(\2\2\u0125>\3\2\2\2\u0126\u0127\7")
        buf.write("~\2\2\u0127\u0128\7~\2\2\u0128@\3\2\2\2\u0129\u012a\7")
        buf.write("?\2\2\u012a\u012b\7?\2\2\u012bB\3\2\2\2\u012c\u012d\7")
        buf.write("#\2\2\u012d\u012e\7?\2\2\u012eD\3\2\2\2\u012f\u0130\7")
        buf.write(">\2\2\u0130F\3\2\2\2\u0131\u0132\7>\2\2\u0132\u0133\7")
        buf.write("?\2\2\u0133H\3\2\2\2\u0134\u0135\7@\2\2\u0135J\3\2\2\2")
        buf.write("\u0136\u0137\7@\2\2\u0137\u0138\7?\2\2\u0138L\3\2\2\2")
        buf.write("\u0139\u013a\7<\2\2\u013a\u013b\7<\2\2\u013bN\3\2\2\2")
        buf.write("\u013c\u013d\7*\2\2\u013dP\3\2\2\2\u013e\u013f\7+\2\2")
        buf.write("\u013fR\3\2\2\2\u0140\u0141\7]\2\2\u0141T\3\2\2\2\u0142")
        buf.write("\u0143\7_\2\2\u0143V\3\2\2\2\u0144\u0145\7\60\2\2\u0145")
        buf.write("X\3\2\2\2\u0146\u0147\7.\2\2\u0147Z\3\2\2\2\u0148\u0149")
        buf.write("\7=\2\2\u0149\\\3\2\2\2\u014a\u014b\7<\2\2\u014b^\3\2")
        buf.write("\2\2\u014c\u014d\7}\2\2\u014d`\3\2\2\2\u014e\u014f\7\177")
        buf.write("\2\2\u014fb\3\2\2\2\u0150\u0151\7?\2\2\u0151d\3\2\2\2")
        buf.write("\u0152\u0169\7\62\2\2\u0153\u0157\t\4\2\2\u0154\u0156")
        buf.write("\5i\65\2\u0155\u0154\3\2\2\2\u0156\u0159\3\2\2\2\u0157")
        buf.write("\u0155\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u0164\3\2\2\2")
        buf.write("\u0159\u0157\3\2\2\2\u015a\u015c\5g\64\2\u015b\u015a\3")
        buf.write("\2\2\2\u015b\u015c\3\2\2\2\u015c\u015e\3\2\2\2\u015d\u015f")
        buf.write("\5i\65\2\u015e\u015d\3\2\2\2\u015f\u0160\3\2\2\2\u0160")
        buf.write("\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0163\3\2\2\2")
        buf.write("\u0162\u015b\3\2\2\2\u0163\u0166\3\2\2\2\u0164\u0162\3")
        buf.write("\2\2\2\u0164\u0165\3\2\2\2\u0165\u0167\3\2\2\2\u0166\u0164")
        buf.write("\3\2\2\2\u0167\u0169\b\63\3\2\u0168\u0152\3\2\2\2\u0168")
        buf.write("\u0153\3\2\2\2\u0169f\3\2\2\2\u016a\u016b\7a\2\2\u016b")
        buf.write("h\3\2\2\2\u016c\u016d\t\5\2\2\u016dj\3\2\2\2\u016e\u016f")
        buf.write("\5e\63\2\u016f\u0170\5m\67\2\u0170\u0171\3\2\2\2\u0171")
        buf.write("\u0172\b\66\4\2\u0172\u017c\3\2\2\2\u0173\u0175\5e\63")
        buf.write("\2\u0174\u0176\5m\67\2\u0175\u0174\3\2\2\2\u0175\u0176")
        buf.write("\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u0178\5o8\2\u0178\u0179")
        buf.write("\3\2\2\2\u0179\u017a\b\66\5\2\u017a\u017c\3\2\2\2\u017b")
        buf.write("\u016e\3\2\2\2\u017b\u0173\3\2\2\2\u017cl\3\2\2\2\u017d")
        buf.write("\u017f\7\60\2\2\u017e\u0180\t\5\2\2\u017f\u017e\3\2\2")
        buf.write("\2\u0180\u0181\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182")
        buf.write("\3\2\2\2\u0182n\3\2\2\2\u0183\u0185\t\6\2\2\u0184\u0186")
        buf.write("\t\7\2\2\u0185\u0184\3\2\2\2\u0185\u0186\3\2\2\2\u0186")
        buf.write("\u0187\3\2\2\2\u0187\u018b\t\4\2\2\u0188\u018a\t\5\2\2")
        buf.write("\u0189\u0188\3\2\2\2\u018a\u018d\3\2\2\2\u018b\u0189\3")
        buf.write("\2\2\2\u018b\u018c\3\2\2\2\u018cp\3\2\2\2\u018d\u018b")
        buf.write("\3\2\2\2\u018e\u0192\t\b\2\2\u018f\u0191\t\t\2\2\u0190")
        buf.write("\u018f\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190\3\2\2\2")
        buf.write("\u0192\u0193\3\2\2\2\u0193r\3\2\2\2\u0194\u0192\3\2\2")
        buf.write("\2\u0195\u019b\5w<\2\u0196\u019a\n\n\2\2\u0197\u0198\7")
        buf.write("^\2\2\u0198\u019a\5u;\2\u0199\u0196\3\2\2\2\u0199\u0197")
        buf.write("\3\2\2\2\u019a\u019d\3\2\2\2\u019b\u0199\3\2\2\2\u019b")
        buf.write("\u019c\3\2\2\2\u019c\u019e\3\2\2\2\u019d\u019b\3\2\2\2")
        buf.write("\u019e\u019f\5w<\2\u019f\u01a0\b:\6\2\u01a0t\3\2\2\2\u01a1")
        buf.write("\u01a2\t\13\2\2\u01a2v\3\2\2\2\u01a3\u01a4\7$\2\2\u01a4")
        buf.write("x\3\2\2\2\u01a5\u01a6\13\2\2\2\u01a6\u01a7\b=\7\2\u01a7")
        buf.write("z\3\2\2\2\u01a8\u01ae\5w<\2\u01a9\u01ad\n\f\2\2\u01aa")
        buf.write("\u01ab\7^\2\2\u01ab\u01ad\5u;\2\u01ac\u01a9\3\2\2\2\u01ac")
        buf.write("\u01aa\3\2\2\2\u01ad\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2")
        buf.write("\u01ae\u01af\3\2\2\2\u01af\u01b2\3\2\2\2\u01b0\u01ae\3")
        buf.write("\2\2\2\u01b1\u01b3\t\r\2\2\u01b2\u01b1\3\2\2\2\u01b3\u01b4")
        buf.write("\3\2\2\2\u01b4\u01b5\b>\b\2\u01b5\u01b6\b>\t\2\u01b6|")
        buf.write("\3\2\2\2\u01b7\u01bd\5w<\2\u01b8\u01bc\n\n\2\2\u01b9\u01ba")
        buf.write("\7^\2\2\u01ba\u01bc\5u;\2\u01bb\u01b8\3\2\2\2\u01bb\u01b9")
        buf.write("\3\2\2\2\u01bc\u01bf\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd")
        buf.write("\u01be\3\2\2\2\u01be\u01c0\3\2\2\2\u01bf\u01bd\3\2\2\2")
        buf.write("\u01c0\u01c1\7^\2\2\u01c1\u01c2\n\13\2\2\u01c2\u01c3\3")
        buf.write("\2\2\2\u01c3\u01c4\b?\n\2\u01c4\u01c5\b?\13\2\u01c5~\3")
        buf.write("\2\2\2\31\2\u0085\u008e\u0091\u0098\u0157\u015b\u0160")
        buf.write("\u0164\u0168\u0175\u017b\u0181\u0185\u018b\u0192\u0199")
        buf.write("\u019b\u01ac\u01ae\u01b2\u01bb\u01bd\f\b\2\2\3\63\2\3")
        buf.write("\66\3\3\66\4\3:\5\3=\6\3>\7\3>\b\3?\t\3?\n")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CMT = 1
    WS = 2
    OF = 3
    INHERIT = 4
    OUT = 5
    TRUE = 6
    FALSE = 7
    BREAK = 8
    RETURN = 9
    FOR = 10
    CONTINUE = 11
    DO = 12
    FUNCTION = 13
    ELSE = 14
    IF = 15
    WHILE = 16
    BOOL_TYP = 17
    INT_TYP = 18
    FLOAT_TYP = 19
    STRING_TYP = 20
    ARR_TYP = 21
    VOID_TYP = 22
    AUTO_TYP = 23
    PLUS = 24
    MINUS = 25
    MUL = 26
    DIV = 27
    MOD = 28
    NOT = 29
    AND = 30
    OR = 31
    D_EQ = 32
    NOT_EQ = 33
    LESS = 34
    LEQ = 35
    GREAT = 36
    GEQ = 37
    CONCAT = 38
    LB = 39
    RB = 40
    SLB = 41
    SRB = 42
    DOT = 43
    COMMA = 44
    SM = 45
    COlON = 46
    LCB = 47
    RCB = 48
    EQ = 49
    INTEGER = 50
    FLOAT = 51
    ID = 52
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
            "CMT", "WS", "OF", "INHERIT", "OUT", "TRUE", "FALSE", "BREAK", 
            "RETURN", "FOR", "CONTINUE", "DO", "FUNCTION", "ELSE", "IF", 
            "WHILE", "BOOL_TYP", "INT_TYP", "FLOAT_TYP", "STRING_TYP", "ARR_TYP", 
            "VOID_TYP", "AUTO_TYP", "PLUS", "MINUS", "MUL", "DIV", "MOD", 
            "NOT", "AND", "OR", "D_EQ", "NOT_EQ", "LESS", "LEQ", "GREAT", 
            "GEQ", "CONCAT", "LB", "RB", "SLB", "SRB", "DOT", "COMMA", "SM", 
            "COlON", "LCB", "RCB", "EQ", "INTEGER", "FLOAT", "ID", "STRING", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "CMT", "WS", "OF", "INHERIT", "OUT", "TRUE", "FALSE", 
                  "BREAK", "RETURN", "FOR", "CONTINUE", "DO", "FUNCTION", 
                  "ELSE", "IF", "WHILE", "BOOL_TYP", "INT_TYP", "FLOAT_TYP", 
                  "STRING_TYP", "ARR_TYP", "VOID_TYP", "AUTO_TYP", "PLUS", 
                  "MINUS", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "D_EQ", 
                  "NOT_EQ", "LESS", "LEQ", "GREAT", "GEQ", "CONCAT", "LB", 
                  "RB", "SLB", "SRB", "DOT", "COMMA", "SM", "COlON", "LCB", 
                  "RCB", "EQ", "INTEGER", "UNDER", "DIGIT", "FLOAT", "DEC", 
                  "EXP", "ID", "STRING", "ESCAPE", "D_QUOTE", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[49] = self.INTEGER_action 
            actions[52] = self.FLOAT_action 
            actions[56] = self.STRING_action 
            actions[59] = self.ERROR_CHAR_action 
            actions[60] = self.UNCLOSE_STRING_action 
            actions[61] = self.ILLEGAL_ESCAPE_action 
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
            self.text = self.text[1:]
     

        if actionIndex == 6:
            raise UncloseString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            self.text = self.text[1:]
     

        if actionIndex == 8:
            raise IllegalEscape(self.text)
     


