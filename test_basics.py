# tests/test_basics.py
def test_addition():
    """
    TC-US000-001: pytest sanity check.

    This test verifies that the testing environment is set up correctly.
    It ensures that:
    - Pytest is installed and can discover and run tests
    - A basic mathematical operation works as expected
    - The test suite reports a passing result for this trivial case
    """
    assert 2 + 2 == 4
