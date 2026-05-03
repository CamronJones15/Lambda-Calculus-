class Var:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Lambda:
    def __init__(self, param, body):
        self.param = param
        self.body = body

    def __str__(self):
        return f"(λ{self.param}.{self.body})"
    
class Apply:
    def __init__(self, func, arg):
        self.func = func
        self.arg = arg

    def __str__(self):
        return f"({self.func} {self.arg})"
    
def substitute(expr, var, value):
    if isinstance(expr, Var):
        if expr.name == var:
            return value
        else:
            return expr
    elif isinstance(expr, Lambda):
        if expr.param == var:
            return expr  # No substitution inside the body
        else:
            new_body = substitute(expr.body, var, value)
            return Lambda(expr.param, new_body)
    elif isinstance(expr, Apply):
        new_func = substitute(expr.func, var, value)
        new_arg = substitute(expr.arg, var, value)
        return Apply(new_func, new_arg)
    else:
        raise ValueError("Unknown expression type")

def beta_reduce(expr):
    if isinstance(expr, Apply):
        if isinstance(expr.func, Lambda):
            return substitute(expr.func.body, expr.func.param, expr.arg)
        return Apply(beta_reduce(expr.func), beta_reduce(expr.arg))
    elif isinstance(expr, Lambda):
        return Lambda(expr.param, beta_reduce(expr.body))
    return expr

def evaluate(expr, steps=10):
    print("Start:", expr)
    for i in range(steps):
        new_expr = beta_reduce(expr)
        if str(new_expr) == str(expr):
            print("Done:", expr)
            return expr
        
        expr = new_expr
        print(f"Step {i+1}:", expr)

    print(f"Step{i + 1 }:", expr)
    return expr

expr = Apply(
    Lambda("f", Lambda("x", Apply(Var("f"), Apply(Var("f"), Var("x"))))),
    Lambda("y", Var("y"))
)
# expr = Apply(
#     Lambda("x", Apply(Var("x"), Var("x"))),
#     Lambda("y", Var("y"))
# )
evaluate(expr)
