import sys

'''data = list(map(str.strip, sys.stdin))
print(data)'''
dt = ['01.Ольга Рождественская - Три белых коня.mp3', '02.Kazaхи - Это Новый год!.mp3', '03.Наталья Могилевская и '
                                                                                        'Дмитрий Гордон - '
                                                                                        'Завируха.mp3', '04.Потап и '
                                                                                                        'Настя - Все '
                                                                                                        'пучком.mp3',
      '05. Диверсанты и Маня - Замуж за Деда Мороза.mp3', '06.MMDance feat. Konstantin Ozeroff - Новогодняя .mp3',
      '07.Alex Neo & Bozool George - Подари, новый год.mp3', '08,LiLi & Konstantino - К нам приходит Новый год.mp3',
      '09,Дмитрий Колдун - Падал снег.mp3', '10.Дискотека Авария - Новогодняя (Dj Рыжов Remix).mp3', '100.DJ SLON & '
                                                                                                     'KATYA - Про '
                                                                                                     'новый год.mp3',
      '101.SWEETLANA - Новогоднее чудо.mp3', '102.Владимир Алмазов - В новый год.mp3', '103.Белый День - Новый '
                                                                                       'год.mp3', '104.Анюта Ильина - '
                                                                                                  'С новым '
                                                                                                  'годом.mp3',
      '105.Влад Чехов - Новогодняя.mp3', '106.Alex Kafer & LERA - С новым годом.mp3', '107.В. Королёв - Открывай '
                                                                                      'бутылочку шампанского.mp3',
      '108.Ирма Брикк - Новогодняя.mp3', '109.DJ PRAPOR & Drive Device - Новый год.mp3', '11,Блестящие - Новогодняя '
                                                                                         'песня.mp3', '110,'
                                                                                                      'Стоматолог и '
                                                                                                      'Фисун - Новый '
                                                                                                      'Год.mp3',
      '111.MSEVEN - Новый год по-новому.mp3', '112.Андрей Ковалёв - Новогодние города.mp3', '113. ПАОЛА - Новый '
                                                                                            'год.mp3', '114.Таисия '
                                                                                                       'Повалий - '
                                                                                                       'Новогодний '
                                                                                                       'торт.mp3',
      '115.София Ротару - Новогодний вечер.mp3', '116.SEREBRO - Новый год.mp3', '117.ALISHER - Новый год.mp3',
      '118.ГАЛАМАРТОВНА - Хулиганка зима.mp3', '119. Ирина Баженова - Новогодняя - корпоративная.mp3', '12,'
                                                                                                       'Группа 3.15 - '
                                                                                                       'Самый Новый '
                                                                                                       'Год.mp3',
      '120 Dress Code - Новогодний гопачок.mp3', '121.Таня Аверман - Сказка в новый год.mp3', '122.Сергей Любавин и '
                                                                                              'Анна Гуричева - '
                                                                                              'Кружится снег.mp3',
      '123.NEXET - Наш новый год.mp3', '124.Дуэт Лето - Новый год, страна вперёд!.mp3', '125.Юлия Беретта - С новым '
                                                                                        'годом, друзья.mp3',
      '126.Мария Богомолова - С новым годом.mp3', '127.Наталья Нейт - Новогодняя.mp3', '128.Наташа Королёва feat. '
                                                                                       'Герман Титов - Мой Дед '
                                                                                       'Мороз.mp3', '129.Сергей '
                                                                                                    'Лазарев - Новый '
                                                                                                    'год.mp3', '13,'
                                                                                                               'Алек'
                                                                                                               'сандр'
                                                                                                               ' Абд'
                                                                                                               'улов'
                                                                                                               ' - '
                                                                                                               'Старый'
                                                                                                               ' Новый'
                                                                                                               ' '
                                                                                                               'год'
                                                                                                               '.mp3',
      '130.Юля Шатунова - Праздник детства.mp3', '131.Анжелика Пушнова - Новогодняя.mp3', '132.Пьер Нарцисс feat. '
                                                                                          'Алеся Боярских - Новый '
                                                                                          'год.mp3', '133.Николай '
                                                                                                     'Басков - Вот '
                                                                                                     'пришёл новый '
                                                                                                     'год.mp3',
      '134.РОЖДЕСТВО - Новый год, новый год (remix).mp3', '135,Чай Вдвоём - Новогодний поцелуй (Alex Dea remix).mp3',
      '136.ЮТА и Ян Марти - С новым годом, друзья!.mp3', '137.Никита Хазановский - Новый год.mp3', '138.СТРЕЛКИ - С '
                                                                                                   'новым годом ('
                                                                                                   'version '
                                                                                                   '2015).mp3',
      '139.Inna Felix - Новый год.mp3', '14.Наташа Королева - Новогодняя.mp3', '140.Наталия Королёва - '
                                                                               'Па-па-поздравляю.mp3', '141.Диана '
                                                                                                       'Шарапова - '
                                                                                                       'Новогодний '
                                                                                                       'бал.mp3',
      '142.Андрей Куряев - С новым годом.mp3', '143.Анжелика Рута - От зимы до зимы (Новогодняя).mp3', '144.Николай '
                                                                                                       'Юхименко и '
                                                                                                       'Анастасия '
                                                                                                       'Мендус - '
                                                                                                       'Новый '
                                                                                                       'год.mp3',
      '145.Тамерлан и Алена Омаргалиева - Новогодние поздравления.mp3', '146.Иванушки International - Ирония '
                                                                        'судьбы.mp3', '147.Александр Ковалёв - '
                                                                                      'Влюблённый Дед Мороз.mp3',
      '148.М. Шуфутинский,Е.Голицына,Л.Шепилова - Новый Год.mp3', '149.ASTUDIO,Николай Басков,Валерия,Виа Гра,Винтаж,'
                                                                  'Филипп Киркоров,Ани Лорак,Татьяна Овсиенко - '
                                                                  'Счастье в каждый дом..(Новый год!).mp3',
      '15.Натали - Новогодняя.mp3', '150.ВИА Пламя - Снег кружится.mp3', '16.Андрей Леницкий - Новогодняя.mp3',
      '17.StanSax - Рулит Дед Мороз.mp3', '18.Reflex - Это Новый год.mp3', '19.Н.Бродская - Звенит январская '
                                                                           'вьюга.mp3', '20 София Ротару - Новый '
                                                                                        'год.mp3',
      '22.Авет Маркарян - Новый год.mp3', '23.Маргарита Суханкина - Новый год на планете Любовь.mp3', '24.Сергей '
                                                                                                      'Лазарев - '
                                                                                                      'Новый год ('
                                                                                                      'HarDrum '
                                                                                                      'remix).mp3',
      '25.MC Zali _ DJ Half feat. Karina Kari - Этот Новый Год (Prime-Music.net).mp3', '26.Верка Сердючка - '
                                                                                       'Новогодняя.mp3',
      '28.Ирина Билык - Дед Мороз.mp3', '29.New Самоцветы - Новогодние игрушки.mp3', '30.ВИА Гра - Диско.mp3',
      '31.Виталий Кочетков - Навагодняя.mp3',
      '33.Валерий Меладзе и София Ротару - Новый год.mp3', '34.HELLO - Новогодняя.mp3', '35.ДЭЯ - С новым годом.mp3',
      '36.ELLA feat. 7 Гномов - Новый год.mp3', '37.STEREOСНЫ - Новый год приходит в столицу.mp3',
      '38.Dress Code - Новогодний Гопачк.mp3', '39.Афина - Новогодняя.mp3', '40.Феликс Луцкий - Календарь.mp3',
      '41.Андрей Дрюня & Алимханов - Желаем Счастья в Новый Год.mp3',
      '42.Владислав Агафонов - 31 число - Новый Год.mp3',
      '43.MMDance - Новогодняя.mp3', '44.ЧИ-ЛИ - Новый год в постели.mp3',
      '45.ПОТАП и Настя Каменских - Новый год.mp3', '46.Анюта Ильина - С новым годом.mp3', '47.Mr Credo -Снег.mp3',
      '48.Ковалёв Андрей and Саша project - Песенка Деда Мороза.mp3', '49.Игрушки International - Шишки-Ёлки.mp3',
      '50.Пающие Трусы - Новогодняя.mp3', '51.Татьяна Морозова - Новогодняя ночь.mp3',
      '52.София Ротару - Белая зима.mp3', '53.Верка Сердючка - Елки.mp3',
      '54.Гр. Ленинград, feat. Игорь Вдовин - Новый год.mp3',
      '55,Кай Метов, feat. Арина и Размер Project - Новый год.mp3', '56.ВИРУС - Новый год идёт.mp3',
      '57.Пающие Трусы - Тазик оливье.mp3', '58.ДЮНА - Новый год в бутылке.mp3',
      '59.Марина Соболева - С новым годом, Россияне.mp3', '60.Сергей Никитин - Диалог у новогодней елки.mp3',
      '61 Аркадий Укупник - Снегурочка.mp3', '62.Инна Маликова - Новогодний снег.mp3', '63.ПРОПАГАНДА - Ёлки-палки.mp3',
      '64.Анжелика Агурбаш - Здравствуй, новый год.mp3', '65.Фабрика Звёзд 3 - С новым годом.mp3',
      '66.Валерия - Моя Москва (Happy mix).mp3', '67.Дилижанс - Новогодняя.mp3', '68,DEMO - Новый год идёт....mp3',
      '69.Татьяна Овсиенко - Новый год.mp3', '70.Алина Гросу - Новый год.mp3', '71. Владимир Цветаев - Новый год.mp3',
      '72.Карт-Бланш - Здравствуй, опа, новый год.mp3', '73.Александр Закшевский - С новым годом, друзья!.mp3',
      '74.Оля Полякова - С новым годом!.mp3', '75.Ivan Lexx & Andy One 2 - Новый год.mp3',
      '76.EVA feat. Саша Ветер - Новогодняя.mp3', '77.София Ротару - Новогодняя.mp3',
      '78.Романтик Тайм - Ёлочка гори.mp3', '79.Биг Бэта - Это новый год, да.mp3', '80.Аня Ангел-А - Это новый год.mp3',
      '81.Алина Захарова - Новогоднее оливье.mp3', '82, МИШЕЛЬ - Новогодняя.mp3', '83.Олег Пахомов - Новый год.mp3',
      '84,Диля Даль - Новогодняя.mp3', '85.Katrin Moro - С новым годом.mp3',
      '86.Юлия Морозова feat. Роман Богачёв - Новогодняя.mp3', '87.Наталья Родина - Новогодняя.mp3',
      '88.S.U.27 - С новым годом.mp3', '89.БонТорГас - Опа, новый год.mp3', '90,СЕРДЦЕ - С новым годом, Зая.mp3',
      '91.Дядя Жора & Бигуди Шоу - С новым годом.mp3', '92.Aruba Ice & GREYSOUND - Новогодняя.mp3',
      '93.DJ FAVORITE & Laura Grig feat. Гарик Мошенник - С новым годом.mp3',
      '94.OKSI - Новогодняя.mp3', '95.Наталья Новикова - Здравствуй, новый год!.mp3', '96.Настя Кудри - Новый год.mp3',
      '97.Катя Ростовцева - Пожелай мне на новый год.mp3', '98.Даниил Иванов - 5 минут до конца декабря.mp3',
      '99.TIMA - В новый год.mp3']
