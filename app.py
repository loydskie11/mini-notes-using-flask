from flask import Flask, render_template, request, redirect

app = Flask(__name__)
notes = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        note = request.form.get('note')
        if note:
            notes.append(note)
        return redirect('/')
    
    query = request.args.get('query', '').strip()
    filtered_notes = []

    if query:
        if query.isdigit():
            idx = int(query)
            if 0 <= idx < len(notes):
                filtered_notes = [notes[idx]]
        else:
            filtered_notes = [note for note in notes if query.lower() in note.lower()]
    else:
        filtered_notes = notes
    return render_template('index.html', notes=filtered_notes, query=query)

@app.route('/delete/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    if 0 <= note_id < len(notes):
        notes.pop(note_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
