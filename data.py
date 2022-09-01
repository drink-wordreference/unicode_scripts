import enum

from ranges import Range, RangeDict

from code_point import UnicodeCodePoint

class Script(enum.Enum):
  LATN = 'Latin'
  CYRL = 'Cyrillic'
  GREK = 'Greek'

class URange(Range):
  def __init__(self, start, end):
    super().__init__(UnicodeCodePoint(start), UnicodeCodePoint(end))

DATA = {
  Script.LATN: [
    URange(0x0041, 0x005A),
    URange(0x0061, 0x007A),
    URange(0x00C0, 0x00D6),
    URange(0x00D8, 0x00F6),
    URange(0x00F8, 0x00FF),
    URange(0x0100, 0x017F),
  ]
}

RANGE_DICT = RangeDict((r, s) for s in DATA for r in DATA[s])
