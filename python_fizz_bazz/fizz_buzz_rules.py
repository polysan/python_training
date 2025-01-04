from fizz_buzz_logic import ReplaceRuleInterface


# class CyclicNumberRule:
class CyclicNumberRule(ReplaceRuleInterface):
    def __init__(self, base: int, replacement: str):
        self.__base: int = base
        self.__replacement: str = replacement

    def match(self, carry: str, n: int) -> bool:
        return n % self.__base == 0

    def apply(self, carry: str, n: int):
        return carry + self.__replacement


# class PassThroughRule:
class PassThroughRule(ReplaceRuleInterface):
    def __init__(self):
        super().__init__()

    def match(self, carry, n) -> bool:
        return carry == ""

    def apply(self, carry, n) -> None:
        return str(n)
