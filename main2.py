#hola mundo en python
#print("hola mundo");

#print("hola");
#print('¿cual es su nombre socio?');

#miNombre = input();

#print("hola "+miNombre);


#adivinar el numero programa de practica
"""import random;
print("hola jugador");
print("como te llamas?");

NombrePlayer = input();

print("bienvenido "+NombrePlayer);

numero = random.randint(1,20);

print("bueno "+NombrePlayer+" estoy pensando en un numero del 1 al 20");

NumeroIntentos = 0;

while NumeroIntentos < 8:
    print("di tu numero")
    estimacion = input();
    estimacion = int(estimacion);
    if estimacion < numero:
        print("tu numero esta por debajo");
        NumeroIntentos += 1;

    if estimacion > numero:
        print("tu numero esta por encima");
        NumeroIntentos += 1;

    if estimacion == numero:
        break;

if estimacion == numero:
    NumeroIntentos = str(NumeroIntentos);
    print("¡CORRECTO PAPU! LO LOGRASTE EN " + NumeroIntentos + " INTENTOS");

if estimacion != numero:
    numero = str(numero);
    print("fallaste papu estaba pensando en el "+numero);"""""


#me dice cuantas letras tiene mi nombre
"""""""""
def DecirHola(Nombre):
    print("hola "+Nombre+" tu nombre tiene "+ str(len(Nombre))+" letras");

Nombre = input();
DecirHola(Nombre);"""""

#juego marik de los dragons mi pes
"""""""""
import random;
import time;

def mostrarIntro():
    print("estas en tierra de dragones. Frente a ti")
    print("hay dos cuevas, en una de ellas el dragon es generoso y")
    print("compartira su tesoro contigo. E l otro dragon es codicioso y")
    print("tiene hambre")
    print("")

def elegirCueva():
    cueva = '';
    while cueva !='1' and cueva !='2':
        print("que cueva eligiras 1 o 2");
        cueva = input();

    return cueva;

def explorarCueva(cuevaElegida):
    print("te aproximas a la cueva");
    time.sleep(2);
    print("es fria y tenebrosa");
    time.sleep(2);
    print("aparece un gran dragon frente a ti abre la jeta y..");
    time.sleep(2);
    print();

    cuevaAmigable = random.randint(1,2);

    if cuevaElegida == str(cuevaAmigable):
        print('te regala su tesoro');

    else:
        print("se lo traga mi pes");

jugarDeNuevo = 'si';

while jugarDeNuevo == 'si' or jugarDeNuevo == 's':
    mostrarIntro();

    numeroDeCueva = elegirCueva();

    explorarCueva(numeroDeCueva);

    print('¿Quieres jugar de nuevo? si o no')

    jugarDeNuevo = input();
"""""

#jodiendo un tal
"""
import time;

def suma(x ,y):
    return x+y;


def sumaAcincuenta():
    numero = 1;
    while numero <= 50:
        print(numero);
        time.sleep(0.5);
        numero += 1;
    if numero == 50:
        print("acabamo");


x=5;
y=5;

print(suma(x,y));
print("\n");
sumaAcincuenta();
"""







