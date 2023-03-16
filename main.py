import scrapper as spy
import keyboards as kb
import config as cnfg
import classes as cl
import datetime
import os.path
import json
import os

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.utils.markdown import text, hlink, link
from aiogram.types import ReplyKeyboardRemove
from datetime import timedelta, datetime
from aiogram.dispatcher.filters import Text
from aiogram import Bot, types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor

from lj_girl_class import LJGirls
from lu_person_list import LUPersons
import link_spy.link_spy.spiders.link_spider as spider


storage = MemoryStorage()
bot = Bot(token = cnfg.TOKEN)
dp = Dispatcher(bot, storage = storage)
scheduler = AsyncIOScheduler(timezone="Europe/Kiev")
lu_persons = LUPersons()
GirlLU = cl.GirlLU()
lu_person_tmp_list = list()
lj_person_tmp_list = list()
lu_person_tmp_day1_list = list()
lj_person_tmp_day1_list = list()
lu_person_tmp_day0_list = list()
lj_person_tmp_day0_list = list()

logo_rus_gif = cnfg.logo_rus_gif
logo_ukr_gif = cnfg.logo_ukr_gif
logo_eng_gif = cnfg.logo_eng_gif
url_about_us = cnfg.url_about_us
url_registr_lu = cnfg.url_registr_lu
url_account_livu_lu = cnfg.url_account_livu_lu
url_earned_coins_lu = cnfg.url_earned_coins_lu
url_cost_and_level_lu = cnfg.url_cost_and_level_lu
url_ww_and_min_lu = cnfg.url_ww_and_min_lu
url_call_types_lu = cnfg.url_call_types_lu
url_turn_to_lu = cnfg.url_turn_to_lu
url_search_lu = cnfg.url_search_lu
url_search_and_call_lu = cnfg.url_search_and_call_lu
url_message_section_lu = cnfg.url_message_section_lu
url_Friend_list_lu = cnfg.url_Friend_list_lu
url_black_list_lu = cnfg.url_black_list_lu
url_secrets_and_tips_lu = cnfg.url_secrets_and_tips_lu
url_adult_content_lu = cnfg.url_adult_content_lu
url_message_templates_lu = cnfg.url_message_templates_lu
url_reward_lu = cnfg.url_reward_lu
url_bonuses_and_gifts_lu = cnfg.url_bonuses_and_gifts_lu
url_contests_lu = cnfg.url_contests_lu
url_fines_lu = cnfg.url_fines_lu
url_important_points_lu = cnfg.url_important_points_lu
url_working_week_and_pay = cnfg.url_working_week_and_pay
url_payment_method = cnfg.url_payment_method_lu
url_verification_methods_lu = cnfg.url_verification_methods_lu
url_first_verif_lu = cnfg.url_first_verif_lu
url_second_verif_lu = cnfg.url_second_verif_lu
url_third_verif_lu = cnfg.url_third_verif_lu

#Command for cancel FSM without saving data
@dp.message_handler(state = "*", commands = "Отмена")
@dp.message_handler(Text(equals = "Отмена", ignore_case = True), state = "*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    async with state.proxy() as data:
        await bot.send_message(384187187, text = "Пользователь отменил ввод данных. Уже введенные данные:\n" + data)
    await state.finish()
    await message.reply('Ввод данных отменен')

#Start function
@dp.message_handler(commands = ['start'])
async def process_start_command(message: types.Message):
    await message.reply("Компания Chatzen приветствует Вас!\nПожалуйста, выберите язык\n"
                        "\nКомпанія Chatzen вітає вас!\nБудь ласка, виберіть мову\n\n"
                        "Chatzen welcomes you!\nPlease choose your language", reply_markup = kb.language_kb)


### 1 Language page

#English language button
@dp.callback_query_handler(lambda call: call.data == 'en')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id = callback_query.message.chat.id,
                             message_id = callback_query.message.message_id)
    await bot.send_animation(callback_query.from_user.id,
                             caption = "The section is in development. Please go back.",
                             animation = logo_eng_gif,
                             reply_markup = kb.back_en)

#Go back from english language page
@dp.callback_query_handler(lambda call: call.data == 'go_back')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id = callback_query.message.chat.id,
                             message_id = callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id,
                           text = "Компания Chatzen приветствует Вас!\n"
                                  "Пожалуйста, выберите язык\n"
                                  "\nКомпанія Chatzen вітає вас!\nБудь ласка, виберіть мову\n\n"
                                  "Chatzen welcomes you!\nPlease choose your language",
                           reply_markup = kb.language_kb)

#Ukrainian language button
@dp.callback_query_handler(lambda call: call.data == 'ua')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id = callback_query.message.chat.id,
                             message_id = callback_query.message.message_id)
    await bot.send_animation(callback_query.from_user.id,
                             caption = "Розділ в розробці. \nБудь ласка, поверніться назад.",
                             animation = logo_ukr_gif,
                             reply_markup = kb.back_ua)

#Go back from Ukrainian language page
@dp.callback_query_handler(lambda call: call.data == 'go_back_ua')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id = callback_query.message.chat.id,
                             message_id = callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id,
                           text = "Компания Chatzen приветствует Вас!\n"
                                  "Пожалуйста, выберите язык\n"
                                  "\nКомпанія Chatzen вітає вас!\n"
                                  "Будь ласка, виберіть мову\n\n"
                                  "Chatzen welcomes you!\nPlease choose your language",
                           reply_markup = kb.language_kb)

#Russian language button
@dp.callback_query_handler(lambda call: call.data == 'ru')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id = callback_query.message.chat.id,
                             message_id = callback_query.message.message_id)
    await bot.send_animation(callback_query.from_user.id,
                             caption = "Мы предлагаем несколько приложений для заработка.\n"
                                       "Вы можете работать как в одном, так и в нескольких приложениях.\n"
                                       "Вам необходимо выбрать приложение, зарегистрироваться и пройти обучение,\n"
                                       "чтобы зарабатывать достаточно, а также не получать штрафы.\n"
                                       "И привязать кошелёк для выплат.",
                             animation = logo_rus_gif,
                             reply_markup = kb.main_catalog)

### 2 Russian Catalog

#LivU/Yaar page
@dp.callback_query_handler(lambda call: call.data == 'LU')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id,
                           text = "Выберите раздел, которого касается Ваш вопрос",
                           reply_markup = kb.LivUYaar_catalog)

#To switch from slave pages for LivU/Yaar to LivU/Yaar main page
@dp.callback_query_handler(lambda call: call.data == 'LivU/Yaar')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.edit_message_text(text = "Выберите раздел, которого касается Ваш вопрос",
                                chat_id = callback_query.message.chat.id,
                                message_id = callback_query.message.message_id,
                                reply_markup = kb.LivUYaar_catalog)

