from flask import Flask, request, render_template, flash, redirect, url_for
import numpy as np
import pickle

app = Flask(__name__, template_folder="templates")
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# Load the model
model = pickle.load(open('prediction_model.pkl', 'rb'))

# Helper function to convert 'Yes'/'No' to 1/0
def yes_no_to_int(value):
    return 1 if value.strip().lower() == 'yes' else 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/predict', methods=['POST'])
def predict():
    try:
        print("Form data received:", request.form)

        cgpa = request.form.get('cgpa', '0')
        projects = yes_no_to_int(request.form.get('projects', 'No'))
        workshops = request.form.get('certifications', '0')
        mini_projects = request.form.get('mini_projects', '0')
        skills = request.form.get('skills', '')
        communication_skills = request.form.get('Communication Skills Rating', '0')
        internship = yes_no_to_int(request.form.get('internships', 'No'))
        hackathon = yes_no_to_int(request.form.get('hackathon', 'No'))
        tw_percentage = request.form.get('12th percentage', '0')
        te_percentage = request.form.get('10th percentage', '0')
        backlogs = request.form.get('backlogs', '0')


        # Skill count logic
        skill_count = 1 if skills.strip() != '' else 0
        skill_count += skills.count(',')

        features = np.array([
            float(cgpa), float(projects), float(workshops), float(mini_projects),
            float(skill_count), float(communication_skills), float(internship),
            float(hackathon), float(tw_percentage), float(te_percentage), float(backlogs)
        ])

        print("Features prepared for prediction:", features)

        output = model.predict([features])[0]
        print("Prediction output:", output)

        if output == 1:
            flash('🎉 Congratulations!! You have high chances of getting placed!\nKeep up the good work and continue sharpening your skills!', 'success')
        else:
            flash('🙁 Sorry! You have low chances of getting placed.\nFocus on building projects, gaining certifications, and practicing interviews.', 'danger')

        return redirect(url_for('home'))

    except Exception as e:
        print("❌ Error in /predict route:", str(e))
        flash(f"⚠️ Something went wrong: {str(e)}", 'warning')
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
