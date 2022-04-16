"""
Situación
El departamento de Talento Humano de la Universidad El Bosque, a raíz de la participación en un proyecto muy especial,
requiere poder procesar la nómina de docentes contratados por horas. Para tal efecto ha establecido los siguientes
lineamientos:

• La nómina será procesada semanalmente, digitando por cada docente las horas trabajadas
en la semana y el valor establecido por hora.

• A todos los docentes que trabajen más de 40 horas en la semana, se les reconocerán como
horas extras y se pagarán a un valor de 1,5 de la hora normal.

• Al salario bruto obtenido en el punto anterior se le calculará el 9% para los parafiscales.

• Para cada docente se le calcularán provisiones para prima de servicio 8.33%, cesantías 8.33%,
 intereses de cesantía 1.0% y vacaciones 4.17%.

• A cada uno se le descontará el aporte de 4% para salud y el 4% para pensión.

El director de Talento Humano le ha solicitado a usted como programador, que le desarrolle un
programa en lenguaje Python que le permita:

• Leer desde el teclado los datos de nombre, horas trabajadas y valor hora, por cada docente del proyecto.
• Mostrar en consola el sueldo bruto.
• Mostrar en consola los descuentos por parafiscales, salud y pensión.
• Mostrar en consola el sueldo neto a pagar.
• Mostrar en consola las provisiones hechas para prima, cesantías, intereses de cesantía y vacaciones.
• Los cálculos de sueldo bruto, descuentos, sueldo neto y provisiones, deberán ser realizados a través de
funciones o procedimientos y serán llamados en el programa principal.

Autor: Alejandro Meneses Roldan
Fecha 31/05/2021
"""

nombre = ''
horas_trabajadas = valor_hora = float(0)
cantidad_horas_extra = salario_bruto = salario_neto = total_horas_extra = descuento_parafiscales = float(0)
descuento_salud = descuento_pension = prov_prima = prov_cesantias = inter_cesantias = prov_vacaciones = float(0)

def horas_extra (horas_trabajadas):
    if horas_trabajadas > 40 :
        horas_extra = (horas_trabajadas - 40)
    else:
        horas_extra = 0
    return horas_extra

def valor_horas_extra (cantidad_horas_extra,valor_hora):
    if cantidad_horas_extra == 0 :
        return 0
    valor_horas_extra = (cantidad_horas_extra * valor_hora) * 1.5
    return valor_horas_extra

def salariobruto(horas_trabajadas,cantidad_horas_extra,valor_hora,total_horas_extra):
    global horas_total
    horas_total = horas_trabajadas - cantidad_horas_extra
    salariobruto = (horas_total * valor_hora) + total_horas_extra
    if cantidad_horas_extra == 0:
        salariobruto = int(salariobruto)
    else:
        salariobruto = float(round(salariobruto,1))
    return salariobruto

def parafiscales (salario_bruto):
    parafiscales = salario_bruto * 0.09
    return parafiscales

def salud (salario_bruto):
    salud = salario_bruto * 0.04
    return salud

def pension (salario_bruto):
    pension = salario_bruto * 0.04
    return pension

def salarioneto (salario_bruto,descuento_parafiscales,descuento_salud,descuento_pension):
    salarioneto = salario_bruto - (descuento_parafiscales + descuento_salud + descuento_salud)
    return salarioneto

def prima (salario_neto):
    prima = salario_bruto * 0.0833
    return prima

def cesantias (salario_neto):
    cesantias = salario_bruto * 0.0833
    return cesantias

def int_cesantias (salario_neto):
    int_cesantias = salario_bruto * 0.01
    return int_cesantias

def vacaciones (salario_neto):
    vacaciones = salario_bruto * 0.0417
    return vacaciones

