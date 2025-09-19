from models import Antibiotic, Vaccine, Vitamin


if __name__ == "__main__":
    medicines = [
        Antibiotic("Test1", 10, 50.0),
        Vitamin("Tet3", 20, 5.0),
        Vaccine("Test3", 2, 300.0)
    ]

    for med in medicines:
        print(med.info())