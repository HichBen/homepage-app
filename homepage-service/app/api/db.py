import os

from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()


homepage = Table(
    'homepage',
    metadata,
    Column('group_id', Integer, primary_key=True),
    Column('welcome_message', String(500)),
    Column('about_section', String(250)),
    Column('email', String(10)),
    Column('phone_number', String(10)),
    Column('website', String(10)),
    Column('group_name', String(10)),
)

database = Database(DATABASE_URI)