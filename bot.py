import datetime
import random
import telebot
from tok import TOKEN
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from images.randomIMAGE import img
from music import dt
from translate import Translator
import requests
from mongodb import mdb, search_or_save_user, save_user_info

tb = telebot.TeleBot(TOKEN)
due = 0
flag = 0
total = 0
user = ''
reply_keyboard = [['/info'],
                  ['/game_quiz'], ['/add_functions']]
communication = [['/contacts'], ['/website'], ['/download_game'], ['/back']]
main_answer = [['/yes'], ['/no']]
addFunction = [['/christmas_art'], ['/advice'], ['/time_untilNY'],
               ['/back']]
ART = [['/christmas_image'], ['/christmas_music'],
       ['/back_to']]
reply_close_timer = [['/close']]
choicer = [['/1'], ['/2'], ['/3'], ['/4'], ['/main_window']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
markupFUNC = ReplyKeyboardMarkup(addFunction, one_time_keyboard=False)
markupART = ReplyKeyboardMarkup(ART, one_time_keyboard=False)
markup_choice = ReplyKeyboardMarkup(choicer, one_time_keyboard=False, resize_keyboard=True)
markup2 = ReplyKeyboardMarkup(communication, one_time_keyboard=False)
markup3 = ReplyKeyboardMarkup(main_answer, one_time_keyboard=False)
markup4 = ReplyKeyboardMarkup(reply_close_timer, one_time_keyboard=False)


def christmas_art(update, context):
    update.message.reply_text(f'1) Случайная рождественская картинка.\n2) Случайная рождественская Музыка.',
                              reply_markup=markupART)


def get_advice(update, context):
    update.message.reply_text("Подгружаю совет...")
    response = requests.get('https://api.adviceslip.com/advice')
    data = response.json()
    text = data['slip']['advice']
    translator = Translator(to_lang="RU")
    translation = translator.translate(text)
    if 'WARNING' in translation:
        try:
            tr_url = "https://translated-mymemory---translation-memory.p.rapidapi.com/api/get"
            lang_pair = "en|ru"
            headers = {
                'x-rapidapi-key': "7e5cc6f72fmshd5472477a995ccep10b72cjsnaed447d4c2e9",
                'x-rapidapi-host': "translated-mymemory---translation-memory.p.rapidapi.com"
            }
            querystring = {"q": text, "langpair": lang_pair, "de": "a@b.c", "onlyprivate": "0", "mt": "1"}
            print(querystring)
            response = requests.request("GET", tr_url, headers=headers, params=querystring)
            print(response.json())
            translation = response.json()['matches'][0]['translation']
            update.message.reply_text(translation,
                                      reply_markup=markupFUNC)
        except Exception as r:
            update.message.reply_text(text,
                                      reply_markup=markupFUNC)
    else:
        update.message.reply_text(translation,
                                  reply_markup=markupFUNC)


def info(update, context):
    update.message.reply_text('Игра платформер с видом сбоку. С большим количеством персонажей и с '
                              'проработанным главным героем.\nКоротко о сюжете.\nДед Мороз шёл далеко далеко, '
                              'за тридевять земель, '
                              ' чтобы подарить подарки маленьким детишкам.\nНо тут случается беда! Он падает с '
                              'обрыва и теряет все свои вещи.\n Помогите любимому Дедушке Морозу найти подарки и'
                              ' дойти до'
                              ' детишек.\n Вам предстоит встретиться с волшебными хитрыми коробками и трудностями '
                              'сурового климата отдалённых мест.', reply_markup=markup2)


def download_game(update, context):
    update.message.reply_text('Ссылка на архив - https://clck.ru/UQido \nСсылка на установщик - https://clck.ru/UVGK2')


def website(update, context):
    update.message.reply_text('Наш сайт: https://clck.ru/UWG6a', reply_markup=markup2)


def add_functions(update, context):
    update.message.reply_text('1) Рандомная картинка или музыка с Рождеством!\n2) Случайный совет на день!\n3) '
                              'Сколько дней до нового года?', 
                              reply_markup=markupFUNC)


def christmas_image(update, context):
    update.message.reply_text('Загружаю картинку...')
    photo = random.choice(img)
    if not photo:
        photo = random.choice(img)
    tb.send_photo(update.message.chat_id,
                  photo)


def christmas_music(update, context):
    try:
        ms = random.choice(dt)
        update.message.reply_text(f'Идет загрузка...\n{ms[:-4]}...')
        print(f'music/{ms}')
        mus = open(f'music/{ms}', 'rb')
        tb.send_document(update.message.chat_id, mus)
    except Exception as r:
        update.message.reply_text('ОШИБКА! Попробуйте еще раз! Или чуть похже...')


def contacts(update, context):
    photo = 'https://i.pinimg.com/originals/d0/8f/0a/d08f0a9a93af07aa14a710fb3bc92f4d.jpg'
    tb.send_photo(update.message.chat_id,
                  photo)
    update.message.reply_text(
        f"@slaav1k")
    photo2 = 'https://yt3.ggpht.com/ytc/AAUvwnhG1cgFUA4dLNGFb_D5DkPHEiFtL13RurafMUc=s900-c-k-c0x00ffffff-no-rj'
    tb.send_photo(update.message.chat_id,
                  photo2)
    update.message.reply_text(f"@pasha882")


def game_quiz(update, context):
    update.message.reply_text(
        f"Хочешь сыграть в викторину?", reply_markup=markup3)


def yes(update, context):
    global flag
    global user
    user = search_or_save_user(mdb, update.effective_user, total)
    print(update.effective_user)
    flag = 1
    update.message.reply_text(
        f"Тогда мы НАЧНАЕМ!\nГде живет дед мороз?\n1) На северном полюсе.\n2) На южном полюсе.\n3) В Крыму!\n4) В "
        f"Солотче!", reply_markup=markup_choice)


def help(update, context):
    update.message.reply_text(
        "Если что-то пошло не так пропишите или нажмите /start.")


def first(update, context):
    global flag, total
    if flag == 1:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nКак называется праздник, на который приходит Дед Мороз?\n1) Пасха.\n2) День "
            f"знаний. "
            "\n3) Новый Год.\n4) Масленица.", reply_markup=markup_choice)
    elif flag == 5:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nЧто на ногах у Деда Мороза?\n1) Унты.\n2) Валенки."
            "\n3) Сапоги.\n4) Черевички.", reply_markup=markup_choice)
    elif flag == 13:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nУ представителей какого народа под Новый год принято вспоминать о "
            f"совершенных грехах и давать "
            "обещание искупить их новыми делами в Новом году?\n1) Евреи.\n2) Aфганцы. "
            "\n3) Греки.\n4) Японцы.", reply_markup=markup_choice)
    elif flag == 14:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nКитайцы считают, что первый день наступившего года окутан злыми духами, "
            f"которых необходимо "
            "отпугнуть. Чем китайцы их отпугивают?\n1) Рисом.\n2) Чаем. "
            "\n3) Петардами.\n4) Волшебными словами.", reply_markup=markup_choice)
    elif flag == 29:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nКаким образом волк из русской народной сказки «Лиса и волк» ловил рыбу в "
            f"проруби?\n1) "
            "Удочкой.\n2) "
            "Хвостом. "
            "\n3) Лапой.\n4) Пастью.", reply_markup=markup_choice)
    else:
        global user
        user = search_or_save_user(mdb, update.effective_user, total)
        if int(user["total"]) < total:
            user = save_user_info(mdb, user, update.effective_user, total)
        all_info = list(mdb.users.find({}))
        out_info1 = []
        out_info = []
        for i in all_info:
            out_info1.append((i["name"], int(i["total"])))
        out_info1 = sorted(out_info1, key=lambda x: x[1], reverse=True)
        k = 0
        for i in out_info1:
            k += 1
            out_info.append(f'{k}) {i[0]} {i[1]}')
        out_info = "\n".join(out_info)
        print(list(all_info))
        update.message.reply_text(
            f'ТЫ не угадал! Твой счет: {total}')
        total = 0
        update.message.reply_text(
            f'А теперь рекорды! \n{out_info}')
        update.message.reply_text(
            f'Игра окончена!', reply_markup=markup)


