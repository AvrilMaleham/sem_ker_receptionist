import os
import asyncio
import asyncpg
from typing import List, Optional, Tuple
from datetime import datetime, timedelta
from pydantic import BaseModel, EmailStr
from semantic_kernel.skill_definition import kernel_function
from schemas import *

# -----------------------------
# Database URL & Connection
# -----------------------------
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://username:password@localhost/salon_db")

async def get_connection():
    return await asyncpg.connect(DATABASE_URL)

# -----------------------------
# CRUD Plugin Class
# -----------------------------

class SalonDbPlugin:
    """Async plugin exposing Salon DB CRUD operations as Semantic Kernel functions."""

    @kernel_function(name="GetCustomerByFirstName", description="Fetch a customer by first name.")
    async def get_customer_by_first_name(self, first_name: str) -> Customer:
        conn = await get_connection()
        row = await conn.fetchrow(
            "SELECT id, first_name, last_name, address, phone_number, email, card_num FROM customer WHERE first_name = $1",
            first_name
        )
        await conn.close()
        return Customer(**row)
    
    @kernel_function(name="GetCustomerByFirstNameLastName", description="Fetch a customer by first name and last name.")
    async def get_customer_by_first_name_last_name(self, first_name: str, last_name: str) -> Customer:
        conn = await get_connection()
        row = await conn.fetchrow(
            "SELECT id, first_name, last_name, address, phone_number, email, card_num FROM customer WHERE first_name = $1 AND last_name = $2",
            first_name, last_name
        )
        await conn.close()
        return Customer(**row)
    
    @kernel_function(name="CreateCustomer", description="Create a new customer.")
    async def create_customer(self, data: CustomerCreate) -> Customer:
        conn = await get_connection()
        row = await conn.fetchrow(
            "INSERT INTO customer (first_name, last_name, address, phone_number, email, card_num)"
            " VALUES ($1, $2, $3, $4, $5) RETURNING id, first_name, last_name, address, phone_number, email, card_num",
            data.first_name, data.last_name, data.address, data.phone_number, data.email, data.card_num
        )
        await conn.close()
        return Customer(**row)   

    # Repeat for Staff
    @kernel_function(name="GetStaffByFirstName", description="Fetch a staff member by first name.")
    async def get_staff_by_first_name(self, staff_first_name: str) -> Staff:
        conn = await get_connection()
        row = await conn.fetchrow(
            "SELECT id, first_name, last_name, address, phone_number, email, staff_type"
            " FROM staff WHERE first_name = $1 AND staff_type LIKE '%stylist'", staff_first_name
        )
        await conn.close()
        return Staff(**row)
    
    @kernel_function(name="GetStaffByFirstNameLastName", description="Fetch a staff member by first name and last name.")
    async def get_staff_by_first_name_last_name(self, staff_first_name: str, staff_last_name: str) -> Staff:
        conn = await get_connection()
        row = await conn.fetchrow(
            "SELECT id, first_name, last_name, address, phone_number, email, staff_type"
            " FROM staff WHERE first_name = $1 AND last_name = $2 AND staff_type LIKE '%stylist'", staff_first_name, staff_last_name
        )
        await conn.close()
        return Staff(**row)
    
    @kernel_function(name="GetStaffByType", description="Fetch the list of all staff members by type.")
    async def get_staff_by_type(self, staff_type: str) -> Staff:
        conn = await get_connection()
        row = await conn.fetchrow(
            "SELECT id, first_name, last_name, address, phone_number, email, staff_type"
            " FROM staff WHERE staff_type = $1", staff_type
        )
        await conn.close()
        return Staff(**row)
    
    @kernel_function(name="GetServiceByStylist", description="Fetch the list of all services for a given stylist.")
    async def get_service_by_stylist(self, stylist_first_name: str, stylist_last_name: str) -> Service:
        staff_details = await self.get_staff_by_first_name_last_name(stylist_first_name, stylist_last_name) 
        staff_id = staff_details.id
        conn = await get_connection()
        row = await conn.fetchrow(
        """
        WITH sty_ser AS (
          SELECT
            stylist_id,
            service_id
          FROM
            stylist_service
          WHERE
            stylist_id = $1
        )
        SELECT
          a.id,
          a.name,
          a.cost,
          a.duration,
          a.related_services,
          a.skill_level
        FROM
          service a
          INNER JOIN sty_ser b ON a.id = b.service_id
        """,  staff_id
    )
        await conn.close()
        return Service(**row)
    
    @kernel_function(name="GetStylistByService", description="Fetch the list of all stylists who perform a given service.")
    async def get_stylist_by_service(self, service_name: str) -> Staff:
        conn = await get_connection()
        row = await conn.fetchrow(
        """
        WITH serv AS (
            SELECT id
             FROM service
            WHERE
             name = $1
        ),
        sty_ser AS (
          SELECT
            stylist_id
          FROM
            stylist_service INNER JOIN serv
          ON 
            service_id = id
        )
        SELECT
          a.id,
          a.first_name,
          a.last_name,
          a.address,
          a.phone_number,
          a.email,
          a.staff_type
        FROM
          staff a
          INNER JOIN sty_ser b ON a.id = b.stylist_id;
        """,  service_name
    )
        await conn.close()
        return Staff(**row)

@kernel_function(
    name="GetLastAppointmentByCustomer",
    description="Fetch the last appointment a customer had by giving the customer ID as an input."
)
async def get_last_appointment_by_customer(self, customer_id: str) -> Appointment:
    conn = await get_connection()
    row = await conn.fetchrow(
        """
        SELECT
          id,
          start_datetime,
          end_datetime,
          service_details,
          stylist_id,
          customer_id,
          noshow,
          notes
        FROM appointment
        WHERE customer_id = $1
          AND start_datetime < now()  -- only past appointments
        ORDER BY start_datetime DESC
        LIMIT 1;
        """,
        customer_id
    )
    await conn.close()

    return Appointment(**row) if row else None

@kernel_function(
    name="CheckScheduleAvailabilty",
    description="Check which appointments are available."
)
async def create_appointment(self, customer_id: str) -> Appointment:
    conn = await get_connection()
    row = await conn.fetchrow(
        """
        SELECT
          id,
          start_datetime,
          end_datetime,
          service_details,
          stylist_id,
          customer_id,
          noshow,
          notes
        FROM appointment
        WHERE customer_id = $1
          AND start_datetime < now()  -- only past appointments
        ORDER BY start_datetime DESC
        LIMIT 1;
        """,
        customer_id
    )
    await conn.close()

    return Appointment(**row) if row else None

@kernel_function(name="CreateAppointment", description="Create a new appointment.")
async def create_appointment(self, data: AppointmentCreate) -> Appointment:
        conn = await get_connection()
        row = await conn.fetchrow(
            "INSERT INTO appointment (start_datetime, end_datetime, service_details, stylist_id, customer_id, noshow, notes)"
            " VALUES ($1, $2, $3, $4, $5, $6, $7)"
            " RETURNING id, start_datetime, end_datetime, service_details, stylist_id, customer_id, noshow, notes",
            data.start_datetime, data.end_datetime, data.service_details,
            data.stylist_id, data.customer_id, data.noshow, data.notes
        )
        await conn.close()
        return Appointment(**row)
