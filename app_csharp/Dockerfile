FROM mcr.microsoft.com/dotnet/framework/sdk:4.8 AS build

WORKDIR /NothernLightsAnimation

COPY app_csharp/ .

RUN nuget restore app_csharp/packages.config

RUN msbuild NothernLightsAnimation/NothernLightsAnimation.csproj /p:Configuration=Release

FROM mcr.microsoft.com/dotnet/framework/aspnet:4.8 AS runtime

WORKDIR /inetpub/wwwroot

COPY --from=build /src/app_csharp/bin/Release/ .

EXPOSE 80

CMD ["C:\\Windows\\System32\\inetsrv\\iisreset.exe", "/start"]
