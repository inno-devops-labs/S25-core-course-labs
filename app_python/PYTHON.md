# Python web-application

### Framework: `Flask`
I have chosen this lightweight web framework due to its simplicity
in usage. It is easy to create a toy web application with Flask.
Moreover, it is flexible and easy to extend in the future if needed.

### Best practices
* **Modularity**: HTML code and CSS styles are splitted from the Python code
* **Error handling**: checking whether the given timezone exists or not
* **Easy to update/modify**: the name of the city and appropriate timezone are in global vars
* **Comments**: help to navigate in the code


### Manual Testing
Checked manually for different cities and timezones (for instance,
Europe/Berlin and Asia/Tokyo). Moreover, checked the behaviour in case of an invalid
timezone.

### Unit tests
I have considered two major aspects: getting timezone and the home page itself.
Therefore, I check both in a valid case with default timezone, then I give
invalid (unknown) timezone and check the behaviour of the function related
to returning currrent time (should return None in this case) and main
function related to rendering the page (should return status 200 and a
message that contains info about 'timezone'). Moreover, I check that time
changes constantly (sleep for a couple of seconds and compare two responses).

#### Best practices
* **Use of test client**: to test accessibility of different routes (in this case
only '/' - home page)
* **Separation**: tests are splitted from the main application and have no influence
on it
* **Testing invalid (edge) cases**: related to invalid timezone
* **Simplicity**: tests are logical and simple

