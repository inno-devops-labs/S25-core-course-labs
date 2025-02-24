# Stage 1: Build the application
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build

# Set working directory to match the project's subfolder
WORKDIR /src/MoscowTimeApp

# Copy project file and restore dependencies
COPY MoscowTimeApp/*.csproj .
RUN dotnet restore

# Copy remaining source code
COPY MoscowTimeApp/ .

# Publish the app
RUN dotnet publish "MoscowTimeApp.csproj" \
    -c Release \
    -o /app \
    --no-restore

# Stage 2: Runtime image
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS runtime
WORKDIR /app

# Copy build artifacts from the build stage
COPY --from=build /app .

# Set environment variables for production
ENV ASPNETCORE_ENVIRONMENT=Production
ENV ASPNETCORE_URLS=http://+:80

# Create non-root user
RUN adduser -u 5678 --disabled-password --gecos "" appuser && \
    chown -R appuser:appuser /app
USER appuser

# Expose port and run the app
EXPOSE 80
ENTRYPOINT ["dotnet", "MoscowTimeApp.dll"]