opus_bot = """Я Віртуальний асистент <b>Перечинського районного суду</b>.
Я вмію находити дату судового засідання за прізвищем, ім'ям і за номером справи, а також сповіщаю про дату і час засідання."""

instruction = """Наше спілкування буде проходити так:
- Вибираєте🕹 розділ в меню;
- Натискаєте📲 на кнопки в меню;
- А я Вам відпишу📨."""

contact = """ контактні дані:</b></u>

📍E-mail📧: inbox@pr.zk.court.gov.ua

📍Телефон📞: (03145)2-11-96

📍Адреса📮: пл. Народна, 15, м. Перечин, 89200.

📍Карти🗺 проїзду 🚖 👇."""

notice = """ перейшовши на вебпортал, можна передивитися всі оголошення про виклик до Перечинського районного суду."""

electronic_court = " електронний суд дозволяє подавати учасникам судового процесу " \
                   "до суду документи в електронному вигляді, а також надсилати таким учасникам " \
                   'процесуальних документів в електронному вигляді, паралельно з документами у ' \
                   'паперовому вигляді відповідно до процесуального ' \
                   'процесуального законодавства.\n\n<a href="https://id.court.gov.ua/">' \
                   "Перейти в Електронний Суд🔗.</a>\n\n."

court_app = "Також Ви можете скористатися Нашим офіційним мобільним додатком <b>Електронного суду в " \
            "Україні єСуд</b> призначеним для доступу до Електронного суду з мобільних пристроїв. " \
            "<b>Для використання додатку Вам необхідно бути зареєстрованим в електронному " \
            'кабінеті</b>.\n\n<a href="https://cabinet.court.gov.ua">Перейти в Електронний' \
            " кабінет🔗.</a>\n\n."

push = " в цьому розділі можна скористатися сервісом *<b>" \
       "Сповіщення</b>*.\nСуть сервісу проста, Ви отримаєте📩 повідомлення про дату і час " \
       "судового засідання.\n\nЩоб підписатися✍🏻 на сервіс Вам потрібно набрати⌨" \
       " прізвище та ім'я, яке цікавит або номер справи і відправити боту📥." \
       "\n\n<b>Попередження</b>❗\nПрізвище та ім'я набирати можна з малої букви, а " \
       "апостроф в тексті заміняється на пробіл. Щодо номера справи" \
       " набираємо⌨ відповідно до зразків '304/555/20'. <b>Інформацію" \
       "вказуйте правильно</b>💯." \
       "\n\nЩоб скасувати підписку натисніть\nна👉 /cancel або на кнопку 🔙_Назат_"

meeting_date = """ в даному розділі можна подивитися дату засідання нажавши🕹 на ниже вказані кнопки👇:

 📍 Натискаємо📲 на 🎫<b>Пошук за прізвищем та ім’ям (П.І.П.) або номером справи</b> -  набираємо П.І.П. або номером 
 справи як на зразку 304/555/20 чи 555/22 і відправляємо📥.

 📍 Натискаємо📲 на 🗓️<b>Пошук за датою</b> - вибираємо дату і прізвище судді і відправляємо📥.
 """

list_court = """
в даному розділі можна вибрати🕹 суд зі списка👇:

📍 ⚖️Закарпатський апеляційний суд;

📍 ⚖️Ужгородський міськрайонний суд;

📍 ⚖️Великоберезнянський районний суд.

Та подивитися дату засідання."""

input_instruction = """ набирати можна номер справи або текст з малої букви, апостроф в тексті можна заміняти на пробіл.

<b>Попередження</b>❗, якщо буде введено тільки прізвище або ім’я чи 304 номер, то Вам видасть всі засідання призначені на даний запит.
Щоб скасувати пошук натисніть на👉 /cancel."""

url_data = [
    {"url": "https://pr.zk.court.gov.ua/new.php", "payload": "q_court_id=0708",
     "referer": "https://pr.zk.court.gov.ua/sud0708/gromadyanam/csz/", "file_name": "data/data_pr00.json"},
    {"url": "https://pr.zk.court.gov.ua/new.php", "payload": "q_court_id=0708",
     "referer": "https://pr.zk.court.gov.ua/sud0708/gromadyanam/csz/", "file_name": "data/data_pr.json"},
    {"url": "https://zka.court.gov.ua/new.php", "payload": "q_court_id=4806",
     "referer": "https://zka.court.gov.ua/sud4806/gromadyanam/csz/", "file_name": "data/data_zka.json"},
    {"url": "https://ug.zk.court.gov.ua/new.php", "payload": "q_court_id=0712",
     "referer": "https://ug.zk.court.gov.ua/sud0712/gromadyanam/csz/", "file_name": "data/data_ug.json"},
    {"url": "https://vb.zk.court.gov.ua/new.php", "payload": "q_court_id=0702",
     "referer": "https://vb.zk.court.gov.ua/sud0702/gromadyanam/csz/", "file_name": "data/data_vb.json"}
]

callback_btn = [
    {"url": "https://pr.zk.court.gov.ua/sud0708/gromadyanam/csz/", "callback": "callback_pr"},
    {"url": "https://zka.court.gov.ua/sud4806/gromadyanam/csz/", "callback": "callback_appel"},
    {"url": "https://ug.zk.court.gov.ua/sud0712/gromadyanam/csz/", "callback": "callback_uz"},
    {"url": "https://vb.zk.court.gov.ua/sud0702/gromadyanam/csz/", "callback": "callback_vb"}
]

wep_url = [
    {"url": "https://starlit-marzipan-56ef4f.netlify.app"},
    {"url": "https://starlit-marzipan-56ef4f.netlify.app/appellate"},
    {"url": "https://starlit-marzipan-56ef4f.netlify.app/uzhhorod"},
    {"url": "https://starlit-marzipan-56ef4f.netlify.app/greatberezny"}
]

button_mapping = {
    "📅Перечинський р-н суд": 0,
    "📅Апеляційний суд": 1,
    "📅Ужгородський м-р суд": 2,
    "📅В.Березнянський\nр-н суд": 3
}

callback_mapping = {
    'callback_pr': 0,
    'callback_appel': 1,
    'callback_uz': 2,
    'callback_vb': 3
}

json_files = [
    {"pad": 'data/data_pr.json'},
    {"pad": 'data/data_zka.json'},
    {"pad": 'data/data_ug.json'},
    {"pad": 'data/data_vb.json'}
]
