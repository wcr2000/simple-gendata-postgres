# Create Database postgres with container
Follow the step<br>
1.Docker Pull & Run in cmd
```cmd
docker pull postgres:latest
docker run --name test-postgres -e POSTGRES_PASSWORD=root -e POSTGRES_DB=test -p 5432:5432 -d postgres
```
<br>You should have postgres images and container in your docker and run localhost<br>
From above you will connect database by this information
```python
dbname = "test"
user = "postgres"
password = "root"
host = "localhost"
port = "5432"
```

# Generate simple data in python
when you finish step setup container from above you can next step with python
<br>
don't forget create environment
<br>
```cmd
cd your_path\project

python -m venv env

env\scripts\activate
```
and pip install lib
```cmd
pip install requirements.txt
```
<br>
when you setting env finished you can config about username , password , ... in connect_postgres_db.py

<br>and Run main.py
```cmd
py main.py
```