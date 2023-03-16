from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import config as cnfg
from aiogram.utils.markdown import text, hlink, link

#Language select keyboard
import config


language_kb = InlineKeyboardMarkup()
language_kb.add(InlineKeyboardButton("English", callback_data='en'))
language_kb.add(InlineKeyboardButton("Русский", callback_data='ru'))
language_kb.add(InlineKeyboardButton("Українська", callback_data='ua'))

#Back to english catalog button
back_en = InlineKeyboardMarkup()
back_en.add(InlineKeyboardButton("Go back", callback_data='go_back'))

phone_nub_kb = ReplyKeyboardMarkup(resize_keyboard=True)
phone_nub_kb.add(KeyboardButton("Отправить свой контакт", request_contact=True))

#Back to ukrainian catalog button
back_ua = InlineKeyboardMarkup()
back_ua.add(InlineKeyboardButton("Повернутися назад", callback_data = 'go_back_ua'))

#Back to russian catalog button
to_catalog = InlineKeyboardMarkup()
to_catalog_Button = InlineKeyboardButton("Вернутся назад", callback_data = 'to_catalog')
to_catalog.add(to_catalog_Button)

test_kb = InlineKeyboardMarkup()
test_bt = InlineKeyboardButton('Запланировать', callback_data='test_1')
test_kb.add(test_bt)
test_kb.add(to_catalog_Button)

#Main menu keyboard
main_catalog = InlineKeyboardMarkup()
main_catalog.add(InlineKeyboardButton("LivU/Yaar", callback_data='LU'))
main_catalog.add(InlineKeyboardButton("LiveJoy", callback_data='LJ'))
main_catalog.add(InlineKeyboardButton("FancyMe", callback_data = 'FancyMe'))
main_catalog.add(InlineKeyboardButton("Зарегистрировать подругу", callback_data = 'register_girl'))
main_catalog.add(InlineKeyboardButton("О нас", url=cnfg.url_about_us))
main_catalog.add(InlineKeyboardButton("Выбор языка", callback_data = 'Language_selection'))

#Register girl page keyboard
register_girl_kb = InlineKeyboardMarkup()
register_girl_kb.add(InlineKeyboardButton("LivU/Yaar", callback_data = 'register_girl_lu'))
register_girl_kb.add(InlineKeyboardButton("LiveJoy",callback_data = 'register_girl_lj'))
register_girl_kb.add((InlineKeyboardButton("FancyMe", callback_data = 'register_girl_fancy')))
register_girl_kb.add(to_catalog_Button)

#LivUYaar catalog keyboard
LivUYaar_catalog = InlineKeyboardMarkup()
LivUYaar_catalog.add(InlineKeyboardButton("Регистрация", callback_data = 'registration_lu'))
LivUYaar_catalog.add(InlineKeyboardButton("Изучение правил", callback_data = 'Learning the rules_lu'))
LivUYaar_catalog.add(InlineKeyboardButton("Финансы", callback_data = 'Finance_lu'))
LivUYaar_catalog.add(InlineKeyboardButton("Верификация профиля", callback_data = 'Profile verification_lu'))
LivUYaar_catalog.add(InlineKeyboardButton("Поддержка", callback_data = 'Support_lu'))
LivUYaar_catalog.add(InlineKeyboardButton("Новости и акции LivU", url = cnfg.url_news_in_app_lu))
LivUYaar_catalog.add(to_catalog_Button)

#LiveJoy catalog keyboard
LiveJoy_catalog = InlineKeyboardMarkup()
LiveJoy_catalog.add(InlineKeyboardButton("Регистрация", callback_data = 'registration_lj'))
LiveJoy_catalog.add(InlineKeyboardButton("Изучение правил", callback_data = 'Learning the rules_lj'))
LiveJoy_catalog.add(InlineKeyboardButton("Финансы", callback_data = 'Finance_lj'))
LiveJoy_catalog.add(InlineKeyboardButton("Поддержка", callback_data = 'Support_lj'))
LiveJoy_catalog.add(InlineKeyboardButton("Новости и акции приложения", url = cnfg.url_news_in_app_lj))
LiveJoy_catalog.add(to_catalog_Button)

#Back to LiveJoy button
to_LiveJoy_catalog_kb = InlineKeyboardMarkup()
to_LiveJoy_catalog_btn = InlineKeyboardButton("Вернуться назад", callback_data = 'LiveJoy')
to_LiveJoy_catalog_kb.add(to_LiveJoy_catalog_btn)

