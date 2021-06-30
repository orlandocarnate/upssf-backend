# UPSSF Full Stack React, Django, and PostGres website conversion
Convert an old static website for a non-profit organization into a full stack web app using Django Rest API for the backend and React for the front end. Postgresql will be the database. The project will be done incrementally.

1. Front end will be using the React.js framework.
2. Bring in data (Articles, Officers, Scholars) from a JSON file before creating datatabase.
3. Create Backend with Django
4. Create Rest API using Django Rest Framework to JSON data for the articles, officers, and scholars pages.
5. Implement Rich Text in the body of the articles and scholars using Django-Summernote.
6. Display Rich Text in React front end.
7. Incorporate Authentication and Authorization.
8. Use PostGreSQL for the database.

![Home Page](./readme-homepage.jpg)

## Technologies, APIS, and Frameworks used:
* [ReactJS](https://reactjs.org/) A JavaScript library for building user interfaces
* [Django Web Framework](https://www.djangoproject.com/) Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.
* [Django Rest Framework](https://www.django-rest-framework.org/) Django REST framework is a powerful and flexible toolkit for building Web APIs.
* [React Bootstrap](https://react-bootstrap.github.io/) React-Bootstrap replaces the Bootstrap JavaScript. Each component has been built from scratch as a true React component, without unneeded dependencies like jQuery.
* [Django CORS Headers](https://pypi.org/project/django-cors-headers/) A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses. This allows in-browser requests to your Django application from other origins.
* [AWS Amplify](https://docs.aws.amazon.com/amplify/latest/userguide/getting-started.html) AWS Amplify enables developers to develop and deploy cloud-powered mobile and web apps. The Amplify Framework is a comprehensive set of SDKs, libraries, tools, and documentation for client app development. The Amplify Console provides a continuous delivery and hosting service for web applications.
* [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service. it is used to perform three main functions in any combination: domain registration, DNS routing, and health checking.

AWS Amplify is used for deployment. Whenever the app's GitHub repository is updated, AWS Amplify automatically deploys the latest version.

## Notes
* use Proxy in `/frontend/package.json`
* change `Officers.json` from a class component a **functional** component.
* use useState and useEffect in `Officers.json`.

### Test uWSGI
sudo uwsgi --module=backend.wsgi:application --env=DJANGO_SETTINGS_MODULE=backend.settings.pro --master --pidfile=/tmp/project-master.pid --http=localhost:8000 --uid=1000 --virtualenv=/django-servers/venv