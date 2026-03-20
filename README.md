# Workout Tracker

A simple, modern, and lightweight web application for tracking your workouts, personal records, and volume over time. Built with Python, Flask, and an SQLite database, featuring a clean dark-mode UI.

## Features
- **Add Workouts**: Log your exercises, sets, reps, and weights.
- **Track History**: View all your past workouts in a neat, filterable table.
- **Personal Records (PRs)**: Automatically tracks and displays your highest weight lifted per exercise.
- **Volume tracking**: Automatically calculates and charts your total workout volume over time.
- **Dark Mode**: Comes with a built-in dark mode toggle for comfortable viewing.
- **No Heavy Frameworks**: Front-end is rendered with pure HTML and vanilla CSS for blistering fast performance.

## Tech Stack
- **Backend**: Python 3, Flask
- **Database**: SQLite (via Flask-SQLAlchemy)
- **Frontend**: HTML5, custom Vanilla CSS, beginner-friendly JavaScript
- **Charting**: Chart.js for data visualization

## How to Run Locally

### Prerequisites
Make sure you have [Python 3](https://www.python.org/downloads/) installed on your machine.

### Installation & Setup

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone https://github.com/nithipan123-creator/workout_tracker.git
   cd workout-tracker
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   
   # Windows:
   .venv\Scripts\activate
   
   # MacOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Open your browser**:
   Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000). The `workouts.db` database file will automatically be created the first time the app starts.

## Future Improvements & Ideas
*Feel free to tackle these as you expand the project!*
- **User Authentication**: Allow multiple users to register and have their own separate workout logs.
- **Export to CSV**: Add a button to let users download their workout history.
- **Rest Timer**: Include a simple JavaScript countdown timer on the "Add Workout" page.
- **Exercise Database**: Pre-populate a list of exercises to choose from via a dropdown rather than typing the name manually every time.
- **Muscle Group Tags**: Tag exercises by muscle group (e.g., Chest, Back, Legs) and chart which groups are being trained the most.
- **Pagination**: As the history table grows, split it into multiple pages.
- **Responsive Dashboard Cards**: Enhance the UI to allow drag-and-drop customization of widget placement.
