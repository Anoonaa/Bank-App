#!/usr/bin/env python3

"""
Creating tables for database 'bank'
"""

from sqlalchemy import (
    Column, DATE, DATETIME, ForeignKey, Integer, PrimaryKeyConstraint, String
)

from database import Base, get_engine


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    firstname = Column(String(50), nullable=False)
    middlename = Column(String(50), nullable=True)
    lastname = Column(String(50), nullable=False)

    email = Column(String(100), nullable=False)

    city = Column(String(50), nullable=False)
    dob = Column(DATE, nullable=False)
    phone = Column(String(15), nullable=False)


class Branch(Base):
    __tablename__ = "branches"

    id = Column(Integer, primary_key=True)
    city = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)


class Account(Base):
    __tablename__ = "accounts"

    account_number = Column(Integer, primary_key=True)
    account_opened_on = Column(DATETIME, nullable=False)
    account_status = Column(String(10), nullable=False)
    account_type = Column(String(50), nullable=False)
    opening_balance = Column(Integer, nullable=False)

    branch_id = Column(Integer, ForeignKey("branches.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)


class TransactionDetails(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    transaction_amount = Column(Integer, nullable=False)
    transaction_date = Column(DATETIME, nullable=False)
    transaction_medium = Column(String(10), nullable=False)
    transaction_type = Column(String(10), nullable=False)

    account_number = Column(
        Integer, ForeignKey("accounts.account_number"), nullable=False
    )


class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, nullable=False)
    loan_amount = Column(Integer, nullable=False)
    loan_approved_on = Column(DATETIME, nullable=False)
    loan_duration = Column(Integer, nullable=False)
    loan_interest = Column(Integer, nullable=False)
    loan_status = Column(String(10), nullable=False)
    loan_type = Column(String(50), nullable=False)

    account_number = Column(
        Integer, ForeignKey("accounts.account_number"), nullable=False
    )

    branch_id = Column(Integer, ForeignKey("branches.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)

    # Primary key constraint made up of 'customer_id' and 'branch_id'
    __table_args__ = (
        PrimaryKeyConstraint(
            "customer_id", "branch_id", name="loan_customer_id_branch_id_pk"
        ),
    )


def create_tables():
    engine = get_engine()  # Getting engine connected to the 'bank' database
    Base.metadata.create_all(engine)  # Creating tables


if __name__ == "__main__":
    create_tables()
