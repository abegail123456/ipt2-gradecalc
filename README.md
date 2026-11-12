# ipt2-gradecalc

A small grade calculator for IT 316 – Integrative Programming and Technologies 2.
It computes a final grade (30% prelim, 30% midterm, 40% finals) and a PASSED/FAILED remark.

## Team

Team Description: Our team works together to develop and improve the Grade Calculator while gaining practical experience in version control, software testing, and CI/CD processes under the guidance of Sir Clyde.
Team description: We work together as a team to develop and enhance the grade calculator while learning and applying version control, software testing, and CI/CD practices.

| Role | Name | GitHub username |
|------|------|-----------------|
| Partner A | Abegail E. Dormendo | abegail123456 |
| Partner B | Fredelly Reyes | reyesfredellysalino-cell |

## How to run the tests

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -v --cov=grades --cov-report=term-missing
```
