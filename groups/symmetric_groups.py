from example_code.groups import Group
import numpy as np


class SymmetricGroup(Group):
    """A symmetric group represented by a permutation of the
    integers between 0 and n-1 inclusive."""

    symbol = "S"

    def _validate(self, value):
        """Ensure that value is an allowed element value in this group."""
        if not (isinstance(value, np.ndarray)
                and np.all(sorted(value) == np.arange(0, self.n))):
            raise ValueError(
                (
                    "Element value must be a list containing a permutation of "
                    f"the integers between 0 and {self.n - 1} inclusive"
                )
            )

    def operation(self, a, b):
        """Perform the group operation on two values.
        
        The group operation is composition of permutations.
        """
        return a[b]
