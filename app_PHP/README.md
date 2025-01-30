# PHP Web Application: Display Current Time in Moscow

As the title says, this application uses **PHP** to display current time in Moscow rendering.

**PHP** as a language is ideal for such small applications as this.

I use
```date_default_timezone_set('Europe/Moscow');)```
to initialize the timezone to Moscow, as we need to be accurate to it's time

I also use `date('Y-m-d H:i:s')` to format the time in line `$current_time = date('Y-m-d H:i:s');` to follow the most common time formats.

## Installation

To run the application locally you need to have PHP on your machine:

1. **Clone the repository:**
```bash
git clone https://your-repository-url.git
cd app_python
```

2. **Install PHP (if necessary):**

For windows [this link](https://windows.php.net/downloads/releases/php-8.4.3-Win32-vs17-x64.zip) is sufficient, 
but depending on your machine you might need to find another option in [the official site](https://www.php.net/manual/en/install.php).

3. **Navigate to the app:**

In the terminal, navigate to the ```app_PHP``` folder.
4. **Run the app:**
```bash 
php -S 0.0.0.0:8000 PHPtest.php
```

*Note:* I assume that you have inserted the php.exe into your path (for Windows), 
you may need to use the .exe file instead if you do not want to update the path variables.

5. **Follow the browser link:**
    
Go to ``http://127.0.0.1:8000/`` in your browser to view the application.

