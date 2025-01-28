# Steps

1. Clone repository using `git clone https://github.com/oth33r/S25-core-course-labs.git`
2. Checkout branch lab1 `git checkout lab1`
3. Go to `app_python` folder using `cd app_python`
4. Install all the requirements `pip install -r requirements.txt`
5. Start `uvicorn app:app --reload`

## Docker

First we need to go to folder with app `cd app_python`

### How to build?

docker build -t dsaee/lab2:v1.0 .

### How to pull?

docker pull dsaee/lab2:v1.0

### How to run?

docker run -d -p 8000:8000 dsaee/lab2:v1.0
