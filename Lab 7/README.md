# Lab 7 – Fuzz Testing

## Objective
Use Hypothesis property-based fuzz testing to identify input-validation failures in the Pizza Order application and harden it against unexpected inputs.

## Deliverables
- `pizza_order.py` – corrected application with defensive input validation.
- `test_processor.py` – updated Hypothesis tests for all three application functions.
- `Lab_7_Fuzz_Testing_Report.pdf` – report with execution evidence and clickable links to this repository and the Lab 7 folder.

## Functions tested
1. `toppings_price(toppings_csv)`
2. `pizza_inches(size)`
3. `split_bill(text)`

## Dependencies
```bash
python3 -m pip install hypothesis pytest
```

## Run
```bash
python3 pizza_order.py
python3 -m pytest test_processor.py -v
```

## Result
The original implementation failed under generated edge-case inputs. After defensive input validation was added, all three Hypothesis tests passed.
