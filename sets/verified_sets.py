from numbers import Integral


class UniquenessError(KeyError):
    pass


class VerifiedSet(set):
    def __init__(self, iterable):
        for item in iterable:
            self._verify(item)
        super().__init__(iterable)

    def _verify(self, item):
        raise NotImplementedError

    def add(self, element):
        self._verify(element)
        super().add(element)

    def update(self, *s):
        for set in s:
            for item in set:
                self._verify(item)
        super().update(*s)

    def symmetric_difference_update(self, s):
        for item in s:
            self._verify(item)
        super().symmetric_difference_update(s)

    def union(self, *s):
        for set in s:
            for item in set:
                self._verify(item)
        c = super().union(*s)
        return type(self)(c)

    def intersection(self, *s):
        for set in s:
            for item in set:
                self._verify(item)
        c = super().intersection(*s)
        return type(self)(c)

    def difference(self, *s):
        for set in s:
            for item in set:
                self._verify(item)
        c = super().difference(*s)
        return type(self)(c)

    def symmetric_difference(self, s):
        for item in s:
            self._verify(item)
        c = super().symmetric_difference(s)
        return type(self)(c)

    def copy(self):
        c = super().copy()
        return type(self)(c)


class IntSet(VerifiedSet):
    def _verify(self, item):
        if not isinstance(item, Integral):
            raise TypeError("IntSet expected an integer, got "
                            f"{type(item).__name__}")


class UniqueSet(VerifiedSet):
    def _verify(self, item):
        if self.__contains__(item):
            raise UniquenessError(f"UniqueSet already contains {item}; it "
                                  "must contain unique elements")
