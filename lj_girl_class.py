from aiogram import Bot
import keyboards as kb
import datetime
import os
import config as cnfg
import json

class LJGirls:
    lj_day0_list = list()
    lj_day1_list = list()
    lj_day2_list = list()
    lj_every_saturday_list = list()

    async def lj_work(self,bot: Bot):
        if datetime.datetime.today().weekday() == 5:
            for elem in self.lj_every_saturday_list:
                    await bot.send_message(chat_id = elem,
                                           text = "Осталось всего пару дней до конца отчётной недели! А впереди выходные, звонков будет много! Самое время "
                                                "поработать и получить свою первую зарплату!\nВ понедельник в 14:00 будет обнуление баллов. Если получилось "
                                                "так, что Вы не успеете заработать минимум - 20,000 баллов, то они перенесутся на следующую неделю и Вы "
                                                "сможете дособирать их.\n\nУбедитесь, что Вы не забыли зарегистрироваться в Binance и привязать счёт в "
                                                "LiveJoy, или воспользуйтесь нашим счётом Binance (После чего Вам необходимо привязать карту в разделе Финансы",
                                           reply_markup = kb.every_sathurday_message_lj)

        for elem in self.lj_day2_list:
            await bot.send_message(chat_id = elem,
                                   text = "Приветствуем! Сегодня третий нашей совместной работы! Мы очень рады видеть Вас в нашей "
                                        "команде и надеемся на Ваш высокий заработок! Надеемся, что Вы получаете удовольствие "
                                        "от работы и Вы стремитесь зарабатывать еженедельно не менее 300 долларов")
            await bot.send_message(chat_id = elem,
                                   text = "Позаботьтесь о красивом фоне Вашего рабочего места и хорошем освещении. У Вас должен "
                                        "быть ухоженный внешний вид и хорошее настроение во время работы. Используйте яркие "
                                        "аксессуары - серьги, браслеты и прочее. Такие мелочи запоминаются и помогут Вам "
                                        "получить постоянных собеседников.\nБудьте благодарны пользователю за общение и подарки")
            await bot.send_message(chat_id = elem,
                                   text = "Также, мы предлагаем Вам дополнительный заработок! Рекомендуйте нас своей знакомой "
                                        "или подруге, помогите ей зарегистрироваться, объясните ей правила и получите процент от "
                                        "её заработка в качестве бонуса!\nБонус выплачивается, если подруга вышла на минимум в течении первой недели.",
                                   reply_markup = kb.third_day_activ_lj_kb)

        self.lj_every_saturday_list.extend(self.lj_day2_list)
        self.lj_day2_list.clear()

        for elem in self.lj_day1_list:
            await bot.send_message(chat_id = elem,
                                   text = "Приветствуем! Вас можно поздравить? Вы заработали свои первые 5,000 баллов?",
                                   reply_markup = kb.second_day_activ_lj_kb)
        self.lj_day2_list.extend(self.lj_day1_list)
        self.lj_day1_list.clear()

        self.lj_day1_list.extend(self.lj_day0_list)
        self.lj_day0_list.clear()

    async def write(self,filename):
        with open(filename, 'w') as fh:
            json.dump(self,fh,cls=LJGirlsEncoder, indent=4)

    async def read(self,filename):
        if os.path.exists(cnfg.lj_database) == False or os.stat(cnfg.lj_database).st_size == 0:
            await self.write(filename)
        with open(filename,'r') as fh:
            girl = json.load(fh)
            self.lj_day0_list = girl['lj_day0_list']
            self.lj_day1_list = girl['lj_day1_list']
            self.lj_day2_list = girl['lj_day2_list']
            self.lj_every_saturday_list = girl['lj_every_saturday_list']

    async def check_id(self,id):
        if self.lj_day0_list.count(id) > 0:
            return 1
        elif self.lj_day1_list.count(id) > 0:
            return 1
        elif self.lj_day2_list.count(id) > 0:
            return 1
        elif self.lj_every_saturday_list.count(id) > 0:
            return 1
        else:
            return 0

class LJGirlsEncoder(json.JSONEncoder):
    def default(self,o):
        if isinstance(o,LJGirls):
            return {'lj_day0_list': o.lj_day0_list,
                    'lj_day1_list': o.lj_day1_list,
                    'lj_day2_list': o.lj_day2_list,
                    'lj_every_saturday_list': o.lj_every_saturday_list}
        return super().default(o)

