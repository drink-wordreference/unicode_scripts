import re

from .data import Script, RANGE_DICT

def DetectScript(char):
  """Detects the script of a character"""

  try:
    return RANGE_DICT[ord(char)]
  except KeyError:
    return None

_WORD = '(?=\S)[^/\[\]]+'
IPA_REGEX = fr'(?:^|(?<=\W))(/{_WORD}/|\[{_WORD}\])(?:$|(?=\W))'

# TODO: Add tests.
def FindAndRemoveIPA(string):
  return re.sub(IPA_REGEX, '', string)

def DetectScripts(string):
  """Detects all scripts used in the string"""

  no_ipa_string = FindAndRemoveIPA(string)
  scripts = {DetectScript(char) for char in no_ipa_string}
  scripts.discard(None)
  if len(no_ipa_string) < len(string):
    scripts.add(Script.IPA)
  return scripts
