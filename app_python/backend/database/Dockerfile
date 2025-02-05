FROM postgres:13

# Set environment variables
ENV POSTGRES_DB=times
ENV POSTGRES_USER=myuser

# Copy the initialization SQL script
COPY init.sql /docker-entrypoint-initdb.d/init.sql
