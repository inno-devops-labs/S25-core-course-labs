# C web application design

## Framework choice

I decided to use [Mongoose](https://github.com/cesanta/mongoose) for this task since
it allowed me to write the application in pure C instead of C++, is used by multiple big companies,
is relatively easy to set up, has no dependencies, and can be asynchronous.

I also have decided not to use Cmake or other similar build tools because of the size of the project,
that can easily be compiled and executed in a command line by hands.

## Best practices

### Code quality

I used the following techniques to ensure code standarts and code quality:

- Moving the timezone into a global constant variable
- Commenting
- Using cpplint for checking codestyle
- Abstracting pieces of code into functions so that actual page code is small
- Rudimentary logging so that activity on the page can be seen
- Descriptive or standart variable names

### Testing

I tested the application in different timezones, and it provided me with the
same time as before, the Moscow time. The time is neatly formatted and even
displays nicely on mobile devices. CSS sheet loads correctly and affects page.

### Other

HTML template was changed a bit to better fit C formatting, and both HTML and CSS are still separate
from the main code and load in at runtime. I have implemented a default error message so that
the user gets a reply in any circumstance. All the mongoose files are in a separate folder,
which is then used in compilation.
