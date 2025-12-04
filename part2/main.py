
data = []
counter = 0

#Import words from data file
f = open('./data.txt')
for word in f:
    data.append(word)

# Start at 50
current = 50

# Main loop
for x in data:
    coeff,val = x[0],int(x[1:])

    print(f'Current value is {current}. Moving dial {val} to the {coeff}')
    
    val = val%100
    
    if coeff == 'L':
        val *= -1
    
    current += val
    
    if current < 0:
        current = 100 + current
    elif current > 100:
        current = abs(100 - current)
        
    if current == 100:
        current = 0

    if current == 0:
        print(f'0 found!')
        counter += 1
print(f'Password is {counter}')