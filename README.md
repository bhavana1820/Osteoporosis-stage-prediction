# Osteoporosis-stage-prediction

to create env : python -m venv venv
if error try : Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

then to activate : env\Scripts\activate

pip install -r requirements.txt

python src/model_training.py

streamlit run app/app.py
