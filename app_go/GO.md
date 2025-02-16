# Framework and Coding Standards & Practices

In this document you will find reasoning behind choice of technologies, and descriptions of applied practices.
I recommend reading the [README.md](/app_go/README.md) to understand the features of the project

## Technologies used

1. Golang
    - Go is a statically typed compiled language with garbage collection with simplistic C-like syntax.
    It allows to develop web API-s fastly and conveniently without sacrificing performance.
    - Chi HTTP router. There are many options from standard library to fiber and gin frameworks. I liked chi better for this project because it's efficient, minimalistic, and compatable with standard library.
    - Slog logging package. This is a standard library's logging package. There are alternatives like zap, logrus, and zerolog, but if I decide to use them, I won't have to get rid of slog, I might just provide a corresponding adapter for it. This approach is more generic, so the implementations of logging may be swapped easily.

2. SQLite
    - The reason behind this database is the performance you get with such a lightweight system.

3. HTMX
    - My application does not have (and does not need) a dedicated heavyweight frontend. Instead it is just a single HTML page with HTMX script inside. It uses hypermedia to do network calls and changes the structure of DOM based on the replies

## Practices applied

1. Clean code architecture
    - I followed "typical" architecture of golang applications. All the starting points are in the **cmd**, functionality in **internal**, and the html views are in the **templates** folders.
    - I tried to separate the concerns correspondingly, so that all the network communications are on one level, and database communications are on another. There was no business logic, so I decided that I don't need a separate service level just for calling functions twice instead of once.

2. .yaml config utilization
    - The project is configurable via .yaml files, path to the relevant config must be specified in .env.
    - Project uses cleanenv package by [Ilya Kaznacheev](https://github.com/ilyakaznacheev/cleanenv) , which is designed to parse these .yaml configurations.

3. Descriptive logging.
    - Structured logging for each of the requests.
    - Different log formats depending on the environment specified in the config. It is text for local env, and JSON for dev and prod env-s. This provides readable logs for developers that test locally, and appropriate format of logs for log aggregators like grafana, kebana, etc.

## Future improvements

1. Database migrations
    - Right now, table in the databse is initialized directly in the code. It would be better to separate the sql for migrations, and do it in a clearer way.

2. Test the system
    - Add unit tests, integration tests, etc.

3. Provide better documentation
    - Add endpoint documentation, for example, by using swagger ui.

4. Add pagination for management
    - Right now, if there are too many urls, they will just make the html bigger till beyond infinity.
