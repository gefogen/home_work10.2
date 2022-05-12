from flask import Flask  # Импортируем Flask
import json  # Импортируем json

with open("candidates.json", "r", encoding="utf-8") as file:
    content: list = json.load(file)  # Импортируем данные из candidates.json в приложение

app = Flask(__name__)  # Создаем экземпляр Flask'а


@app.route("/")  # Создаем роут для главной страницы
def page_main():    # Функция, которая возвращает данные главной страницы
    men = ""    # Строка, которую мы будем возвращать в качестве результат
    for people in content:      # Перебор по списку
        men += "Имя кандидата - " + people['name'] + "\n" + \
               "Позиция кандидата - " + people['position'] + "\n" + \
               "Навыки через запятую - " + people['skills'] + "\n\n\n"
    return f"<h3><pre>" + men + "</pre></h3>"   # Возвращаем результат


@app.route("/candidate/<int:id>")  # Создаем роут для вывода данных кандидата
def page_candidate(id):
    """Возвращает данные кандидата"""
    for people in content:      # Перебор по списку
        if people['id'] == id:      # Проверяем наличие кандидата
            return f"""<img src="{people['picture']}">\n""" + \
                   "<h3><pre>" + "Имя кандидата - " + people['name'] + "\n" + \
                   "Позиция кандидата - " + people['position'] + "\n" + \
                   "Навыки через запятую - " + people['skills'] + "\n" + "</pre></h3>"  # Возвращаем результат

    return "У нас нет такого кандидата"


@app.route("/skills/<skill>")  # Создаем роут для вывода кандидатов, в списке навыков у которых содержится skill
def page_skills(skill):  # Функция, которая возвращает этих самых кандидатов
    men = ""    # Строка, которую мы будем возвращать в качестве результат
    for people in content:      # Перебор по списку
        chel = people["skills"].lower().split(", ")     # Переменная для поиска точного совпадения, а не соответствий
        if skill in chel:
            men += "Имя кандидата - " + people['name'] + "\n" + \
                   "Позиция кандидата - " + people['position'] + "\n" + \
                   "Навыки через запятую - " + people['skills'] + "\n\n\n"
    if len(men) > 0:
        return f"<h3><pre>" + men + "</pre></h3>"   # Возвращаем результат
    return "У нас нет такого навыка"


if __name__ == "__main__":
    app.run(debug=True)     # Запускаем
