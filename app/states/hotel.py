from aiogram.fsm.state import State, StatesGroup


class HotelState(StatesGroup):
    waiting_city = State()
    waiting_checkin = State()
    waiting_checkout = State()
    waiting_guests = State()