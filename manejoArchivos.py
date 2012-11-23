def addfileagenda(contacto):
    try:
        afile = open('agenda.txt', 'a')
    except:
        afile = open('agenda.txt', 'w')
    for key in contacto.keys():
        afile.write(key + ' ' + str(contacto[key]) + '\n')
    afile.close()
