using Microsoft.AspNetCore.Mvc;
using MoscowTimeApp.Models;
using Prometheus;
using System.Diagnostics;

namespace MoscowTimeApp.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        private static readonly Counter MoscowTimeRequests = Metrics
            .CreateCounter("moscow_time_requests_total", "Number of requests to the Moscow Time endpoint.");

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            MoscowTimeRequests.Inc();

            // Get Moscow time (UTC+3)
            DateTime utcTime = DateTime.UtcNow;
            DateTime moscowTime = utcTime.AddHours(3);
            ViewBag.MoscowTime = moscowTime.ToString("yyyy-MM-dd HH:mm:ss");
            return View();
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
