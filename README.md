# Introduction

![Add an image]()

Pixavibe is a Full-Stack web application designed to facilitate content sharing among users, akin to a simplified version of Instagram. Utilizing and Django Rest Framework for the back-end and React for the front-end, the application provides a seamless user experience for browsing, posting, and interacting with content.
Pixavibe API is the backend service used by the [Pixavibe Application](https://github.com/JaqiKal/pixavibe).

<hr>


## Table of Contents
- [Introduction](#introduction)
  - [Live Site](#live-site)
  - [React Frontend](#react-frontend)
  - [The Strategy Plane](#the-strategy-plane)
    - [Development Goals mapped with User Stories](#development-goals-mapped-with-user-stories)
    - [Learning Outcomes and Skill Development](#learning-outcomes-and-skill-development)
    - [Agile Planning and Development](#agile-planning-and-development)
        - [Overview of Agile Methodology](#overview-of-agile-methodology)
        - [Project Tracking (GitHub Projects)](#project-tracking-github-projects)
        - [Epics](#epics)
        - [User Stories](#user-stories)
        - [MoSCoW Prioritization](#moscow-prioritization)
  - [The Structure Plane](#the-structure-plane)
    - [API Endpoints](#api-end-points)
    - [Data Modeling and Database Design](#data-modeling-and-database-design)
        - [Entity-Relationship Diagram](#entity-relationship-diagram)
        - [Database Schema](#database-schema)
        - [Data Flow](#data-flow)
  - [The Skeleton Plane](#the-skeleton-plane)
    - [Features](#features)
        - [Implemented Features](#implemented-features)
        - [Future Features](#future-features)
    - [Security](#security)
    - [Technologies](#technologies)
    - [Testing](#testing)
  - [The Surface pLane](#the-surface-plane)
    - [Setup](#setup)
    - [Deployment](#deployment)
        - [Version Control](#version-control)
        - [Prerequisites](#prerequisites)
        - [Heroku Deployment](#heroku-deployment)
        - [Local Deployment](#local-deployment)
            - [How to Fork](#how-to-fork)
            - [How to Clone](#how-to-clone)
    - [Credits](#Credits)
    - [Content](#Content)
    - [Acknowledgements](#Acknowledgements)

## Live Site

[Pixavibe site]()

## React Frontend

[Pixavibe Application](https://github.com/JaqiKal/pixavibe)

## The Strategy Plane

### Development Goals mapped with User Stories


| Development Goals                              | Corresponding User Stories                                          |
|------------------------------------------------|---------------------------------------------------------------------|
| **Primary Objective:**                         |                                                                     |
| To create a user-friendly, responsive platform that enables users to share and interact with various content types (photos, videos, text). | **US-22:** Create New Posts<br>**US-23:** View Post Details<br>**US-24:** Like Posts<br>**US-25:** View Most Recent Posts |
| **Secondary Objectives:**                      |                                                                     |
| Implement essential social media features such as liking, commenting, and following. | **US-34:** Add Comments to Posts<br>**US-42:** Follow/Unfollow Users<br>**US-27:** View Liked Posts<br>**US-28:** View Followed Users' Posts<br>**US-30:** Add Tags to Posts<br>**US-47:** Block Users |
| Ensure smooth and intuitive navigation for users. | **US-14:** Navbar View on Every Page<br>**US-15:** Seamless Page Navigation<br>**US-29:** Infinite Scroll<br>**US-32:** View Post Page |
| Maintain high performance and scalability of the application. | **US-10:** Integrate Front-End and API                             |
| **Developer Goals:**                          |                                                                     |
| Build a robust, scalable back-end using Django Rest Framework. | **US-7:** DRF - Set Up Django Project<br>**US-8:** DRF - Design Database Models<br>**US-9:** DRF - Implement API CRUD Operations |
| Develop a dynamic, responsive front-end with React.js. | **US-5:** Design Responsive UI<br>**US-6:** Create Reusable Components |
| Emphasize clean, maintainable code and efficient database usage. | **US-3:** SP - Set Up Project Repositories                        |
| Ensure secure user authentication and authorization mechanisms. | **US-11:** DRF - Secure User Data<br>**US-16:** Sign Up for New Account<br>**US-17:** Sign In to Access Features<br>**US-18:** Logged In Status Check<br>**US-19:** Maintain Logged-In Status<br>**US-20:** Conditional Sign In/Up Options |
| Document the development process and deployment steps clearly in README files for both front-end and back-end repositories. | **US-4:** SP - Configure Dev Environment<br>**US-12:** Write React Component Tests<br>**US-13:** DRF - Write API Endpoint Tests |
| **User-Centric Goals:**                       |                                                                     |
| Provide an intuitive interface for users to easily post, edit, and delete content. | **US-22:** Create New Posts<br>**US-33:** Edit My Post Details<br>**US-37:** Delete My Comments<br>**US-38:** Edit My Comment<br>**US-44:** Edit My Profile<br>**US-45:** Update Username and Password |
| Enable social interactions through commenting, liking, and following other users. | **US-34:** Add Comments to Posts<br>**US-24:** Like Posts<br>**US-42:** Follow/Unfollow Users<br>**US-21:** View User Avatars<br>**US-36:** Read Comments on Posts<br>**US-35:** View Comment Dates |
| Ensure easy navigation and content discovery through effective search and filter functionalities. | **US-26:** Search Posts by Keywords<br>**US-31:** Search Posts by Tags<br>**US-43:** View All Posts by Specific User<br>**US-40:** View Most Followed Profiles<br>**US-41:** View User Stats |
| Deliver a responsive design for optimal user experience across devices. | **US-5:** Design Responsive UI                                     |
| **Learning Outcomes and Skill Development:**   |                                                                     |
| To master Full-Stack development by building a comprehensive web application from scratch. | **US-7:** DRF - Set Up Django Project<br>**US-10:** Integrate Front-End and API |
| To improve front-end skills with React.js, focusing on component-based architecture, state management, and responsive design. | **US-6:** Create Reusable Components<br>**US-5:** Design Responsive UI |
| To refine back-end development abilities using Django Rest Framework, emphasizing API development, database design, and secure authentication. | **US-8:** DRF - Design Database Models<br>**US-11:** DRF - Secure User Data<br>**US-46:** DRF - Implement Blocking Functionality<br>**US-48:** DRF - Create Contact Form<br>**US-50:** DRF - Implement Post Tagging |
| To apply Agile methodologies for efficient project management, incorporating user feedback and adapting to changing requirements. | **US-3:** SP - Set Up Project Repositories<br>**US-2:** SP - Identify Key Features |
| To develop essential technical skills in HTML, CSS, JavaScript, React.js, Bootstrap.js, Django Rest Framework, and Git. | **US-4:** SP - Configure Dev Environment                          |
| To strengthen soft skills in problem-solving, documentation, and communication. | **US-1:** SP - Define Project Scope<br>**US-3:** SP - Set Up Project Repositories |
| **Remaining User Stories:**                   |                                                                     |
| View User Profiles                             | **US-39:** View User Profiles                                      |
| Send Feedback to Admins                        | **US-49:** Send Feedback to Admins                                 |


*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Agile Planning and Development

Agile methodologies and principles guide the planning and creation of Pixavibe. While not adhering strictly to traditional Agile methodologies, such as scheduled sprints or scrums. The development process is inspired by Agile principles, focusing on flexibility, continuous improvement, and rapid adaptation to change. Sprints is not used as the project benefits more from focusing directly on larger goals and milestones, which are already well-defined with clear start and end dates. The approach is straightforward, development of features in a logical sequence, addressing core functionalities first before expanding to more complex features.

When encountering bugs or issues, rather than halting development, these are recorded as bug issues and added to the backlog. This allows to continue progressing in other areas while periodically revisiting and prioritizing the backlog based on severity and impact. This method ensures that development momentum is maintained while systematically addressing and resolving issues.

Feedback from users are actively sought and analyzed to identify areas for improvement, ensuring that the product continuously evolves to meet the needs and expectations of its users effectively.

For details please follow link to: [Github Project board](#)    §§§§§§§§§§§§§§§§§§§§§§§§§

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

#### Project Tracking (GitHub Projects)

#### Epics

- *Scope*: This Epic defines the overall scope of the backend application, detailing the APIs to be implemented, the data models required, and the integration points with the frontend.

- *Development*: This epic covers the development environment setup, including the configuration of the Django Rest Framework, database setup, and any necessary middleware.

- *Navigation & Authentication*: This epic covers the implementation of user authentication, including signup, login, and logout endpoints. It ensures secure access to the API endpoints.

- *Adding & Liking Posts*: This epic covers the backend functionality for creating new posts and managing likes on posts. It includes the necessary API endpoints and database schema to support these actions.

- *Posts Page*: This epic covers the creation of API endpoints to fetch posts from the database. It includes pagination, filtering, and sorting functionalities to support the frontend posts page.

- *Profile Page*: This epic covers the backend creation of user profile management endpoints. It allows users to view and update their profiles, including personal information and their posts.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

#### User Stories

<details>
<summary>User Story Table</summary>
SP =  Set up phase, aka inception /sprint zero, foundational tasks necessary before main development begins.
DRF = developing functionalities that are typically part of the Django REST Framework (DRF) phase
The unmarked are part of the development during Frontend phase. These are pivotal during the main development cycles and often follow the setup done in the IN phase.

| US-ID | Area |  User story Title | Statement | 
|-------|------|-------------------|-----------|
| 1 | Scope | SP - Define Project Scope | As a product owner, I want to define the project scope and vision so that all stakeholders have a clear understanding of the project's goals and objectives |
| 2 | Scope | SP - Identify Key Features | As a product owner, I want to identify key features and functionalities required for the application so that it meets user needs effectively |
| 3 | Development | SP - Set Up Project Repositories | As a developer, I want to set up a project repository for the front-end and back-end so that I can manage the codebase efficiently |
| 4 | Development | SP - Configure Dev Environment | As a developer, I want to configure the development environment so that I can ensure consistent setup across different machines |
| 5 | Development | Design Responsive UI | As a developer, I want to design a responsive user interface using React so that users have a seamless experience across devices |
| 6 | Development | Create Reusable Components | As a developer, I want to create reusable components in React so that the codebase is maintainable and scalable |
| 7 | Development | DRF - Set Up Django Project | As a developer, I want to create a Django project and set up the Django Rest Framework so that I can build the API |
| 8 | Development | DRF - Design Database Models | As a developer, I want to design database models so that the data is structured logically |
| 9 | Development | DRF - Implement API CRUD Operations | As a developer, I want to implement CRUD operations in the API so that users can manage their content |
| 10 | Development | Integrate Front-End and API| As a developer, I want to integrate the front-end with the back-end API so that data can be fetched and displayed dynamically |
| 11 | Development | DRF - Secure User Data | As a developer, I want to secure user data by storing passwords hashed and ensuring sensitive information is protected |
| 12 | Development | Write React Component Tests | As a developer, I want to write tests so that I can ensure the functionality of my React components |
| 13 | Development | DRF - Write API Endpoint Tests | As a developer, I want to write tests so that I can verify the correctness of the API endpoints |
| 14 | Navigation & Authentication | Navbar View on Every Page | As a user I can view a navbar from every page so that I can navigate easily between pages |
| 15 | Navigation & Authentication | Seamless Page Navigation | As a user I can navigate through pages quickly so that I can view content seamlessly without page refresh |
| 16 | Navigation & Authentication | Sign Up for New Account | As a user I can create a new account so that I can access all the features for signed up users |
| 17 | Navigation & Authentication | Sign In to Access Features | As a user I can sign in to the app so that I can access functionality for logged in users 
| 18 | Navigation & Authentication | Logged In Status Check | As a user I can tell if I am logged in or not so that I can log in if I need to |
| 19 | Navigation & Authentication | Maintain Logged-In Status | As a user I can maintain my logged-in status until I choose to log out so that my user experience is not compromised |
| 20 | Navigation & Authentication | Conditional Sign In/Up Options | Conditional rendering - As a logged out user I can see sign in and sign up options so that I can sign in/sign up |
| 21 | Navigation & Authentication | View User Avatars | As a user I can view user's avatars so that I can easily identify users of the application |
| 22 | Adding & Liking Posts | Create New Posts | As a logged in user I can create posts so that I can share my images with the world! |
| 23 | Adding & Liking Posts | View Post Details | As a user I can view the details of a single post so that I can learn more about it |
| 24 | Adding & Liking Posts | Like Posts | As a logged in user I can like a post so that I can show my support for the posts that interest me |
| 25 | The Posts Page | View Most Recent Posts | As a user I can view all the most recent posts, ordered by most recently created first so that I am up to date with the newest content |
| 26 | The Posts Page | Search Posts by Keywords | As a user, I can search for posts with keywords, so that I can find the posts and user profiles I am most interested in |
| 27 | The Posts Page | View Liked Posts | As a logged in user I can view the posts I liked so that I can find the posts I enjoy the most |
| 28 | The Posts Page | View Followed Users' Posts | As a logged in user I can view content filtered by users I follow so that I can keep up to date with what they are posting about |
| 29 | The Posts Page | Infinite scroll | As a user I can keep scrolling through the images on the site, that are loaded for me automatically so that I don't have to click on "next page" etc |
| 30* | The Posts Page | Add Tags to Posts | As a user, I want to add tags to my posts so that they are easier to find |
| 31* | The Posts Page | Search Posts by Tags | As a user, I want to search for posts by tags so that I can find related content |
| 32 | The Post Page | View Post Page |  As a user I can view the posts page so that I can read the comments about the post |
| 33 | The Post Page | Edit My Post Details | As a post owner I can edit my post title and description so that I can make corrections or update my post after it was created |
| 34 | The Post Page | Add Comments to Posts | As a logged in user I can add comments to a post so that I can share my thoughts about the post |
| 35 | The Post Page | View Comment Dates |  As a user I can see how long ago a comment was made so that I know how old a comment is |
| 36 | The Post Page | Read Comments on Posts | As a user I can read comments on posts so that I can read what other users think about the posts |
| 37 | The Post Page | Delete My Comments | As an owner of a comment I can delete my comment so that I can control removal of my comment from the application |
| 38 | The Post Page | Edit My comment | As an owner of a comment I can edit my comment so that I can fix or update my existing comment |
| 39 | The Profile Page | View User Profiles | As a user I can view other users profiles so that I can see their posts and learn more about them |
| 40 | The Profile Page | View Most Followed Profiles | As a user I can see a list of the most followed profiles so that I can see which profiles are popular |
| 41 | The Profile Page | View User Stats | As a user I can view statistics about a specific user: bio, number of posts, follows and users followed so that I can learn more about them |
| 42 | The Profile Page | Follow/Unfollow Users | Follow/Unfollow a user: As a logged in user I can follow and unfollow other users so that I can see and remove posts by specific users in my posts feed |
| 43 | The Profile Page | View All Posts by specific User | As a user I can view all the posts by a specific user so that I can catch up on their latest posts, or decide I want to follow them |
| 44 | The Profile Page | Edit My Profile | As a logged in user I can edit my profile so that I can change my profile picture and bio |
| 45 | The Profile Page | Update username and password | As a logged in user I can update my username and password so that I can change my display name and keep my profile secure |
| 46 | The Profile Page | DRF - Implement Blocking Functionality | As a developer, I want to implement a blocking functionality so that users can manage their privacy effectively |
| 47 | The Profile Page | Block Users | As a user, I want to be able to block other users so that they cannot interact with my content |
| 48 | The Profile Page | DRF - Create Contact Form | As a developer, I want to create a contact form that stores user queries, complaints, or suggestions in the Contact model so that the platform can handle user feedback |
| 49 | The Profile Page | Send Feedback to Admins | As a user, I want to send feedback or queries to the platform administrators so that I can report issues or suggest improvements |
| 50 | The Profile Page | DRF - Implement Post Tagging | As a developer, I want to implement tagging functionality for posts so that users can categorize their content |
</details> <br>

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

#### MoSCoW Prioritization

By focusing on the Must Have features, the project ensures the highest priority tasks are completed first, delivering a functional and valuable product to users. The Should Have and Could Have features provide room for enhancements and future iterations, aligning with both the MoSCoW method and the Pareto principle for effective project management.

- Must Have: <br>
  Includes tasks that set up the project foundation and core functionalities necessary for the project to operate (setting up the environment, repositories, core CRUD operations, and essential user features).

- Should Have: <br>
  Enhances usability, maintainability, and user experience, but are not critical for the initial launch (responsive design, navigation improvements, additional user profile features).

- Could Have: <br>
  Adds value but can be deferred without impacting the core functionality (tagging, advanced user interactions, and feedback mechanisms).

- Won't Have: <br>
  Deferred features that are not essential for the initial launch but could be considered for future phases (infinite scroll).
<br>

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

<details>
<summary>Prioritized User stories </summary>

| Phase    | US-ID | Must Have                    | Should Have               | Could Have                         |
|----------|-------|------------------------------|---------------------------|------------------------------------|
| SP       | 1     | Define Project Scope         |                           |                                    |
| SP       | 2     | Identify Key Features        |                           |                                    |
| SP       | 3     | Set Up Project Repositories  |                           |                                    |
| SP       | 4     | Configure Dev Environment    |                           |                                    |
| DRF      | 7     | Set Up Django Project        |                           |                                    |
| DRF      | 8     | Design Database Models       |                           |                                    |
| DRF      | 9     | Implement API CRUD Operations|                           |                                    |
| DRF      | 10    | Integrate Front-End and API  |                           |                                    |
| DRF      | 11    | Secure User Data             |                           |                                    |
| Frontend | 16    | Sign Up for New Account      |                           |                                    |
| Frontend | 17    | Sign In to Access Features   |                           |                                    |
| Frontend | 22    | Create New Posts             |                           |                                    |
| Frontend | 23    | View Post Details            |                           |                                    |
| Frontend | 24    | Like Posts                   |                           |                                    |
| Frontend | 25    | View Most Recent Posts       |                           |                                    |
| Frontend | 39    | View User Profiles           |                           |                                    |
| Frontend | 42    | Follow/Unfollow Users        |                           |                                    |
| Frontend | 44    | Edit My Profile              |                           |                                    |
| Frontend | 5     |                              | Design Responsive UI      |                                    |
| Frontend | 6     |                              | Create Reusable Components|                                    |
| Frontend | 12    |                              | Write React Component Tests|                                   |
| Frontend | 13    |                              | Write API Endpoint Tests  |                                    |
| Frontend | 14    |                              | Navbar View on Every Page |                                    |
| Frontend | 15    |                              | Seamless Page Navigation  |                                    |
| Frontend | 18    |                              | Logged In Status Check    |                                    |
| Frontend | 19    |                              | Maintain Logged-In Status |                                    |
| Frontend | 20    |                              | Conditional Sign In/Up Options|                                 |
| Frontend | 21    |                              | View User Avatars         |                                    |
| Frontend | 27    |                              | View Liked Posts          |                                    |
| Frontend | 28    |                              | View Followed Users' Posts|                                    |
| Frontend | 32    |                              | View Post Page            |                                    |
| Frontend | 33    |                              | Edit My Post Details      |                                    |
| Frontend | 34    |                              | Add Comments to Posts     |                                    |
| Frontend | 36    |                              | Read Comments on Posts    |                                    |
| Frontend | 37    |                              | Delete My Comments        |                                    |
| Frontend | 38    |                              | Edit My comment           |                                    |
| Frontend | 43    |                              | View All Posts by specific User|                               |
| Frontend | 45    |                              | Update username and password|                                 |
| Frontend | 30    |                              |                           | Add Tags to Posts                  |
| Frontend | 31    |                              |                           | Search Posts by Tags               |
| Frontend | 35    |                              |                           | View Comment Dates                 |
| Frontend | 40    |                              |                           | View Most Followed Profiles        |
| Frontend | 41    |                              |                           | View User Stats                    |
| DRF      | 46    |                              |                           | Implement Blocking Functionality   |
| Frontend | 47    |                              |                           | Block Users                        |
| DRF      | 48    |                              |                           | Create Contact Form                |
| Frontend | 49    |                              |                           | Send Feedback to Admins            |
| DRF      | 50    |                              |                           | Implement Post Tagging             |
| Frontend | 29    |                              |                           | Infinite scroll                    |
</details>
<br>

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

## The Structure Plane

### API Endpoints

List and descriptions of available API endpoints.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Data Modeling and Database Design

#### Entity-Relationship Diagram

The Entity-Relationship Diagram (ERD) provides a visual representation of the database's structure. It helps in planning and illustrating the SQL tables and the relationships between them. The ERD is an essential part of the database design that shows the entities, their attributes, and the types of relationships among the entities.

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

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   


##### Permissions and Roles

XXXX

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

#### Database Schema

#### Data Flow

To follow best practice, a flowchart was created for the app's logic, and mapped out before coding began using a free version of Draw.io. Please note, that the flowchart provided is designed to offer a simplified visual overview of the application's core workflow. While it captures the essential operations and user interactions, some implementation details and error-handling mechanisms are abstracted for clarity. The actual application logic may involve additional steps and checks not depicted in the flowchart.

![Data Flow](/documentation/readme-image/flowchart.webp)

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

## The Skeleton Pane

### Features

A list of the implemented and planned features in the project.

#### Implemented Features

- Model X
- Model Y
- Model Z

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

#### Future Features

The following will be added in future iterations of this project:

- A
- B
- C

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Security

Security measures and practices implemented in the project.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Technologies

Technologies and tools used in the project.

#### Language

- [Python](https://www.python.org/) serves as the back-end programming language.

#### Frameworks, libraries and dependencies

- [Django](https://www.djangoproject.com/) a framework for developing web applications written in Python, structures the back-end functionality.
- [Django REST framework](https://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs
- [Cloudinary](https://cloudinary.com/) a cloud-based platform, is used for storing and serving images, enhancing media management in the application.
- [Pillow](https://pypi.org/project/pillow/) an image resizing, rotation and transformation

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

#### Database

- [PostgreSQL](https://dbs.ci-dbs.net/) provided by the Code Institute, is employed as the database system for its robustness and compatibility with Django.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

#### Tools and Services

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
- [PostgreSQL](https://dbs.ci-dbs.net/) a powerful, open source object-relational database system.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Testing

Information on how the project is tested, including tools and methodologies.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

## The Surface Plane
### Setup 

#### Setting up Django project with Cloudinary 

##### Requirements
cloudinary==1.40.0
Django==3.2.25
django-cloudinary-storage==0.3.0
Pillow==8.2.0

##### In the Terminal
- Install Django: ```pip install ‘django<4’```
- Create Project: ```django-admin startproject drf_api .```
- Install Cloudinary Storage: ```pip install django-cloudinary-storage==0.3.0```
- Install Pillow (Image Processing): ```pip install Pillow==8.2.0```

##### In drf_api / settings.py:
- Add Installed Apps to 'settings.py'

##### In the IDE:
- Create an 'env.py' file within the top level directory

##### In env.py:
- Create a cloudinary account and create space for images.: ```import os```
- Set the URL value as a variable CLOUDINARY_URL: ```os.environ['CLOUDINARY_URL'] = 'cloudinary://<cloudinary_key>' ```

##### In drf_api / settings.py: 
- Import os:
    ```text
    from pathlib import Path
    import os
    ```
- Add statement to import env.py if it exists - below import os:
    ```py
    if os.path.exists('env.py'):
        import env
    ```
- Set CLOUDINARY_STORAGE variable equals to the CLOUDINARY_URL variable. Place directly below imports:
    ```py
    CLOUDINARY_STORAGE = {
        'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
    }
    ```
- Define Media Storage URL. Place directly below: ```MEDIA_URL = '/media/'```
- Define Default File Storage to Cloudinary. Place directly below: ``` DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage' ```

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

##### In the Terminal
- Git add, commit and push

### Deployment

Detailed instructions for deploying the project, both locally and to production environments (e.g., Heroku).

#### Version Control

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

#### Heroku Deployment

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

#### Local Deployment

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

##### How to Fork

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

##### How to Clone

### Credits

#### Content

Throughout the development of Pixavibe, a variety of resources have been utilized to ensure the platform is robust, user-friendly, and engaging. Below is a list of key documentation, blogs, tutorials, and guides that have been instrumental in crafting the features and functionality of ScrollStack:

- **Bootstrap**: Extensively used for styling and responsive design, making the site accessible on a variety of devices - [Bootstrap documentation](https://getbootstrap.com/).
- **Django**: As the backbone of our platform, Django's comprehensive documentation has been crucial for backend development - [Django documentation](https://docs.djangoproject.com/en/5.0/).

- **Sources of inspiration and guidance in general**:
  - X
  - Y
  - Z
  - This resources is only available to enrolled students at The Code Institute:
    - The Code Institute Diploma in Full Stack Software Development (Advanced Front-End) Walk-through project Django REST framework (backend)

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

#### Acknowledgements

I would like to thank! 

- The whole team at [Code Institute Slack community](https://code-institute-room.slack.com) for their teaching and support.
- To all engaged fellow students at all channels and a special shout out to slack channel [community sweden](https://app.slack.com/client/T0L30B202/C03J2BCURV3).
- My mentor [Jubril Akolade](https://github.com/jubrillionaire/)
- My immediate and extended family, as well as my friends, who support and cheer me on!

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*    