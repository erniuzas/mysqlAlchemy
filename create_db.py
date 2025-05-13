from database import engine, Base
from models.darbuotojai import Darbuotojai
from models.imone import Imone

# Sukuria visas lenteles duomenų bazėje
Base.metadata.create_all(bind=engine)

print("Lentelės sukurtos sėkmingai!")