#Back to LivU/Year button
to_LivU_catalog_kb = InlineKeyboardMarkup()
to_LivU_catalog_btn = InlineKeyboardButton("Вернуться назад", callback_data = 'LivU/Yaar')
to_LivU_catalog_kb.add(to_LivU_catalog_btn)

#LiveJoy registration keyboard
LiveJoy_registration = InlineKeyboardMarkup()
LiveJoy_registration.add(InlineKeyboardButton("Как зарегестрироваться", url = cnfg.url_how_registr_lj))
LiveJoy_registration.add(InlineKeyboardButton("Запросить ссылку", callback_data = 'get_link_lj'))
LiveJoy_registration.add(to_LiveJoy_catalog_btn)

#LiveJoy registration link keyboard
LiveJoy_registration_link = InlineKeyboardMarkup()
LiveJoy_registration_link.add(InlineKeyboardButton("Я успешно зарегистрировалась", callback_data = 'verify_good_lj'))
LiveJoy_registration_link.add(InlineKeyboardButton("Проблемы с верификацией", callback_data = 'verify_bad_lj'))

#LiveJoy finance keyboard
LiveJoy_finance = InlineKeyboardMarkup()
LiveJoy_finance.add(InlineKeyboardButton("Рабочая неделя и выплата", url = cnfg.url_working_week_and_pay_lj))
LiveJoy_finance.add(InlineKeyboardButton("Метод выплаты - Binance", url = cnfg.url_binance_lj))
LiveJoy_finance.add(InlineKeyboardButton("Проблемы с Binance", callback_data = 'binance_register_bad_lj'))
LiveJoy_finance.add(to_LiveJoy_catalog_btn)

#LiveJoy finance binance register keyboard
LiveJoy_finance_binance = InlineKeyboardMarkup()
LiveJoy_finance_binance.add(InlineKeyboardButton("Куда вводить эту информацию", url = cnfg.url_where_put_info_lj))
LiveJoy_finance_binance.add(InlineKeyboardButton("Привязать карту", callback_data = 'enter_card_number'))
LiveJoy_finance_binance.add(to_LiveJoy_catalog_btn)

#LiveJoy rules keyboard
LiveJoy_rules = InlineKeyboardMarkup()
LiveJoy_rules.add(InlineKeyboardButton("Интерфейс приложения", callback_data = 'interface_app_lj'))
LiveJoy_rules.add(InlineKeyboardButton("Обучающий курс", callback_data = 'tutorial_lj'))
LiveJoy_rules.add(to_LiveJoy_catalog_btn)
LiveJoy_back_to_rules_kb = InlineKeyboardMarkup()
LiveJoy_back_to_rules_bt = InlineKeyboardButton("Вернуться назад", callback_data = 'back_to_rules_lj')
LiveJoy_back_to_rules_kb.add(LiveJoy_back_to_rules_bt)

#LiveJoy rules interface app keyboard
LiveJoy_rules_appinterface = InlineKeyboardMarkup()
LiveJoy_rules_appinterface.add(InlineKeyboardButton("Личный кабинет - Оглавление", url = cnfg.url_personal_page_lj))
LiveJoy_rules_appinterface.add(InlineKeyboardButton("Пользователи онлайн", url = cnfg.url_users_online_lj))
LiveJoy_rules_appinterface.add(InlineKeyboardButton("Случайный видеочат", url = cnfg.url_random_videochat_lj))
LiveJoy_rules_appinterface.add(InlineKeyboardButton("История звонков", url = cnfg.url_call_history_lj))
LiveJoy_rules_appinterface.add(InlineKeyboardButton("Мой профиль", url = cnfg.url_my_profile_lj))
LiveJoy_rules_appinterface.add(InlineKeyboardButton("Мои доходы", url = cnfg.url_my_income_lj))
LiveJoy_rules_appinterface.add(InlineKeyboardButton("Сообщения", url = cnfg.url_message_lj))
LiveJoy_rules_appinterface.add(LiveJoy_back_to_rules_bt)

