from flask import Blueprint #define that this file is a blueprint of our application (contains routes, urls, etc.)
from flask import render_template #import the render_template function
from flask_login import login_required, current_user
from flask import request #import request function to enable redirects to form requests
from flask import flash #import flash function for alerting if input is not vaild
from .models import Note
from . import db
import json
from flask import jsonify


views = Blueprint('views', __name__) #define a blueprint

#to define a view:
@views.route('/', methods=['GET', 'POST']) #the home() function (defined below) will run whenever we go to our "/" route (homepage)
@login_required

def home():

    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short.', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note Added !', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])

def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})