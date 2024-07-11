
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_planner', methods=['POST'])
def create_planner():
    tasks = request.form.getlist('tasks[]')
    time_slots = request.form.getlist('time_slots[]')

    planner = create_smart_planner(tasks, time_slots)

    return render_template('planner.html', planner=planner)

@app.route('/delete_planner')
def delete_planner():
    delete_planner_data()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