#To switch from main catalog to LiveJoy
@dp.callback_query_handler(lambda call: call.data == 'LJ')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id = callback_query.message.chat.id,
                             message_id = callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id,
                           text = "Выберите раздел, которого касается Ваш вопрос",
                           reply_markup = kb.LiveJoy_catalog)

#To switch from slave pages for LiveJoy to LiveJoy main page
@dp.callback_query_handler(lambda call: call.data == 'LiveJoy')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.edit_message_text(text = "Выберите раздел, которого касается Ваш вопрос",
                                chat_id = callback_query.message.chat.id,
                                message_id = callback_query.message.message_id,
                                reply_markup = kb.LiveJoy_catalog)

#FancyMe page
@dp.callback_query_handler(lambda call: call.data == 'FancyMe')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id = callback_query.message.chat.id,
                             message_id = callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id,
                           text = "Раздел в разработке.\nПожалуйста, вернитесь назад.",
                           reply_markup = kb.to_catalog)

#Language selection page
@dp.callback_query_handler(lambda call: call.data == 'Language_selection')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id = callback_query.message.chat.id,
                             message_id = callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id,
                           text = "Компания Chatzen приветствует Вас!\n"
                                  "Пожалуйста, выберите язык\n"
                                  "\nКомпанія Chatzen вітає вас!\n"
                                  "Будь ласка, виберіть мову\n\n"
                                  "Chatzen welcomes you!\nPlease choose your language",
                           reply_markup = kb.language_kb)

#Back to catalog button
@dp.callback_query_handler(lambda call: call.data == 'to_catalog')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id = callback_query.message.chat.id,
                             message_id = callback_query.message.message_id)
    await bot.send_animation(callback_query.from_user.id,
                             caption = "Мы предлагаем несколько приложений для заработка.\n"
                                       "Вы можете работать как в одном, так и в нескольких приложениях.\n"
                                       "Вам необходимо выбрать приложение, зарегистрироваться и пройти обучение,\n"
                                       "чтобы зарабатывать достаточно, а также не получать штрафы.\n"
                                       "И привязать кошелёк для выплат.",
                             animation = logo_rus_gif,
                             reply_markup = kb.main_catalog)

#Girlfriend registration
@dp.callback_query_handler(lambda call: call.data == 'register_girl')
async def register_girl_page(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id = callback_query.message.chat.id,
                             message_id = callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id,
                           text = "Рекомендуйте нас своей знакомой или подруге, помогите ей "
                                  "зарегистрироваться, объясните ей правила и получите процент "
                                  "от её заработка в качестве бонуса! Бонус выплачивается, если "
                                  "подруга вышла на минимум в течении первой недели. В какое "
                                  "приложение Вы хотите зарегистрировать подругу?",
                           reply_markup = kb.register_girl_kb)

#FSM to registration girlfriend in LivU/Yaar
@dp.callback_query_handler(lambda call: call.data == 'register_girl_lu')
async def register_girl_lu(callback_query: types.CallbackQuery, state: FSMContext):
    await cl.FSMRegisterGirlLU.your_id_lu.set()
    await bot.send_message(callback_query.from_user.id, text = "Введите свой ID")

@dp.message_handler(state = cl.FSMRegisterGirlLU.your_id_lu)
async def load_your_id_lu(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['your_id_lu'] = message.text
    await cl.FSMRegisterGirlLU.next()
    await message.reply("Введите ID подруги")

@dp.message_handler(state = cl.FSMRegisterGirlLU.girl_id_lu)
async def load_girl_id_lu(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['girl_id_lu'] = message.text
        await bot.send_message(chat_id=cnfg.admin_tg_id, text=f"Регистрация знакомой в LivU\n"
                                                              f"Telegram ID: @{message.from_user.username}\n"
                                                              f"ID девушки: {data['your_id_lu']}\n"
                                                              f"ID подруги: {data['girl_id_lu']}")
    await state.finish()
    await message.answer("Спасибо за совместную работу! "
                         "Пожалуйста, ожидайте выплаты при "
                         "условии, что подруга заработает "
                         "20,000 монет за первую неделю", reply_markup = kb.to_catalog)

#FSM for registration girlfriend in LiveJoy
@dp.callback_query_handler(lambda call: call.data == 'register_girl_lj')
async def register_girl_lj(callback_query: types.CallbackQuery, state: FSMContext):
    await cl.FSMRegisterGirlLJ.your_nickname_lj.set()
    await bot.send_message(callback_query.from_user.id, text = "Введите свой ник")

@dp.message_handler(state = cl.FSMRegisterGirlLJ.your_nickname_lj)
async def load_your_nickname_lj(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['your_nickname_lj'] = message.text
    await cl.FSMRegisterGirlLJ.next()
    await message.reply("Введите ник подруги")

@dp.message_handler(state = cl.FSMRegisterGirlLJ.girl_nickname_lj)
async def load_girl_nickname_lj(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['girl_nickname_lj'] = message.text
        await bot.send_message(chat_id=cnfg.admin_tg_id,
                               text=f"Регистрация знакомой в LiveJoy\n"
                                    f"Telegram ID: @{message.from_user.username}\n"
                                    f"Ник девушки: {data['your_nickname_lj']}\n"
                                    f"Ник подруги: {data['girl_nickname_lj']}")
    await state.finish()
    await message.answer("Спасибо за совместную работу! "
                         "Пожалуйста, ожидайте выплаты при "
                         "условии, что подруга заработает "
                         "20,000 монет за первую неделю", reply_markup = kb.to_catalog)

#Registration girlfriend in FancyMe button
@dp.callback_query_handler(lambda call: call.data == 'register_girl_fancy')
async def register_girl_fency_page(c: types.CallbackQuery):
    await bot.edit_message_text(text = "Раздел в разработке. Пожалуйста, вернитесь назад",
                                chat_id = c.from_user.id,
                                message_id = c.message.message_id,
                                reply_markup = kb.to_catalog)

### 3 LivU/Yaar_catalog

#Registration LivU/Yaar page
@dp.callback_query_handler(lambda call: call.data == 'registration_lu')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.edit_message_text(text = "Регистрация",
                                chat_id = callback_query.from_user.id,
                                message_id = callback_query.message.message_id,
                                reply_markup = kb.LU_registr_kb)

#About rules in LivU/Yaar page
@dp.callback_query_handler(lambda call: call.data == 'Learning the rules_lu')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.edit_message_text(message_id = callback_query.message.message_id,
                                chat_id = callback_query.from_user.id,
                                text = "Изучение правил",
                                reply_markup = kb.LU_rules_kb)

#About finance in LivU/Yaar page
@dp.callback_query_handler(lambda call: call.data == 'Finance_lu')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id = callback_query.from_user.id,
                                message_id = callback_query.message.message_id,
                                text = "Финансы",
                                reply_markup = kb.LU_finance_kb)

#Profile verification in LivU/Yaar page
@dp.callback_query_handler(lambda call: call.data == 'Profile verification_lu')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id = callback_query.from_user.id,
                                message_id = callback_query.message.message_id,
                                text = "Существует 3 способа верификации аккаунта:\n"
                                       "1 Способ: Верификация в приложении\n"
                                       "2 Способ: Ручная проверка на сайте\n"
                                       "3 Способ: Ручная проверка через почту",
                                reply_markup = kb.LU_verification_kb)
#LivU/Yaar support page
@dp.callback_query_handler(lambda call: call.data == 'Support_lu')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id = callback_query.from_user.id,
                                message_id = callback_query.message.message_id,
                                text = "Верификация профиля",
                                reply_markup = kb.LU_support_kb)

#Go back to main page of LivU/Yaar
@dp.callback_query_handler(lambda call: call.data == 'to_LivUYaar_catalog')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id = callback_query.from_user.id,
                                text = "Выберите раздел, которого касается Ваш вопрос",
                                message_id = callback_query.message.message_id,
                                reply_markup = kb.LivUYaar_catalog)

