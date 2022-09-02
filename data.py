import enum

from .ranges import Range, RangeDict

from .code_point import UnicodeCodePoint

class Script(enum.Enum):
  Zzzz = 'Unknown'
  Zyyy = 'Common'
  IPA  = 'IPA'
  Latn = 'Latin'
  Grek = 'Greek'
  Copt = 'Coptic'
  Cyrl = 'Cyrillic'
  Armn = 'Armenian'
  Hebr = 'Hebrew'
  Arab = 'Arabic'
  Syrc = 'Syriac'
  Thaa = 'Thaana'
  Nkoo = "N'Ko"
  Samr = 'Samaritan'
  Mand = 'Mandaic'
  Deva = 'Devanagari'
  Beng = 'Bengali'
  Guru = 'Gurmukhi'
  Gujr = 'Gujarati'
  Orya = 'Oriya'
  Taml = 'Tamil'
  Telu = 'Telugu'
  Knda = 'Kannada'
  Mlym = 'Malayalam'
  Sinh = 'Sinhala'
  Thai = 'Thai'
  Laoo = 'Lao'
  Tibt = 'Tibetan'
  Mymr = 'Myanmar'
  Geor = 'Georgian'
  Hang = 'Hangul'
  Ethi = 'Ethiopic'
  Cher = 'Cherokee'
  Cans = 'Unified Canadian Aboriginal Syllabics'
  Ogam = 'Ogham'
  Runr = 'Runic'
  Tglg = 'Tagalog'
  Hano = 'Hanunoo'
  Buhd = 'Buhid'
  Tagb = 'Tagbanwa'
  Khmr = 'Khmer'
  Mong = 'Mongolian'
  Limb = 'Limbu'
  Tale = 'Tai Le'
  Talu = 'New Tai Lue'
  Bugi = 'Buginese'
  Lana = 'Tai Tham'
  Bali = 'Balinese'
  Sund = 'Sundanese'
  Batk = 'Batak'
  Lepc = 'Lepcha'
  Olck = 'Ol Chiki'
  Brai = 'Braille'
  Glag = 'Glagolitic'
  Tfng = 'Tifinagh'
  Hani = 'Han'
  Hrkt = 'Japanese syllabaries'
  Bopo = 'Bopomofo'
  Yiii = 'Yi'
  Lisu = 'Lisu'
  Vaii = 'Vai'
  Bamu = 'Bamum'
  Sylo = 'Syloti Nagri'
  Phag = 'Phags-pa'
  Saur = 'Saurashtra'
  Kali = 'Kayah Li'
  Rjng = 'Rejang'
  Java = 'Javanese'
  Cham = 'Cham'
  Tavt = 'Tai Viet'
  Mtei = 'Meitei Mayek'
  Linb = 'Linear B'
  PHAISTOS = 'Phaistos Disc'
  Lyci = 'Lycian'
  Cari = 'Carian'
  Ital = 'Old Italic'
  Goth = 'Gothic'
  Perm = 'Old Permic'
  Ugar = 'Ugaritic'
  Xpeo = 'Old Persian'
  Dsrt = 'Deseret'
  Shaw = 'Shavian'
  Osma = 'Osmanya'
  Osge = 'Osage'
  Elba = 'Elbasan'
  Aghb = 'Caucasian Albanian'
  Vith = 'Vithkuqi'
  Lina = 'Linear A'
  Cprt = 'Cypriot syllabary'
  Armi = 'Imperial Aramaic'
  Palm = 'Palmyrene'
  Nbat = 'Nabataean'
  Hatr = 'Hatran'
  Phnx = 'Phoenician'
  Lydi = 'Lydian'
  Mero = 'Meroitic Hieroglyphs'
  Merc = 'Meroitic Cursive'
  Khar = 'Kharoshthi'
  Sarb = 'Old South Arabian'
  Narb = 'Old North Arabian'
  Mani = 'Manichaean'
  Avst = 'Avestan'
  Prti = 'Inscriptional Parthian'
  Phli = 'Inscriptional Pahlavi'
  Phlp = 'Psalter Pahlavi'
  Orkh = 'Old Turkic'
  Hung = 'Old Hungarian'
  Rohg = 'Hanifi Rohingya'
  Yezi = 'Yezidi'
  Sogo = 'Old Sogdian'
  Sogd = 'Sogdian'
  Ougr = 'Old Uyghur'
  Chrs = 'Chorasmian'
  Elym = 'Elymaic'

