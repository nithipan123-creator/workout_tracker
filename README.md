# 🏋️ Workout Tracker

A modern, lightweight, and fully functional web application for logging workouts, tracking personal records, and visualizing training volume over time. Built with Python, Flask, and an SQLite database, this project emphasizes a clean, responsive user interface and zero-friction usability.

---

## 🚀 Live Demo
[Click here to use the app](https://workout-tracker-zuib.onrender.com)

---

## ✨ Features

- **Comprehensive Workout Management**: Easily add, edit, and delete workouts. Log your exercises, sets, reps, and weights with precision.
- **Detailed Workout History**: View all your past workouts in a neat, filterable table, ensuring you can always review your past performance.
- **Track Personal Records (PRs)**: Automatically tracks and displays your highest weight lifted per exercise, giving you immediate insight into your progress.
- **Volume Tracking**: Automatically calculates and charts your total workout volume over time to help visualize your training load.
- **Clean UI & Usability**: A meticulously crafted, responsive interface with intuitive navigation and a built-in dark mode toggle for comfortable viewing across all devices.

---

## 🛠️ Tech Stack

- **Backend**: Python 3, Flask
- **Database**: SQLite (managed via Flask-SQLAlchemy)
- **Frontend**: HTML5, Vanilla CSS, JavaScript
- **Charting**: Chart.js for data visualization
- **Deployment**: Render

---

## 💻 Installation & Local Setup

### Prerequisites
Make sure you have [Python 3](https://www.python.org/downloads/) installed on your machine.

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nithipan123-creator/workout_tracker
   cd workout_tracker
   ```

2. **Create and activate a virtual environment** (optional but highly recommended):
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

5. **Access the application**:
   Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) in your web browser. The `workouts.db` database file will automatically be created upon the first launch.

---

## 📖 Usage

1. **Dashboard**: Upon launching, the main dashboard provides a quick overview of your personal records and recent workouts, alongside a volume progress chart.
2. **Add Workout**: Navigate to the "Add Workout" page to log new exercises. Enter the exercise name, sets, reps, and weight.
3. **History**: Go to the "History" tab to view your complete workout log. Use the exercise filter to search for specific movements. You can edit or delete entries directly from this page.

---

## 📂 Project Structure

```text
workout_tracker/
│
├── app.py                  # Main Flask application and routes
├── models.py               # Database schemas and models
├── requirements.txt        # Python dependencies
├── Procfile                # Deployment configuration for Render
├── static/                 # Static assets
│   ├── css/
│   │   └── styles.css      # Custom styling variables and rules
│   └── js/
│       └── main.js         # Frontend interactivity (charts, dark mode)
├── templates/              # HTML templates (Jinja2)
│   ├── base.html           # Base layout
│   ├── dashboard.html      # Home dashboard page
│   ├── history.html        # Workout history table
│   ├── add_workout.html    # Form to insert workouts
│   └── edit_workout.html   # Form to edit workouts
└── README.md               # Project documentation
```

---

## 🔮 Future Improvements

Here are a few technical and feature upgrades planned for the future:

1. **User Authentication**: Implement user registration and login (via Flask-Login) to support multiple independent users.
2. **Exercise Autocomplete**: Pre-populate a database of standard exercises (e.g., Squat, Bench Press, Deadlift) allowing users to select them via a searchable dropdown.
3. **Export Functionality**: Add a feature to let users download their workout history as a CSV or PDF file.
4. **Data Analytics Enhancements**: Provide deeper insights, such as volume per muscle group and average intensity charts.
5. **REST API Migration**: Separate the backend into a standalone RESTful API to support a future mobile application or decoupled frontend framework.
6. **Integration Testing**: Add comprehensive unit and integration tests using `pytest` to ensure application stability.

---
