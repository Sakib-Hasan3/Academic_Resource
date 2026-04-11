try:
    from z3 import *  # Correct import
    print("Z3 imported successfully")

    # Define domain
    Person = DeclareSort("Person")

    # Predicates
    Parent = Function('Parent', Person, Person, BoolSort())
    Grandparent = Function('Grandparent', Person, Person, BoolSort())

    # Constants
    John = Const('John', Person)
    Mary = Const('Mary', Person)
    Joe = Const('Joe', Person)

    # Solver
    s = Solver()

    # Variables for rules
    x = Const('x', Person)
    y = Const('y', Person)
    z = Const('z', Person)

    # Rules: Parent(x,y) and Parent(y,z) -> Grandparent(x,z)
    s.add(ForAll([x, y, z], Implies(And(Parent(x, y), Parent(y, z)), Grandparent(x, z))))

    # Facts
    s.add(Parent(John, Mary))
    s.add(Parent(Mary, Joe))

    # Query: prove Grandparent(John, Joe)
    s.push()
    s.add(Not(Grandparent(John, Joe)))
    res = s.check()
    print("Result:", res)

    if res == unsat:
        print("✅ Grandparent(John, Joe) is proved.")
    else:
        print("❌ Cannot prove Grandparent(John, Joe).")

except ImportError as e:
    print(f"Z3 not available: {e}")
    print("Please install z3-solver: pip install z3-solver")
except Exception as e:
    print(f"Error: {e}")
