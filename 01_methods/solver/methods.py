from fractions import Fraction

from .functions import BaseFunction
from .utils import debug_log


class BaseMethod:
    def __init__(self, param: Fraction) -> None:
        self._param = param

    def m_value(self, x: list, func: BaseFunction, tau: int) -> Fraction:
        raise NotImplementedError()

    def metric(self, i: int, m: Fraction, x: list, func: BaseFunction) -> Fraction:
        raise NotImplementedError()

    def x_next(self, t: int, m: Fraction, x: list, func: BaseFunction) -> Fraction:
        return Fraction(1, 2) * (x[t] + x[t - 1] - (func.at(x[t]) - func.at(x[t - 1])) / m)

    def solve(self, x_from: Fraction, x_to: Fraction, func: BaseFunction, steps: int):
        x_tests = [x_from, x_to]
        debug_log("k = 1")
        yield x_from
        debug_log("k = 2")
        yield x_to
        for i in range(3, steps + 1):
            debug_log("k =", i)
            x = sorted(x_tests)
            debug_log("Λ", *x)
            tau = len(x) - 1
            debug_log("τ", tau)
            z = [func.at(tochka) for tochka in x]
            debug_log("z", *z)
            m = self.m_value(x, func, tau)
            debug_log("m", m)
            R = [self.metric(j, m, x, func) for j in range(1, tau + 1)]
            debug_log("R", *R)
            t = R.index(max(R)) + 1
            debug_log("t", t)
            x_next = self.x_next(t, m, x, func)
            x_tests.append(x_next)
            yield x_next


class PiyavskiMethod(BaseMethod):
    def __init__(self, param: Fraction) -> None:
        super().__init__(param)

    def metric(self, i: int, m: Fraction, x: list, func: BaseFunction) -> Fraction:
        return Fraction(1, 2) * (m * (x[i] - x[i - 1]) - (func.at(x[i]) + func.at(x[i - 1])))

    def m_value(self, /) -> Fraction:
        return self._param


class StronginMethod(BaseMethod):
    def __init__(self, param: Fraction) -> None:
        super().__init__(param)

    def metric(self, i: int, m: Fraction, x: list, func: BaseFunction) -> Fraction:
        val = m * (x[i] - x[i - 1])
        return val + (func.at(x[i]) - func.at(x[i - 1])) ** 2 / val - 2 * (func.at(x[i]) + func.at(x[i - 1]))

    def m_value(self, x: list, func: BaseFunction, tau: int) -> Fraction:
        mu = [abs(func.at(x[j]) - func.at(x[j - 1])) / (x[j] - x[j - 1])
              for j in range(1, tau + 1)]
        m = max(mu)
        return m * self._param if m != 0 else 1


METHODS = {
    "piyavski": PiyavskiMethod,
    "strongin": StronginMethod,
}