class URange(Range):
  def __init__(self, start, end):
    super().__init__(UnicodeCodePoint(start), UnicodeCodePoint(end))

# Comments indicate the official title(s) of the Unicode Block.
DATA = {
  Script.Latn: [
    URange(0x0041, 0x005A),  # Basic Latin
    URange(0x0061, 0x007A),  # Latin-1 Supplement
    URange(0x00C0, 0x00D6),  # "
    URange(0x00D8, 0x00F6),  # "
    URange(0x00F8, 0x00FF),  # "
    URange(0x0100, 0x02AF),  # Latin Extended-A + Latin Extended-B +
                             # IPA Extensions
    URange(0x1E00, 0x1EFF),  # Latin Extended Additional
    URange(0x1D00, 0x1D25),  # Phonetic Extensions
    URange(0x1D6C, 0x1D9A),  # " + Phonetic Extensions Supplement
    URange(0x2C60, 0x2C7B),  # Latin Extended-C
    URange(0x2C7E, 0x2C7F),  # "
    URange(0xA722, 0xA787),  # Latin Extended-D
    URange(0xA78B, 0xA7D9),  # "
    URange(0xA7F5, 0xA7F7),  # "
    URange(0xA7FA, 0xA7FF),  # "
    URange(0xAB30, 0xAB5A),  # Latin Extended-E
    URange(0xAB60, 0xAB68),  # "
    URange(0xFB00, 0xFB06),  # Alphabetic Presentation Forms
  ],
  Script.Grek: [
    URange(0x0370, 0x0373),  # Greek and Coptic
    URange(0x0376, 0x0377),  # "
    URange(0x037B, 0x037D),  # "
    URange(0x037F, 0x037F),  # "
    URange(0x0386, 0x0386),  # "
    URange(0x0388, 0x03E1),  # "
    URange(0x03F0, 0x03FF),  # "
    URange(0x1F00, 0x1FBC),  # Greek Extended
    URange(0x1FC2, 0x1FCC),  # "
    URange(0x1FD0, 0x1FDC),  # "
    URange(0x1FE0, 0x1FEC),  # "
    URange(0x1FF0, 0x1FFC),  # "
    URange(0x1D26, 0x1D2A),  # Phonetic Extensions
  ],
  Script.Copt: [
    URange(0x03E2, 0x03EF),  # Greek and Coptic
    URange(0x2C80, 0x2CEF),  # Coptic
    URange(0x2CF2, 0x2CF3),  # "
  ],
  Script.Cyrl: [
    URange(0x0400, 0x0481),  # Cyrillic
    URange(0x048A, 0x052F),  # " + Cyrillic Supplement
    URange(0x1C80, 0x1C88),  # Cyrillic Extended-C
    URange(0x1D2B, 0x1D2B),  # Phonetic Extensions
    URange(0xA640, 0xA66E),  # Cyrillic Extended-B
    URange(0xA680, 0xA69B),  # "
  ],
  Script.Armn: [
    URange(0x0531, 0x0556),  # Armenian
    URange(0x0560, 0x0588),  # "
    URange(0xFB13, 0xFB17),  # Alphabetic Presentation Forms
  ],
  Script.Hebr: [
    URange(0x05D0, 0x05F2),  # Hebrew
    URange(0xFB1D, 0xFB4F),  # Alphabetic Presentation Forms
  ],
  Script.Arab: [
    URange(0x0620, 0x063F),  # Arabic
    URange(0x0641, 0x064A),  # "
    URange(0x066E, 0x066F),  # "
    URange(0x0671, 0x0673),  # "
    URange(0x0675, 0x06D3),  # "
    URange(0x06D5, 0x06D5),  # "
    URange(0x06EE, 0x06EF),  # "
    URange(0x06FA, 0x06FF),  # "
    URange(0x0750, 0x077F),  # Arabic Supplement
    URange(0x0870, 0x0882),  # Arabic Extended-B
    URange(0x0886, 0x0886),  # "
    URange(0x0889, 0x088D),  # "
    URange(0x08A0, 0x08C8),  # Arabic Extended-A
    URange(0xFB50, 0xFDFF),  # Arabic Presentation Forms-A
    URange(0xFE70, 0xFEFC),  # Arabic Presentation Forms-B
  ],
  Script.Syrc: [
    URange(0x0710, 0x0710),  # Syriac
    URange(0x0712, 0x072F),  # "
    URange(0x074D, 0x074F),  # "
    URange(0x0860, 0x086A),  # Syriac Supplement
  ],
  Script.Thaa: [
    URange(0x0780, 0x07A5),  # Thaana
    URange(0x07B1, 0x07B1),  # "
  ],
  Script.Nkoo: [
    URange(0x07CA, 0x07EA),  # NKo
  ],
  Script.Samr: [
    URange(0x0800, 0x0815),  # Samaritan
  ],
  Script.Mand: [
    URange(0x0840, 0x0858),  # Mandaic
  ],
  Script.Deva: [
    URange(0x0904, 0x0939),  # Devanagari
    URange(0x0958, 0x0961),  # "
    URange(0x0972, 0x097F),  # "
    URange(0xA8FE, 0xA8FE),  # Devanagari Extended
  ],
  Script.Beng: [
    URange(0x0985, 0x09B9),  # Bengali
    URange(0x09CE, 0x09CE),  # "
    URange(0x09DC, 0x09E1),  # "
    URange(0x09F0, 0x09F1),  # "
    URange(0x09FC, 0x09FC),  # "
  ],
  Script.Guru: [
    URange(0x0A05, 0x0A39),  # Gurmukhi
    URange(0x0A59, 0x0A5E),  # "
  ],
  Script.Gujr: [
    URange(0x0A85, 0x0AB9),  # Gujarati
    URange(0x0AE0, 0x0AE1),  # "
    URange(0x0AF9, 0x0AF9),  # "
  ],
  Script.Orya: [
    URange(0x0B05, 0x0B39),  # Oriya
    URange(0x0B5C, 0x0B61),  # "
    URange(0x0B71, 0x0B71),  # "
  ],
  Script.Taml: [
    URange(0x0B85, 0x0BB9),  # Tamil
  ],
  Script.Telu: [
    URange(0x0C05, 0x0C39),  # Telugu
    URange(0x0C58, 0x0C61),  # "
  ],
  Script.Knda: [
    URange(0x0C85, 0x0CB9),  # Kannada
    URange(0x0CDD, 0x0CE1),  # "
  ],
  Script.Mlym: [
    URange(0x0D04, 0x0D3A),  # Malayalam
    URange(0x0D54, 0x0D56),  # "
    URange(0x0D5F, 0x0D61),  # "
    URange(0x0D7A, 0x0D7F),  # "
  ],
  Script.Sinh: [
    URange(0x0D85, 0x0DC6),  # Sinhala
  ],
  Script.Thai: [
    URange(0x0E01, 0x0E2E),  # Thai
  ],
  Script.Laoo: [
    URange(0x0E81, 0x0EAE),  # Lao
    URange(0x0EDE, 0x0EDF),  # "
  ],
  Script.Tibt: [
    URange(0x0F40, 0x0F6C),  # Tibetan
  ],
  Script.Mymr: [
    URange(0x1000, 0x102A),  # Myanmar
    URange(0x103F, 0x103F),  # "
    URange(0x104C, 0x1055),  # "
    URange(0x105A, 0x105D),  # "
    URange(0x1061, 0x1061),  # "
    URange(0x1065, 0x1066),  # "
    URange(0x106E, 0x1070),  # "
    URange(0x1075, 0x1082),  # "
    URange(0x108E, 0x108E),  # "
    URange(0xA9E0, 0xA9E4),  # Myanmar Extended-B
    URange(0xA9E7, 0xA9EF),  # "
    URange(0xA9FA, 0xA9FE),  # "
    URange(0xAA60, 0xAA6F),  # Myanmar Extended-A
    URange(0xAA74, 0xAA76),  # "
    URange(0xAA78, 0xAA7A),  # "
    URange(0xAA7E, 0xAA7F),  # "
  ],
  Script.Geor: [
    URange(0x10A0, 0x10FA),  # Georgian
    URange(0x10FC, 0x10FF),  # "
    URange(0x1C90, 0x1CBF),  # Georgian Extended
    URange(0x2D00, 0x2D2D),  # Georgian Supplement
  ],
  Script.Hang: [
    URange(0x1100, 0x115E),  # Hangul Jamo
    URange(0x1161, 0x11FF),  # "
    URange(0x3131, 0x3163),  # Hangul Compatibility Jamo
    URange(0x3165, 0x318E),  # "
    URange(0xA960, 0xA97F),  # Hangul Jamo Extended-A
    URange(0xAC00, 0xD7FF),  # Hangul Syllables +
                             # Hangul Jamo Extended-B
    URange(0xFFA1, 0xFFDF),  # Halfwidth and Fullwidth Forms
  ],
  Script.Ethi: [
    URange(0x1200, 0x135A),  # Ethiopic
    URange(0x1380, 0x138F),  # Ethiopic Supplement
    URange(0x2D80, 0x2DDF),  # Ethiopic Extended
    URange(0xAB00, 0xAB2F),  # Ethiopic Extended-A
  ],
  Script.Cher: [
    URange(0x13A0, 0x13FF),  # Cherokee
    URange(0xAB70, 0xABBF),  # Cherokee Supplement
  ],
  Script.Cans: [
    URange(0x1401, 0x166C),  # Unified Canadian Aboriginal Syllabics
    URange(0x166F, 0x167F),  # "
    URange(0x18B0, 0x18F5),  # " Extended
  ],
  Script.Ogam: [
    URange(0x1681, 0x169A),  # Ogham
  ],
  Script.Runr: [
    URange(0x16A0, 0x16EA),  # Runic
    URange(0x16F1, 0x16F8),  # "
  ],
  Script.Tglg: [
    URange(0x1700, 0x1711),  # Tagalog
    URange(0x171F, 0x171F),  # "
  ],
  Script.Hano: [
    URange(0x1720, 0x1731),  # Hanunoo
  ],
  Script.Buhd: [
    URange(0x1740, 0x1751),  # Buhid
  ],
  Script.Tagb: [
    URange(0x1760, 0x1770),  # Tagbanwa
  ],
  Script.Khmr: [
    URange(0x1780, 0x17B3),  # Khmer
  ],
  Script.Mong: [
    URange(0x1820, 0x18AA),  # Mongolian
  ],
  Script.Limb: [
    URange(0x1900, 0x191E),  # Limbu
  ],
  Script.Tale: [
    URange(0x1950, 0x1974),  # Tai Le
  ],
  Script.Talu: [
    URange(0x1980, 0x19C9),  # New Tai Lue
  ],
  Script.Bugi: [
    URange(0x1A00, 0x1A16),  # Buginese
  ],
  Script.Lana: [
    URange(0x1A20, 0x1A54),  # Tai Tham
    URange(0x1AA0, 0x1AA2),  # "
  ],
  Script.Bali: [
    URange(0x1B05, 0x1B33),  # Balinese
    URange(0x1B45, 0x1B4C),  # "
  ],
  Script.Sund: [
    URange(0x1B83, 0x1BA0),  # Sundanese
    URange(0x1BAE, 0x1BAF),  # "
    URange(0x1BBB, 0x1BBF),  # "
  ],
  Script.Batk: [
    URange(0x1BC0, 0x1BE5),  # Batak
  ],
  Script.Lepc: [
    URange(0x1C00, 0x1C23),  # Lepcha
    URange(0x1C4D, 0x1C4F),  # "
  ],
  Script.Olck: [
    URange(0x1C5A, 0x1C77),  # Ol Chiki
  ],
  Script.Brai: [
    URange(0x2800, 0x28FF),  # Braille Patterns
  ],
  Script.Glag: [
    URange(0x2C00, 0x2C5F),  # Glagolitic
  ],
  Script.Tfng: [
    URange(0x2D30, 0x2D67),  # Tifinagh
  ],
  Script.Hani: [
    URange(0x2E80, 0x2FDF),  # CJK Radicals Supplement +
                             # Kangxi Radicals
    URange(0x3190, 0x319F),  # Kanbun
    URange(0x31C0, 0x31EF),  # CJK Strokes
    URange(0x3400, 0x9FFF),  # CJK Unified Ideographs Extension A +
                             # Yijing Hexagram Symbols +
                             # CJK Unified Ideographs
    URange(0xF900, 0xFAFF),  # CJK Compatibility Ideographs
  ],
  Script.Hrkt: [
    URange(0x3040, 0x30FF),  # Hiragana + Katakana
    URange(0x31F0, 0x31FF),  # Katakana Phonetic Extensions
    URange(0xFF66, 0xFF9F),  # Halfwidth and Fullwidth Forms
  ],
  Script.Bopo: [
    URange(0x3100, 0x312F),  # Bopomofo
    URange(0x31A0, 0x31BF),  # Bopomofo Extended
  ],
  Script.Yiii: [
    URange(0xA000, 0xA4CF),  # Yi Syllables + Yi Radicals
  ],
  Script.Lisu: [
    URange(0xA4D0, 0xA4FD),  # Lisu
  ],
  Script.Vaii: [
    URange(0xA500, 0xA60D),  # Vai
    URange(0xA610, 0xA62B),  # "
  ],
  Script.Bamu: [
    URange(0xA6A0, 0xA6EF),  # Bamum
  ],
  Script.Sylo: [
    URange(0xA800, 0xA801),  # Syloti Nagri
    URange(0xA803, 0xA805),  # "
    URange(0xA807, 0xA80A),  # "
    URange(0xA80C, 0xA822),  # "
  ],
  Script.Phag: [
    URange(0xA840, 0xA866),  # Phags-pa
    URange(0xA869, 0xA870),  # "
  ],
  Script.Saur: [
    URange(0xA882, 0xA8B3),  # Saurashtra
  ],
  Script.Kali: [
    URange(0xA90A, 0xA925),  # Kayah Li
  ],
  Script.Rjng: [
    URange(0xA930, 0xA946),  # Rejang
  ],
  Script.Java: [
    URange(0xA984, 0xA9B2),  # Javanese
  ],
  Script.Cham: [
    URange(0xAA00, 0xAA28),  # Cham
    URange(0xAA40, 0xAA4B),  # "
  ],
  Script.Tavt: [
    URange(0xAA80, 0xAAAF),  # Tai Viet
    URange(0xAADB, 0xAADC),  # "
  ],
  Script.Mtei: [
    URange(0xAAE0, 0xAAEA),  # Meetei Mayek Extensions
    URange(0xABC0, 0xABE2),  # Meetei Mayek
  ],
  Script.Linb: [
    URange(0x10000, 0x100FF),  # Linear B Syllabary +
                               # Linear B Ideograms
  ],
  Script.PHAISTOS: [
    URange(0x101D0, 0x101FC),  # Phaistos Disc
  ],
  Script.Lyci: [
    URange(0x10280, 0x1029F),  # Lycian
  ],
  Script.Cari: [
    URange(0x102A0, 0x102DF),  # Carian
  ],
  Script.Ital: [
    URange(0x10300, 0x1031F),  # Old Italic
    URange(0x1032D, 0x1032F),  # "
  ],
  Script.Goth: [
    URange(0x10330, 0x1034F),  # Gothic
  ],
  Script.Perm: [
    URange(0x10350, 0x10375),  # Old Permic
  ],
  Script.Ugar: [
    URange(0x10380, 0x1039D),  # Ugaritic
  ],
  Script.Xpeo: [
    URange(0x103A0, 0x103CF),  # Old Persian
  ],
  Script.Dsrt: [
    URange(0x10400, 0x1044F),  # Deseret
  ],
  Script.Shaw: [
    URange(0x10450, 0x1047F),  # Shavian
  ],
  Script.Osma: [
    URange(0x10480, 0x1049F),  # Osmanya
  ],
  Script.Osge: [
    URange(0x104B0, 0x104FF),  # Osage
  ],
  Script.Elba: [
    URange(0x10500, 0x1052F),  # Elbasan
  ],
  Script.Aghb: [
    URange(0x10530, 0x10563),  # Caucasian Albanian
  ],
  Script.Vith: [
    URange(0x10570, 0x105BF),  # Vithkuqi
  ],
  Script.Lina: [
    URange(0x10600, 0x1073F),  # Linear A
    URange(0x10760, 0x1076F),  # "
  ],
  Script.Cprt: [
    URange(0x10800, 0x1083F),  # Cypriot Syllabary
  ],
  Script.Armi: [
    URange(0x10840, 0x10855),  # Imperial Aramaic
  ],
  Script.Palm: [
    URange(0x10860, 0x10876),  # Palmyrene
  ],
  Script.Nbat: [
    URange(0x10880, 0x1089E),  # Nabataean
  ],
  Script.Hatr: [
    URange(0x108E0, 0x108F5),  # Hatran
  ],
  Script.Phnx: [
    URange(0x10900, 0x10915),  # Phoenician
  ],
  Script.Lydi: [
    URange(0x10920, 0x10939),  # Lydian
  ],
  Script.Mero: [
    URange(0x10980, 0x1099D),  # Meroitic Hieroglyphs
  ],
  Script.Merc: [
    URange(0x109A0, 0x109B7),  # Meroitic Cursive
  ],
  Script.Khar: [
    URange(0x10A00, 0x10A00),  # Kharoshthi
    URange(0x10A10, 0x10A35),  # "
  ],
  Script.Sarb: [
    URange(0x10A60, 0x10A7C),  # Old South Arabian
  ],
  Script.Narb: [
    URange(0x10A80, 0x10A9C),  # Old North Arabian
  ],
  Script.Mani: [
    URange(0x10AC0, 0x10AE4),  # Manichaean
  ],
  Script.Avst: [
    URange(0x10B00, 0x10B35),  # Avestan
  ],
  Script.Prti: [
    URange(0x10B40, 0x10B55),  # Inscriptional Parthian
  ],
  Script.Phli: [
    URange(0x10B60, 0x10B72),  # Inscriptional Pahlavi
  ],
  Script.Phlp: [
    URange(0x10B80, 0x10B91),  # Psalter Pahlavi
  ],
  Script.Orkh: [
    URange(0x10C00, 0x10C48),  # Old Turkic
  ],
  Script.Hung: [
    URange(0x10C80, 0x10CB2),  # Old Hungarian
    URange(0x10CC0, 0x10CF2),  # "
  ],
  Script.Rohg: [
    URange(0x10D00, 0x10D23),  # Hanifi Rohingya
  ],
  Script.Yezi: [
    URange(0x10E80, 0x10EA9),  # Yezidi
    URange(0x10EB0, 0x10EB1),  # "
  ],
  Script.Sogo: [
    URange(0x10F00, 0x10F1C),  # Old Sogdian
    URange(0x10F27, 0x10F27),  # "
  ],
  Script.Sogd: [
    URange(0x10F30, 0x10F45),  # Sogdian
  ],
  Script.Ougr: [
    URange(0x10F70, 0x10F81),  # Old Uyghur
  ],
  Script.Chrs: [
    URange(0x10FB0, 0x10FC4),  # Chorasmian
  ],
  Script.Elym: [
    URange(0x10FE0, 0x10FF6),  # Elymaic
  ],
}

RANGE_DICT = RangeDict((r, s) for s in DATA for r in DATA[s])
