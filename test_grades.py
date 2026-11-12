# test_grades.py – ACTIVITY 2 STARTER
# Goal: at least 8 tests, use @pytest.mark.parametrize at least once,
#       and reach at least 90% coverage of grades.py.
#
# Run:   python -m pytest -v
#        python -m pytest --cov=grades --cov-report=term-missing
import pytest

from grades import compute_final_grade, remark


# ---------------------------------------------------------------------
# EXAMPLE (keep it – counts as 1 of your 8 tests)
# ---------------------------------------------------------------------
def test_typical_scores():
    prelim, midterm, finals = 80, 85, 90
    result = compute_final_grade(prelim, midterm, finals)
    assert result == pytest.approx(85.5)   # 24 + 25.5 + 36


# ---------------------------------------------------------------------
# TODO 1 – NORMAL VALUES (parametrized)
# ---------------------------------------------------------------------
@pytest.mark.parametrize("prelim, midterm, finals, expected", [
    (70, 75, 80, 75.5),   # 21 + 22.5 + 32
    (90, 90, 90, 90.0),   # 27 + 27 + 36
    (60, 65, 70, 65.5),   # 18 + 19.5 + 28
    (85, 85, 85, 85.0),   # 25.5 + 25.5 + 34
])
def test_compute_final_grade_normal(prelim, midterm, finals, expected):
    assert compute_final_grade(prelim, midterm, finals) == pytest.approx(expected)


# ---------------------------------------------------------------------
# TODO 2 – ZERO AND 100
# ---------------------------------------------------------------------
def test_all_zero():
    assert compute_final_grade(0, 0, 0) == 0.0

def test_all_hundred():
    assert compute_final_grade(100, 100, 100) == 100.0


# ---------------------------------------------------------------------
# TODO 3 – THE PASSING BOUNDARY (remark)
# ---------------------------------------------------------------------
@pytest.mark.parametrize("final_grade, expected", [
    (74.99, "FAILED"),
    (75, "FAILED"),
    (75.01, "PASSED"),
    (0, "FAILED"),
    (100, "PASSED"),
])
def test_remark_boundary(final_grade, expected):
    assert remark(final_grade) == expected


# ---------------------------------------------------------------------
# TODO 4 – INVALID SCORES
# ---------------------------------------------------------------------
@pytest.mark.parametrize("prelim, midterm, finals", [
    (-1, 80, 80),   # prelim below 0
    (101, 80, 80),  # prelim above 100
    (80, -1, 80),   # midterm below 0
    (80, 101, 80),  # midterm above 100
    (80, 80, -1),   # finals below 0
    (80, 80, 101),  # finals above 100
])
def test_invalid_scores_raise_value_error(prelim, midterm, finals):
    with pytest.raises(ValueError):
        compute_final_grade(prelim, midterm, finals)


# ---------------------------------------------------------------------
# TODO 5 (optional) – ROUNDING
# ---------------------------------------------------------------------
def test_result_is_rounded_to_two_decimals():
    # 33*0.3 + 33*0.3 + 34*0.4 = 9.9 + 9.9 + 13.6 = 33.4
    result = compute_final_grade(33, 33, 34)
    assert result == 33.4
    assert isinstance(result, float)