# 1. Use a compatible version
FROM python:3.11-slim

# 2. Set rootless user and make the working directory
RUN useradd dew1769 && mkdir /app && chown -R dew1769 /app

# 3. Working directory
WORKDIR /app

# 4. Copy necessary files to the working directory and install dependencies
COPY --chown=dew1769:dew1769 requirements.txt app.py /app/
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expose the application's port
EXPOSE 5000

# 6. Switch the user
USER dew1769

# 7. Set the command to run app.py
CMD ["python", "app.py"]