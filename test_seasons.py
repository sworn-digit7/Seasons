import pytest
from seasons import minutes

def test_minutes():
    with pytest.raises(SystemExit):
        minutes("January")

    with pytest.raises(SystemExit):
        minutes("January 12, 2020")
