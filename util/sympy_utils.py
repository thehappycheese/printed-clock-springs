from sympy import Float, Integer, Expr

def get_first_float(expr:Expr|float|str):
    if not isinstance(expr, Expr):
        return expr
        raise TypeError(f"Type of expr was {type(expr)}, not float or sympy.Expr")
    floats = list(expr.atoms(Float))
    if floats:
        return float(floats[0])
    ints = list(expr.atoms(Integer))
    if ints:
        return int(ints[0])
    return None