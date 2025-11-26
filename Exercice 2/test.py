from forme import Cercle, Rectangle, Triangle

if __name__ == "__main__":
    formes = [
        Cercle(3),
        Rectangle(4, 5),
        Triangle(6, 2)
    ]

    for f in formes:
        print(f)