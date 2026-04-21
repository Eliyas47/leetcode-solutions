class Solution:
    def evaluate(self, expression: str) -> int:
        def parse(expr, env):
            if expr[0].isdigit() or expr[0] == '-':
                return int(expr)
            if expr[0].isalpha() and expr not in ("let","add","mult"):
                for scope in reversed(env):
                    if expr in scope:
                        return scope[expr]
            if expr.startswith("(add"):
                tokens = split(expr[5:-1])
                return parse(tokens[0], env) + parse(tokens[1], env)
            if expr.startswith("(mult"):
                tokens = split(expr[6:-1])
                return parse(tokens[0], env) * parse(tokens[1], env)
            if expr.startswith("(let"):
                tokens = split(expr[5:-1])
                new_env = env + [{}]
                for i in range(0, len(tokens)-1, 2):
                    var, val = tokens[i], tokens[i+1]
                    if i+1 < len(tokens)-1:
                        new_env[-1][var] = parse(val, new_env)
                return parse(tokens[-1], new_env)

        def split(expr):
            res, bal, cur = [], 0, ""
            for ch in expr + " ":
                if ch == "(":
                    bal += 1
                if ch == ")":
                    bal -= 1
                if ch == " " and bal == 0:
                    if cur:
                        res.append(cur)
                        cur = ""
                else:
                    cur += ch
            return res

        return parse(expression, [])
