from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.debug=True
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)


@app.route("/")
def ask_questions():
    """Generate and show form to ask words."""

    prompts = story.prompts
    return render_template("questions.html", prompts=prompts)


@app.route("/story")
def show_story():
    """Show story result."""

    stories = story.generate(request.args)
    return render_template("story.html", text=stories)



if __name__ == "__main__":
    app.run(debug=True)