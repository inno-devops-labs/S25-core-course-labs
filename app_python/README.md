# Moscow Time Web Application

## Overview
This is a simple web application that displays the current time in Moscow. It is built using **Python** and **Flask**, and containerized using **Docker**.

---

## Docker Instructions

### **How to Build**
1. Clone the repository:
   ```bash
   git clone git clone --branch lab2 https://github.com/Ali12hamdan/S25-core-course-labs.git

   docker pull ali12hamdan/moscow-time:1.0

   docker run -p 5001:5001 ali12hamdan/moscow-time-app:1.0