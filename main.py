incidencias = [
 {"id": 1, "titulo": "Correo sospechoso", "estado": "abierta"},
 {"id": 2, "titulo": "Acceso fallido", "estado": "abierta"},
]

for incidencia in incidencias:
    print(incidencia)


def cambiar_estado(identificador, nuevo_estado):
    for incidencia in incidencias:
        if incidencia["id"] == identificador:
            incidencia["estado"] = nuevo_estado

cambiar_estado(1, "resuelta")
print("Después del cambio:", incidencias[0])
