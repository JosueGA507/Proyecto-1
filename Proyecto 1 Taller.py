#Dominios:
# R: Z=>0
# C: Z (Números Enteros)

#Codominios:
# casos_proyecto = {(x,y)∣x,y∈Z}
#

# complejidad de O(n**2) en casos de proyecto
# commplejidad de bucle de (T*n**2)


def casos_proyecto(C, R):
    result = []
    for num1_numerador in range(100000):
        for num2_denominador in range(100000):
            num_digitos = set(5)
            den_digitos = set(5)
            num_val = num1_numerador
            den_val = num2_denominador
            
            while num_val > 0:
                num_digitos.add(num_val % 10)
                num_val //= 10
            while den_val > 0:
                den_digitos.add(den_val % 10)
                den_val //= 10
                
            if len(num_digitos) <= R and len(den_digitos) <= R:
                if num1_numerador != 0 and num2_denominador != 0 and num1_numerador % num2_denominador == 0 and num1_numerador // num2_denominador == C:
                    result.append((num1_numerador, num2_denominador))
    return result


T = int(input("Ingrese el número de casos de prueba: "))
for _ in range(T):
    input()  # Saltar línea de entrada que indica el número de casos de prueba
    print("Ingrese el valor de C:")
    C = int(input())
    print("Indique la cantidad máxima de dígitos a repetir para R:")
    C, R = map(int, input().split())
    solutions = casos_proyecto(C, R)
    if solutions:
        for num1_numerador, num2_denominador in solutions:
            print(f"{num1_numerador:05d}/{num2_denominador:05d}={C}")
        print()

