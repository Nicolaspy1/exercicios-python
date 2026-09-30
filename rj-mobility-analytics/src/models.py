from sqlalchemy import Column, Float, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class VeiculoModel(Base):
    __tablename__ = "veiculos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ordem = Column(String(20), unique=True, index=True, nullable=False) # Ex: A28123 (identificador do autocarro)
    linha = Column(String(20), index=True) # Ex: 415, 309

    # Relacionamento com as posições de GPS
    posicoes = relationship("PosicaoGPSModel", back_populates="veiculo", cascade="all, delete-orphan")

class PosicaoGPSModel(Base):
    __tablename__ = "posicoes_gps"

    id = Column(Integer, primary_key=True, autoincrement=True)
    veiculo_id = Column(Integer, ForeignKey("veiculos.id"), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    velocidade = Column(Float)
    datahora_servidor = Column(DateTime)

    # Relacionamento reverso
    veiculo = relationship("VeiculoModel", back_populates="posicoes")