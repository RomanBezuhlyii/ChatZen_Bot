from aiogram import Bot
import keyboards as kb
import datetime
import os
import config as cnfg
import json

class LUPersons:
    lu_day_0_list = list()
    lu_day_1_list = list()
    lu_day_2_list = list()
    lu_next_saturday_list = list()

    async  def to_work(self, bot: Bot):
            # Обработка субботы
            if datetime.datetime.today().weekday() == 5:
                for person in self.lu_next_saturday_list:
                    await bot.send_message(chat_id=person, text="Осталось всего пару дней до конца отчётной недели! "
                                                                "А впереди законные выходные, звонков будет много! Самое "
                                                                "время "
                                                                "поработать и получить свою первую зарплату!\nВ понедельник"
                                                                "в 03:00 будет обнуление монет. Если получилось так, "
                                                                "что Вы не "
                                                                "успеете заработать минимум - 20,000 монет, то монеты "
                                                                "перенесутся "
                                                                "на следующую неделю, и Вы сможете дособирать их. "
                                                                "Собирать минимум "
                                                                "можно не более трёх недель.\n\nУбедитесь, что Вы не "
                                                                "забили сообщить "
                                                                "нам номер банковской карты/электронного кошелька.",
                                           reply_markup=kb.LU_persons_sat_kb)
                self.lu_next_saturday_list.clear()

            # Обработка день два
            for person in self.lu_day_2_list:
                await bot.send_message(chat_id=person, text="Приветствуем! Сегодня третий день нашей совместной работы! "
                                                            "Мы очень рады видеть Вас в нашей команде, и надеемся на Ваш высокий "
                                                            "заработок! Надеемся, что Вы получаете удовольствие от работы, и Вы"
                                                            " стремитесь зарабатывать еженедельно не менее 300 долларов.")

                await bot.send_message(chat_id=person, text="Позаботьтесь о красивом фоне Вашего рабочего места и хорошем "
                                                            "освещении. У Вас должен быть ухоженный внешний вид, и хорошее "
                                                            "настроение во время работы. Используйте яркие аксессуары - серьги, "
                                                            "браслеты и прочее. Такие мелочи запоминаются, и помогут Вам получить"
                                                            " постоянных собеседников. Будьте благодарны пользователю за общение "
                                                            "и подарки.")

                await bot.send_message(chat_id=person,
                                       text="Также, мы предлагаем Вам дополнительный заработок! Рекомендуйте нас"
                                            " своей знакомой или подруге, помогите ей зарегистрироваться, "
                                            "объясните ей правила и получите процент от её заработка в качестве"
                                            " бонуса! Бонус выплачивается если, подруга вышла на минимум в "
                                            "течении первой недели.",
                                       reply_markup=kb.LU_persons_second_kb)

            self.lu_next_saturday_list.extend(self.lu_day_2_list)
            self.lu_day_2_list.clear()

            for person in self.lu_day_1_list:
                await bot.send_message(chat_id=person,
                                       text="Приветствуем! Вас можно поздравить? Вы заработали свои первые 5,000 монет?",
                                       reply_markup=kb.LU_persons_first_kb)

            self.lu_day_2_list.extend(self.lu_day_1_list)
            self.lu_day_1_list.clear()

            self.lu_day_1_list.extend(self.lu_day_0_list)
            self.lu_day_0_list.clear()

    async def write(self,filename):
        with open(filename,'w') as fh:
            json.dump(self,fh,cls=LUPersonsEncoder, indent=4)

    async def read(self, filename):
        if os.path.exists(cnfg.lu_database) == False or os.stat(cnfg.lu_database).st_size == 0:
            await self.write(filename)
        with open(filename, 'r') as fh:
            girl = json.load(fh)
            self.lu_day_0_list = girl['lu_day_0_list']
            self.lu_day_1_list = girl['lu_day_1_list']
            self.lu_day_2_list = girl['lu_day_2_list']
            self.lu_next_saturday_list = girl['lu_next_saturday_list']

    async def check_id(self,id):
        if self.lu_day_0_list.count(id) > 0:
            return 1
        elif self.lu_day_1_list.count(id) > 0:
            return 1
        elif self.lu_day_2_list.count(id) > 0:
            return 1
        elif self.lu_next_saturday_list.count(id) > 0:
            return 1
        else:
            return 0

class LUPersonsEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o,LUPersons):
            return {'lu_day_0_list': o.lu_day_0_list,
                    'lu_day_1_list': o.lu_day_1_list,
                    'lu_day_2_list': o.lu_day_2_list,
                    'lu_next_saturday_list': o.lu_next_saturday_list}
        return super().default(o)