def second(update, context):
    global flag, total
    if flag == 4:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nВокруг чего Дед Мороз, Снегурочка и дети водят хоровод?\n1) Вокруг елки.\n2) "
            f"Вокруг пальмы. "
            "\n3) Вокруг березы.\n4) Вокруг дуба.", reply_markup=markup_choice)
    elif flag == 6:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nВ какой стране дети и взрослые находят новогодние подарки на "
            f"подоконнике?\n1) В Польше.\n2) В "
            "Германии. "
            "\n3) В Америке.\n4) В Китае.", reply_markup=markup_choice)
    elif flag == 7:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nСколько шуб у Деда Мороза?\n1) 1.\n2) 2"
            ""
            "\n3) 3.\n4) 4.", reply_markup=markup_choice)
    elif flag == 9:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nЧто символизирует тройка лошадей?\n1) Любовь к троице.\n2) Счастье, радость "
            f"и любовь. "
            "\n3) Количество зимних праздников.\n4) Зимние месяца.", reply_markup=markup_choice)
    elif flag == 11:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nПо указу какого царя датой празднования Нового года на Руси стало 1 "
            f"января?\n1) Ивана "
            "Грозного.\n2) "
            "Александра I."
            "\n3) Петра I.\n4) Александра II.", reply_markup=markup_choice)
    elif flag == 15:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nВ каком городе получил прописку российский Дед Мороз?\n1) Новгород. "
            "\n2) "
            "Тула."
            "\n3) Великий Устюг.\n4) Оренбург.", reply_markup=markup_choice)
    elif flag == 19:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nКто зимой в футболках и платьях, а летом – в шубах?\n1) Человек. "
            "\n2) "
            "Заяц."
            "\n3) Моль.\n4) Медведь.", reply_markup=markup_choice)
    elif flag == 21:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nЧем запасается российский бурый медведь перед зимним сном?\n1) Вяленой рыбой."
            "\n2) "
            "Сушёной малиной."
            "\n3) Терпением.\n4) Подкожным жиром.", reply_markup=markup_choice)
    elif flag == 24:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nКак называют кактус, который цветет только в зимнее время?\n1) Революционер."
            "\n2) "
            "Полярник."
            "\n3) Декабрист.\n4) Коммунист.", reply_markup=markup_choice)
    elif flag == 30:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nКакое слово нужно было собрать Каю из осколков льда в сказке Г.Х. Андерсена "
            f"«Снежная королева», "
            "чтобы стать «самому себе господином», и чтобы получить от королевы «весь свет и пару новых коньков»?\n1) "
            "Дружба. "
            "\n2) "
            "Семья."
            "\n3) Забота.\n4) Вечность.", reply_markup=markup_choice)
    else:
        global user
        user = search_or_save_user(mdb, update.effective_user, total)
        if int(user["total"]) < total:
            user = save_user_info(mdb, user, update.effective_user, total)
        all_info = list(mdb.users.find({}))
        out_info1 = []
        out_info = []
        for i in all_info:
            out_info1.append((i["name"], int(i["total"])))
        out_info1 = sorted(out_info1, key=lambda x: x[1], reverse=True)
        k = 0
        for i in out_info1:
            k += 1
            out_info.append(f'{k}) {i[0]} {i[1]}')
        out_info = "\n".join(out_info)
        print(list(all_info))
        update.message.reply_text(
            f'ТЫ не угадал! Твой счет: {total}')
        total = 0
        update.message.reply_text(
            f'А теперь рекорды! \n{out_info}')
        update.message.reply_text(
            f'Игра окончена!', reply_markup=markup)


