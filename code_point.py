class CodePoint(int):
  """An int that represents a code point and prints as hex"""

  def __new__(cls, arg):
    try:
      arg = ord(arg)
    except TypeError:
      pass
    return super().__new__(cls, arg)

  def __str__(self):
    return hex(self)

  def __repr__(self):
    return hex(self)

class CodePointString(str):
  """A string whose repr() is fully escaped with codepoints

  Example:
    repr(CodePointString('z')) -> r"'\x7A'"  # (prints as: '\x7A')
  """

  def __new__(cls, arg):
    if isinstance(arg, int):
      arg = chr(arg)
    return super().__new__(cls, arg)

  def __repr__(self):
    return "'" + ''.join(self.escape_char(c) for c in self) + "'"

  @staticmethod
  def escape_char(c):
    s = f'{ord(c):X}'
    if len(s) <= 2:
      pad = 2
      char = 'x'
    elif len(s) <= 4:
      pad = 4
      char = 'u'
    elif len(s) <= 8:
      pad = 8
      char = 'U'
    else:
      assert(False)
    return '\\' + char + (pad - len(s)) * '0' + s

class UnicodeCodePoint(CodePoint):
  """An int that represents a code point and prints as U+0000"""

  def __str__(self):
    return f'U+{self:04X}'
