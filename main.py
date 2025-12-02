
data = []
counter = 0

#Import words from data file
f = open('data.txt')
for word in f:
    data.append(word)

# Start at 50
current = 50

# Main loop
for x in data:
    coeff,val = x[0],int(x[1:])
    if coeff == 'R':
        current += val
        if current > 99:
            current -= 100
    else:
        current -= val
        if current < 0:
            current += 100
    print(current)
    if current == 0:
        counter += 1
print(f'Password is {counter}')