def third(update, context):
    global flag, total
    if flag == 2:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nЧто спрятано в мешке у Деда Мороза?\n1) Гранаты.\n2) Фрукты."
            "\n3) Спорт инвентарь.\n4) Подарки.", reply_markup=markup_choice)
    elif flag == 8:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nСколько лошадей запрягает в сани Дед Мороз?\n1) Двух.\n2) Трех."
            "\n3) Четырех.\n4) Семерых.", reply_markup=markup_choice)
    elif flag == 12:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nВ какой стране в XVI веке появилась первая елочная игрушка?\n1) "
            f"Саксония.\n2) Австралия. "
            "\n3) Богемия.\n4) Германия.", reply_markup=markup_choice)
    elif flag == 16:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nЧему равна «сумма» декабря, января и февраля? \n1) Лету. "
            "\n2) "
            "Весне."
            "\n3) Осени.\n4) Зиме.", reply_markup=markup_choice)
    elif flag == 20:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nКакое из этих животных каждую зиму сбрасывает рога? \n1) Баран. "
            "\n2) "
            "Лось."
            "\n3) Буйвол.\n4) Рогач.", reply_markup=markup_choice)
    elif flag == 23:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nКакой ягодный кустарник НЕ роняет на зиму листья?\n1) Малина. "
            "\n2) "
            "Брусника."
            "\n3) Смородина.\n4) Ежевика.", reply_markup=markup_choice)
    elif flag == 25:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nКаким из слов заканчивается название 1-й симфонии П.И. Чайковского "
            f"«Зимние…»?\n1) Морозы. "
            "\n2) "
            "Праздники."
            "\n3) Каникулы.\n4) Грёзы.", reply_markup=markup_choice)
    elif flag == 27:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nВ каком из этих зимних видов спорта соревнуются на санях?\n1) Фристайл. "
            "\n2) "
            "Биатлон."
            "\n3) Шорт-трек.\n4) Скелетон.", reply_markup=markup_choice)
    else:
        global user
        user = search_or_save_user(mdb, update.effective_user, total)
        if int(user["total"]) < total:
            user = save_user_info(mdb, user, update.effective_user, total)
        all_info = list(mdb.users.find({}))
        out_info1 = []
        out_info = []
        for i in all_info:
            out_info1.append((i["name"], int(i["total"])))
        out_info1 = sorted(out_info1, key=lambda x: x[1], reverse=True)
        k = 0
        for i in out_info1:
            k += 1
            out_info.append(f'{k}) {i[0]} {i[1]}')
        out_info = "\n".join(out_info)
        print(list(all_info))
        update.message.reply_text(
            f'ТЫ не угадал! Твой счет: {total}')
        total = 0
        update.message.reply_text(
            f'А теперь рекорды! \n{out_info}')
        update.message.reply_text(
            f'Игра окончена!', reply_markup=markup)


