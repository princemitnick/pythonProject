liste = []


def __readVar__() -> None:
    c = 5
    while c != 0:
        name = input("Put a name in the list: ")
        liste.append(name)
        c -= 1

def readList() -> None:
    for i in range(len(liste)):
        print(liste[i])

if __name__ == '__main__':
    __readVar__()
    readList()