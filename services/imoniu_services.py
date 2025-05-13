from database import get_session
from models.imone import Imone

def prideti_imone():
    session = get_session()
    print("Pridedama imone...")
    pavadinimas = input("Iveskite imones pavadinima: ")

    nauja_imone = Imone(
        pavadinimas=pavadinimas
    )

    session.add(nauja_imone)
    session.commit()
    print("Imone prideta!")

def rodyti_imones():
    session = get_session()
    print("Rodomos visos imones:")
    imones = session.query(Imone).all()
    for imone in imones:
        print(f"ID: {imone.id}, Pavadinimas: {imone.pavadinimas}")

def istrinti_imone():
    session = get_session()
    print("Istrinama imone...")
    imone_id = input("Iveskite imones ID, kuria norite istrinti: ")

    imone = session.query(Imone).filter(Imone.id == imone_id).first()
    if imone:
        session.delete(imone)
        session.commit()
        print("Imone istrinta!")
    else:
        print("Imone nerasta.")