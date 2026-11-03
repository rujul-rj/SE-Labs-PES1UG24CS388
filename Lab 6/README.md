# Lab 6: Code and Branch Coverage Analysis

## Application
Pizza Order application from the assigned repository `SETAPESU26/L6_L7_24_pizza_order`.

## Deliverables
- `CodeCoverageTest_pizza_order.py` — tests used for statement/code coverage.
- `BranchCoverageTest_pizza_order.py` — tests used for branch coverage.
- `Lab_6_Code_and_Branch_Coverage_Report.pdf` — report with analysis and terminal evidence.
- `Code_Coverage_Result.png` — terminal output showing 20 tests passed and 100% statement coverage.
- `Branch_Coverage_Result.png` — terminal output showing 17 tests passed, 24 branches, zero partial branches and 100% coverage.

## Results
| Measurement | Result |
|---|---:|
| Code coverage of `pizza_order.py` | 100% |
| Branch coverage of `pizza_order.py` | 100% |
| Code coverage tests | 20 passed |
| Branch coverage tests | 17 passed |

## Commands
```bash
coverage erase
coverage run -m pytest -v CodeCoverageTest_pizza_order.py
coverage report -m

coverage erase
coverage run --branch -m pytest -v BranchCoverageTest_pizza_order.py
coverage report -m
```
