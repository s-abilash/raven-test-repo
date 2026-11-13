"""Unit tests for app.calculator and the app.main CLI."""

import io
import unittest
from contextlib import redirect_stderr, redirect_stdout

from app.calculator import add, divide, multiply, subtract
from app.main import main


class CalculatorTests(unittest.TestCase):
    """Tests for the four arithmetic operations."""

    def test_add(self) -> None:
        """Adds two numbers."""
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self) -> None:
        """Subtracts the second number from the first."""
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self) -> None:
        """Multiplies two numbers."""
        self.assertEqual(multiply(4, 2.5), 10)

    def test_divide(self) -> None:
        """Divides the first number by the second."""
        self.assertEqual(divide(9, 3), 3)

    def test_divide_by_zero_raises(self) -> None:
        """Dividing by zero raises a clear ZeroDivisionError."""
        with self.assertRaisesRegex(ZeroDivisionError, "Cannot divide by zero"):
            divide(1, 0)


class CliTests(unittest.TestCase):
    """Tests for the command-line entry point."""

    def test_cli_add(self) -> None:
        """`add 2 3` prints 5.0 and exits 0."""
        out = io.StringIO()
        with redirect_stdout(out):
            code = main(["add", "2", "3"])
        self.assertEqual(code, 0)
        self.assertEqual(out.getvalue().strip(), "5.0")

    def test_cli_divide_by_zero(self) -> None:
        """`divide 1 0` reports an error and exits 1."""
        err = io.StringIO()
        with redirect_stderr(err):
            code = main(["divide", "1", "0"])
        self.assertEqual(code, 1)
        self.assertIn("Cannot divide by zero", err.getvalue())


if __name__ == "__main__":
    unittest.main()
