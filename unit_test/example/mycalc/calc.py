class Calculator(object):

    def mod(self, dividend, divisor):
        remainder = dividend % divisor
        quotient = (dividend - remainder) / divisor
        return quotient, remainder

