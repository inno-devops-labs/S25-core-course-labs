using Microsoft.AspNetCore.Mvc;
using MoscowTimeApp.Models;
using Prometheus;
using System.Diagnostics;

namespace MoscowTimeApp.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        private static readonly string VisitsFilePath = Path.Combine("data", "visits");

        private static readonly Counter MoscowTimeRequests = Metrics
            .CreateCounter("moscow_time_requests_total", "Number of requests to the Moscow Time endpoint.");

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            MoscowTimeRequests.Inc();
            IncrementVisitCount();
            
            // Get Moscow time (UTC+3)
            DateTime utcTime = DateTime.UtcNow;
            DateTime moscowTime = utcTime.AddHours(3);
            ViewBag.MoscowTime = moscowTime.ToString("yyyy-MM-dd HH:mm:ss");
            return View();
        }

        [HttpGet("/visits")]
        public IActionResult Visits()
        {
            int count = GetVisitCount();
            return Content($"Visits: {count}", "text/plain");
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

        private int GetVisitCount()
        {
            try
            {
                if (!Directory.Exists(Path.GetDirectoryName(VisitsFilePath)))
                {
                    Directory.CreateDirectory(Path.GetDirectoryName(VisitsFilePath));
                }

                if (!System.IO.File.Exists(VisitsFilePath))
                {
                    System.IO.File.WriteAllText(VisitsFilePath, "0");
                }

                string content = System.IO.File.ReadAllText(VisitsFilePath);
                return int.TryParse(content, out int count) ? count : 0;
            }
            catch
            {
                return 0;
            }
        }

        private void IncrementVisitCount()
        {
            int count = GetVisitCount() + 1;
            System.IO.File.WriteAllText(VisitsFilePath, count.ToString());
        }
    }
}
