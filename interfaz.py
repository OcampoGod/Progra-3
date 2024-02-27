def menu():
    print("\nBIENVENIDO A DATOS ABIERTOS COLOMBIA, EN ESTA SECCIÓN PODRAS CONSULTAR LOS CASOS DE COVID-19 EN EL PAÍS")
    limite_registros = int(input("Digite el limite de registros: "))
    nombredepartamento = input("Digite el departamento (EN MAYUSCULA): ")
    return [limite_registros, nombredepartamento]
