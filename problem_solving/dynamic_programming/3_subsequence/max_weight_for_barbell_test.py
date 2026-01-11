import pytest

from .max_weight_for_barbell import get_max_weights


@pytest.mark.parametrize("weights, maxCapacity, expected", [
    ([7, 1, 5, 6, 2], 7, 7),  # From example
    ([1, 2, 3], 6, 6),  # All weights can be used
    ([], 5, 0),  # No weights
    ([5], 5, 5),  # Single weight equals capacity
    ([6, 4, 3], 5, 4),  # Cannot combine to make 5
    ([8, 10, 9], 7, 0),  # All weights too large
    ([1, 1, 1, 1, 1, 1, 1], 5, 5),  # Duplicates
    ([1, 4, 3, 5], 7, 7),  # Best combo 4 + 3
])
def test_get_max_weights(weights, maxCapacity, expected):
    assert get_max_weights(weights, maxCapacity) == expected
