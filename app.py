from flask import Flask, render_template, request
from stories import Story, story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

@app.route("/")
def madlibs_form():
  # story = Story(
  #     ["place", "noun", "verb", "adjective", "plural_noun"],
  #     """Once upon a time in a long-ago {place}, there lived a
  #      large {adjective} {noun}. It loved to {verb} {plural_noun}."""
  # )
  return render_template("index.html",words=story.prompts)


@app.route("/story")
def madlibs_story():
  sentence = story.generate(request.args)
  return render_template("story.html", new_story=sentence)
