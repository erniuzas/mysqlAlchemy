from database import get_session, get_engine, Base
from services import darbuotojai_services
from services import imoniu_services

def main():
    # Create the database and tables
    engine = get_engine()
    Base.metadata.create_all(engine)

    # Start the main menu loop
    while True:
        print("\n--- Darbuotojų valdymo sistema ---")
        print("1. Pridėti darbuotoją")
        print("2. Rodyti darbuotojus")
        print("3. Ištrinti darbuotoją")
        print("4. Pridėti įmonę")
        print("5. Išeiti")

        choice = input("Pasirinkite veiksmą (1-4): ")

        if choice == "1":
            print("Pridėti darbuotoją:")
            darbuotojai_services.prideti_darbuotoja()
        elif choice == "2":
            print("Rodyti darbuotojus:")
            darbuotojai_services.rodyti_darbuotojus()
        elif choice == "3":
            print("Ištrinti darbuotoją:")
            darbuotojai_services.istrinti_darbuotoja()
        elif choice == "4":
            print("Pridėti įmonę:")
            imoniu_services.prideti_imone()
        elif choice == "5":
            print("Išeinama iš programos.")
            break
        else:
            print("Neteisingas pasirinkimas, bandykite dar kartą.")

if __name__ == "__main__":
    main()






