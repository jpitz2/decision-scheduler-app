python -m venv venv   --> creates virtual environment, only done once
venv\Scripts\activate   --> activates venv, run every time

pip install -r backend/requirements.txt   --> installs requirements, only needs to be done when adding new packages to requirements.txt

cd backend   --> enter "backend" folder
uvicorn main:app --reload   --> run once at beginning of workday, and server will automatically track changes in code and restart server

deactivate --> exits out of venv