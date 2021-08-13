from flask import Blueprint, request, url_for, render_template, redirect
import pickle

from .forms import PromptForm

bp = Blueprint("robot", __name__, url_prefix="/")


def parse_output(output):
    lst_of_str = []
    for dct in output:
        str = dct["generated_text"]
        lst_of_str.append(str)
        return "".join(lst_of_str)


@bp.route("/talk", methods=["GET", "POST"])
@bp.route("/", methods=["GET", "POST"])
def talk():
    form = PromptForm()
    if form.validate_on_submit():
        prompt = form.prompt.data
        return redirect(url_for("robot.predict", prompt=prompt))
    return render_template("index.html", form=form)


@bp.route("/predictions", methods=["GET", "POST"])
def predict():
    prompt = request.args.get("prompt")
    with open("flaskr/generator.bin", "rb") as f_in:
        model = pickle.load(f_in)
    txt = parse_output(model(prompt, max_length=200))
    print(txt)
    return txt
