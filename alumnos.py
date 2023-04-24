def alumnos():

    alumnos = []

    respuesta = True

    while respuesta:

        alumno = []

        alumno.append(input("ingrese el nombre del alumno:\n"))
        alumno.append(float(input("ingrese la primera nota:\n")))
        alumno.append(float(input("ingrese la segunda nota:\n")))
        alumno.append(float(input("ingrese la tercera nota:\n")))

        alumnos.append(alumno)

        respuesta = input("¿desea ingresar otro alumno?\nIngrese s para si.\nIngrese cualquier cosa para no.\n")
        if respuesta == "s":
            respuesta = True
        else:
            respuesta = False


    if len(alumnos) > 0:
        print("listado de las notas de los alumnos")
        print("nombre\tnota1\tnota2\tnota3")
        for alumno in alumnos:
            print(alumno[0]+"\t"+(alumno[1])+"\t\t"+str(alumno[2])+"\t\t"+str(alumno[3]))

    if len(alumnos) > 0:
        print("\nlistado de los promedios de los alumnos")
        print("Nombre\tPromedio")
        for alumno in alumnos:
            promedio = (alumno[1]+alumno[2]+alumno[3])/3
            print(alumno[0]+"\t" +str(round(promedio,1)))