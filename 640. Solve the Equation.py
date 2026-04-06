class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(expr):
            coeff, const = 0, 0
            i, sign = 0, 1
            while i < len(expr):
                if expr[i] in '+-':
                    sign = 1 if expr[i] == '+' else -1
                    i += 1
                num, is_num = 0, False
                while i < len(expr) and expr[i].isdigit():
                    num = num * 10 + int(expr[i])
                    i += 1
                    is_num = True
                if i < len(expr) and expr[i] == 'x':
                    coeff += sign * (num if is_num else 1)
                    i += 1
                else:
                    const += sign * num
            return coeff, const

        lhs, rhs = equation.split('=')
        coeff_lhs, const_lhs = parse(lhs)
        coeff_rhs, const_rhs = parse(rhs)

        coeff = coeff_lhs - coeff_rhs
        const = const_rhs - const_lhs

        if coeff == 0:
            return "Infinite solutions" if const == 0 else "No solution"
        return f"x={const // coeff}"
