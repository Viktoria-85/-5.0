class calculator:

    def sum( a, b):
        res = calc.sum(4, 5)
        return a+b

    def sub(self, a, b):
        return a-b

    def mul(self, a, b):
        return a*b

    def div(self, a, b):
        if (b == 0):
            raise ArithmeticError('на ноль делить нельзя')

        return a/b

    def pow(self, a, b = 2):
        return a**b

    def avg(self, numbers):
        s = sum(numbers)
        for num in numbers:
           s += num
        return s / len(numbers) if numbers else 0

        # s = self.sum('s', 'num')

        # [1,2,3,]

        for num in nums:
            s = s + num

            l = len(nums)

            return self.div(s, l)

