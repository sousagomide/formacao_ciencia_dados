import numpy as np

def check(peso):
    if peso <= 10:
        return 'R$ 50.00'
    elif peso > 11 and peso <= 20:
        return 'R$ 80.00'
    else:
        return 'Transposte não aceito...'
    
for i in np.random.randint(1, 100, 5):
    print(f'Peso: {i}kg Status: {check(i)}')


