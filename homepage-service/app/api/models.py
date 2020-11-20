from pydantic import BaseModel
from typing import List, Optional


class HomePageIn(BaseModel):
    welcome_message: Optional[str] = None
    about_section: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    website: Optional[str] = None
    group_name: str
    events: Optional[List[int]] = None


class HomePageOut(HomePageIn):
    group_id: int


class HomePage(BaseModel):
    group_id: int
    welcome_message: Optional[str] = None
    about_section: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    website: Optional[str] = None
    group_name: str
    events: Optional[List[int]] = None


class HomePageUpdate(HomePageIn):
    welcome_message: Optional[str] = None
    about_section: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    website: Optional[str] = None
    group_name: Optional[str] = None
    events: Optional[List[int]] = None

