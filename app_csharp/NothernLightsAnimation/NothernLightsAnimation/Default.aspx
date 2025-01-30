<%@ Page Title="Home Page" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="NothernLightsAnimation._Default" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Northern Lights Animation</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body, html {
                width: 100%;
                height: 100%;
                overflow: hidden;
                background: black;
                font-family: Arial, sans-serif;
            }
            h1 {
                position: absolute;
                top: 10%;
                width: 100%;
                text-align: center;
                color: white;
                font-size: 2.5rem;
                z-index: 2;
            }
            .northern-lights {
                position: absolute;
                width: 100%;
                height: 100%;
                background: linear-gradient(45deg, rgba(0, 0, 0, 0.5), 
                rgba(0, 255, 150, 0.6), 
                rgba(0, 0, 255, 0.6), 
                rgba(245, 165, 206, 1),
                rgba(0, 0, 0, 0.5));
                background-size: 200% 200%;
                animation: aurora 8s infinite alternate;
            }
            @keyframes aurora {
                0% {
                    background-position: 0% 50%;
                }
                100% {
                    background-position: 100% 50%;
                }
            }
    </style>
    </head>
    <body>
        <form id="form1" runat="server">
            <h1>Welcome to the Northern Lights Show!</h1>
            <div class="northern-lights"></div>
        </form>
    </body>
</html>
    

</asp:Content>
