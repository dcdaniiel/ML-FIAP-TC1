import numpy as np

from churn.config import SEED, set_seed


def test_set_seed_is_reproducible():
    set_seed(SEED)
    first = np.random.rand(3)
    set_seed(SEED)
    second = np.random.rand(3)
    assert np.array_equal(first, second)
