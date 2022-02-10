def printHello(firstName, lastName):
    print("Hola ", lastName, firstName-lastName)
    printHello(firstName = "James", lastName = "Bond")


def expedirINE(name, edad=18):
    print("INE de ",name, edad)

expedirINE("Paulo", 18)