from database import get_session
from models.darbuotojai import Darbuotojai
from datetime import datetime, date
from models.imone import Imone

session = get_session()
imones = session.query(Imone).all()
print("Pasirinkite imones ID: ")
for imone in imones:
    print(f"ID: {imone.id}, Pavadinimas: {imone.pavadinimas}")
imone_id = int(input("Iveskite imones ID: "))

def prideti_darbuotoja():
    session = get_session()
    print("Pridedamas darbuotojas...")
    vardas = input("Iveskite darbuotojo varda: ")
    pavarde = input("Iveskite darbuotojo pavarde: ")
    gimimo_data = input("Iveskite darbuotojo gimimo data (YYYY-MM-DD): ")
    try:
        gimimo_data = datetime.strptime(gimimo_data, "%Y-%m-%d").date()
    except ValueError:
        print("Gimimo data turi buti teisingame formate (YYYY-MM-DD).")
        return
    
    pareigos = input("Iveskite darbuotojo pareigas: ")
    
    try:
        atlyginimas = int(input("Iveskite darbuotojo atlyginima: "))
    except ValueError:
        print("Atlyginimas turi buti skaicius.")
        return
    
    dirba_nuo_input = input("Iveskite data, nuo kada dirba (YYYY-MM-DD), palikite tuscia laukeli, jei norite siandienos datos: ")

    if dirba_nuo_input.strip():
        try:
            dirba_nuo = datetime.strptime(dirba_nuo_input, "%Y-%m-%d").date()
        except ValueError:
            print("Data turi buti teisingame formate (YYYY-MM-DD).")
            return
    else:
        dirba_nuo = date.today()


    naujas_darbuotojas = Darbuotojai(
        vardas=vardas,
        pavarde=pavarde,
        gimimo_data=gimimo_data,
        pareigos=pareigos,
        atlyginimas=atlyginimas,
        dirba_nuo=dirba_nuo,
        imone_id=imone_id
    )

    try:
        naujas_darbuotojas.validate()
        session.add(naujas_darbuotojas)
        session.commit()
        print("Darbuotojas pridetas!")
    except ValueError as e:
        print(f"Klaida: {e}")


def rodyti_darbuotojus():
    session = get_session()
    print("Rodomi visi darbuotojai:")
    darbuotojai = session.query(Darbuotojai).all()
    for darbuotojas in darbuotojai:
        print(f"ID: {darbuotojas.id}, Vardas: {darbuotojas.vardas}, Pavarde: {darbuotojas.pavarde}, "
                f"Gimimo data: {darbuotojas.gimimo_data}, Pareigos: {darbuotojas.pareigos}, "
                f"Atlyginimas: {darbuotojas.atlyginimas}, Dirba nuo: {darbuotojas.dirba_nuo}")
            
def istrinti_darbuotoja():
    session = get_session()
    print("Istrinamas darbuotojas...")
    darbuotojo_id = int(input("Iveskite darbuotojo ID, kuri norite istrinti is saraso: "))
    darbuotojas = session.query(Darbuotojai).filter(Darbuotojai.id == darbuotojo_id).first()
    if darbuotojas:
        session.delete(darbuotojas)
        session.commit()
        print("Darbuotojas istrintas!")
    else:
        print("Darbuotojas nerastas.")

    