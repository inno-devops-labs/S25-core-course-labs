'''
COMMENT
'''
from datetime import datetime
import re
import unittest
from moscow_app import app, MOSCOW


class TestMoscowApp(unittest.TestCase):
    '''
    DOCSTRING CLASS
    '''
    test_app = app.test_client()

    def test_status_code(self):
        '''
        Check that request to html page is granted
        '''
        response = self.test_app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_response_content(self):
        '''
        To check that the html content consists of required message
        '''
        response = self.test_app.get('/')
        self.assertIn(b'Moscow Time:', response.data)
    
    def test_validate_time(self):
        '''
        comment
        '''
        response = self.test_app.get('/')
        msc = datetime.now(MOSCOW)
        current = datetime.today()
        # needed to measure time units to cast to a single integer
        # meaning number of seconds
        values = [3600, 60, 1]
        # needed to prove approximate equality between
        # 23:59:59 and 00:00:01 time dates, for instance
        cycle = 3600 * 60 * 24
        # error means what difference between times is allowed to be true
        error = 5

        response_text = response.data.decode('utf-8')

        start = response_text.find("Moscow Time:")
        msc_response = re.search(r'\d\d:\d\d:\d\d', response_text[start:]).group(0)
        tmp = [int(x) for x in msc_response.split(":")]
        msc_response = sum(a*b for a,b in zip(values,tmp))

        start = response_text.find("Your Timezone:")
        current_response = re.search(r'\d\d:\d\d:\d\d', response_text[start:]).group(0)
        tmp = [int(x) for x in current_response.split(":")]
        current_response = sum(a*b for a,b in zip(values, tmp))

        # Gathering datetime the same way as in our app
        tmp = [int(x) for x in msc.strftime("%H:%M:%S").split(":")]
        msc = sum(a*b for a,b in zip(values, tmp))
        tmp = [int(x) for x in current.strftime("%H:%M:%S").split(":")]
        current = sum(a*b for a,b in zip(values, tmp))

        self.assertTrue(abs(msc_response-msc) <= error
            or abs(abs(msc_response - msc) - cycle) <= error)
        self.assertTrue(abs(current_response-current) <= error
            or abs(abs(current_response - current) - cycle) <= error)

if __name__ == '__main__':
    unittest.main()