def fourth(update, context):
    global flag, total
    if flag == 3:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nКак зовут внучку Деда Мороза?\n1) Дюймовочка.\n2) Снегурочка."
            "\n3) Несмеяна.\n4) Мария Васильевна.")
    elif flag == 10:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nКак величали сурового предшественника современного русского Деда Мороза?\n1) "
            f"Дед Колотун.\n2) "
            "Дед Трескун. "
            "\n3) Дед Вьюговей.\n4) Дед Иван.", reply_markup=markup_choice)
    elif flag == 17:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nНазовёте «зимний» синоним глагола «поколотить»? \n1) Побить. "
            "\n2) "
            "Отмутузить."
            "\n3) Исколотить.\n4) Отметелить.", reply_markup=markup_choice)
    elif flag == 18:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nВо что впадают зимой некоторые животные?\n1) В детство. "
            "\n2) "
            "В спячку."
            "\n3) В бешенство.\n4) В беспамятство.", reply_markup=markup_choice)
    elif flag == 22:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nКакой из этих зверей зимой в спячку НЕ впадает?\n1) Бурый медведь. "
            "\n2) "
            "Барсук."
            "\n3) Куница.\n4) Сурок.", reply_markup=markup_choice)
    elif flag == 26:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nВ каком городе прорыт канал Зимняя канавка?\n1) В Москве. "
            "\n2) "
            "В Астрахани."
            "\n3) В Санкт-Петербурге.\n4) В Волгограде.", reply_markup=markup_choice)
    elif flag == 28:
        flag += 1
        total += 1
        update.message.reply_text(
            f"Верно! Ваш счет = {total}\nКакая из перечисленных птиц средней полосы России НЕ улетает на зимовку?\n1) "
            f"Щегол. "
            "\n2) "
            "Соловей."
            "\n3) Скворец.\n4) Ласточка.", reply_markup=markup_choice)
    elif flag == 31:
        global user
        update.message.reply_text(
            "Верно!\nТы ответил верно НА ВСЕ ВОПРОСЫ!", reply_markup=markup_choice)
        update.message.reply_text(
            f'Игра окончена!', reply_markup=markup)
        photo = open('images/pers.jpg', 'rb')
        tb.send_photo(update.message.chat_id,
                      photo)
        user = search_or_save_user(mdb, update.effective_user, total)
        if int(user["total"]) < total:
            user = save_user_info(mdb, user, update.effective_user, total)
        all_info = list(mdb.users.find({}))
        out_info1 = []
        out_info = []
        for i in all_info:
            out_info1.append((i["name"], int(i["total"])))
        out_info1 = sorted(out_info1, key=lambda x: x[1], reverse=True)
        k = 0
        for i in out_info1:
            k += 1
            out_info.append(f'{k}) {i[0]} {i[1]}')
        out_info = "\n".join(out_info)
        update.message.reply_text(
            f'Твой счет: {total}.\n')
        update.message.reply_text(
            f'Рейтинговая таблица... \n{out_info}')
    else:
        user = search_or_save_user(mdb, update.effective_user, total)
        if int(user["total"]) < total:
            user = save_user_info(mdb, user, update.effective_user, total)
        all_info = list(mdb.users.find({}))
        out_info1 = []
        out_info = []
        for i in all_info:
            out_info1.append((i["name"], int(i["total"])))
        out_info1 = sorted(out_info1, key=lambda x: x[1], reverse=True)
        k = 0
        for i in out_info1:
            k += 1
            out_info.append(f'{k}) {i[0]} {i[1]}')
        out_info = "\n".join(out_info)
        print(list(all_info))
        update.message.reply_text(
            f'ТЫ не угадал! Твой счет: {total}')
        total = 0
        update.message.reply_text(
            f'А теперь рекорды! \n{out_info}')
        update.message.reply_text(
            f'Игра окончена!', reply_markup=markup)