#LiveJoy rules tutorial keyboard
LiveJoy_rules_tutorial = InlineKeyboardMarkup()
LiveJoy_rules_tutorial.add(InlineKeyboardButton("Об основных задачах", url = cnfg.url_general_tasks_lj))
LiveJoy_rules_tutorial.add(InlineKeyboardButton("О типах звонков", url = cnfg.url_call_types_lj))
LiveJoy_rules_tutorial.add(InlineKeyboardButton("О видах подарков", url = cnfg.url_presents_types_lj))
LiveJoy_rules_tutorial.add(InlineKeyboardButton("О рейтинговой системе", url = cnfg.url_rating_system_lj))
LiveJoy_rules_tutorial.add(InlineKeyboardButton("Об оплате", url = cnfg.url_about_payment_lj))
LiveJoy_rules_tutorial.add(InlineKeyboardButton("О правилах", url = cnfg.url_about_rules_lj))
LiveJoy_rules_tutorial.add(InlineKeyboardButton("О бонусной системе", url = cnfg.url_bonus_system_lj))
LiveJoy_rules_tutorial.add(InlineKeyboardButton("Советы от опытных сотрудников", url = cnfg.url_secrets_and_tips_lj))
LiveJoy_rules_tutorial.add(InlineKeyboardButton("О контенте 18+", url = cnfg.url_adult_content_lj))
LiveJoy_rules_tutorial.add(InlineKeyboardButton("О бонусах", url = cnfg.url_about_bonus_lj))
LiveJoy_rules_tutorial.add(InlineKeyboardButton("О штрафах", url = cnfg.url_about_fine_lj))
LiveJoy_rules_tutorial.add(InlineKeyboardButton("О почасовой оплате", url = cnfg.url_hourly_rate_lj))
LiveJoy_rules_tutorial.add(LiveJoy_back_to_rules_bt)

#LiveJoy Support keyboard
LiveJoy_support = InlineKeyboardMarkup()
LiveJoy_support.add(InlineKeyboardButton("Профиль не подтвердили", callback_data = 'registration_error_lj'))
LiveJoy_support.add(InlineKeyboardButton("Мне пришёл штраф", callback_data = 'fine_error_lj'))
LiveJoy_support.add(InlineKeyboardButton("Мне не пришла зарплата", callback_data = 'salary_error_lj'))
LiveJoy_support.add(InlineKeyboardButton("Нет нужного варианта", callback_data = 'else_error_lj'))
LiveJoy_support.add(to_LiveJoy_catalog_btn)

to_LivUYaar_catalog_btn = InlineKeyboardButton("Вернуться назад", callback_data = 'to_LivUYaar_catalog')
to_LivUYaar_catalog_kb = InlineKeyboardMarkup()
to_LivUYaar_catalog_kb.add(to_LivUYaar_catalog_btn)


to_LivUYaar_first_btn = InlineKeyboardButton("Вернуться к изучению правил или обратиться в поддержку",
                                       callback_data='to_LivUYaar_first')

to_LivUYaar_first_kb = InlineKeyboardMarkup()
to_LivUYaar_first_kb.add(to_LivUYaar_first_btn)

#LivUYaar registration keyboard
LU_registr_kb = InlineKeyboardMarkup()
LU_registr_kb.add(InlineKeyboardButton("Как зарегистрироваться", url = config.url_registr_lu))
LU_registr_kb.add(InlineKeyboardButton("Ввести данные", callback_data = 'enter data_lu'))
LU_registr_kb.add(to_LivUYaar_catalog_btn)

#LivUYaar rules keyboard
LU_rules_kb = InlineKeyboardMarkup()
LU_rules_kb.add(InlineKeyboardButton("Интерфейс приложения", callback_data = 'Application Interface_lu'))
LU_rules_kb.add(InlineKeyboardButton("Обучающий курс", callback_data = 'Tutorial_lu'))
LU_rules_kb.add(to_LivUYaar_catalog_btn)

LU_rul_app_kb = InlineKeyboardMarkup()
LU_rul_app_kb.add(InlineKeyboardButton("Личный кабинет", url = config.url_account_lu))
LU_rul_app_kb.add(InlineKeyboardButton("Как посмотреть заработанные монеты", url = config.url_earned_coins_lu))
LU_rul_app_kb.add(InlineKeyboardButton("Стоимость звонка и уровень стримера", url = config.url_cost_and_level_lu))  #callback_data='Cost and level_lu'
LU_rul_app_kb.add(InlineKeyboardButton("Рабочая неделя и минимум", url = config.url_ww_and_min_lu))    #callback_data='Working week and minimum_lu'
LU_rul_app_kb.add(InlineKeyboardButton("Вернутся назад", callback_data = 'Learning the rules_lu'))

