from flask import Flask, render_template
from flask import request
from flask_misaka import Misaka
import jellyfish

import glob

app = Flask(__name__)
Misaka(app)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return search(request.form)
    else:
        return render_template("home.html")

# @app.route("/about")
# def about():
#     return render_template("about.html")

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
    mkd = open('templates/{}.md'.format(page)).readlines()
    return render_template('template.html', entry=page.title(), text=' '.join(mkd))


@app.route("/test")
def test():
    return render_template("template.html", text='*this is an example*')

if __name__ == "__main__":
    app.run()
