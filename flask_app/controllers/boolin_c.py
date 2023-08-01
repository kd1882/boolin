from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.boolin_m import Boolin
from flask_app.config.utils import synonyms

@app.route('/createBool', methods=['POST'])
def createBool():
    print(request.form)

    temp_bool = Boolin.boolean_search_generator(request.form["query_string"], synonyms)

    session["string_output"] = temp_bool
    return redirect('/')
