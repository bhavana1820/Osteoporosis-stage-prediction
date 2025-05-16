# Osteoporosis-stage-prediction


-> Clone the repository :

git clone https://github.com/bhavana1820/Osteoporosis-stage-prediction.git


-> To create environment : 

python -m venv venv

if error try : Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned


-> then to activate venv :

venv\Scripts\activate


-> Intsall the requirements : 

pip install -r requirements.txt


-> To create dataset : 

python .\dataset\create_dataset.py


-> Train the model : 

python .\src\model_training.py


-> Run the Streamlit app : 

streamlit run app/app.py


-> To deactivate environment : 

deactivate 


-> To change the settings to it's original setting : 

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Restricted


File structure :

![File Structure](https://github.com/user-attachments/assets/ef387dcb-df04-47a1-98e0-956b62e3b1e3)
