FROM python:3.11-alpine3.15

# working directorate
WORKDIR /app_python 

# copy the file with dependencies to our directory and install them 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# create a new user and grant him permissions to the directory 
RUN adduser -D user
COPY --chown=user:user app.py .
COPY --chown=user:user static/ static/
COPY --chown=user:user templates/ templates/

# switch to the created user 
USER user

# open a port to access the application 
EXPOSE 8000

# run the web application 
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
