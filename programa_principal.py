import controlAg


def main():
    continuar = True
    contactos = {}
    while (continuar):
        print """Que tarea desea realizar?\n
        1. Agregar contacto.\n
        2. Modificar contacto.\n
        3. Mostrar contactos\n
        4. Eliminar contacto\n
        5. Finalizar ejecucion\n
        """
        try:
            menuValue = int(raw_input('Ingrese nro: '))
        except Exception, e:
            print 'Ingrese un Nro. entero, error(%s)' % e
            menuValue = int(raw_input('Ingrese nro: '))
        if (menuValue == 1):
            controlAg.manipularContactos(contactos)
        elif (menuValue == 2):
            controlAg.modificarContactos(contactos)
        elif (menuValue == 3):
            controlAg.mostrarContactos(contactos)
        elif (menuValue == 4):
            controlAg.eliminarContacto(contactos)
        elif (menuValue == 5):
            continuar = False
            print 'See ya later'
        elif():
            print 'Ingrese un valor de la lista'


if __name__ == "__main__":
    main()
