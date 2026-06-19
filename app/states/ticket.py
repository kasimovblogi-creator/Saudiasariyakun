from aiogram.fsm.state import State, StatesGroup


class TicketState(StatesGroup):
    waiting_from_city = State()
    waiting_to_city = State()
    waiting_date = State()