#App interface of LivU/Yaar info page
@dp.callback_query_handler(lambda call: call.data == 'Application Interface_lu')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id = callback_query.from_user.id,
                                message_id = callback_query.message.message_id,
                                text = "Выберите раздел, которого касается Ваш вопрос",
                                reply_markup = kb.LU_rul_app_kb)

#LivU/Yaar tutorial page
@dp.callback_query_handler(lambda call: call.data == 'Tutorial_lu')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id = callback_query.from_user.id,
                                message_id = callback_query.message.message_id,
                                text = 'Обучающий курс',
                                reply_markup = kb.LU_rul_tutor_kb)

@dp.callback_query_handler(lambda call: call.data == 'enter data_lu')
async def process_callback(callback_query: types.CallbackQuery):
    await cl.FSMRegisterLU.GirlID_LU.set()
    await bot.send_message(callback_query.from_user.id, text = 'Введите свой ID')

@dp.message_handler(state=cl.FSMRegisterLU.GirlID_LU)
async def load_ID_LU(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['GirlID_LU'] = message.text
    await cl.FSMRegisterLU.next()
    await message.reply(text = "Нажмите \"Отправить свой контакт\". Перед этим убедитесь, что в настройках конфиденциальности у Вас открыта "
                               "возможность поиска по номеру телефона (Настройки - Конфиденциальность "
                               "- Номер телефона - Кто может найти меня по номеру. Укажите параметр \"Все\", "
                               "чтобы мы могли написать Вам, подтвердить регистрацию и добавить Вас в наш чат.",
                        reply_markup = kb.phone_nub_kb)

@dp.message_handler(state=cl.FSMRegisterLU.Phone_number, content_types=['contact'])
async def set_phone_number_lu(message: types.Message, state: FSMContext):
    if message.contact != None:
        async with state.proxy() as data:
            data['Phone_number'] = message.contact.phone_number
        await cl.FSMRegisterLU.next()
        await message.reply('Отправьте скриншот главной страницы (с аватором и ID)', reply_markup=ReplyKeyboardRemove())

#Problem with coins in LivU/Yaar
@dp.message_handler(content_types = ['photo'], state = cl.FSMRegisterLU.Main_page_LU)
async def load_mp_LU(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Main_page_LU'] = message.photo[-1].file_id
    await cl.FSMRegisterLU.next()
    await message.reply('Отправьте скриншот страницы с загруженными фото и видео')

@dp.message_handler(content_types = ['photo'], state = cl.FSMRegisterLU.Page_LU)
async def load_reg_LU(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Page_LU'] = message.photo[-1].file_id
    await cl.FSMRegisterLU.next()
    await message.reply('Если Вы из регионов РФ/ЛДНР прикрепите ещё две фотографии:')
    await bot.send_message(chat_id = message.from_user.id,
                           text = "3. Главная страница паспорта;",
                           reply_markup = kb.LU_registr_finish)

@dp.callback_query_handler(lambda call: call.data == 'LU_finish_st1', state="*")
async def process_callback1(c: types.CallbackQuery, state: FSMContext):
#    await GirlLU.send_to_admin(bot, cnfg.admin_tg_id, c.from_user.username)
    async with state.proxy() as data:
        await bot.send_message(chat_id=cnfg.admin_tg_id, text=f"Telegram ID: @{c.from_user.username}\n"
                                                         f"Номер телефона: {data['Phone_number']}\n" 
                                                         f"LivU/Yaar ID: {data['GirlID_LU']}")
        media_group = types.MediaGroup()
        media_group.attach_photo(photo=data['Main_page_LU'],  caption="1. Главная страница.")
        media_group.attach_photo(photo=data['Page_LU'], caption="2. Страница с загруженными фото и видео.")
        await bot.send_media_group(chat_id=cnfg.admin_tg_id, media=media_group)
    await state.finish()
    await bot.send_message(chat_id = c.from_user.id,
                           text = "Спасибо!\nОжидайте подтверждение профиля. "
                                  "Сейчас Вы можете приступить к изучению правил "
                                  "и регистрации в финансовой системе, чтобы получать выплаты",
                           reply_markup = kb.to_LivUYaar_catalog_kb)
    if datetime.now().hour < 9:
        lu_person_tmp_day0_list.append(c.from_user.id)
    else:
        lu_person_tmp_day1_list.append(c.from_user.id)
    lu_girl = LUPersons()
    print(f"Day0 {lu_person_tmp_day0_list}\nDay1: {lu_person_tmp_day1_list}")#test

@dp.message_handler(content_types = ['photo'], state = cl.FSMRegisterLU.Main_page_passports_LU)
async def load_reg_LU(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Main_page_passports_LU'] = msg.photo[-1].file_id
    await cl.FSMRegisterLU.next()
    await bot.send_message(chat_id = msg.from_user.id,
                           text = "4. Ваше селфи с паспортом.")


@dp.message_handler(content_types = ['photo'], state = cl.FSMRegisterLU.Selfie_LU)
async def load_reg_LU(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Selfie_LU'] = msg.photo[-1].file_id
        await bot.send_message(chat_id=cnfg.admin_tg_id, text=f"Telegram ID: @{msg.from_user.username}\n"
                                                         f"Номер телефона: {data['Phone_number']}\n"
                                                         f"LivU/Yaar ID: {data['GirlID_LU']}")
        media_group = types.MediaGroup()
        media_group.attach_photo(photo=data['Main_page_LU'], caption="1. Главная страница.")
        media_group.attach_photo(photo=data['Page_LU'], caption="2. Страница с загруженными фото и видео.")
        media_group.attach_photo(photo=data['Main_page_passports_LU'], caption="3. Главная страница паспорта.")
        media_group.attach_photo(photo=data['Selfie_LU'], caption="4. Селфи с паспортом.")
        await bot.send_media_group(chat_id=cnfg.admin_tg_id, media=media_group)
    await state.finish()
    await bot.send_message(chat_id = msg.from_user.id,
                           text="Спасибо!\nОжидайте подтверждение профиля. "
                                "Сейчас Вы можете приступить к изучению правил "
                                "и регистрации в финансовой системе, чтобы получать выплаты",
                           reply_markup = kb.to_LivUYaar_catalog_kb)
    if datetime.now().hour < 9:
        lu_person_tmp_day0_list.append(msg.from_user.id)
    else:
        lu_person_tmp_day1_list.append(msg.from_user.id)
    lu_girl = LUPersons()
    print(f"Day0 {lu_person_tmp_day0_list}\nDay1: {lu_person_tmp_day1_list}")#test

## 5 LivU/Yaar Profile verification
@dp.callback_query_handler(lambda call: call.data == 'coins_error_lu')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id = callback_query.from_user.id,
                                message_id = callback_query.message.message_id,
                                text = "Рабочая неделя длится с понедельника по воскресенье и "
                                       "заработанные за этот период монеты обнуляются в "
                                       "понедельник в 3 часа утра. Визуально монеты не "
                                       "отображаются в приложении на новой неделе (т.е. в "
                                       "3 часа ночи понедельника у Вас обнулятся монеты), "
                                       "но они будут видны в общем еженедельном отчёте. "
                                       "Еженедельный отчёт по заработанным монетам Вы сможете "
                                       "увидеть в среду в общей группе.",
                                reply_markup = kb.LU_toSupport)

#You have a fine in LivU/Yaar
@dp.callback_query_handler(lambda call: call.data == 'fine_error_lu')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id = callback_query.from_user.id,
                                message_id = callback_query.message.message_id,
                                text = "Не забывайте, в Поиске, звонке по стене Богинь, "
                                       "как и в первые 30 секунд приватного звонка, "
                                       "робот фиксирует все виды нарушений "
                                       "(После 30 секунд приватного звонка робот отключается). "
                                       "За нарушение правил будет наложен штраф. "
                                       "В поиске Вы можете лишь спросить «Привет, как дела?» "
                                       "или «Ты мне нравишься, давай пообщаемся/давай поиграем "
                                       "в привате». Штрафы возмещаются в процентном соотношении "
                                       "от недельной зарплаты. Первый штраф - 5%. Второй - 20%. "
                                       "Третий -50% от вашей недельной зарплаты. "
                                       "Четвёртый штраф - 100% и вплоть до удаления аккаунта.\n\n"
                                       + link(title = 'Обновите свои знания о Правилах работы в приложении LivU.',
                                              url = 'http://chatzen.tilda.ws/lerning-page-livu#rec418670299'),
                                parse_mode = "Markdown",
                                reply_markup = kb.LU_toSupport)

#You don`t have a salary in LivU/Yaar
@dp.callback_query_handler(lambda call: call.data == 'salary_error_lu')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                message_id=callback_query.message.message_id,
                                parse_mode="Markdown",
                                reply_markup=kb.LU_toSupport,
                                text = "Минимальное количество заработанных монет для выплаты "
                                       "зарплаты - 20,000. Оплата происходит в пятницу на Вашу "
                                       "карту. Например, рабочая неделя длилась с 1 января по 7 "
                                       "января. Отчёт за эту неделю вы увидите 10 января. Оплата "
                                       "произойдёт 12 января. Мы рекомендуем сделать запись "
                                       "экрана раздела доходов в воскресенье, перед сном (до "
                                       "3 часов утра понедельника), чтобы Вы могли сравнить "
                                       "заработанные монеты с отчётом.\n\n" +
                                       link(title = 'Более подробно читайте в разделе доходов в'
                                       ' обучающем материале',
                                            url = 'http://chatzen.tilda.ws/withdrawal#rec421600218'))


@dp.callback_query_handler(lambda call: call.data == 'Link card_lu')
async def process_callback(c: types.CallbackQuery):
    await cl.FSMPaymentInfoLU.LivID.set()
    await bot.send_message(chat_id = c.from_user.id, text = "Введите свой ID LivU/Yaar")

@dp.message_handler(state = cl.FSMPaymentInfoLU.LivID)
async def process_callback(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['LivID'] = msg.text
    await cl.FSMPaymentInfoLU.next()
    await bot.send_message(chat_id =msg.from_user.id, text = "Фамилия и Имя (на русском языке)")

@dp.message_handler(state = cl.FSMPaymentInfoLU.full_name)
async def process_callback(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['full_name'] = msg.text
    await cl.FSMPaymentInfoLU.next()
    await bot.send_message(chat_id = msg.from_user.id,
                           text = "Введите номер карты/номер телефона для СБП, или номер "
                                  "электронного кошелька")

@dp.message_handler(state = cl.FSMPaymentInfoLU.card_info)
async def process_callback(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['card_info'] = msg.text
    await bot.send_message(chat_id = cnfg.admin_tg_id,
                           text = f"Платежная информация девушки LivU\n"
                                  f"ID LivU: {data['LivID']}\n"
                                  f"Telegram ID: @{msg.from_user.username}\n"
                                  f"ФИ: {data['full_name']}\n"
                                  f"Реквизиты: {data['card_info']}")
    await state.finish()
    await bot.send_message(chat_id = msg.from_user.id,
                           text = "Спасибо!\n"
                                  "При достижении минимума заработанных монет (20,000) Вам "
                                  "будет переведена зарплата и предоставлен чек-квитанция по "
                                  "переводу.\nСейчас Вы можете вернуться назад.",
                           reply_markup = kb.to_LivUYaar_catalog_kb)

#FSM Additional problem in LivU
@dp.callback_query_handler(lambda call: call.data == 'No_option_lu')
async def registration_error_page_lu(callback_query: types.CallbackQuery, state: FSMContext):
    await cl.FSMAdditionalProblemLU.id_lu.set()
    await bot.send_message(callback_query.from_user.id, text = "Введите свой ID LivU")

@dp.message_handler(state = cl.FSMAdditionalProblemLU.id_lu)
async def load_sup_id_lu(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id_lu'] = message.text
    await cl.FSMAdditionalProblemLU.next()
    await message.reply(text = "Нажмите \"Отправить свой контакт\". Перед этим убедитесь, что в настройках конфиденциальности у Вас открыта "
                               "возможность поиска по номеру телефона (Настройки - Конфиденциальность "
                               "- Номер телефона - Кто может найти меня по номеру). Укажите параметр \"Все\", "
                               "чтобы мы могли написать Вам, подтвердить регистрацию и добавить Вас в наш чат.",
                        reply_markup = kb.phone_nub_kb)

@dp.message_handler(state = cl.FSMAdditionalProblemLU.phone_number, content_types=['contact'])
async def load_sup_phone_number_lu(message: types.Message, state: FSMContext):
    if message.contact != None:
        async with state.proxy() as data:
            data['phone_number'] = message.contact.phone_number
        await cl.FSMAdditionalProblemLU.next()
        await message.reply(text = "Коротко опишите проблему", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(state = cl.FSMAdditionalProblemLU.problem_text)
async def load_sup_problem_text_lu(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['problem_text'] = message.text
        await bot.send_message(chat_id = cnfg.admin_tg_id, text = f"Обращение в поддержку LivU\n"
                                                                  f"Telegram ID: @{message.from_user.username}\n"
                                                                  f"ID LivU: {data['id_lu']}\n"
                                                                  f"Номер телефона: {data['phone_number']}\n"
                                                                  f"Краткое описание проблемы: {data['problem_text']}")
    await state.finish()
    await message.answer("Обращение в поддержку принято. Ожидайте ответа Специалиста 🕒 . "
                         "Не создавайте новые запросы до тех пор, пока специалист не выйдет "
                         "на связь!", reply_markup = kb.to_LivUYaar_catalog_kb)

#Второй день после активации
@dp.callback_query_handler(lambda call: call.data == 'LU_persons_first_kb_yes')
async def process_callback(c: types.CallbackQuery):
    await bot.send_message(chat_id = c.from_user.id,
                           text = "Вы отлично справляетесь! Это оказалось не сложно, верно? Но это только начало! "
                                  "Опытные сотрудники могут заработать 20,000 за несколько часов работы! Мы рекомендуем "
                                  "ещё раз перечитать советы и хитрости от опытных сотрудников, применить их на практике"
                                  ", и уже через несколько недель начать зарабатывать по 150-200-300 долларов в неделю!")
    await bot.send_message(chat_id = c.from_user.id,
                           text = "Не забывайте про вознаграждения за активность! Чем выше Ваш уровень, тем больше бонус!"
                                  " Заходите в приложение ежедневно, заработайте минимум монет для получения бонуса, и "
                                  "активируйте его! Помимо этого, участвуйте в конкурсах, чтобы заработать дополнительные"
                                  " монеты, которые также будут переведены в Вашу зарплату")
    await bot.send_message(chat_id = c.from_user.id,
                           text = "Также, ещё раз перечитайте правила приложения LivU, чтобы избежать их нарушений, "
                                  "и не получить штраф!",
                           reply_markup = kb.LU_persons_first_yes_kb)

@dp.callback_query_handler(lambda call: call.data == 'LU_persons_first_kb_no')
async def process_callback(c: types.CallbackQuery):
    await bot.send_message(chat_id = c.from_user.id,
                           text = "Это совсем плохо( Некоторые Ваши коллеги-новички постарались, и за вчерашний день уже"
                                  " успели заработать свои первые 30 долларов, и их доход растёт! При внимательном "
                                  "прочтении и применении правил работы, Вы сможете также достаточно зарабатывать!\n\n"
                                  "Как и любой профиль в социальных сетях, профиль в LivU/Yaar необходимо раскрутить. "
                                  "Первые 1-2 недели Вам необходимо больше времени уделять приложению,"
                                  " и функции Поиска в нём.")

    await bot.send_message(chat_id = c.from_user.id,
                           text = "Вернитесь к чтению правил. Ваше задание на сегодня - изучить правила и зайдите в "
                                  "Поиск. Будьте милы. У Вас 5-15 секунд на то, чтобы заинтересовать собеседника, и "
                                  "перевести его в личный звонок. Позаботьтесь о красивом фоне Вашего рабочего места и "
                                  "хорошем освещении. У Вас должен быть ухоженный внешний вид, и хорошее настроение во "
                                  "время работы. Используйте яркие аксессуары. Серьги, браслеты и прочее. Такие мелочи "
                                  "запоминаются, и помогут Вам получить постоянных собеседников.\n\nБудьте благодарны "
                                  "пользователю за общение и подарки. Помимо этого, участвуйте в конкурсах, чтобы "
                                  "заработать дополнительные монеты, которые также будут переведены в Вашу зарплату!",
                           reply_markup = kb.first_day_lu_kb)

# 3.6 LivU/Yaar Support

### 4 LiveJoy catalog

#Registration page on LiveJoy
@dp.callback_query_handler(lambda call: call.data == 'registration_lj')
async def livejoy_registration_page(callback_query: types.CallbackQuery):
    await bot.edit_message_text(text = "Регистрация",
                                chat_id = callback_query.message.chat.id,
                                message_id = callback_query.message.message_id,
                                reply_markup = kb.LiveJoy_registration)

#Support page on LiveJoy
@dp.callback_query_handler(lambda call: call.data == 'Support_lj')
async def livejoy_support_page(callback_query: types.CallbackQuery):
    await bot.edit_message_text(text = "Поддержка",
                                chat_id = callback_query.message.chat.id,
                                message_id = callback_query.message.message_id,
                                reply_markup = kb.LiveJoy_support)

#Rules page on LiveJoy
@dp.callback_query_handler(lambda call: call.data == 'Learning the rules_lj')
async def livejoy_rules_page(callback_query: types.CallbackQuery):
    await bot.edit_message_text(text = "Изучение правил",
                                chat_id = callback_query.message.chat.id,
                                message_id = callback_query.message.message_id,
                                reply_markup = kb.LiveJoy_rules)

#Finance page on LiveJoy
@dp.callback_query_handler(lambda call: call.data == 'Finance_lj')
async def livejoy_finance_page(callback_query: types.CallbackQuery):
    await bot.edit_message_text(text = "Финансы",
                                chat_id = callback_query.message.chat.id,
                                message_id = callback_query.message.message_id,
                                reply_markup = kb.LiveJoy_finance)

#Back to rules page in LiveJoy
@dp.callback_query_handler(lambda call: call.data == 'back_to_rules_lj')
async def livejoy_back_to_rules_catalog(callback_query: types.CallbackQuery):
    await bot.edit_message_text(text = "Изучение правил",
                                chat_id = callback_query.message.chat.id,
                                message_id = callback_query.message.message_id,
                                reply_markup = kb.LiveJoy_rules)

## 4.1 LiveJoy registration

#Get invite lin in LiveJoy
@dp.callback_query_handler(lambda call: call.data == 'get_link_lj')
async def livejoy_registration_link_page(callback_query: types.CallbackQuery):
    sp = spider.Link()
    with open('parse_data.txt', 'r') as fh:
        urls = json.load(fh)
        sp.link = urls['link']
        sp.date = urls['date']
    print(sp.link)
    print(sp.date)
    await bot.edit_message_text(text = "Для продолжения зарегестрируйтесь" + link(' по этой ссылке',
                                            url = sp.link) + "\n\nПосле регистрации по ссылке верифицируйте профиль в приложении. У вас получилось?",
                                parse_mode = "Markdown",
                                chat_id = callback_query.message.chat.id,
                                message_id = callback_query.message.message_id,
                                reply_markup = kb.LiveJoy_registration_link)

#Successful verification in LiveJoy
@dp.callback_query_handler(lambda call: call.data == 'verify_good_lj')
async def livejoy_registration_link_good(callback_query: types.CallbackQuery):
    await bot.edit_message_text(text = "Спасибо за регистрацию! Пожалуйста, ожидайте уведомление "
                                       "в приложении. В течении суток мы проверим Ваш профиль и "
                                       "подтвердим его. Если Ваш профиль не подтвердили в течении "
                                       "суток, пожалуйста, обратитесь в раздел Поддержка подраздел "
                                       "«Я зарегистрировалась, но мой профиль не подтвердили»",
                                chat_id = callback_query.message.chat.id,
                                message_id = callback_query.message.message_id,
                                reply_markup = kb.to_LiveJoy_catalog_kb)
    if datetime.now().hour < 9:
        lj_person_tmp_day0_list.append(callback_query.from_user.id)
    else:
        lj_person_tmp_day1_list.append(callback_query.from_user.id)
    print(f"Day0 {lj_person_tmp_day0_list}\nDay1: {lj_person_tmp_day1_list}")#test

#FSM Unsuccessful verification in LiveJoy
@dp.callback_query_handler(lambda call: call.data == 'verify_bad_lj')
async def livejoy_registration_link_page(callback_query: types.CallbackQuery, state: FSMContext):
    await cl.FSMContactsLJ.email.set()
    await bot.send_message(callback_query.from_user.id, text = "Введите Ваш адрес электронной почты")

@dp.message_handler(state = cl.FSMContactsLJ.email)
async def load_reg_email_lj(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
    await cl.FSMContactsLJ.next()
    await message.reply(text = "Нажмите \"Отправить свой контакт\". Перед этим убедитесь, что в настройках конфиденциальности у Вас открыта "
                               "возможность поиска по номеру телефона (Настройки - Конфиденциальность "
                               "- Номер телефона - Кто может найти меня по номеру). Укажите параметр \"Все\", "
                               "чтобы мы могли написать Вам, подтвердить регистрацию и добавить Вас в наш чат.",
                        reply_markup = kb.phone_nub_kb)

@dp.message_handler(state = cl.FSMContactsLJ.phone_number, content_types=['contact'] )
async def load_reg_phone_number_lj(message: types.Message, state: FSMContext):
    if message.contact != None:
        async with state.proxy() as data:
            data['phone_number'] = message.contact.phone_number
            await bot.send_message(chat_id = cnfg.admin_tg_id, text = f"Telegram ID: @{message.from_user.username}\n"
                                                                      f"Email: {data['email']}\n"
                                                                      f"Номер телефона: {data['phone_number']}")
        await state.finish()
        await message.answer('Пожалуйста, ожидайте.', reply_markup=ReplyKeyboardRemove())
        await message.answer('Вам напишет наша поддержка', reply_markup = kb.to_LiveJoy_catalog_kb)
        if datetime.now().hour < 9:
            lj_person_tmp_day0_list.append(message.from_user.id)
        else:
            lj_person_tmp_day1_list.append(message.from_user.id)
        print(f"Day0 {lj_person_tmp_day0_list}\nDay1: {lj_person_tmp_day1_list}")  # test

## 4.2 LiveJoy finance

#FSM Problem with registration binance in LiveJoy
@dp.callback_query_handler(lambda call: call.data == 'binance_register_bad_lj')
async def livejoy_finance_binance_page(callback_query: types.CallbackQuery):
    await bot.edit_message_text(text = "Если по какой-то причине у Вас не получилось зарегистрироваться "
                                       "в системе Binance, то Вы можете использовать наши данные. И в "
                                       "день зарплаты мы сможем перечислить Вашу зарплату на Вашу "
                                       "банковскую карту. Введите в приложение LiveJoy:\n"
                                       "1NUu7teqy8Hc6FEMfshHTusSEsUckQLSye\n"
                                       "Balakin Sergey\n"
                                       "mr.sergeybalakin@gmail.com",
                                chat_id = callback_query.message.chat.id,
                                message_id = callback_query.message.message_id,
                                reply_markup = kb.LiveJoy_finance_binance)

@dp.callback_query_handler(lambda call: call.data == 'enter_card_number')
async def livejoy_finance_page(callback_query: types.CallbackQuery, state: FSMContext):
    await cl.FSMPaymentInfoLJ.nickname_lj.set()
    await bot.send_message(callback_query.from_user.id, text = "Введите свой Ник LiveJoy")

@dp.message_handler(state = cl.FSMPaymentInfoLJ.nickname_lj)
async def load_fin_nickname_lj(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['nickname_lj'] = message.text
    await cl.FSMPaymentInfoLJ.next()
    await message.reply("Фамилия и Имя (на русском языке)")

@dp.message_handler(state = cl.FSMPaymentInfoLJ.first_second_name)
async def load_fin_first_second_name_lj(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['first_second_name'] = message.text
    await cl.FSMPaymentInfoLJ.next()
    await message.reply("Введите номер карты/номер телефона для СБП, или номер электронного кошелька")

@dp.message_handler(state = cl.FSMPaymentInfoLJ.payment_card)
async def load_fin_card_lj(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['payment_card'] = message.text
        await bot.send_message(chat_id = cnfg.admin_tg_id, text = f"Проблемы с регистрацией Binance LiveJoy\n"
                                                                  f"Telegram ID: @{message.from_user.username}\n"
                                                                  f"Ник LiveJoy: {data['nickname_lj']}\n"
                                                                  f"Имя и фамилия: {data['first_second_name']}\n"
                                                                  f"Номер карты: {data['payment_card']}")
    await state.finish()
    await message.answer("Спасибо! При достижении минимума заработанных баллов (20,000) "
                        "Вам будет переведена зарплата и предоставлен чек-квитанция по "
                        "переводу. Сейчас Вы можете вернуться назад", reply_markup = kb.to_LiveJoy_catalog_kb)

## 4.3 LiveJoy rules

#App interface in LiveJoy
@dp.callback_query_handler(lambda call: call.data == 'interface_app_lj')
async def livejoy_rules_interface_app_page(callback_query: types.CallbackQuery):
    await bot.edit_message_text(text = "Интерфейс приложения",
                                chat_id = callback_query.message.chat.id,
                                message_id = callback_query.message.message_id,
                                reply_markup = kb.LiveJoy_rules_appinterface)

#Tutorial page in LiveJoy
@dp.callback_query_handler(lambda call: call.data == 'tutorial_lj')
async def livejoy_rules_interface_app_page(callback_query: types.CallbackQuery):
    await bot.edit_message_text(text = "Обучающий курс",
                                chat_id = callback_query.message.chat.id,
                                message_id = callback_query.message.message_id,
                                reply_markup = kb.LiveJoy_rules_tutorial)

## 4.4 LiveJoy_Support

#FSM Registration problem in LiveJoy
@dp.callback_query_handler(lambda call: call.data == 'registration_error_lj')
async def registration_error_page(callback_query: types.CallbackQuery, state: FSMContext):
    await cl.FSMSupportRegisterProblem.nickname_lj.set()
    await bot.send_message(callback_query.from_user.id, text = "Введите свой ник Livejoy")

@dp.message_handler(state = cl.FSMSupportRegisterProblem.nickname_lj)
async def load_sup_nickname_lj(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['nickname_lj'] = message.text
    await cl.FSMSupportRegisterProblem.next()
    await message.reply(text = "Нажмите \"Отправить свой контакт\". Перед этим убедитесь, что в настройках конфиденциальности у Вас открыта "
                               "возможность поиска по номеру телефона (Настройки - Конфиденциальность "
                               "- Номер телефона - Кто может найти меня по номеру). Укажите параметр \"Все\", "
                               "чтобы мы могли написать Вам, подтвердить регистрацию и добавить Вас в наш чат.",
                        reply_markup = kb.phone_nub_kb)

@dp.message_handler(state = cl.FSMSupportRegisterProblem.phone_number, content_types=['contact'])
async def load_sup_phone_number_lj(message: types.Message, state: FSMContext):
    if message.contact != None:
        async with state.proxy() as data:
            data['phone_number'] = message.contact.phone_number
        await cl.FSMSupportRegisterProblem.next()
        await message.reply(text = "Введите дату своей регистрации", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(state = cl.FSMSupportRegisterProblem.registration_data)
async def load_sup_registr_data_lj(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['registration_data'] = message.text
        await bot.send_message(chat_id = cnfg.admin_tg_id, text = f"Проблемы с верификацией LiveJoy\n"
                                                                  f"Telegram ID: @{message.from_user.username}\n"
                                                                  f"Ник в LiveJoy: {data['nickname_lj']}\n"
                                                                  f"Номер телефона: {data['phone_number']}\n"
                                                                  f"Дата регистрации: {data['registration_data']}")
    await state.finish()
    await message.answer("Обращение в поддержку принято. Ожидайте ответа Специалиста 🕒 . "
                         "Не создавайте новые запросы до тех пор, пока специалист не выйдет "
                         "на связь!", reply_markup = kb.to_LiveJoy_catalog_kb)

#FSM Else problems in LiveJoy
@dp.callback_query_handler(lambda call: call.data == 'else_error_lj')
async def else_error_lj_page(callback_query: types.CallbackQuery, state: FSMContext):
    await cl.FSMSupportAdditionalProblem.nickname_lj.set()
    await bot.send_message(callback_query.from_user.id, text = "Введите свой ник LiveJoy")

@dp.message_handler(state = cl.FSMSupportAdditionalProblem.nickname_lj)
async def load_sup_else_problem_lj(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['nickname_lj'] = message.text
    await cl.FSMSupportAdditionalProblem.next()
    await message.reply(text = "Нажмите \"Отправить свой контакт\". Перед этим убедитесь, что в настройках конфиденциальности у Вас открыта "
                               "возможность поиска по номеру телефона (Настройки - Конфиденциальность "
                               "- Номер телефона - Кто может найти меня по номеру). Укажите параметр \"Все\", "
                               "чтобы мы могли написать Вам, подтвердить регистрацию и добавить Вас в наш чат.",
                        reply_markup = kb.phone_nub_kb)

@dp.message_handler(state = cl.FSMSupportAdditionalProblem.phone_number, content_types=['contact'])
async def load_sup_add_phone_number_lj(message: types.Message, state: FSMContext):
    if message.contact != None:
        async with state.proxy() as data:
            data['phone_number'] = message.contact.phone_number
        await cl.FSMSupportAdditionalProblem.next()
        await message.reply(text = "Коротко опишите проблему", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(state = cl.FSMSupportAdditionalProblem.problem_short_description)
async def load_sup_else_description_problem_lj(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['problem_short_description'] = message.text
        await bot.send_message(chat_id = cnfg.admin_tg_id, text = f"Обращение в поддержку LiveJoy\n"
                                                                  f"Telegram ID: @{message.from_user.username}\n"
                                                                  f"Ник LiveJoy: {data['nickname_lj']}\n"
                                                                  f"Номер телефона: {data['phone_number']}\n"
                                                                  f"Краткое описанеи проблемы: {data['problem_short_description']}")
    await state.finish()
    await message.answer("Обращение в поддержку принято. Ожидайте ответа " 
                         "Специалиста 🕒. Не создавайте новые запросы "
                         "до тех пор, пока специалист не выйдет на связь!", reply_markup = kb.to_LiveJoy_catalog_kb)

#You have fine in LiveJoy
@dp.callback_query_handler(lambda call: call.data == 'fine_error_lj')
async def fine_error_lj_message(callback_query: types.CallbackQuery):
    await bot.edit_message_text(text =  "Одно из самых частых нарушений - Вас не видно "
                                        "собеседнику. Вы должны быть хорошо освещены. "
                                        "Убедитесь в том, что освещения достаточно "
                                        "для камеры вашего смартфона. Также, в случайных "
                                        "видеозвонках обязательно смотрите в камеру "
                                        "смартфона. При нарушении какого-либо из "
                                        "правил, ваши баллы будут вычтены. 1-е нарушение "
                                        "- вычет 2,000 баллов. 2-е нарушение - вычет "
                                        "5,000 баллов. 3-е нарушение - 10,000 баллов. "
                                        "4-е нарушение - списание всех баллов и блокировка "
                                        "аккаунта\n\n"
                                        + link('Обновите свои знания о Правилах работы в приложении LiveJoy',
                                               url = cnfg.url_livejoy_rules),
                                parse_mode = "Markdown",
                                chat_id = callback_query.message.chat.id,
                                message_id = callback_query.message.message_id,
                                reply_markup = kb.to_LiveJoy_catalog_kb)

#You don`t have a salary in LiveJoy
@dp.callback_query_handler(lambda call: call.data == 'salary_error_lj')
async def salary_error_lj_message(callback_query: types.CallbackQuery):
    await bot.edit_message_text(text =  "Минимальное количество заработанных баллов для " 
                                        "выплаты зарплаты - 20,000. Оплата происходит в "
                                        "промежутке с понедельника по среду на вашу карту." 
                                        " Например, рабочая неделя длилась с 1 января по 7 "
                                        "января. Оплата произойдёт 8-10 января\n\n"
                                        + link('Более подробно читайте в разделе доходов в обучающем материале',
                                               url = cnfg.url_salery_up),
                                parse_mode = "Markdown",
                                chat_id = callback_query.message.chat.id,
                                message_id = callback_query.message.message_id,
                                reply_markup = kb.to_LiveJoy_catalog_kb)

async def test_func(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id,
                           text = f"Message_time1 to user: {callback_query.from_user.id}")

@dp.callback_query_handler(lambda call: call.data == 'test_1')
async def test_2(callback_query: types.CallbackQuery):
    await distribution()

@dp.callback_query_handler(lambda call: call.data == 'second_day_successful')
async def second_day_successful_earn(c: types.CallbackQuery):
    await bot.send_message(c.from_user.id,
                           text = "Вы отлично справляетесь! Это оказалось не сложно, верно? Но это только "
                                  "начало! Опытные сотрудники могут заработать 20,000 за несколько часов "
                                  "работы! Мы рекомендуем ещё раз перечитать советы и хитрости от "
                                  "опытных сотрудников, применить их на практике, и уже через несколько "
                                  "недель начать зарабатывать по 150-200-300 долларов в неделю!")
    await bot.send_message(c.from_user.id,
                           text = "Не забывайте про бонусы! Чем больше Вы заработали баллов, тем больше бонус!\n\n"
                                  "Помимо этого, участвуйте в конкурсах, которые прописаны в чате акций, "
                                  "чтобы повысить Вашу зарплату!")
    await bot.send_message(c.from_user.id,
                           text = "Также, ещё раз перечитайте правила приложения LiveJoy, чтобы избежать "
                                  "их нарушений, и не получить штраф!",
                           reply_markup = kb.second_day_activ_successful_lj_kb)

@dp.callback_query_handler(lambda call: call.data == 'second_day_unsuccessful')
async def second_days_unsuccessful_earn(c: types.CallbackQuery):
    await bot.send_message(c.from_user.id,
                           text = "Это совсем плохо (Некоторые Ваши коллеги-новички постарались и за "
                                  "вчерашний день уже успели заработать свои первые 30 долларов и их "
                                  "доход растёт!\nПри внимательном прочтении и применении правил работы, "
                                  "Вы сможете также достаточно зарабатывать!\n\n Как и любой профиль в "
                                  "социальных сетях, профиль в LiveJoy необходимо раскрутить. Первые 1-2 "
                                  "недели Вам необходимо больше времени уделять приложению, и пребывать в нём")
    await bot.send_message(c.from_user.id,
                           text = "Вернитесь к чтению правил. Ваше задание на сегодня - изучить правила и "
                                  "зайти в Поиск. Будьте милы. У Вас 5-15 секунд на то, чтобы заинтересовать "
                                  "собеседника и перевести его в личный звонок. Позаботьтесь о красивом фоне "
                                  "Вашего рабочего места и хорошем освещении. У Вас должен быть ухоженный внешний "
                                  "вид и хорошее настроение во время работы. Используйте яркие аксессуары. Серьги, "
                                  "браслеты и прочее. Такие мелочи запоминаются и помогут Вам получить постоянных "
                                  "собеседников. Будьте благодарны пользователю за общение и подарки. Помимо этого, "
                                  "участвуйте в конкурсах, которые прописаны в чате акций, чтобы повысить Вашу зарплату!",
                           reply_markup = kb.second_day_activ_back_to_catalog_lj_kb)

async def distribution():
    global bot
    lu_persons = LUPersons()
    lj_persons = LJGirls()

    await lu_persons.read(cnfg.lu_database)
    await lu_persons.to_work(bot)
    await lu_persons.write(cnfg.lu_database)

    await lj_persons.read(cnfg.lj_database)
    await lj_persons.lj_work(bot)
    await lj_persons.write(cnfg.lj_database)

async def list_update():
    lu_persons = LUPersons()
    lj_persons = LJGirls()

    await lu_persons.read(cnfg.lu_database)
    for elem in lu_person_tmp_day0_list:
        if await lu_persons.check_id(elem) == 0:
            lu_persons.lu_day_0_list.append(elem)
    print(f"LU::::::::::::::::Current ID Day0: {lu_persons.lu_day_0_list}")
    lu_person_tmp_day0_list.clear()
    for elem in lu_person_tmp_day1_list:
        if await lu_persons.check_id(elem) == 0:
            lu_persons.lu_day_1_list.append(elem)
    print(f"LU::::::::::::::::Current ID Day1: {lu_persons.lu_day_1_list}")
    lu_person_tmp_day1_list.clear()
    await lu_persons.write(cnfg.lu_database)

    await lj_persons.read(cnfg.lj_database)
    for elem in lj_person_tmp_day0_list:
        if await lj_persons.check_id(elem) == 0:
            lj_persons.lj_day0_list.append(elem)
    print(f"LJ::::::::::::::::Current ID Day0: {lj_persons.lj_day0_list}")
    lj_person_tmp_day0_list.clear()
    for elem in lj_person_tmp_day1_list:
        if await lj_persons.check_id(elem) == 0:
            lj_persons.lj_day1_list.append(elem)
    print(f"LJ::::::::::::::::Current ID Day1: {lj_persons.lj_day1_list}")
    lj_person_tmp_day1_list.clear()
    await lj_persons.write(cnfg.lj_database)

async def check_person_list():
    if len(lu_person_tmp_day0_list) >= 1 or len(lu_person_tmp_day1_list) >= 1 or len(lj_person_tmp_day0_list) >= 1 or len(lj_person_tmp_day1_list) >= 1:
        await list_update()

async def parse_inv_link():
    parsing_data = spider.Link()
    await spy.parse_link()
    if os.path.exists('parse_data.txt') == False or os.stat('parse_data.txt').st_size == 0:
        with open('parse_data.txt', 'w') as fh:
            json.dump(parsing_data, fh, cls=spider.SpiderEncoder, indent=4)
    with open('parse_data.txt', 'r') as fh:
        urls = json.load(fh)
        parsing_data.link = urls['link']
        parsing_data.date = urls['date']
    date_fin = datetime.strptime(parsing_data.date, "%Y-%m-%d %H:%M:%S")
    date_fin += timedelta(minutes=2)
    scheduler.add_job(parse_inv_link, 'date', run_date=date_fin)
    print(parsing_data.link)
    print(parsing_data.date)

async def on_startup(self):
    await parse_inv_link()
    scheduler.print_jobs()

if __name__ == '__main__':
    scheduler.add_job(distribution, 'cron', day='*', hour=9, minute=00, jitter=120)
    scheduler.add_job(check_person_list, 'interval', seconds=30)
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)
