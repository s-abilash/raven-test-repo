# Simple Math Calculator

A tiny standard-library-only Python calculator: add, subtract, multiply, divide.

## Usage

```bash
python -m app.main add 2 3        # 5.0
python -m app.main divide 10 4    # 2.5
python -m app.main divide 1 0     # Error: Cannot divide by zero (exit code 1)
```

Or from Python:

```python
from app.calculator import add, divide
add(2, 3)      # 5
divide(9, 3)   # 3.0
```

## Tests

```bash
python -m unittest discover -s tests
```
