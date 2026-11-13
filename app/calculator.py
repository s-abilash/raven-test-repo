"""Basic arithmetic operations: add, subtract, multiply, divide."""

import logging

logger = logging.getLogger(__name__)


def add(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a: First operand.
        b: Second operand.

    Returns:
        The sum ``a + b``.
    """
    result = a + b
    logger.debug("add(%s, %s) = %s", a, b, result)
    return result


def subtract(a: float, b: float) -> float:
    """Subtract one number from another.

    Args:
        a: Number to subtract from.
        b: Number to subtract.

    Returns:
        The difference ``a - b``.
    """
    result = a - b
    logger.debug("subtract(%s, %s) = %s", a, b, result)
    return result


def multiply(a: float, b: float) -> float:
    """Multiply two numbers.

    Args:
        a: First factor.
        b: Second factor.

    Returns:
        The product ``a * b``.
    """
    result = a * b
    logger.debug("multiply(%s, %s) = %s", a, b, result)
    return result


def divide(a: float, b: float) -> float:
    """Divide one number by another.

    Args:
        a: Dividend.
        b: Divisor; must not be zero.

    Returns:
        The quotient ``a / b``.

    Raises:
        ZeroDivisionError: If ``b`` is zero.
    """
    if b == 0:
        logger.warning("divide(%s, %s) rejected: division by zero", a, b)
        raise ZeroDivisionError("Cannot divide by zero")
    result = a / b
    logger.debug("divide(%s, %s) = %s", a, b, result)
    return result
