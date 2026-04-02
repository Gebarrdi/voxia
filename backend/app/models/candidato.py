# models/candidato.py — modelos de la base de datos
# Cada clase representa una tabla en PostgreSQL

from sqlalchemy import String, Text, Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.database import Base


class PartidoPolitico(Base):
    __tablename__ = "partido_politico"

    # Columnas
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    siglas: Mapped[str] = mapped_column(
        String(20), nullable=False, unique=True
    )
    logo_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, server_default=func.now()
    )

    # Relación — un partido tiene muchos candidatos
    candidatos: Mapped[list["Candidato"]] = relationship(
        back_populates="partido"
    )


class Candidato(Base):
    __tablename__ = "candidato"

    # Columnas
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    partido_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("partido_politico.id"), nullable=False
    )
    nombre: Mapped[str] = mapped_column(String(150), nullable=False)
    foto_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    biografia: Mapped[str | None] = mapped_column(Text, nullable=True)
    fuente_jne: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, server_default=func.now()
    )

    # Relaciones
    partido: Mapped["PartidoPolitico"] = relationship(
        back_populates="candidatos"
    )
    propuestas: Mapped[list["Propuesta"]] = relationship(
        back_populates="candidato", cascade="all, delete-orphan"
    )
    antecedentes: Mapped[list["Antecedente"]] = relationship(
        back_populates="candidato", cascade="all, delete-orphan"
    )


class Tema(Base):
    __tablename__ = "tema"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(
        String(80), nullable=False, unique=True
    )
    descripcion: Mapped[str | None] = mapped_column(Text, nullable=True)
    icono: Mapped[str | None] = mapped_column(String(50), nullable=True)

    # Relación
    propuestas: Mapped[list["Propuesta"]] = relationship(
        back_populates="tema"
    )


class Propuesta(Base):
    __tablename__ = "propuesta"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    candidato_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("candidato.id"), nullable=False
    )
    tema_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tema.id"), nullable=False
    )
    descripcion: Mapped[str] = mapped_column(Text, nullable=False)
    fuente: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, server_default=func.now()
    )

    # Relaciones
    candidato: Mapped["Candidato"] = relationship(
        back_populates="propuestas"
    )
    tema: Mapped["Tema"] = relationship(
        back_populates="propuestas"
    )


class Antecedente(Base):
    __tablename__ = "antecedente"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    candidato_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("candidato.id"), nullable=False
    )
    tipo: Mapped[str] = mapped_column(String(50), nullable=False)
    descripcion: Mapped[str] = mapped_column(Text, nullable=False)
    fuente_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, server_default=func.now()
    )

    # Relación
    candidato: Mapped["Candidato"] = relationship(
        back_populates="antecedentes"
    )
