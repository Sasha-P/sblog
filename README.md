# Django PROJECT-TEST

Used: Django 1.9.7

Playground for experiment.

Contain two apps studdb and blog

##studdb

to be described...

##blog

Simple blog with REST interface

###Blog REST API

Used: Django REST framework 3.3.3

- user registration

    request: `POST`
    url: `/blog/api/v1/user/reg/`
    fields: `email`, `password`, `first_name` and `last_name`

- user authentication

    request: `POST`
    url: `/blog/api/v1/user/auth/`
    fields: `email_or_username` and `password`

    return: **`<token>`**

- user profile

    request: `GET`
    url: `/blog/api/v1/user/`
    header: `Authorization: Token <token>`

- user posts list

    request: `GET`
    url: `/blog/api/v1/user/posts/`
    header: `Authorization: Token <token>`

- all posts list with pagination

    request: `GET`
    url: `/blog/api/v1/post/`
    header: `Authorization: Token <token>`

- create new post

    request: `POST`
    url: `/blog/api/v1/post/`
    header: `Authorization: Token <token>`
    fields: `title` and `text`

- search post by title

    request: `POST`
    url: `/blog/api/v1/post/search/`
    header: `Authorization: Token <token>`
    fields: `query`


Based on [DjangoGirls](http://tutorial.djangogirls.org/) tutorial with using [Bootstrap](http://getbootstrap.com/).
