#!/usr/bin/env python

import codecs
import json

import argparse
from flask import Flask, Markup, render_template
import markdown

import app_config
from render_utils import make_context, smarty_filter, urlencode_filter
import static

app = Flask(__name__)

app.jinja_env.filters['smarty'] = smarty_filter
app.jinja_env.filters['urlencode'] = urlencode_filter

# Example application views
@app.route('/')
def index():
    context = make_context()

    with open('data/featured.json') as f:
        context['featured'] = json.load(f)

    return render_template('index.html', **context)

@app.route('/about')
def about():
    context = make_context()

    f = codecs.open("posts/intro.md", mode="r", encoding="utf-8")
    contents = f.read()
    html = markdown.markdown(contents)
    context['markdown'] = Markup(html)

    return render_template('post.html', **context)

@app.route('/posts/<string:slug>')
def _post(slug):
    context = make_context()

    f = codecs.open("posts/%s.md" % slug, mode="r", encoding="utf-8")
    contents = f.read()
    html = markdown.markdown(contents)
    context['markdown'] = Markup(html)

    return render_template('post.html', **context)

app.register_blueprint(static.static)

# Boilerplate
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port')
    args = parser.parse_args()
    server_port = 8000

    if args.port:
        server_port = int(args.port)

    app.run(host='0.0.0.0', port=server_port, debug=app_config.DEBUG)
