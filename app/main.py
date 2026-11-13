"""Command-line entry point: ``python -m app.main <op> <a> <b>``."""

import argparse
import logging
import sys
from typing import Callable, Dict, List, Optional

from app.calculator import add, divide, multiply, subtract

logger = logging.getLogger(__name__)

OPERATIONS: Dict[str, Callable[[float, float], float]] = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}


def main(argv: Optional[List[str]] = None) -> int:
    """Parse arguments, run the requested operation, and print the result.

    Args:
        argv: Argument list to parse; defaults to ``sys.argv[1:]`` when None.

    Returns:
        Process exit code: 0 on success, 1 on a calculation error.
    """
    parser = argparse.ArgumentParser(description="Simple math calculator")
    parser.add_argument("operation", choices=sorted(OPERATIONS))
    parser.add_argument("a", type=float)
    parser.add_argument("b", type=float)
    args = parser.parse_args(argv)

    try:
        result = OPERATIONS[args.operation](args.a, args.b)
    except ZeroDivisionError as exc:
        logger.error("Calculation failed: %s", exc)
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
