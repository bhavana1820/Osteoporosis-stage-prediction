# Osteoporosis-stage-prediction

<!-- To create environment  -->
python -m venv venv

if error try : Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned


<!-- then to activate venv  -->
venv\Scripts\activate


<!-- Intsall the requirements -->
pip install -r requirements.txt


<!-- To create dataset  -->
python .\dataset\create_dataset.py


<!-- Train the model -->
python .\src\model_training.py


<!-- Run the Streamlit app -->
streamlit run app/app.py


<!-- To deactivate environment -->
deactivate 


<!-- To change the settings to it's original setting -->
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Restricted


File structure :

osteoporosis-prediction/
├── app/
│ └── app.py   # Streamlit web application
├── dataset/
│ ├── osteoporosis_data_men.csv
│ ├── osteoporosis_data_women.csv
│ └── create_dataset.py   # Script to generate synthetic datasets
├── src/
│ ├── data_preprocessing.py   # Data preprocessing & scaler functions
│ └── model_training.py   # Train and save models
│ └── evaluate_model.py   # Evaluate accuracy and metrics
├── model_men.pkl
├── model_women.pkl
├── README.md
└── requirements.txt
