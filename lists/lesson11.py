"""
What’s List Comprehension Anyways?
List comprehension is a concise way of creating lists. Say you want to filter out all customers from your 
database who earn more than $1,000,000. This is what a newbie not knowing list comprehension would do:
"""
# (name, $-income)
customers = [("Ronny", 290000),
             ("Mike", 20000),
             ("Shaun", 1100000),
             ("Kim", 450000)]

# your high-value customers earning >$1M
# high_rollers = []
# for customer, income in customers:
#     if income>1000000:
#         high_rollers.append(customer)
# print(high_rollers)
#['Shaun']

high_rollers = [x for x,y in customers if y>1000000]
print(high_rollers) #['Shaun']

"""
Python Docs
A list comprehension consists of brackets containing an expression followed by a for clause, then zero 
or more for or if clauses. The result will be a new list resulting from evaluating the expression in 
the context of the for and if clauses which follow it
"""