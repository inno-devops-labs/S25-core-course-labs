# Stage 1: Build the application
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src/MoscowTimeApp
COPY MoscowTimeApp/*.csproj .
RUN dotnet restore
COPY MoscowTimeApp/ .
RUN dotnet publish "MoscowTimeApp.csproj" \
    -c Release \
    -o /app \
    --no-restore

# Stage 2: Use Distroless .NET runtime image (nonroot by default)
FROM mcr.microsoft.com/dotnet/aspnet:8.0-noble-chiseled
WORKDIR /app

# Copy build artifacts and set ownership for nonroot user (UID 65532)
COPY --from=build --chown=65532:65532 /app .

# Set environment variables for production
ENV ASPNETCORE_ENVIRONMENT=Production
ENV ASPNETCORE_URLS=http://+:80

# Run as nonroot user (pre-configured in Distroless)
USER 65532:65532

# Expose port and run the app
EXPOSE 80
ENTRYPOINT ["dotnet", "MoscowTimeApp.dll"]