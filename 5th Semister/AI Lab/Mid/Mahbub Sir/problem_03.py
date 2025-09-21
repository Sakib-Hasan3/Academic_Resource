from z3 import * 

#domain:
Person = DeclareSort("Person")
Animal = DeclareSort("Animal")

#predicated:
Owns = Function("Owns",Person,Animal,BoolSort())
Dog = Function("Dog",Animal,Animal,BoolSort())
OwnsDog = Function("OwnsDog",Person,Animal,BoolSort())


# constant:
Tom = Const("Tom",Person)
Spike = Const("Spike",Animal)

# Solver:
s = Solver()

# constant:
x = Const("x",Person)
y = Const("y",Animal)


# rule:
s.add(
    ForAll([x,y],
           Implies(
               And(Owns(x,y),Dog(y,y)),
               OwnsDog(x,y)
           ))
)


#info:
s.add(Owns(Tom,Spike))
s.add(Dog(Spike,Spike))


#query:
s.push()
s.add(Not(OwnsDog(Tom,Spike)))

res = s.check()
if res == unsat:
    print("✅ Tom owns a Dog (proved).")
else:
    print("❌ Cannot prove Tom owns a Dog.")
