from systems import *

if __name__=='__main__':
    # Entradas 
    # Temperatura (grados Celsius)
    t1 = Trapezoid('Congelado', -20, -20, -10, 5)
    t2 = Triangle('Frio', -10, 5, 15)
    t3 = Triangle('Normal', 10, 15, 20)
    t4 = Triangle('Tibio', 15, 25, 35)
    t5 = Trapezoid('Caliente', 30, 40, 45, 45)
    # Humedad del suelo (%)
    h1 = Trapezoid('Seca', 0, 0,  5, 12)
    h2 = Trapezoid('Humeda', 6, 12, 18, 20)
    h3 = Trapezoid('Mojada', 16, 25, 50, 50)
    
    # Salidas
    # Duración de riego (minutos)
    d1 = Trapezoid('Corto', 0, 0, 8, 20)
    d2 = Trapezoid('Medio', 10, 25, 40, 55)
    d3 = Trapezoid('Prolongado', 45, 60, 80, 80)

    # Reglas
    # Modelo de Mamdani
    r1 = MamdaniRule('r1', And(Predicate('temp', t1), Predicate('hum', h3)), Predicate('duration', d1)) 
    r2 = MamdaniRule('r2', And(Predicate('temp', t1), Predicate('hum', h2)), Predicate('duration', d1)) 
    r3 = MamdaniRule('r3', And(Predicate('temp', t1), Predicate('hum', h1)), Predicate('duration', d3)) 
    r4 = MamdaniRule('r4', And(Predicate('temp', t2), Predicate('hum', h3)), Predicate('duration', d1)) 
    r5 = MamdaniRule('r5', And(Predicate('temp', t2), Predicate('hum', h2)), Predicate('duration', d2)) 
    r6 = MamdaniRule('r6', And(Predicate('temp', t2), Predicate('hum', h1)), Predicate('duration', d3)) 
    r7 = MamdaniRule('r7', And(Predicate('temp', t3), Predicate('hum', h3)), Predicate('duration', d1)) 
    r8 = MamdaniRule('r8', And(Predicate('temp', t3), Predicate('hum', h2)), Predicate('duration', d2)) 
    r9 = MamdaniRule('r9', And(Predicate('temp', t3), Predicate('hum', h1)), Predicate('duration', d3)) 
    r10 = MamdaniRule('r10', And(Predicate('temp', t4), Predicate('hum', h3)), Predicate('duration', d1)) 
    r11 = MamdaniRule('r11', And(Predicate('temp', t4), Predicate('hum', h2)), Predicate('duration', d2)) 
    r12 = MamdaniRule('r12', And(Predicate('temp', t4), Predicate('hum', h1)), Predicate('duration', d3)) 
    r13 = MamdaniRule('r13', And(Predicate('temp', t5), Predicate('hum', h3)), Predicate('duration', d1)) 
    r14 = MamdaniRule('r14', And(Predicate('temp', t5), Predicate('hum', h2)), Predicate('duration', d2)) 
    r15 = MamdaniRule('r15', And(Predicate('temp', t5), Predicate('hum', h1)), Predicate('duration', d3)) 

    rules = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15]
    # Inputs (temperatura, humedad del suelo)
    inputs = {'temp':35, 'hum': 5}
    #Experiments
    #35 - 30 -> 8.2  9.6  7.0
    #17 - 30 -> 8.0  8.0  6.4
    #0 - 35  -> 7.8  8.0  6.0

    #20 - 8 -> 50.1  52.8 66.2
    #20 - 10 ->42.7  40.0 32.5
    #40 - 10 ->41.2  38.4 32.5
    #-10 - 15 ->7.0  8.0  4.0
    #-10 - 10 ->33.7 16.0 6.0

    #-5 - 0 ->65.3  64.0  67.5
    #35 - 5 ->64.7  64.0  66.2

    # Deffuzifiers
    centroid = Centroid(50)
    mom = MOM(50)
    bisector = Bisection(50)
    # Systems
    mamdani1 = Mamdani(rules, centroid)
    output = mamdani1.compute(inputs)
    print('Outputs by centroid --> {0}'.format(output))

    mamdani2 = Mamdani(rules, mom)
    output = mamdani2.compute(inputs)
    print('Outputs by mean of maximums --> {0}'.format(output))

    mamdani3 = Mamdani(rules, bisector)
    output = mamdani3.compute(inputs)
    print('Outputs by bisector --> {0}'.format(output))