def final(nombre,horas_trabajadas,valor_hora,cantidad_horas_extra,total_horas_extra,salario_bruto,descuento_parafiscales,descuento_salud,descuento_pension,salario_neto,prov_prima,prov_cesantias,inter_cesantias,prov_vacaciones):
    print('                                                                               ')
    print('                                                                               ')
    print('   ╔═══════════════════════════════════════════════════════════════════╗       ')
    print('   ║               ░░▒▒▓▓██  NOMINA DEL EMPLEADO  ██▓▓▒▒░░             ║       ')
    print('   ╠═══════════════════════════════════════════════════════════════════╣       ')
    print('   ║                                                                   ║       ')
    print('   ║  Nombre del empleado              :   {:<28}║'.format(nombre.upper()))
    print('   ║  Horas trabajadas por el empleado :   {:<15,.2f}             ║'.format(horas_trabajadas))
    print('   ║  Valor de la hora trabajada       : $ {:<15,.2f}             ║'.format(valor_hora))
    print('   ║                                                                   ║       ')
    print('   ╠═══════════════════════════════════════════════════════════════════╣       ')
    print('   ║                                                                   ║       ')
    print('   ║  Cantidad de horas totales trabajadas         :   {:<15,.2f} ║'.format(horas_trabajadas))
    print('   ║  Cantidad de horas normales trabajadas        :   {:<15,.2f} ║'.format(horas_total))
    print('   ║  Valor pagado en horas normales al empleado   : $ {:<15,.2f} ║'.format(horas_total * valor_hora))
    print('   ║  Cantidad de horas extras trabajadas          :   {:<15,.2f} ║'.format(cantidad_horas_extra))
    print('   ║  Valor pagado en horas extras al empleado     : $ {:<15,.2f} ║'.format(total_horas_extra))
    print('   ║  Sueldo bruto del empleado                    : $ {:<15,.2f} ║'.format(salario_bruto))
    print('   ║  Descuento por parafiscales (9%)              : $ {:<15,.2f} ║'.format(round(descuento_parafiscales,3)))
    print('   ║  Descuento por salud (4%)                     : $ {:<15,.2f} ║'.format(round(descuento_salud,3)))
    print('   ║  Descuento por pensión (4%)                   : $ {:<15,.2f} ║'.format(round(descuento_pension,3)))
    print('   ╠═══════════════════════════════════════════════════════════════════╣       ')
    print('   ║  EL SALARIO NETO A PAGAR A {:<20}                   ║'.format(nombre.upper()))
    print('   ║  ES : $ {:<15,.2f}                                           ║'.format(salario_neto))
    print('   ╠═══════════════════════════════════════════════════════════════════╣       ')
    print('   ║                                                                   ║       ')
    print('   ║  Provisión de prima de servicios (8.33%) : $ {:<15,.2f}      ║'.format(round(prov_prima,3)))
    print('   ║  Provisión de cesantias (8.33%)          : $ {:<15,.2f}      ║'.format(round(prov_cesantias,3)))
    print('   ║  Provisión de Vacaciones (4.17%)         : $ {:<15,.2f}      ║'.format(round(prov_vacaciones,3)))
    print('   ║  Intereses a las cesantías (1.0%)        : $ {:<15,.2f}      ║'.format(round(inter_cesantias,3)))
    print('   ║                                                                   ║       ')
    print('   ╚═══════════════════════════════════════════════════════════════════╝       ')

def final_bot():
    print(int(horas_total * valor_hora))
    print(total_horas_extra)
    print(salario_bruto)
    print(round(descuento_parafiscales,1))
    print(round(descuento_salud,1))
    print(round(descuento_pension,1))
    print(round(descuento_parafiscales + descuento_salud + descuento_pension,1))
    print(round(salario_neto,1))
    print(round(prov_prima,1))
    print(round(prov_cesantias,1))
    print(round(inter_cesantias,1))
    print(round(prov_vacaciones,1))

def inicio():
    global nombre
    global horas_trabajadas
    global valor_hora
    print('')
    print('   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓██████████████████████▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░')
    print('   ▒                                                                               ▒')
    print('   ▓         ░░▒▒▓▓██  BIENVENIDO AL SISTEMA DE NOMINA EL BOSQUE  ██▓▓▒▒░░         ▓')
    print('   █                                                                               █')
    print('   ▓                                       ░░▒▒▓▓██   Powered By MINTIC  ██▓▓▒▒░░  ▓')
    print('   ▒                                                                               ▒')
    print('   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓██████████████████████▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░')
    print('')
    print('───────────────────────────────────────────────────────────────────────────────────────────')
    nombre = input("Por favor digite el nombre del empleado              : ")
    print('───────────────────────────────────────────────────────────────────────────────────────────')
    horas_trabajadas = capturadecimal ('Por favor digite las horas trabajadas por el empleado: ')
    print('───────────────────────────────────────────────────────────────────────────────────────────')
    valor_hora =capturadecimal ('Por favor digite el valor de la hora trabajada       : ')
    print('───────────────────────────────────────────────────────────────────────────────────────────')

def capturadecimal (mensaje):
    while True:
        try:
            num = float(input(mensaje))
            break
        except:
            error("\n\nEL DATO INGRESADO DEBE SER NUMERICO\n\n")
            pass
    return num

def error(mensaje):
    print (mensaje)

inicio()

cantidad_horas_extra = horas_extra (horas_trabajadas)
total_horas_extra = valor_horas_extra (cantidad_horas_extra,valor_hora)
salario_bruto = salariobruto(horas_trabajadas,cantidad_horas_extra,valor_hora,total_horas_extra)
descuento_parafiscales = parafiscales (salario_bruto)
descuento_salud = salud (salario_bruto)
descuento_pension = pension (salario_bruto)
salario_neto = salarioneto (salario_bruto,descuento_parafiscales,descuento_salud,descuento_salud)
prov_prima = prima (salario_neto)
prov_cesantias = cesantias (salario_neto)
inter_cesantias = int_cesantias (salario_neto)
prov_vacaciones = vacaciones (salario_neto)

#final_bot()
final(nombre,horas_trabajadas,valor_hora,cantidad_horas_extra,total_horas_extra,salario_bruto,descuento_parafiscales,descuento_salud,descuento_pension,salario_neto,prov_prima,prov_cesantias,inter_cesantias,prov_vacaciones)
