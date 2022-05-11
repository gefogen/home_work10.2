from flask import Flask
import json

with open("candidates.json", "r", encoding="utf-8") as file:
    content:list = json.load(file)

app = Flask(__name__)


@app.route("/")
def page_main():
    men = ""
    for people in content:
        men += "Имя кандидата - " + people['name'] + "\n" +\
               "Позиция кандидата - " + people['position'] + "\n" +\
               "Навыки через запятую - " + people['skills'] + "\n\n\n"
    return f"<h3><pre>" + men + "</pre></h3>"


@app.route("/candidate/<int:id>")
def page_candidate(id):
    for people in content:
        if people['id'] == id:
            return  f"""<img src="{people['picture']}">\n""" +\
                    "<h3><pre>" + "Имя кандидата - " + people['name'] + "\n" +\
                    "Позиция кандидата - " + people['position'] + "\n" +\
                    "Навыки через запятую - " + people['skills'] + "\n" + "</pre></h3>"

@app.route("/skills/<skill>")
def page_skills(skill):
    men = ""
    for people in content:
        if skill in people['skills'].lower():
            men += "Имя кандидата - " + people['name'] + "\n" + \
                   "Позиция кандидата - " + people['position'] + "\n" + \
                   "Навыки через запятую - " + people['skills'] + "\n\n\n"
    return f"<h3><pre>" + men + "</pre></h3>"

if __name__ == "__main__":
    app.run(debug=True)
