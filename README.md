
# Pixavibe API
![amiresponsive](/documentation/readme-image/amiresponsive.webp)
<br>
<br>
Pixavibe is a full-stack web application designed for content sharing, similar to a simplified version of Instagram. It uses Django Rest Framework for the back-end and React for the front-end, providing a seamless user experience for browsing, posting, and interacting with content. Users can post images, comment on posts, and follow other users. They can also create personal feeds by following users and liking posts and hide unwanted content. 
<br>
<br>

The Pixavibe API serves as the backend service for the [Pixavibe Application](https://github.com/JaqiKal/pixavibe).

<hr>

## Table of Contents
- [Pixavibe API](#pixavibe-api)
  - [General Details](#general-details)
  - [Database model](#database-model)
  - [Technologies](#technologies)
  - [Development setup](#development-setup)
  - [Deployment](#deployment)
  - [Credits](#Credits)
    - [Content](#Content)
    - [Acknowledgements](#Acknowledgements)

## General Details

This is the API for the Pixavibe backend application. Detailed information about strategy, structure, skeleton, surface plane, testing and open issues is found in the frontend repository README and TESTING information.

- The Pixavibe [frontend repository](https://github.com/JaqiKal/pixavibe)

- The [Pixavibe live site](https://pixavibe-frontend-e53fa907f215.herokuapp.com/)

## Database model

In the development environment, Pixavibe uses SQLite, which is simple to set up and ideal for development and testing. For the production environment, PostgreSQL is used due to its robustness, scalability, and advanced features suitable for handling a live web application.

### Data Modeling and Database Design

#### Entity-Relationship Diagram

The Entity-Relationship Diagram (ERD) provides a visual representation of the database's structure. It helps in planning and illustrating the SQL tables and the relationships between them. The ERD is an essential part of the database design that shows the entities, their attributes, and the types of relationships among the entities.

REWORK!!   
- Remove boolean is_active  from 
- Rename Tag to HAshtag
- Add category

![erd](/documentation/readme-image/erd.webp)

##### Relationships

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

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   nd the types of relationships among the entities.

#### Database Schema

#### Data Flow

To follow best practice, a flowchart was created for the app's logic, and mapped out before coding began using a free version of Draw.io. Please note, that the flowchart provided is designed to offer a simplified visual overview of the application's core workflow. While it captures the essential operations and user interactions, some implementation details and error-handling mechanisms are abstracted for clarity. The actual application logic may involve additional steps and checks not depicted in the flowchart.

![Data Flow](/documentation/readme-image/flowchart.webp)

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### API Endpoints

TO BE DEFINED     ---- List and descriptions of available API endpoints.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

## Technologies

<details>
<summary>Technologies and tools used in the backend part of the project.</summary>
<br>

**Language**

- [Python](https://www.python.org/) serves as the back-end programming language.

**Frameworks, libraries and dependencies**

- [Django](https://www.djangoproject.com/) a framework for developing web applications written in Python, structures the back-end functionality.
- [Django REST framework](https://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs
- [Cloudinary](https://cloudinary.com/) a cloud-based platform, is used for storing and serving images, enhancing media management in the application.
- [Pillow](https://pypi.org/project/pillow/) an image resizing, rotation and transformation

**Tools and Services**

- [Code Institute Python Linter](https://pep8ci.herokuapp.com/) a tool to check Python code against some of the style conventions in PEP8.
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

## Testing & Issues

For information on how the project is tested & Issues encountered, please refer to the [pixavibe repository, TESTING.md](https://github.com/JaqiKal/pixavibe/blob/main/TESTING.md)

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

## Development setup

### Initial Setup of the api

The project utilizes GitHub for version control and Gitpod as the integrated development environment (IDE).

<details>
<summary>These steps outline the initial setup and essential commands for managing the Pixavibe api project</summary>
<br>

1. **Create a New Repository on GitHub:**
    - Navigate to "Repositories" and click on "New".
    - Select "Public" for the repository visibility.
    - Choose the template: "Code-Institute-Org/react-ci-template".
    - Name the repository: "drf-api".
    - Click on "Create Repository".

2. **Git Commands for Version Control:**
    - Stage all changes before committing: `git add .`
    - Stage individual file changes before committing: `git add <filename>`
    - Commit the staged changes with a message written in imperative mood: `git commit -m "your message"`
    - Push the changes to the GitHub repository: `git push`

3. **Run the Server Locally:**
    - To start the server locally (with `DEBUG=True`), run: `python manage.py runserver`
    - This command loads the website in the built-in terminal.

4. **Database Migrations:**
    - To create new database migrations, run: `python manage.py makemigrations`
    - To apply pending migrations, run: `python manage.py migrate`

5. **Manage Dependencies:**
    - To create or update the `requirements.txt` file, run: `pip freeze --local > requirements.txt`
    - To install the dependencies listed in `requirements.txt`, run: `pip install -r requirements.txt`

6. **Create a Superuser:**
    - To create a superuser (from the Heroku terminal), run: `python manage.py createsuperuser`
    - Follow the prompts to set the username, email, and password.

7. **Start a New Django Project:**
    - To create a new Django project in the current directory, run: `django-admin startproject <project name> .`

8. **Create a New Django App:**
    - To create a new app within the project, run: `python manage.py startapp <app name>`


9. **Setting up Django Project with Cloudinary**
    - **Requirements:**

      - cloudinary
      - Django
      - django-cloudinary-storage
      - Pillow

    - **In the Terminal:**

      - Install Django: `pip install ‘django<4’`
      - Create Project: `django-admin startproject drf_api .`
      - Install Cloudinary Storage: `pip install django-cloudinary-storage==0.3.0`
      - Install Pillow (Image Processing): `pip install Pillow==8.2.0`

     - **In `drf_api/settings.py`:**

       - Add Installed Apps to `settings.py`:
          ```py
          INSTALLED_APPS = [
              ...,
              'cloudinary_storage',
              'django.contrib.staticfiles',
              'cloudinary',
              ...
          ]
          ```

     - **In the IDE:**

        - Create an env.py file within the top-level directory.

       - In env.py:
          - Create a Cloudinary account and set the URL value as a variable: 

            ```py
            import os
            os.environ['CLOUDINARY_URL'] = 'cloudinary://<cloudinary_key>'
            ```

        - In drf_api/settings.py:
          - Import os:
            ```py
            from pathlib import Path
            import os
            ```
        - Add a statement to import env.py if it exists:

          ```py
          if os.path.exists('env.py'):
              import env
          ```
        - Set CLOUDINARY_STORAGE variable equal to the CLOUDINARY_URL variable:
       
            ```py
          CLOUDINARY_STORAGE = {
              'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
          }

       - Define Media Storage URL: 

          ```py 
          MEDIA_URL = '/media/'
          ```

            - Define Default File Storage to Cloudinary:

      - In the Terminal:
        - Git add, commit and push.
  </details>
  <br>

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

## Deployment

<details>
<summary>Heroku Initial setup</summary>
<br>

**Project settings**

- Include ```https://<your_app_name>.herokuapp.com``` in the ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS lists inside the settings.py file.
- Make sure that the environment variables (DATABASE_URL, SECRET_KEY, and CLOUDINARY_URL) are correctly set to ```os.environ.get("<variable_name>")```
- If making changes to static files or apps, make sure to run collectstatic or migrate as needed.
- Commit and push to the repository.

**Requirements**

In order to deploy the API, Heroku needs information about the technologies used.

- Create a plain file called Procfile without any file suffix, at the root level of the project.
- Type ```web: gunicorn fooroom.wsgi:application``` into the Procfile and save.
- In your IDE terminal, type ```pip3 freeze local > requirements.txt``` to create the requirements.
- (Optional) Create a runtime.txt and type ```python-3.11.9``` (or whichever version you use)
- Commit and push these files to the project repository.

**Create Heroku App**

1. Sign in or sign up to [Heroku](https://heroku.com/).
2. Click the button that says "Create new app."
3. Enter a unique app name.
4. Choose your region from the dropdown menu.
5. Click the "Create app" button.

6. For Heroku to be able to process and render the project, you must define some environment variables.

    - Go to the settings page of your new app
    - Scroll down and open the Config Vars
    - Add a DATABASE_URL variable and assign it a link to your database
    - Add a SECRET_KEY variable and assign it a secret key of your choice
    - Add a CLOUDINARY_URL variable and assign it a link to your Cloudinary
    - Add an ALLOWED_HOST variable and assign it the url of the deployed heroku link
    - Add a CLIENT_ORIGIN variable and assign it the url of your deployed frontend app
    - Add a CLIENT_ORIGIN_DEV variable and assign it the url of your local development client

7.  Scroll down on the page, select "Add Buildpack." The buildpacks will install dependencies that are not included in the `requirements.txt`.
    - It's crucial to arrange the buildpacks correctly! First, choose Python and then Node.js. If they're not in this sequence, you can reorder them by dragging.

8. Once your Heroku settings and GitHub repository are up to date, connect them to each other.
    - Deploy by either pushing your code to Heroku, connecting your GitHub repository to Heroku, or using the Heroku CLI to deploy your application.
    - For this project, we're using GitHub as our method. After choosing GitHub, confirm the connection. Then, search for your repository name, and once Heroku finds your repository, click "connect."
    - Scroll down to the section "Automatic Deploys."
    - Click "Enable automatic deploys" or choose "Deploy branch" to manually deploy.
    - Click "Deploy branch" and wait for the app to be built. Once this is done, a message should appear letting you know that the app was successfully deployed.
    - Click the button "View" to see the app.
9. Open Your Application:
    - Open your application from the Heroku dashboard or using the CLI command: `heroku open`

For more detailed instructions and troubleshooting, visit the [official Heroku Dev Center](https://devcenter.heroku.com/).
</details>
<br>

<details>
<summary>GitHub - How to fork and How to Clone the repository</summary>
<br>

**How to Fork**

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, [EmilionR/pp5-api](https://github.com/EmilionR/pp5-api)
3. Click the Fork button in the top right corner.

**How to Clone the Repository**

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, [EmilionR/pp5-api](https://github.com/EmilionR/pp5-api)
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.
</details>
<br>

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

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