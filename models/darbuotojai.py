from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import date
from database import Base

class Darbuotojai(Base):
    __tablename__ = "darbuotojai"
    id = Column(Integer, primary_key=True, autoincrement=True)
    vardas = Column(String(50), nullable=False)
    pavarde = Column(String(50), nullable=False)
    gimimo_data = Column(Date, default=date.today)
    pareigos = Column(String(50), nullable=False)
    atlyginimas = Column(Integer, nullable=False)
    dirba_nuo = Column(Date, default=date.today)

    imone_id = Column(Integer, ForeignKey("imones.id"))
    imone = relationship("Imone", back_populates="darbuotojai")




    def validate(self):
        if not self.vardas or not self.pavarde:
            raise ValueError("Vardas ir pavarde negali buti tusti.")
        if self.atlyginimas < 0:
            raise ValueError("Atlyginimas negali buti neigiamas.")
        if self.gimimo_data >= date.today():
            raise ValueError("Gimimo data negali buti siandienos ar ateities data.")
        if self.dirba_nuo > date.today():
            raise ValueError("Data, nuo kada dirba, negali buti ateities data.")

    def __repr__(self):
        return f"<Darbuotojai(id={self.id}, vardas='{self.vardas}', pavarde='{self.pavarde}', " \
               f"gimimo_data='{self.gimimo_data}', pareigos='{self.pareigos}', " \
               f"atlyginimas={self.atlyginimas}, dirba_nuo='{self.dirba_nuo}')>"