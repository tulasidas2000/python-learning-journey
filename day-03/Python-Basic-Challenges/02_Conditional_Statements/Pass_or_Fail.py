## Entering the marks

marks = int(input('Enter Marks'))

if marks >= 0 and marks <= 100:
    print('Valid')
else:
    print('Invalid')


## Determine pass or fail


math = int(input('Enter Maths Marks'))
phy = int(input('Enter Physics Marks'))
chem = int(input('Enter Chemestry Marks'))

if math >= 45 and phy >= 45 and chem >= 45:
    print('Passed')
else:
    print('Failed')