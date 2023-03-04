# 1000mg/1000ml = 1000ppm
# 1mg/1ml = 1000ppm
# multiply the subtraction by 1000

def vol():
    mass = float(input('Mass: '))
    ppm = float(input('ppm: '))    
    vol = (mass/ppm)*1000
    return str(vol) + ' ml'

def mass():
    ppm = float(input('ppm: '))
    vol = float(input('Volume: '))
    mass = (ppm*vol)/1000
    return str(mass) + ' mg'

def ppm():
    mass=float(input('Mass: '))
    vol=float(input('Volume: '))
    ppm = (mass/vol)*1000
    return str(ppm) + ' ppm'
    
def calcManager():
    print('''
1- Solve for Mass
2- Solve for Volume
3- Solve for ppm
''')
    user = int(input('Enter: '))
    if user == 1:
        print(mass())
    elif user == 2:
        print(vol())
    elif user == 3:
        print(ppm())    
    else:
        print('Invalid Input')
    



if __name__ == "__main__":
    print("""
Please use the following measurment units.
Mass = mg
Volume = ml
Concentration = ppm
    """)
    calcManager()
