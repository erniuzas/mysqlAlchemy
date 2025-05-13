# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from database import Base



# class Pareigos(Base):
#     __tablename__ = "pareigos"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     pavadinimas = Column(String(50), nullable=False)
    

# class DarbuotojaiPareigos(Base):
#     __tablename__ = "darbuotojai_pareigos"
#     darbuotojas_id = Column(Integer, ForeignKey("darbuotojai.id"), primary_key=True)
#     pareigos_id = Column(Integer, ForeignKey("pareigos.id"), primary_key=True)

#     darbuotojas = relationship("Darbuotojai", back_populates="pareigos")
#     pareigos = relationship("Pareigos", back_populates="darbuotojai")
