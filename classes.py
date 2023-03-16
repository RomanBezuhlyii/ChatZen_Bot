from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, types

class FSMContactsLJ(StatesGroup):
    email = State()
    phone_number = State()

class FSMPaymentInfoLJ(StatesGroup):
    nickname_lj = State()
    first_second_name = State()
    payment_card = State()

class FSMSupportRegisterProblem(StatesGroup):
    nickname_lj = State()
    phone_number = State()
    registration_data = State()

class FSMSupportAdditionalProblem(StatesGroup):
    nickname_lj = State()
    phone_number = State()
    problem_short_description = State()

class FSMRegisterGirlLU(StatesGroup):
    your_id_lu = State()
    girl_id_lu = State()

class FSMRegisterGirlLJ(StatesGroup):
    your_nickname_lj = State()
    girl_nickname_lj = State()

class FSMRegisterLU(StatesGroup):
    GirlID_LU = State()
    Phone_number = State()
    Main_page_LU = State()
    Page_LU = State()
    Main_page_passports_LU = State()
    Selfie_LU = State()


class GirlLU:
    GirlID_LU = ''
    Phone_number = ''
    Main_page_LU = ''
    Page_LU = ''
    Main_page_passports_LU = ''
    Selfie_LU = ''

    async def send_to_admin(self, bot: Bot, admin_tg_id, user_tg_id):
        await bot.send_message(chat_id=admin_tg_id, text=f"Telegram ID клиента: @{user_tg_id}\n"
                                                         f"Номер телефона: {self.Phone_number}\n" 
                                                         f"LivU/Yaar ID: {self.GirlID_LU}")

        media_group = types.MediaGroup()
        media_group.attach_photo(photo=self.Main_page_LU,  caption="1. Главная страница.")
        media_group.attach_photo(photo=self.Page_LU, caption="2. Страница с загруженными фото и видео.")
        await bot.send_media_group(chat_id=admin_tg_id, media=media_group)

    async def send_to_admin_all(self, bot: Bot, admin_tg_id, user_tg_id):
        await bot.send_message(chat_id=admin_tg_id, text=f"Telegram ID клиента: @{user_tg_id}\n"
                                                         f"Номер телефона: {self.Phone_number}\n"
                                                         f"LivU/Yaar ID: {self.GirlID_LU}")
        media_group = types.MediaGroup()
        media_group.attach_photo(photo=self.Main_page_LU, caption="1. Главная страница.")
        media_group.attach_photo(photo=self.Page_LU, caption="2. Страница с загруженными фото и видео.")
        media_group.attach_photo(photo=self.Main_page_passports_LU, caption="3. Главная страница паспорта.")
        media_group.attach_photo(photo=self.Selfie_LU, caption="4. Селфи с паспортом.")
        await bot.send_media_group(chat_id=admin_tg_id, media=media_group)


class FSMPaymentInfoLU(StatesGroup):
    LivID = State()
    full_name = State()
    card_info = State()

class FSMAdditionalProblemLU(StatesGroup):
    id_lu = State()
    phone_number = State()
    problem_text = State()
