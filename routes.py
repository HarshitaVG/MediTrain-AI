import joblib
from flask import render_template, request, flash, redirect, url_for, session
from app import app

# Load the trained model and vectorizer
model = joblib.load('models/prescription_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

# Define follow-up questions based on symptoms
follow_up_questions = {
    'cough': ['Is the cough dry or productive? (Answer: dry/productive)', 'How long have you had the cough? (Answer in days)', 'Do you have any other symptoms like fever or chills? (Answer: Yes/No)'],
    'fever': ['How high is your fever? (Answer: low/medium/high)', 'How long have you had the fever? (Answer in days)', 'Do you have any other symptoms like headaches or body aches? (Answer: Yes/No)'],
    'fatigue': ['How severe is your fatigue? (Answer: mild/moderate/severe)', 'Do you feel fatigued all the time or only at certain times? (Answer: all the time/sometimes)', 'Have you noticed any other symptoms along with fatigue? (Answer: Yes/No)']
    # Add more symptom mappings as needed
}

# Define possible diagnoses based on answers
diagnosis_mapping = {
    'cough': {
        'productive': 'bronchitis, pneumonia',
        'dry': 'asthma, viral infection',
        'fever': 'flu, COVID-19'
    },
    'fever': {
        'high': 'infection, inflammatory disease',
        'headache': 'flu, meningitis',
        'body aches': 'flu, viral infection'
    },
    'fatigue': {
        'severe': 'anemia, chronic fatigue syndrome',
        'constant': 'depression, thyroid disorder',
        'other symptoms': 'mono, autoimmune disease'
    }
    # Add more mappings as needed
}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/prescribe', methods=['GET', 'POST'])
def prescribe():
    if request.method == 'POST':
        if 'follow_up_stage' not in session:
            symptoms = request.form['symptoms']
            if not symptoms.strip():
                flash('Please enter symptoms.')
                return redirect(url_for('prescribe'))

            session['symptoms'] = symptoms
            session['follow_up_stage'] = 0
            session['answers'] = []

        symptoms = session['symptoms']
        follow_up_stage = session['follow_up_stage']
        answers = session['answers']

        symptom_list = [symptom.strip() for symptom in symptoms.split(',')]
        questions = []
        for symp in symptom_list:
            if symp in follow_up_questions:
                questions.extend(follow_up_questions[symp])

        if 'answer' in request.form:
            answer = request.form['answer'].lower().strip()
            if 'how long' in questions[follow_up_stage] and not answer.isdigit():
                flash('Please enter a valid number of days.')
                return render_template('prescribe.html', question=questions[follow_up_stage])
            elif 'yes' in questions[follow_up_stage] and answer not in ['yes', 'no']:
                flash('Please answer with Yes or No.')
                return render_template('prescribe.html', question=questions[follow_up_stage])

            if not answer:
                flash('Please provide an answer.')
                return render_template('prescribe.html', question=questions[follow_up_stage])

            answers.append(answer)
            session['answers'] = answers
            session['follow_up_stage'] += 1
            follow_up_stage += 1

        if follow_up_stage < len(questions):
            question = questions[follow_up_stage]
            return render_template('prescribe.html', question=question)

        # Provide possible diagnoses
        possible_issues = []
        for symptom, answer in zip(symptom_list, answers):
            if symptom in diagnosis_mapping and answer in diagnosis_mapping[symptom]:
                possible_issues.append(diagnosis_mapping[symptom][answer])

        symptoms_vector = vectorizer.transform([symptoms])
        prescription = model.predict(symptoms_vector)

        if not prescription:
            prescription = search_common_prescriptions(symptom_list)

        # Ensure session['symptoms'] is set
        symptom_name = session.get('symptoms', 'specified symptoms')

        # Clear session after prescription
        session.pop('symptoms', None)
        session.pop('follow_up_stage', None)
        session.pop('answers', None)

        return render_template('prescribe.html', prescription=prescription, possible_issues=possible_issues, symptom_name=symptom_name)
    return render_template('prescribe.html')

def search_common_prescriptions(symptoms):
    # Implement the logic to search for common prescriptions based on combined symptoms
    # This is a placeholder function, you'll need to implement the actual search logic
    combined_symptoms = " ".join(symptoms)
    # Example common prescriptions for demonstration purposes
    common_prescriptions = {
        'cough fever': 'acetaminophen, diphenhydramine',
        'fatigue weight loss': 'metformin, fluticasone'
        # Add more common prescriptions as needed
    }
    return common_prescriptions.get(combined_symptoms, 'No common prescription found')
