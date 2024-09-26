

<!-- ABOUT THE PROJECT -->
## Grocery Recommendation System
A system that recommends groceries by identifying related products based on user input and preferences.


### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Python][Python.img]][Python-url]
* [![Django][Django.img]][Django-url]
* [![Docker][Docker.img]][Docker-url]
* [![GitHub Actions][GitHubActions.img]][GitHubActions-url]
* [![HTML][HTML.img]][HTML-url]
* [![CSS][CSS.img]][CSS-url]
* [![Render][Render.img]][Render-url] 





<!-- GETTING STARTED -->
## Description
A grocery recommendation system that uses the Apriori algorithm to suggest related items based on user input. The API is built with Django, containerized using Docker, and deployed on Render. GitHub Actions automates CI/CD to streamline the deployment process.
### Machine Learning Model Link

[github.com/SA-K1B/Grocery_recommendation_model](https://github.com/SA-K1B/Grocery_recommendation_model)

### Installation with Docker


1. Clone the repo
   ```sh
   git clone https://github.com/SA-K1B/Django_Grocery_recommendation.git
   ```
2. Build Image 
   ```sh
   docker compose --build
   ```
3. Run a container
   ```sh
   docker compose up
   ```   
### Installation without Docker


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
     pip install --upgrade pip

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