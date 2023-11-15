sandwich_orders = [
    'pastrami', 'veggie', 'cheese', 'pastrami',
    'chicken', 'mix', 'pastrami']
finished_sandwiches = []

print("we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print()
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print()
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")