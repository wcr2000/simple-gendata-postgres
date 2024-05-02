# Create Database postgres with container
Follow the step<br>
1.docker pull
```cmd
docker pull postgres:latest
docker run --name test-postgres -e POSTGRES_PASSWORD=root -e POSTGRES_DB=test -p 5432:5432 -d postgres
```
<br>You should have postgres images and container in your docker

# Generate simple data in python