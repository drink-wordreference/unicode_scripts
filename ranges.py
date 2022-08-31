import bisect

# TODO: Use a proper unit test framework for all these tests.
def _assert_error(thunk, expect):
  try:
    thunk()
  except expect:
    return
  except:
    pass
  assert(False)

class Range:
  """Comparable inclusive range

  Properties:
    - For any Range(a, b), a <= b
    - For any number n, n is in Range(a, b) iff a <= n <= b
    - Range(a, b) < Range(c, d) iff b < c

  Examples:
    - Range(3, 1) -> ValueError
    - 0 in Range(1, 4) -> False
    - 1 in Range(1, 4) -> True
    - 2 in Range(1, 4) -> True
    - 4 in Range(1, 4) -> True
    - 5 in Range(1, 4) -> False
    - Range(1, 4) < Range(5, 9) -> True
    - Range(1, 4) < Range(4, 9) -> False
  """

  def __init__(self, start, end):
    if end < start:
      raise ValueError(f'Invalid range Range({start}, {end}). End of '
                       f'range must be greater than or equal to '
                       f'start of range.')
    self._start = start
    self._end = end

  def __repr__(self):
    return f'Range({self._start}, {self._end})'

  def start(self):
    return self._start

  def end(self):
    return self._end

  def __eq__(self, other):
    return self._start == other._start and self._end == other._end

  def __lt__(self, other):
    return self._end < (
        other._start if isinstance(other, Range) else other)

  def __gt__(self, other):
    return self._start > (
        other._end if isinstance(other, Range) else other)

  def __contains__(self, n):
    return self._start <= n <= self._end

  def __iter__(self):
    return range(self._start, self._end + 1)

  # TODO: Use a proper unit test framework for all these tests.
  @classmethod
  def _test(cls):
    _assert_error(lambda: cls(3, 1), ValueError)
    assert(0 not in Range(1, 4))
    assert(1 in Range(1, 4))
    assert(2 in Range(1, 4))
    assert(4 in Range(1, 4))
    assert(5 not in Range(1, 4))
    assert(Range(1, 4) < Range(5, 9))
    assert(not (Range(1, 4) < Range(4, 9)))
    assert(Range(5, 9) > Range(1, 4))
    assert(Range(1, 4) != Range(2, 5))
    assert(Range(1, 4) != Range(1, 5))
    assert(Range(1, 4) == Range(1, 4))
    assert(0 < Range(1, 4))
    assert(not (0 > Range(1, 4)))
    assert(not (1 < Range(1, 4)))
    assert(not (1 > Range(1, 4)))
    assert(not (2 < Range(1, 4)))
    assert(not (2 > Range(1, 4)))
    assert(not (4 < Range(1, 4)))
    assert(not (4 > Range(1, 4)))
    assert(not (5 < Range(1, 4)))
    assert(5 > Range(1, 4))

class RangeDict:
  """Dict mapping ranges of numbers to any value

  Optimized for fast lookup by storing the ranges in a sorted list,
  insertions and deletions are slower.

  Example:
  range_dict = RangeDict([(Range(1, 3), 'foo'), (Range(5, 9), 'bar')])
  0 in range_dict -> False
  2 in range_dict -> True
  4 in range_dict -> False
  6 in range_dict -> True
  range_dict[2] -> 'foo'
  range_dict[4] -> 'bar'

  """

  def __init__(self, rangemap):
    """
    Input:
      rangemap: List of 2-tuples, each tuple maps a Range to a value.
    """

    self._data = sorted(rangemap, key=lambda tup: tup[0])
    self._validate()

  def _validate(self):
    prev = None
    for r in self._data:
      if not (prev is None or prev < r):
        assert(not (prev > r))  # This would imply a sorting error.
        raise ValueError(f'RangeDict: Ranges cannot overlap, but {r} '
                         f'overlaps with {prev}.')
      prev = r

  def __repr__(self):
    return f'RangeDict({self._data})'

  def __eq__(self, other):
    return self._data == other._data

  def _find(self, n):
    return bisect.bisect_left(self._data, n, key=lambda tup: tup[0])

  def __contains__(self, n):
    """
    Input:
      n: number
    """

    i = self._find(n)
    return i < len(self._data) and n in self._data[i][0]

  def __getitem__(self, n):
    """
    Input:
      n: number
    """

    i = self._find(n)
    if i < len(self._data) and n in self._data[i][0]:
      return self._data[i][1]
    raise KeyError

  def __setitem__(self, r, value):
    """
    Input:
      r: Range
    """


    i = self._find(r.start())
    if i >= len(self._data) or r < self._data[i][0]:
      self._data.insert(i, (r, value))
    elif r == self._data[i][0]:
      self._data[i] = (r, value)
    else:
      raise KeyError

  def __delitem__(self, r, value):
    """
    Input:
      r: Range
    """

    i = self._find(r.start())
    if i < len(self._data) and r == self._data[i][0]:
      del self._data[i]
    else:
      raise KeyError

  # TODO: Use a proper unit test framework for all these tests.
  @classmethod
  def _test(cls):
    d = RangeDict([(Range(1, 3), 'A'), (Range(5, 9), 'B')])
    assert(d != RangeDict([(Range(1, 3), 'B'), (Range(5, 9), 'A')]))
    assert(d == RangeDict([(Range(5, 9), 'B'), (Range(1, 3), 'A')]))
    _assert_error(
        lambda: RangeDict([(Range(1, 5), 'A'), (Range(5, 9), 'A')]),
        ValueError)
    assert(0 not in d)
    assert(1 in d)
    assert(2 in d)
    assert(3 in d)
    assert(4 not in d)
    assert(5 in d)
    assert(6 in d)
    assert(9 in d)
    assert(10 not in d)
    assert(d[2] == 'A')
    assert(d[6] == 'B')

# TODO: Use a proper unit test framework for all these tests.
def _test_bisect():
  # Verify that bisect_left works the way we intend it to.
  l = [Range(1, 3), Range(5, 9)]
  assert(bisect.bisect_left(l, 0) == 0)
  assert(bisect.bisect_left(l, 1) == 0)
  assert(bisect.bisect_left(l, 1) == 0)
  assert(bisect.bisect_left(l, 2) == 0)
  assert(bisect.bisect_left(l, 3) == 0)
  assert(bisect.bisect_left(l, 4) == 1)
  assert(bisect.bisect_left(l, 5) == 1)
  assert(bisect.bisect_left(l, 6) == 1)
  assert(bisect.bisect_left(l, 9) == 1)
  assert(bisect.bisect_left(l, 10) == 2)

# TODO: Use a proper unit test framework for all these tests.
def _test():
  Range._test()
  _test_bisect()
  RangeDict._test()