LU_rul_tutor_kb = InlineKeyboardMarkup()
LU_rul_tutor_kb.add(InlineKeyboardButton("О типах звонков", url = config.url_call_types_lu)) #callback_data='call types_lu'
LU_rul_tutor_kb.add(InlineKeyboardButton("О начале работы", url = config.url_turn_to_lu))#callback_data='turn-to_lu'
LU_rul_tutor_kb.add(InlineKeyboardButton("Об алгоритме работы в поиске", url = config.url_search_lu))#callback_data='search_lu'
LU_rul_tutor_kb.add(InlineKeyboardButton("О цели Поиска и Приватного звонка", url = config.url_search_and_call_lu ))#callback_data='search and call_lu'
LU_rul_tutor_kb.add(InlineKeyboardButton("О разделе сообщений", url = config.url_message_section_lu))#callback_data='message section_lu'
LU_rul_tutor_kb.add(InlineKeyboardButton("О списке друзей", url = config.url_Friend_list_lu))#callback_data='Friend list_lu'
LU_rul_tutor_kb.add(InlineKeyboardButton("О чёрном списке", url = config.url_black_list_lu))#callback_data='black list_lu'
LU_rul_tutor_kb.add(InlineKeyboardButton("О советах от опытных сотрудников", url = config.url_secrets_and_tips_lu))# callback_data='secrets and tips_lu'
LU_rul_tutor_kb.add(InlineKeyboardButton("О контенте 18+", url = config.url_adult_content_lu))#callback_data='adult content_lu'
LU_rul_tutor_kb.add(InlineKeyboardButton("О шаблонах сообщений", url = config.url_message_templates_lu))#callback_data='message templates_lu'
LU_rul_tutor_kb.add(InlineKeyboardButton("О вознаграждениях за активность", url = config.url_reward_lu))#callback_data='reward_lu'
LU_rul_tutor_kb.add(InlineKeyboardButton("О бонусах и подарках", url = config.url_bonuses_and_gifts_lu))#callback_data='bonuses and gifts_lu'
LU_rul_tutor_kb.add(InlineKeyboardButton("О конкурсах", url = config.url_contests_lu))#callback_data='contests_lu'
LU_rul_tutor_kb.add(InlineKeyboardButton("О штрафах", url = config.url_fines_lu))#callback_data='fines_lu'
LU_rul_tutor_kb.add(InlineKeyboardButton("Об итоге получения обучения", url = config.url_important_points_lu))#callback_data='important points_lu'
LU_rul_tutor_kb.add(InlineKeyboardButton("Вернутся назад", callback_data = 'Learning the rules_lu'))#

#LivUYaar finance keyboard
LU_finance_kb = InlineKeyboardMarkup()
LU_finance_kb.add(InlineKeyboardButton("Рабочая неделя и выплата", url = config.url_working_week_and_pay)) #callback_data='Working week and pay_lu
LU_finance_kb.add(InlineKeyboardButton("Метод выплаты", url = config.url_payment_method_lu)) #callback_data='Payout Method_lu'
LU_finance_kb.add(InlineKeyboardButton("Привязать карту", callback_data = 'Link card_lu'))
LU_finance_kb.add(to_LivUYaar_catalog_btn)

#LivUYaar verification keyboard
LU_verification_kb = InlineKeyboardMarkup()
LU_verification_kb.add(InlineKeyboardButton("Детальнее о верификации", url = config.url_verification_methods_lu  )) #callback_data='verification methods_lu'
LU_verification_kb.add(InlineKeyboardButton("Первый способ", url = config.url_first_verif_lu))#callback_data='first_verif_lu'))
LU_verification_kb.add(InlineKeyboardButton("Второй способ", url = config.url_second_verif_lu))#callback_data='second_verif_lu'))
LU_verification_kb.add(InlineKeyboardButton("Третий способ", url = config.url_third_verif_lu)) #callback_data='third_verif_lu'))
LU_verification_kb.add(to_LivUYaar_catalog_btn)

#LivUYaar Support keyboard
LU_support_kb = InlineKeyboardMarkup()
LU_support_kb.add(InlineKeyboardButton("Не отображаются монеты", callback_data = 'coins_error_lu'))
LU_support_kb.add(InlineKeyboardButton("Мне пришёл штраф", callback_data = 'fine_error_lu'))
LU_support_kb.add(InlineKeyboardButton("Мне не пришла зарплата", callback_data = 'salary_error_lu'))
LU_support_kb.add(InlineKeyboardButton("Нет нужного варианта", callback_data = 'No_option_lu'))
LU_support_kb.add(to_LivUYaar_catalog_btn)

