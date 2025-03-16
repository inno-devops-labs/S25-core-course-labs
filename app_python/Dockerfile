# Use a precise version of base image
FROM python:3.11-bullseye

# Create a new user 'angelika2707' and set up the app directory
RUN useradd angelika2707 \
    && mkdir /app \
    && chown -R angelika2707 /app

# Set the working directory
WORKDIR /app

# Copy the requirements.txt and main.py into the /app
# and set the ownership to the 'angelika2707' user
COPY --chown=angelika2707:angelika2707 requirements.txt main.py /app/

# Create /templates inside /app and set the ownership
RUN mkdir /app/templates && \
    chown -R angelika2707 /app/templates

# Copy /templates into /app/templates,
# and set the ownership to the 'angelika2707' user
COPY --chown=angelika2707:angelika2707 templates/ /app/templates/

# Copy /visits into /app/visits/
# and set the ownership to the 'angelika2707' user
COPY --chown=angelika2707:angelika2707 visits/ /app/visits/

# Install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Switch to the 'angelika2707' user
USER angelika2707

# Running main.py
CMD ["python", "main.py"]