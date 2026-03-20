from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Workout
import os
from sqlalchemy import func
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database path
# Uses DATABASE_URL from environment if set, allowing persistent disk storage in production.
# Falls back to local workouts.db for development.
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'workouts.db'))

app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'super_secret_key_for_flash_messages' # Needed for displaying 'flash' alerts

db.init_app(app)

# Create the database tables automatically if they don't exist yet
with app.app_context():
    db.create_all()

@app.route('/')
def dashboard():
    """
    Renders the main dashboard page.
    Queries the database for Personal Records (max weight) grouped by exercise.
    Also fetches the 5 most recent workouts to display.
    """
    # Get PRs (max weight per exercise) using SQLAlchemy func.max
    prs = db.session.query(
        Workout.exercise_name, 
        func.max(Workout.weight).label('max_weight')
    ).group_by(Workout.exercise_name).all()
    
    # Get the latest 5 workouts
    recent_workouts = Workout.query.order_by(Workout.date.desc()).limit(5).all()
    
    return render_template('dashboard.html', prs=prs, recent_workouts=recent_workouts)

@app.route('/history')
def history():
    exercise_filter = request.args.get('exercise')
    if exercise_filter:
        workouts = Workout.query.filter(Workout.exercise_name.ilike(f'%{exercise_filter}%')).order_by(Workout.date.desc()).all()
    else:
        workouts = Workout.query.order_by(Workout.date.desc()).all()
    
    # Get all unique exercises for the filter dropdown
    exercises = db.session.query(Workout.exercise_name).distinct().all()
    exercises = [e[0] for e in exercises]
    
    return render_template('history.html', workouts=workouts, exercises=exercises, selected_filter=exercise_filter)

@app.route('/add', methods=['GET', 'POST'])
def add_workout():
    if request.method == 'POST':
        exercise_name = request.form['exercise_name']
        sets = int(request.form['sets'])
        reps = int(request.form['reps'])
        weight = float(request.form['weight'])
        notes = request.form.get('notes', '')
        
        workout = Workout(
            exercise_name=exercise_name,
            sets=sets,
            reps=reps,
            weight=weight,
            notes=notes
        )
        
        date_str = request.form.get('date')
        if date_str:
             workout.date = datetime.strptime(date_str, '%Y-%m-%d')
             
        workout.total_volume = workout.calculate_volume()
        
        db.session.add(workout)
        db.session.commit()
        flash('Workout added successfully!', 'success')
        return redirect(url_for('history'))
        
    return render_template('add_workout.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_workout(id):
    workout = Workout.query.get_or_404(id)
    if request.method == 'POST':
        workout.exercise_name = request.form['exercise_name']
        workout.sets = int(request.form['sets'])
        workout.reps = int(request.form['reps'])
        workout.weight = float(request.form['weight'])
        workout.notes = request.form.get('notes', '')
        
        date_str = request.form.get('date')
        if date_str:
            workout.date = datetime.strptime(date_str, '%Y-%m-%d')
            
        workout.total_volume = workout.calculate_volume()
        
        db.session.commit()
        flash('Workout updated successfully!', 'success')
        return redirect(url_for('history'))
        
    return render_template('edit_workout.html', workout=workout)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_workout(id):
    workout = Workout.query.get_or_404(id)
    db.session.delete(workout)
    db.session.commit()
    flash('Workout deleted successfully!', 'success')
    return redirect(url_for('history'))

@app.route('/api/chart_data')
def chart_data():
    """
    API Endpoint returning JSON data for Chart.js.
    Aggregates the total workout volume per day to plot progress over time.
    """
    workouts = Workout.query.order_by(Workout.date).all()
    
    # We aggregate in Python to keep it database agnostic and simple
    summary = {}
    for w in workouts:
        date_key = w.date.strftime('%Y-%m-%d')
        if date_key in summary:
            summary[date_key] += w.total_volume
        else:
            summary[date_key] = w.total_volume
            
    labels = list(summary.keys())
    data = list(summary.values())
    
    return {'labels': labels, 'data': data}

if __name__ == '__main__':
    # Start the Flask app for production
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
