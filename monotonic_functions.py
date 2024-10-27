import sympy
from sympy.logic.boolalg import And, Or, Not
from sympy.logic.boolalg import to_cnf
def is_monotonic_cnf(cnf_expr):
    # Check if all clauses are monotonic
    cnf = boolean_to_cnf(cnf_expr)
    positives = []
    negatives = []
    if isinstance(cnf, And):  # CNF is a conjunction of clauses
        for clause in cnf.args:
            for arg in clause.args:
                if isinstance(arg, sympy.Symbol) and arg not in positives:
                    positives.append(arg)
                elif isinstance(arg, sympy.Not) and arg not in negatives:
                    negatives.append(arg)
    for arg in positives:
        if Not(arg) in negatives:
            return False, positives, negatives, cnf
    return True, positives, negatives, cnf


def boolean_to_cnf(boolean_function_str):
    # Parse the Boolean function string into a symbolic expression
    if isinstance(boolean_function_str, str):
        boolean_function_str = boolean_function_str.replace('!', '~')
    boolean_expr = sympy.sympify(boolean_function_str)

    # Convert the expression to Conjunctive Normal Form (CNF)
    cnf_expr = to_cnf(boolean_expr, simplify=True, force=True)
    return cnf_expr


def parse_cnf_expr(expr):
    """
    Converts a sympy logical expression in CNF into a structured list of clauses.

    Parameters:
    expr: A sympy expression in CNF format (using And, Or, Not).

    Returns:
    list of lists: CNF formula in structured format where each inner list represents a clause.
    """
    clauses = []

    if isinstance(expr, And):
        expr_clauses = expr.args
    else:
        expr_clauses = [expr]  # Single clause CNF

    for clause in expr_clauses:
        literals = []
        if isinstance(clause, Or):
            clause_literals = clause.args
        else:
            clause_literals = [clause]  # Single literal clause

        for lit in clause_literals:
            if isinstance(lit, Not):
                literals.append("-" + (str(lit.args[0])))  # Convert ~x3 to -3
            else:
                literals.append(str(lit))  # Convert x1 to 1

        clauses.append(literals)

    return clauses


