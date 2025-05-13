from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Imone(Base):
    __tablename__ = "imones"
    id = Column(Integer, primary_key=True, autoincrement=True)
    pavadinimas = Column(String(100), nullable=False)

    darbuotojai = relationship("Darbuotojai", back_populates="imone")

    def __repr__(self):
        return f"<Imone(id={self.id}, pavadinimas='{self.pavadinimas}')>"