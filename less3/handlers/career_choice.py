from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from less3.keyboards.prof_keybords import make_row_keyboard

router = Router()

avaitable_jobs = [
    "Программист",
    "Дизайнер",
    "Маркетолог",
    "Повар"
]

avaitable_grades = ['Junior', 'Middle', "Senior"]

class ChoiseProfile(StatesGroup):
    job = State()
    grade = State()

@router.message(Command("prof"))
async def command_prof(message: types.Message, state: FSMContext):
    await message.answer(
        text="Выбирите профессию",
        reply_markup=make_row_keyboard(avaitable_jobs))
    await state.set_state(ChoiseProfile.job)


@router.message(ChoiseProfile.job, F.text.in_(avaitable_jobs))
async def prof_chosen(message: types.Message, state: FSMContext):
    await state.update_data(profession=message.text)
    await message.answer(
        text="Выбирите уровень",
        reply_markup=make_row_keyboard(avaitable_grades))
    await state.set_state(ChoiseProfile.grade)


@router.message(ChoiseProfile.grade, F.text.in_(avaitable_grades))
async def grade_chosen(message: types.Message, state: FSMContext):
     user_data = await state.get_data()
     await message.answer(f"Ваша профессия: {user_data['profession']}\n"
     f"Ваш уровень: {message.text}",
     reply_markup=types.ReplyKeyboardRemove())
     await state.clear()


@router.message(ChoiseProfile.grade)
async def grade_chosen_incorrect(message: types.Message):
    await message.answer(
    text="Выберите уровень",
    reply_markup=make_row_keyboard(avaitable_grades))

