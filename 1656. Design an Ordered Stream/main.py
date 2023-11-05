class OrderedStream:

  def __init__(self, n: int):
    self.a, self.i = [None] * (n+2), 1

  def insert(self, id: int, value: str) -> List[str]:
    a, i, self.a[id] = self.a, self.i, value
    if a[i]:
      self.i = a.index(None, i+1)
      return a[i:self.i]
