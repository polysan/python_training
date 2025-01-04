from abc import ABCMeta
from abc import abstractmethod


class ReplaceRuleInterface(metaclass=ABCMeta):
    @abstractmethod
    def match(self, carry: str, n: int) -> bool:
        raise NotImplementedError()

    def apply(self, carry: str, n: int) -> str:
        raise NotImplementedError()


class NumberConverter:
    def __init__(self, rules: list[ReplaceRuleInterface]):
        self.__rules: list[ReplaceRuleInterface] = rules

    def convert(self, n: int) -> str:
        carry = ""

        for rule in self.__rules:
            if rule.match(carry, n):
                carry = rule.apply(carry, n)
        return carry