LU_toSupport = InlineKeyboardMarkup()
LU_toSupport.add(to_LivUYaar_catalog_btn)

LU_registr_finish = InlineKeyboardMarkup()
LU_registr_finish.add(InlineKeyboardButton("Завершить", callback_data='LU_finish_st1'))

LU_persons_sat_kb = InlineKeyboardMarkup()
LU_persons_sat_kb.add(InlineKeyboardButton("Привязать карту", callback_data='Link card_lu'))
LU_persons_sat_kb.add(InlineKeyboardButton("Вернуться в Главное меню", callback_data='ru'))

LU_persons_second_kb = InlineKeyboardMarkup()
LU_persons_second_kb.add(InlineKeyboardButton("Зарегистрировать подругу", callback_data='register_girl'))
LU_persons_second_kb.add(InlineKeyboardButton("Вернуться в Главное меню", callback_data='LivU/Yaar'))

LU_persons_first_kb = InlineKeyboardMarkup()
LU_persons_first_kb.add(InlineKeyboardButton("Да", callback_data='LU_persons_first_kb_yes'))
LU_persons_first_kb.add(InlineKeyboardButton("Нет", callback_data='LU_persons_first_kb_no'))

first_day_lu_kb = InlineKeyboardMarkup()
first_day_lu_kb.add(InlineKeyboardButton("К правилам или обратиться в поддержку", callback_data = 'LivU/Yaar'))

second_day_activ_lj_kb = InlineKeyboardMarkup()
second_day_activ_lj_kb.add(InlineKeyboardButton("Да", callback_data='second_day_successful'))
second_day_activ_lj_kb.add(InlineKeyboardButton("Нет", callback_data='second_day_unsuccessful'))


second_day_activ_successful_lj_kb = InlineKeyboardMarkup()
second_day_activ_successful_lj_kb.add(InlineKeyboardButton("Советы и хитрости", url = cnfg.url_secrets_and_tips_lj))
second_day_activ_successful_lj_kb.add(InlineKeyboardButton("Бонусы", url = cnfg.url_bonus_system_lj))
second_day_activ_successful_lj_kb.add(InlineKeyboardButton("Штрафы", url = cnfg.url_about_fine_lj))
second_day_activ_successful_lj_kb.add(InlineKeyboardButton("Задать вопрос", callback_data = 'Support_lj'))
second_day_activ_successful_lj_kb.add(InlineKeyboardButton("Вернуться к изучению правил", callback_data = 'Learning the rules_lj'))

LU_persons_first_yes_kb = InlineKeyboardMarkup()
LU_persons_first_yes_kb.add(InlineKeyboardButton("Советы и хитросты", url=config.url_secrets_and_tips_lu))
LU_persons_first_yes_kb.add(InlineKeyboardButton("Вознаграждения за активность", url=config.url_reward_lu))
LU_persons_first_yes_kb.add(InlineKeyboardButton("Еженедельные конкурсы", url=config.url_contests_lu))
LU_persons_first_yes_kb.add(InlineKeyboardButton("Штрафы", url=config.url_fines_lu))
LU_persons_first_yes_kb.add(InlineKeyboardButton("Задать вопрос", callback_data='Support_lu'))
LU_persons_first_yes_kb.add(InlineKeyboardButton("Вернуться к изучению правил", callback_data='Learning the rules_lu'))

second_day_activ_back_to_catalog_lj_kb = InlineKeyboardMarkup()
second_day_activ_back_to_catalog_lj_kb.add(InlineKeyboardButton("К правилам или обратиться в поддержку", callback_data = 'LiveJoy'))

third_day_activ_lj_kb = InlineKeyboardMarkup()
third_day_activ_lj_kb.add(InlineKeyboardButton("Зарегестрировать подругу", callback_data = 'register_girl'))
third_day_activ_lj_kb.add(to_LiveJoy_catalog_btn)

every_sathurday_message_lj = InlineKeyboardMarkup()
every_sathurday_message_lj.add(InlineKeyboardButton("Финансы", callback_data = 'Finance_lj'))
every_sathurday_message_lj.add(to_LiveJoy_catalog_btn)