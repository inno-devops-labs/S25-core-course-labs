# The JS application to calculate distance between two cities

## Runtime environment: `Node.js`
Easy to use, common, a lot of documentation. 

## Framework: `express`
Provides straidforward way to create routing and it is easy
to integrate with external APIs (Yandex Maps API in this case).


### Best practices
* **Modularity**: HTML code and CSS styles are splitted from the Python code
* **Error handling**: checking whether the given city exists or not
* **Easy to update/modify**
* **Comments**: help to navigate in the code
* **Security**: API key is stored in `.env` file

### Testing
Checked manually for different cities (for instance,
Munich and Innopolis). Moreover, checked the behaviour 
in case of entering invalid/unexisting names of cities.
