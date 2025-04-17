from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Orders(Base):
    __tablename__ = 'orders'
    __table_args__ = {'schema': 'northwind'}  

    orderid = Column(Integer, primary_key=True)
    customerid = Column(String(5), ForeignKey('northwind.customers.customerid'))
    employeeid = Column(Integer, ForeignKey('northwind.employees.employeeid'))
    orderdate = Column(Date)

    customer = relationship("Customers")
    employee = relationship("Employees")
    items = relationship("OrderDetails", back_populates="order")

class OrderDetails(Base):
    __tablename__ = 'order_details'
    __table_args__ = {'schema': 'northwind'}

    orderid = Column(Integer, ForeignKey('northwind.orders.orderid'), primary_key=True)
    productid = Column(Integer, ForeignKey('northwind.products.productid'), primary_key=True)
    quantity = Column(Integer)
    unitprice = Column(Numeric)

    order = relationship("Orders", back_populates="items")
    product = relationship("Products")

class Customers(Base):
    __tablename__ = 'customers'
    __table_args__ = {'schema': 'northwind'}

    customerid = Column(String(5), primary_key=True)
    companyname = Column(String)

class Employees(Base):
    __tablename__ = 'employees'
    __table_args__ = {'schema': 'northwind'}

    employeeid = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)

class Products(Base):
    __tablename__ = 'products'
    __table_args__ = {'schema': 'northwind'}

    productid = Column(Integer, primary_key=True)
    productname = Column(String)
