from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

expenses = []

@app.route('/')
def index():
    return render_template('index.html', expenses=expenses)

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        description = request.form['description']
        total = float(request.form['total'])
        participants = request.form.getlist('participants')
        num_participants = len(participants)
        part_per_person = total / num_participants
        expense = {
            'description': description,
            'total': total,
            'participants': participants,
            'part_per_person': part_per_person
        }
        expenses.append(expense)
        return redirect(url_for('index'))
    return render_template('calculator.html')

if __name__ == '__main__':
    app.run(debug=True)
