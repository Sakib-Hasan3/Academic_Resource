# সহজ First-Order Logic (unary predicate) প্রমাণ

# প্রেডিকেট ফাংশন
def Pred(name, arg):
    return f"{name}({arg})"

# রুল: Human(x) => Mortal(x)
rule_from = "Human"
rule_to = "Mortal"

# ফ্যাক্ট: Human(Socrates)
facts = {Pred("Human", "Socrates")}

# কুয়েরি: Mortal(Socrates)
query = Pred("Mortal", "Socrates")

# প্রমাণ লজিক (খুব সহজ ফরওয়ার্ড চেইনিং)
new_fact = Pred(rule_to, "Socrates") if Pred(rule_from, "Socrates") in facts else None
if new_fact:
    facts.add(new_fact)

# রেজাল্ট
print("Knowledge Base:", facts)
print("Query:", query)
print("Proved?", query in facts)


