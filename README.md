# Pixavibe API

# Pixavibe API
![amiresponsive](/documentation/readme-image/amiresponsive.webp)
<br>
<br>
Pixavibe is a full-stack web application designed for content sharing, similar to a simplified version of Instagram. It uses Django Rest Framework for the back-end and React for the front-end, providing a seamless user experience for browsing, posting, and interacting with content. Users can post images, comment on posts, and follow other users. They can also create personal feeds by following users and liking posts and hide unwanted content. 
<br>
<br>
<br>
<br>
Pixavibe is a full-stack web application designed for content sharing, similar to a simplified version of Instagram. It uses Django Rest Framework for the back-end and React for the front-end, providing a seamless user experience for browsing, posting, and interacting with content. Users can post images, comment on posts, and follow other users. They can also create personal feeds by following users and liking posts and hide unwanted content. 
<br>
<br>

The Pixavibe API serves as the backend service for the [Pixavibe Application](https://github.com/JaqiKal/pixavibe).
The Pixavibe API serves as the backend service for the [Pixavibe Application](https://github.com/JaqiKal/pixavibe).

<hr>

## Table of Contents
- [Pixavibe API](#pixavibe-api)
  - [General Details](#general-details)
  - [Database model](#database-model)
  - [Technologies](#technologies)
  - [Testing and Issues](#testing-and-issues)
  - [Deployment](#deployment)
  - [Credits](#Credits)

## General Details

This is the API for the Pixavibe backend application. Detailed information about strategy, structure, skeleton, surface plane, testing and open issues is found in the frontend repository README and TESTING information.

- The Pixavibe [frontend repository](https://github.com/JaqiKal/pixavibe)

- The [Pixavibe live site](https://pixavibe-frontend-e53fa907f215.herokuapp.com/)

## Database model

In the development environment, Pixavibe uses SQLite, which is simple to set up and ideal for development and testing. For the production environment, PostgreSQL is used due to its robustness, scalability, and advanced features suitable for handling a live web application.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*

### Data Modeling and Database Design

<details>
<summary>Entity-Relationship Diagram</summary>
<br>

The Entity-Relationship Diagram (ERD) provides a visual representation of the database's structure. It helps in planning and illustrating the SQL tables and the relationships between them. The ERD is an essential part of the database design that shows the entities, their attributes, and the types of relationships among the entities.

REWORK!!   
- Remove boolean is_active  from 
- Rename Tag to HAshtag
- Add category

REWORK!!   
- Remove boolean is_active  from 
- Rename Tag to HAshtag
- Add category

![erd](/documentation/readme-image/erd.webp)

**Relationships**

- User
  - One-to-One: User.id → Profile.owner
  - One-to-Many: User.id → Post.owner
  - One-to-Many: User.id → Comment.owner
  - Many-to-Many (through Follower): User.id → Follower.owner
  - Many-to-Many (through Follower): User.id → Follower.followed
  - Many-to-Many (through Like): User.id → Like.owner
  - One-to-Many: User.id → Contact.owner
  - One-to-Many: User.id → BlockUser.owner
  - One-to-Many: User.id → BlockUser.target

- Profile
  - One-to-One: Profile.owner → User.id

- Post
  - Many-to-One: Post.owner → User.id
  - One-to-Many: Post.id → Comment.post
  - Many-to-Many (through Like): Post.id → Like.post
  - Many-to-Many: Post.id → Tag.posts

- Comment
  - Many-to-One: Comment.owner → User.id
  - Many-to-One: Comment.post → Post.id

- Like
  - Many-to-One: Like.owner → User.id
  - Many-to-One: Like.post → Post.id

- Follower
  - Many-to-One: Follower.owner → User.id
  - Many-to-One: Follower.followed → User.id

- Tag
   - Many-to-Many: Tag.id → Post.tags

- Contact
   - Many-to-One: Contact.owner → User.id

- BlockUser
  - Many-to-One: BlockUser.owner → User.id
  - Many-to-One: BlockUser.target → User.id
</details>

### Database Schema

<details>

<summary>Data Flow</summary>
<br>

To follow best practice, a flowchart was created for the app's logic, and mapped out before coding began using a free version of Draw.io. Please note, that the flowchart provided is designed to offer a simplified visual overview of the application's core workflow. While it captures the essential operations and user interactions, some implementation details and error-handling mechanisms are abstracted for clarity. The actual application logic may involve additional steps and checks not depicted in the flowchart.

![Data Flow](/documentation/readme-image/flowchart.webp)

</details>
<br>

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*

## Technologies

<details>
<summary>Language</summary>
<br>

- [Python](https://www.python.org/) serves as the back-end programming language.

</details>
<br>

<details>
<summary>Frameworks, libraries and dependencies used in the backend part of the project.</summary>
<br>

- [asgiref==3.8.1](https://pypi.org/project/asgiref/) ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and positioned as an asynchronous successor to WSGI.
- [certifi==2024.2.2](https://pypi.org/project/certifi/) Certifi provides Mozilla’s carefully curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts.
- [cffi==1.16.0](https://pypi.org/project/cffi/) Foreign Function Interface for Python calling C code.
- [charset-normalizer==3.3.2](https://pypi.org/project/charset-normalizer/) A library that helps you read text from an unknown charset encoding.
- [cloudinary==1.40.0](https://pypi.org/project/cloudinary/) allows you to quickly and easily integrate your application with Cloudinary.
- [cryptography==42.0.7](https://pypi.org/project/cryptography/) is a package which provides cryptographic recipes and primitives to Python developers.
- [defusedxml==0.7.1](https://pypi.org/search/?q=defusedxml) XML bomb protection for Python stdlib modules.
- [dj-database-url==0.5.0](https://pypi.org/project/dj-database-url/0.5.0/) This simple Django utility allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
- [dj-rest-auth==2.1.9](https://dj-rest-auth.readthedocs.io/en/2.1.9/) a set of REST API endpoints to handle User Registration and Authentication tasks.
- [Django==3.2.25](https://docs.djangoproject.com/en/5.0/releases/3.2.25/) Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- [django-allauth==0.54.0](https://docs.allauth.org/en/latest/) Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
- [django-cloudinary-storage==0.3.0](https://pypi.org/project/django-cloudinary-storage/0.3.0/) Django Cloudinary Storage is a Django package that facilitates integration with Cloudinary by implementing Django Storage API.
- [django-cors-headers==4.3.1](https://pypi.org/project/django-cors-headers/) is a Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS).
- [django-filter==2.4.0](https://pypi.org/project/django-filter/2.4.0/) django-filter is a reusable Django application for allowing users to filter querysets dynamically.
- [djangorestframework==3.14.0](https://pypi.org/project/djangorestframework/3.14.0/) is a powerful and flexible toolkit for building Web APIs.
- [djangorestframework-simplejwt==4.7.2](https://pypi.org/project/djangorestframework-simplejwt/4.7.2/) A minimal JSON Web Token authentication plugin for Django REST Framework.
- [gunicorn==22.0.0](https://pypi.org/project/gunicorn/22.0.0/) is a Python WSGI HTTP Server for UNIX.
- [idna==3.7](https://pypi.org/project/idna/3.7/) is support for the Internationalized Domain Names in Applications (IDNA) protocol.
- [oauthlib==3.2.2](https://pypi.org/project/oauthlib/3.2.2/) is a generic, spec-compliant, thorough implementation of the OAuth request-signing logic.
- [packaging==24.0](https://pypi.org/project/packaging/24.0/) Core utilities for Python packages.
- [Pillow==8.2.0](https://pypi.org/project/pillow/8.2.0/) The Python Imaging Library enhances your Python interpreter with extensive file format support, efficient data representation, and powerful image processing capabilities.
- [psycopg2==2.9.9](https://pypi.org/project/psycopg2/) PostgreSQL database adapter for the Python programming language. The stand-alone binary package was chosen due to the normal psycopg2 throwing errors.
- [pycparser==2.22](https://pypi.org/project/pycparser/) is a complete parser of the C language.
- [PyJWT==2.8.0](https://pypi.org/project/PyJWT/) JSON Web Token implementation in Python.
- [python3-openid==3.2.0](https://pypi.org/project/python3-openid/) OpenID support for modern servers and consumers.
- [pytz==2024.1](https://pypi.org/project/pytz/2024.1/) allows accurate and cross platform timezone calculations.
- [requests==2.32.2](https://pypi.org/project/requests/2.32.2/) is a simple, yet elegant, HTTP library that allows you to send HTTP/1.1 requests extremely easily.
- [requests-oauthlib==2.0.0](https://pypi.org/project/requests-oauthlib/2.0.0/) provides first-class OAuth library support for Requests.
- [six==1.16.0](https://pypi.org/project/six/1.16.0/) provides utility functions for smoothing over the differences between the Python 2 & 3 versions with the goal of writing Python code that is compatible on both Python versions.
- [sqlparse==0.5.0](https://pypi.org/project/sqlparse/0.5.0/) sqlparse is a non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements.
- [urllib3==2.2.1](https://pypi.org/project/urllib3/2.2.1/) is a HTTP library with thread-safe connection pooling, file post, and more.
</details>
<br>

<details>
<summary>Tools and Services</summary>
<br>

- [Code Institute Python Linter](https://pep8ci.herokuapp.com/) a tool to check Python code against some of the style conventions in PEP8.
- [Code Institute Template](https://github.com/Code-Institute-Org/ci-full-template) provided me with a familiar base from which to build my project.
- [Conventional Commits 1.0.0.](https://www.conventionalcommits.org/en/v1.0.0/) is a lightweight convention on top of commit messages.
- [Diffchecker](https://www.diffchecker.com/text-compare/) is used to check code snippets.
- [Draw.io](https://www.drawio.com/) is useful for planning the application's architecture and flowcharts, especially helpful in the design phase to visualize the application flow.
- [Git](https://git-scm.com/) is used for version control.
- [Gitpod](https://gitpod.io/) streamlines your development process by providing a pre-configured, cloud-based development environment that's instantly ready for coding.
- [Github](https://github.com/) is essential for version control, allowing you to track changes, collaborate with others (if applicable), and secure online code storage.
- [Google Dev Tools](https://developers.google.com/web/tools) is used during testing, debugging and styling.
- [Heroku](https://www.heroku.com/) is a platform for deploying and hosting web applications.
- [Lucidchart](https://www.lucidchart.com/) is used for ERD (entity relationship diagram)
- [PEP8](https://peps.python.org/pep-0008/) a style guide for Python code.
- [PostgreSQL](https://dbs.ci-dbs.net/) provided by the Code Institute, is employed as the database system for its robustness and compatibility with Django.
</details>
<br>
- [PostgreSQL](https://dbs.ci-dbs.net/) provided by the Code Institute, is employed as the database system for its robustness and compatibility with Django.
</details>
<br>

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*

## Testing and Issues

Information about how the project was tested & Issues encountered, please refer to the [pixavibe-frontend repository, TESTING.md](https://github.com/JaqiKal/pixavibe/blob/main/TESTING.md)

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*


## Deployment

<details>
<summary>Version Control</summary>
<br>
The site was created using the Gitpod editor and pushed to github to the remote repository ‘pixavibe-frontend’.
The following git commands were used throughout development to push code to the remote repo:

- `git add <file>` - This command was used to add the file(s) to the staging area before they are committed.
- `git commit -m “commit message”` - This command was used to commit changes to the local repository queue ready for the final step.
- `git push` - This command was used to push all committed code to the remote repository on github.
</details>

### Heroku

 <details>
 <summary>To deploy the project to Heroku, I took the following steps</summary>
 <br>

Create a new workspace in your preferred IDE, in our case it was [Gitpod](https://www.gitpod.io/docs/introduction/getting-started), and set up the new drf-api project. Use [Django REST framwork](https://www.django-rest-framework.org/) guide. 

**Project Settings**

- Include https://<your_app_name>.herokuapp.com in the ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS lists inside the settings.py file.
- Make sure that the environment variables (DATABASE_URL, SECRET_KEY, and CLOUDINARY_URL) are correctly set to os.environ.get("<variable_name>")
- If making changes to static files or apps, make sure to run collectstatic or migrate as needed.
- Commit and push to the repository.

**Requirements**

- Create a plain file called Procfile without any file suffix, at the root level of the project.
  - Add to the Procfile and save.
    - `release: python manage.py makemigrations && python manage.py migrate`
    - `web: gunicorn drf_api.wsgi`
- In your IDE terminal, type pip3 freeze local > requirements.txt to create the requirements.
- (Optional) Create a runtime.txt and type python-3.11.9 (or whichever version you use)
- Commit and push these files to the project repository.

 **Deployment to Heroku**

- In your heroku account, select New and then Create New App.
- Give it a unique name related to your project, choose the correct region for where you are located.
- Create app
- Goto 'Settings' tab and the Config Vars. For Heroku to be able to process and render the project, you must define some environment variables:
  - Add DATABASE_URL variable and assign it a link to your database
  - Add SECRET_KEY variable and assign it a secret key of your choice
  - Add CLOUDINARY_URL variable and assign it a link to your Cloudinary
  - Add ALLOWED_HOST variable and assign it the url of the deployed heroku link
  - Add CLIENT_ORIGIN variable and assign it the url of your deployed frontend app
  - Add CLIENT_ORIGIN_DEV variable and assign it the url of your local development client

- Continue to the 'Deploy' tab. 
  - Select GitHub as the 'deployment method'.
  - Confirm connection to git hub by searching for the correct repository and then connecting to it.
  - To manually deploy project click 'Deploy Branch'. 
      - Don't forget to ensure Debug is false for final deployment
  - Once built a message will appear saying: Your app was successfully deployed. 
  - Click the view button to view the deployed page making a note of it's url.
</details>

### Github

<details>
<summary>How to Fork the Repository</summary>
<br>

- Log in (or sign up) to GitHub.
- Go to the repository for this project, JaqiKal/pixavibe-api.
- Click the Fork button in the top right corner.
- This will create a duplicate of the full project in your GitHub Repository.
</details>
<br>

<details>
<summary>How to Clone the Repository</summary>
<br>

- Log in (or sign up) to GitHub.
- Go to the repository for this project, JaqiKal/pixavibe-api.
- Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
- Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
- Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.
</details>


## Credits

<details>
<summary>Content</summary>
<br>

Throughout the development of Pixavibe, a variety of resources have been utilized to ensure the platform is robust, user-friendly, and engaging. Below is a list of key documentation, blogs, tutorials, and guides that have been instrumental in crafting the backend functionality:

- **Bootstrap**: Extensively used for styling and responsive design, making the site accessible on a variety of devices - [Bootstrap documentation](https://getbootstrap.com/).
- **Django**: As the backbone of our platform, Django's comprehensive documentation has been crucial for backend development - [Django documentation](https://docs.djangoproject.com/en/5.0/).

- **Sources of inspiration and guidance in general**:
  - This resources is only available to enrolled students at The Code Institute:
    - The Code Institute Diploma in Full Stack Software Development (Advanced Front-End) Walk-through project Django REST framework (backend)
  - **Testing inspiration**: is listed in [Pixavibe-Frontend README](https://github.com/JaqiKal/pixavibe-frontend/blob/main/README.md#content)
</details>
<br>


<details>
<summary>Acknowledgement</summary>
<br>

Please see the [frontend README](https://github.com/JaqiKal/pixavibe-frontend/blob/main/README.md).
</details>
<br>

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*    

[To frontend README]()

[To frontend README]()