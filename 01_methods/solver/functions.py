from fractions import Fraction


class BaseFunction:
    def at(self, x: Fraction) -> Fraction:
        return x

    def as_string(self, x: Fraction) -> str:
        return f"({x})"
