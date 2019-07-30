from flask import Flask, render_template
from flask import request
from flask_misaka import Misaka
import mistune
import jellyfish

import glob

app = Flask(__name__)
Misaka(app)

markdown = mistune.Markdown()

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return search(request.form)
    else:
        return render_template("home.html")

@app.route("/about")
def about():
    mkd = open('templates/about.md').read()
    return render_template('template.html', text=mkd)

def search(request_form):
    """
    search method called from both welcome() and about()
    :param request_form:
    :return:
    """
    query = request_form["query"].lower()
    terms = glob.glob("templates/*.md")

    results = []
    for term in terms:
        query_term = term.lower().replace('.md', '').replace('templates/', '')
        similarity = jellyfish.jaro_distance(query_term, query)
        if similarity > 0.5:
            results.append((float("%.2f" % (similarity*100)), query_term, term.replace('templates/', '')))

    results = sorted(results, reverse=True)
    print(results)
    return render_template("search.html", query=query, results=results)

@app.route("/<page>")
def dynamicpath(page):
    mkd = open('templates/{}.md'.format(page)).read()
    return render_template('template.html', entry=page.title(), text=mkd)

if __name__ == "__main__":
    app.run(debug=True)
