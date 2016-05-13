import manejoArchivos


def manipularContactos(contactos):
    nombre = raw_input('Ingrese el nombre del humano: ')
    apellido = raw_input('Ingrese el apellido del sujeto: ')
    valida = True
    while (valida):
        try:
            telefono = int(raw_input('Ingrese el telefono del culiado: '))
            valida = False
        except:
            print 'El nro debe ser un entero'
    newContacto = {nombre + ' ' + apellido: telefono}
    contactos.update(newContacto)
    manejoArchivos.addfileagenda(newContacto)


def modificarContactos(contactos):
    print 'Indique que desea modificar'
    print '1. Nombre y apellido'
    print '2. Telefono'
    opcion = str(raw_input('Ingrese nro: '))
    if opcion == '1':
        print 'No se puede realizar todavia'
    elif opcion == '2':
        manipularContactos(contactos)


def mostrarContactos(contactos):
    for nom, nro in contactos.iteritems():
        print 'Nombre: %s Nro: %i' % (nom, nro)


def eliminarContacto(contactos):
    nombre = raw_input('Humano a depurar: ')
    try:
        contactos.pop(nombre)
        print 'Hecho.'
    except:
        print 'No existe el contacto que desea eliminar'
