from aiogram.fsm.state import State, StatesGroup


class UniversityState(StatesGroup):
    waiting_university = State()
    waiting_major = State()