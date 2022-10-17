from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__) #name of the variable

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
  if request.method == 'POST':
    note = request.form.get('note')

    if len(note) < 1:
      flash('Note is too short!', category='error')
    else:
      new_note = Note(data=note, user_id=current_user.id)
      db.session.add(new_note)
      db.session.commit()
      flash('Note added!', category='success')
  return render_template("home.html", user=current_user) #we will be able to in our template, reference this current user and check if it's authenticated
  
@views.route('/delete-note', methods=['POST'])
def delete_note():
  note = json.loads(request.data) # take in some data from post request
  noteId = note['noteId'] # turn the string in index.js to python dictionary, access the noteId attribute(which is declared in index.js)
  note = Note.query.get(noteId) # look for the note that has the noteId
  if note: # check if it exists or not
    if note.user_id == current_user.id:
      db.session.delete(note)
      db.session.commit()
  return jsonify({}) # return an empty response
