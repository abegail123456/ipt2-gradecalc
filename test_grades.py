# test_grades.py – ACTIVITY 2 STARTER
# Goal: at least 8 tests, use @pytest.mark.parametrize at least once,
#       and reach at least 90% coverage of grades.py.
#
# Run:   python -m pytest -v
#        python -m pytest --cov=grades --cov-report=term-missing
import pytest

from grades import compute_final_grade, remark


# ---------------------------------------------------------------------
# EXAMPLE (keep it – it counts as 1 of your 8 tests)
# Arrange – Act – Assert, like Slide 17.
# ---------------------------------------------------------------------
def test_typical_scores():
    prelim, midterm, finals = 80, 85, 90             # Arrange
    result = compute_final_grade(prelim, midterm, finals)   # Act
    assert result == pytest.approx(85.5)             # Assert: 24 + 25.5 + 36
    # Tip: use pytest.approx() when comparing decimals (floats).


# ---------------------------------------------------------------------
# TODO 1 – NORMAL VALUES
#   Use @pytest.mark.parametrize to check several (prelim, midterm, finals,
#   expected) rows in ONE test function. Work out each expected value by hand.
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# TODO 2 – ZERO AND 100
#   What is the final grade when every score is 0? When every score is 100?
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# TODO 3 – THE PASSING BOUNDARY (remark)
#   74.99 -> ?    75 -> ?    (and maybe 75.01, 0, 100)
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# TODO 4 – INVALID SCORES
#   Scores below 0 or above 100 must raise ValueError.
#   Check each position (prelim, midterm, finals), e.g. -1 and 101.
#       with pytest.raises(ValueError):
#           compute_final_grade(...)
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# TODO 5 (optional) – ROUNDING
#   The result is rounded to 2 decimals. Find inputs that prove it.
# ---------------------------------------------------------------------
