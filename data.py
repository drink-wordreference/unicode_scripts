import enum

from ranges import Range, RangeDict

from code_point import UnicodeCodePoint

class Script(enum.Enum):
  Latn = 'Latin'
  Grek = 'Greek'
  Cyrl = 'Cyrillic'
  Armn = 'Armenian'
  Hebr = 'Hebrew'
  Arab = 'Arabic'
  Syrc = 'Syriac'
  Thaa = 'Thaana'
  Nkoo = "N'Ko"
  Samr = 'Samaritan'
  Mand = 'Mandaic'

class URange(Range):
  def __init__(self, start, end):
    super().__init__(UnicodeCodePoint(start), UnicodeCodePoint(end))

# Comments indicate the official title(s) of the Unicode Range.
DATA = {
  Script.Latn: [
    URange(0x0041, 0x005A),  # Basic Latin
    URange(0x0061, 0x007A),  # Latin-1 Supplement
    URange(0x00C0, 0x00D6),  # "
    URange(0x00D8, 0x00F6),  # "
    URange(0x00F8, 0x00FF),  # "
    URange(0x0100, 0x02AF),  # Latin Extended-A + -B + IPA Extensions
    URange(0x1E00, 0x1EFF),  # Latin Extended Additional
    URange(0xFB00, 0xFB06),  # Alphabetic Presentation Forms
  ],
  Script.Grek: [
    URange(0x0370, 0x0373),  # Greek
    URange(0x0376, 0x0377),  # "
    URange(0x037B, 0x037D),  # "
    URange(0x037F, 0x037F),  # "
    URange(0x0386, 0x0386),  # "
    URange(0x0388, 0x03FF),  # "
    URange(0x1F00, 0x1FBC),  # Greek Extended
    URange(0x1FC2, 0x1FCC),  # "
    URange(0x1FD0, 0x1FDC),  # "
    URange(0x1FE0, 0x1FEC),  # "
    URange(0x1FF0, 0x1FFC),  # "
  ],
  Script.Cyrl: [
    URange(0x0400, 0x0481),  # Cyrillic
    URange(0x048A, 0x052F),  # " + Cyrillic Supplement
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
}

RANGE_DICT = RangeDict((r, s) for s in DATA for r in DATA[s])
