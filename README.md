

<!-- ABOUT THE PROJECT -->
## 🚀 Grocery Recommendation System 
A system that recommends groceries by identifying related products based on user input and preferences.

Check it out live : [grocerypicks.onrender.com](https://grocerypicks.onrender.com/)

<!-- GETTING STARTED -->
<!--## Description-->
<!--A grocery recommendation system that uses the Apriori algorithm to suggest related items based on user input. The API is built with Django, containerized using Docker, and deployed on Render. GitHub Actions automates CI/CD to streamline the deployment process.-->
## 📌 Project Highlights

- **Product Recommendation:** Developed a machine learning model using Apriori algorithm to suggest products based on customers' purchase histories.

- **API Development with Django:** Built an API with Django, enabling smooth integration and user-friendly access to the recommendation system.

- **Unit Testing & Linting:** Implemented unit tests to validate functionality and used Flake8 for effective code linting.
- **Containerized Application:** Containerized the application using Docker to ensure consistent deployment and performance across multiple environments.

- **Automated CI/CD Pipeline:** Configured GitHub Actions to automate the integration and deployment processes to maintain code quality and project integrity.


- **Efficient Deployment Configuration:** Deployed using Gunicorn for performance and Whitenoise for efficient static file handling.

- **Live on Render:** Successfully deployed the application on Render for easy access and scalability.


### 🔧 Tech Stack

* [![Python][Python.img]][Python-url]
* [![Django][Django.img]][Django-url]
* [![Docker][Docker.img]][Docker-url]
* [![GitHub Actions][GitHubActions.img]][GitHubActions-url]
* [![HTML][HTML.img]][HTML-url]
* [![CSS][CSS.img]][CSS-url]
* [![Render][Render.img]][Render-url] 

### ⚡🧠️ Machine Learning Model Link

[github.com/SA-K1B/Grocery_recommendation_model](https://github.com/SA-K1B/Grocery_recommendation_model)

### ⚙️ Installation with Docker


1. Clone the repo
   ```sh
   git clone https://github.com/SA-K1B/Django_Grocery_recommendation.git
   ```
2. Build Image 
   ```sh
   docker compose up --build
   ```
### ⚙️ Installation without Docker
1.  Set up a virtual environment
    ```sh
    python -m venv myenv
    ```
2. Activate the virtual environment
     
    On macOS/Linux
    ```sh
    source myenv/bin/activate
    ```
     On windows
     ```sh
     myenv\Scripts\activate
     ```
3.  Upgrade pip
    ```sh
     python -m pip install --upgrade pip
     ```
4.  Install the required packages
    ```sh
    pip install -r requirements.txt
    ```
5.  Run database migration
    ```sh
    python manage.py migrate

    ```
6. Collect static files
   ```sh
   python manage.py collectstatic --noinput
   ```
7. Run the development server
   ```sh
   python manage.py runserver
   ```


Now, a HTTP server will start up, listening on port 8000. You will see the app running at https://localhost:8000.
### 🔄 CI/CD Workflow


- Every push triggers automated unit tests to validate functionality.
 
- Flake8 performs code linting to ensure coding standards.

- The application is built into a Docker container for consistent deployment and pushed to Docker Hub.
- The application is hosted on Render, deployed from Docker Hub.
 
### WhiteNoise: Serving Static Files Efficiently
 [![WhiteNoise][WhiteNoise.img]][WhiteNoise-url]

A Python package for serving static files directly from web application. While Django includes built-in support for handling static files, it's mainly designed for development purposes and is not optimal for use in production environments.

### Gunicorn: Efficient Application Server
[![Gunicorn][Gunicorn.img]][Gunicorn-url]

Gunicorn is a WSGI compliant web server for Python Applications that receives requests sent to the Web Server from a Client and forwards them onto the Python applications or Web Frameworks.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[CSS-url]: https://www.w3.org/Style/CSS/Overview.en.html
[CSS.img]: https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white
[HTML-url]: https://html.spec.whatwg.org/
[HTML.img]: https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white
[Python-url]: https://www.python.org/
[Python.img]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Django-url]: https://www.djangoproject.com/
[Django.img]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Docker-url]: https://www.docker.com/
[Docker.img]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[GitHubActions-url]: https://github.com/features/actions
[GitHubActions.img]: https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white
[Render-url]: https://render.com/
[Render.img]: https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white

[WhiteNoise-url]: http://whitenoise.evans.io/en/stable/
[WhiteNoise.img]: https://img.shields.io/badge/WhiteNoise-2B8EAD?style=for-the-badge&logo=python&logoColor=white

[Gunicorn-url]: https://gunicorn.org/
[Gunicorn.img]: https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white