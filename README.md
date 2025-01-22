
# MediTrain AI - Medical Assistant

## Overview

MediTrain AI is an AI-powered medical assistant designed to provide users with accurate, empathetic, and clear answers to medical queries. Built using advanced AI models and Flask, MediTrain AI emphasizes user-friendly interactions while ensuring that users are reminded to seek professional healthcare advice for proper diagnosis and treatment.

## Features

* Conversational Context: Retains the context of recent interactions to provide relevant and cohesive responses.
* Medical Focus: Tailored to assist with general medical questions while avoiding direct diagnoses.
* Flask UI: Intuitive and interactive web-based interface for seamless user interaction.
* Empathetic Responses**: Ensures responses are clear, considerate, and accurate.

## Prerequisites

To run MediTrain AI locally, ensure you have the following:

* Python 3.8+
* Libraries specified in `requirements.txt`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/HarshitaVG/MediTrain-AI.git
   cd MediTrain-AI
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python run.py
   ```
2. Open the application in your browser (default: [http://localhost:5000](http://localhost:5000/)).
3. Interact with MediTrain AI by entering your medical queries on the prescription page.

## Project Structure

* `app/`: Main application folder.
  * `__init__.py`: Initializes the Flask application.
  * `routes.py`: Contains the routes and logic for handling requests and generating prescriptions.
  * `static/`: Contains static files like CSS and images.
    * `css/`: Folder for CSS files.
      * `styles.css`: External CSS file for styling your HTML pages (optional if you're using inline CSS).
    
  * `templates/`: Contains HTML templates.
    * `index.html`: Home page template.
    * `prescribe.html`: Prescription page template.
  * `models/`: Contains machine learning models and vectorizers.
    * `prescription_model.pkl`: Trained prescription model file.
    * `vectorizer.pkl`: Trained vectorizer file.

* `requirements.txt`**: List of required Python packages.
* `main.py`: Main script to run your Flask application.
* `README.md`: Project documentation.

## Key Libraries

* Flask: For building the user interface.
* scikit-learn: For machine learning models.
* joblib: For saving and loading models.

## Important Notes

* MediTrain AI is designed as a medical assistant but does not provide medical diagnoses or treatment plans.
* Always consult a certified healthcare professional for medical concerns.

## Future Enhancements

* Add support for multilingual queries.
* Enhance conversation memory to retain context over extended sessions.
* Introduce additional models for region-specific medical advice.

## License

This project is licensed under the MIT License.

---

Enjoy using MediTrain AI and let us know if you have suggestions or encounter issues!

