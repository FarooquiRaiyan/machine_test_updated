Steps to Install Run the Project 

Step 1: Clone the Repo https://github.com/FarooquiRaiyan/machine_test_updated.git 

Step 2:Move to the Machine Test Updated Folder.

Step 3:Create abd Activate the Virtual Environment by (venv\Scripts\activate)

Step 4 : Install the Packages by pip install requirements.txt

Step 5 : Create a database updated_db_fastapi

Step 6 : Create a .env file and add the password there DB_PASSWORD = PASSWORD

Step 7 : Execute the Programme by command  uvicorn main:app  --reload

Step 8 : Check if its working for Categories http://localhost:8000/api/categories

Step 9 : Check if its working for Products http://localhost:8000/api/products

Step 10 : Go for the  Docs : http://localhost:8000/docs 


Schema 
create database updated_db_fastapi;
use updated_db_fastapi;
