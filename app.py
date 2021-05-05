from flask import Flask, render_template, request
from stories import story_bank
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

@app.route("/")
def template_selection():
  return render_template("index.html",story_bank=story_bank)

@app.route("/form")
def madlibs_form():
  user_selection = request.args["template"]
  for story in story_bank:
     if story.title == user_selection:
       selected_story = story
  return render_template("form.html", story=selected_story)


@app.route("/story")
def madlibs_story():
  for story in story_bank:
     if story.title == request.args["title"]:
       selected_story = story
  sentence = selected_story.generate(request.args)
  return render_template("story.html", new_sentence=sentence)
