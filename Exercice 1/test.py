from animal import Chien, Chat, Vache, Robot

def faire_parler(animal):
    print(animal.parler())

if __name__ == '__main__':
    collection_polymorphe = [
        Chien(),
        Chat(),
        Vache(),
        Robot()
    ]
    print("--- Les animaux et le robot se présentent ---")
    for a in collection_polymorphe:
        faire_parler(a)