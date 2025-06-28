from typing import List, Optional, Tuple
from datetime import datetime, timedelta
from pydantic import BaseModel, EmailStr, root_validator
from pydantic_extra_types import CreditCardNumber

class QueryRequest(BaseModel):
    query: str
    
class Customer(BaseModel):
    id: int
    first_name: str
    last_name: str
    address: Optional[str]
    phone_number: Optional[str]
    email: EmailStr
    card_num: CreditCardNumber

class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    address: Optional[str]
    phone_number: Optional[str]
    email: EmailStr
    card_num: CreditCardNumber
class Staff(BaseModel):
    id: int
    first_name: str
    last_name: str
    address: Optional[str]
    phone_number: Optional[str]
    email: EmailStr
    staff_type: str
class Service(BaseModel):
    id: int
    name: str
    cost: float
    duration: int
    related_services: Optional[str]
    skill_level: str
class StylistService(BaseModel):
    stylist_id: int
    service_id: int
class ScheduleParams(BaseModel):
    customer_id: int
    service_ids: List[int]
    skill_level: Optional[str] = None
    staff_id: Optional[int] = None
    
    @root_validator
    def validate_exclusive_or_none(cls, values):
        skill, staff = values.get("skill_level"), values.get("staff_id")
        if skill is not None and staff is not None:
            raise ValueError("Provide at most one of skill_level OR staff_id, not both.")
        return values
class Appointment(BaseModel):
    id: int
    start_datetime: datetime
    end_datetime: datetime
    service_details: Optional[str]
    stylist_id: int
    customer_id: int
    noshow: bool
    notes: Optional[str]

class AppointmentCreate(BaseModel):
    start_datetime: datetime
    end_datetime: datetime
    service_details: Optional[str]
    stylist_id: int
    customer_id: int
    noshow: bool = False
    notes: Optional[str]

class AppointmentUpdate(BaseModel):
    start_datetime: Optional[datetime]
    end_datetime: Optional[datetime]
    service_details: Optional[str]
    stylist_id: Optional[int]
    customer_id: Optional[int]
    noshow: Optional[bool]
    notes: Optional[str]

class Product(BaseModel):
    id: int
    name: str
    brand: Optional[str]
    volume: float
    unit: str
    retail_price: float

class ProductCreate(BaseModel):
    name: str
    brand: Optional[str]
    volume: float
    unit: str
    retail_price: float

class ProductUpdate(BaseModel):
    name: Optional[str]
    brand: Optional[str]
    volume: Optional[float]
    unit: Optional[str]
    retail_price: Optional[float]

class PurchaseHistory(BaseModel):
    transaction_id: int
    product_id: int
    customer_id: int
    staff_id: int
    nbr_items: int
    datetime: datetime

class PurchaseHistoryCreate(BaseModel):
    product_id: int
    customer_id: int
    staff_id: int
    nbr_items: int
    datetime: datetime