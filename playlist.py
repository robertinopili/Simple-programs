playlist = {} #Diccionario vacio
playlist['canciones'] = [] #Lista vacia de canciones

def app(): #Funcion principal
    agregar_playlist = True #Agregar playlist
    while agregar_playlist:
        nombre_playlist = input('Como quiere llamar a la playlist: \r\n')
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False #Ya tenemos un nombre, desactiva el true

            agregar_canciones() #Funcion para llamar a agregar canciones

def agregar_canciones():
    agregar_cancion = True

    while agregar_cancion: #Preguntar al usuario que cancion quiere agregar
        nombre_playlist = playlist['nombre']
        pregunta = f'\r\n Agrega canciones para la playlist {nombre_playlist}:\r\n'
        pregunta += 'Escribe "X" para dejar de agregar canciones\r\n'
        cancion = input(pregunta)
        
        if cancion == 'X': #Dejar de agregar canciones
            agregar_cancion = False
            mostrar_resumen() #Mostrando resumen
        else: #Agregar las canciones
            playlist['canciones'].append(cancion)
            print(playlist)

def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist} \r\n')
    print('Canciones:\r\n')
    for cancion in playlist['canciones']:
        print(cancion)

app()