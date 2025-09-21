from  z3 import * 

# define domain:
Person = DeclareSort("Person")

#Predicated:
Advisor = Function("Advisor",Person,Person,BoolSort()) 
Teacher = Function("Teacher",Person,Person,BoolSort())
Guide = Function("Guide",Person,Person,BoolSort())

# constant:
Alice = Const('Alice',Person)
Bob = Const('Bob',Person)
Carol = Const('Carol',Person)

# solver 
s = Solver()

#variable for rules:
x = Const('x',Person)
y = Const('y',Person)
z = Const('z',Person)


# set rules: 
s.add(ForAll(
    [x,y,z],
    Implies(
        And(Advisor(x,y),Teacher(y,z)),
        Guide(x,z))
    ))


# add facts:
s.add(Advisor(Alice,Bob))
s.add(Teacher(Bob,Carol))


# Now, do query:
s.push()
s.add(Not(Guide(Alice,Carol)))

res = s.check()

if res == unsat:
    print("✅ Guide(Alice, Carol) is proved.")
else:
    print("❌ Cannot prove Guide(Alice, Carol).")
s.pop()
    