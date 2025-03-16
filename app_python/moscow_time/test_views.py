from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.utils.timezone import now 


class TestHomePage(TestCase):
    def test_home_page_status_code(self): 
        url = reverse('moscow_time')
        response = self.client.get(url) 
        self.assertEqual(response.status_code, 200) 
        
    def test_home_page_template_used(self): 
        url = reverse('moscow_time') 
        response = self.client.get(url) 
        self.assertTemplateUsed(response, 'time_display.html')
    
    def test_title_contains(self): 
        url = reverse('moscow_time') 
        response = self.client.get(url)
        self.assertContains(response, "<title>Current Time</title>")
        
    def test_page_shows_current_time(self):
        url = reverse('moscow_time')
        response = self.client.get(url) 
        self.assertContains(response, '<h1 id="time"></h1>') 
        
        self.assertContains(response, 'function updateTime() {')
        self.assertContains(response, 'setInterval(updateTime, 1000);')
        self.assertContains(response, "document.getElementById('time').innerText = moscowTime;")
        self.assertContains(response, "timeZone: 'Europe/Moscow'")
        
    def test_return_404_for_invalid_url(self): 
        response = self.client.get('/invalid_url')
        self.assertEqual(response.status_code, 404) 