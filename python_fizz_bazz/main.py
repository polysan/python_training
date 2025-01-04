from fizz_buzz_logic import NumberConverter
from fizz_buzz_rules import CyclicNumberRule, PassThroughRule

fizz_bazz = NumberConverter(
    [CyclicNumberRule(3, "fizz"), CyclicNumberRule(5, "buzz"), PassThroughRule()]
)

print(fizz_bazz.convert(15))
