# Framework

I decided to choose `FastAPI`, since it compact,
fast and support asynchronous operations. Also, it has
built-in support for data validation library: `Pydantic`.
Compared to `Django`, it has less boilerplate code and
allows developer to make code flexible and avoid
some Django batteries bugs.

# Best practices

1) Code is separated into several `.py` files separated by `Clean arch` principles.
2) Python code has type hinting and annotations
3) Some parameters are taken into environmental variables
4) Program is launched with construction `if __name__ == "__main__"` which ensures that the
   current script is launched as main program (not a subprogram, or library)
5) Auto generation of swagger `/docs`

# Unit testing

I implemented two unit test for my application, one checks that it returns
correct time (in Moscow timezone), another one checks that web framework starts.
For testing I used `pytest`, for mocking `pytest-mock`, also I ve added
100% coverage threshold for tests to pass, forcing developers to test their code. 
