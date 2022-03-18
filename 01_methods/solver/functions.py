from fractions import Fraction


class BaseFunction:
    def at(self, x: Fraction) -> Fraction:
        return abs(x)

    def as_string(self, x: Fraction) -> str:
        return f"({x})"