def time_untilNY(update, context):
    now = datetime.datetime.today()
    NY = datetime.datetime(int(now.year) + 1, 1, 1)
    d = NY - now
    mm, ss = divmod(d.seconds, 60)
    hh, mm = divmod(mm, 60)
    update.message.reply_text('До нового года: {} дней {} часа {} мин {} сек.'.format(d.days, hh, mm, ss))


def start(update, context):
    name = update.effective_user["first_name"]
    print(name)
    update.message.reply_text(
        f"Здраствуйте, {name}. Я помощник деда мороза. Чем могу помочь?\n\n/info - раздел с кратким описанием "
        f"игры, контактами и ссылкой на сайт и на скачивание игры.\n\n/game_quez - мини игра "
        f"викторина.\n\n/add_functions "
        f"- второстепенные умения бота.\n(рандомная новогодня картинка, музыка, случайный совет и счетчик времени до"
        f" НГ.)",
        reply_markup=markup
    )


def menu(update, context):
    update.message.reply_text(
        f"Чем могу помочь?\n\n/info - раздел с кратким описанием "
        f"игры, контактами и ссылкой на сайт и на скачивание игры.\n\n/game_quez - мини игра "
        f"викторина.\n\n/add_functions "
        f"- второстепенные умения бота.\n(рандомная новогодня картинка, музыка, случайный совет и счетчик времени до"
        f" НГ.)",
        reply_markup=markup
    )


def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    updater.start_polling()
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("back", menu))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("website", website))
    dp.add_handler(CommandHandler("time_untilNY", time_untilNY))
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("contacts", contacts))
    dp.add_handler(CommandHandler("game_quiz", game_quiz))
    dp.add_handler(CommandHandler("add_functions", add_functions))
    dp.add_handler(CommandHandler("christmas_art", christmas_art))
    dp.add_handler(CommandHandler("back_to", add_functions))
    dp.add_handler(CommandHandler("advice", get_advice))
    dp.add_handler(CommandHandler("download_game", download_game))
    dp.add_handler(CommandHandler("christmas_image", christmas_image))
    dp.add_handler(CommandHandler("christmas_music", christmas_music))
    dp.add_handler(CommandHandler("yes", yes))
    dp.add_handler(CommandHandler("no", menu))
    dp.add_handler(CommandHandler("1", first))
    dp.add_handler(CommandHandler("2", second))
    dp.add_handler(CommandHandler("3", third))
    dp.add_handler(CommandHandler("4", fourth))
    dp.add_handler(CommandHandler("main_window", menu))
    dp.add_handler(CommandHandler("close_keyboard", close_keyboard))
    updater.idle()  # не комититься


if __name__ == '__main__':
    main()
