# Python application for showing time at Moscow

### Run application with the command
```python
python3 app.py
```

### Framework: `Flask`
I have chosen this lightweight web framework due to its simplicity
in usage. It is easy to create a toy web application with Flask.
Moreover, it is flexible and easy to extend in the future if needed.

### Best practices
* **Modularity**: HTML code is splitted from the Python code
* **Error handling**: checking whether the given timezone exists or not
* **Easy to update/modify**: the name of the city and appropriate timezone are in global vars
* **Comments**: help to navigate in the code


### Project structure
```
app_python/
│
├── app.py
├── templates/
│   └── home.html
```
