using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Moq;
using MoscowTimeApp.Controllers;
using MoscowTimeApp.Models;

public class HomeControllerTests
{
    private readonly Mock<ILogger<HomeController>> _mockLogger;
    private readonly HomeController _controller;

    public HomeControllerTests()
    {
        _mockLogger = new Mock<ILogger<HomeController>>();
        _controller = new HomeController(_mockLogger.Object);
    }

    [Fact]
    public void Index_ReturnsViewWithMoscowTime()
    {
        // Act
        var result = _controller.Index() as ViewResult;

        // Assert
        Assert.NotNull(result);
        Assert.NotNull(result.ViewData);
        Assert.True(result.ViewData.ContainsKey("MoscowTime"));

        // Validate Moscow time calculation
        string? moscowTimeStr = result.ViewData["MoscowTime"] as string;
        Assert.NotNull(moscowTimeStr);

        DateTime parsedTime;
        Assert.True(DateTime.TryParse(moscowTimeStr, out parsedTime));

        DateTime expectedMoscowTime = DateTime.UtcNow.AddHours(3);
        Assert.Equal(expectedMoscowTime.ToString("yyyy-MM-dd HH:mm"), parsedTime.ToString("yyyy-MM-dd HH:mm"));
    }

    [Fact]
    public void Privacy_ReturnsView()
    {
        // Act
        var result = _controller.Privacy() as ViewResult;

        // Assert
        Assert.NotNull(result);
    }
}
