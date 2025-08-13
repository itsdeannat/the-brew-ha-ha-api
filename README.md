# The Brew Ha Ha API

The Brew Ha Ha API is a Django REST Framework project for managing snack and drink orders at a café-style establishment. It allows customers to:

* Browse available snacks and drinks in the database
* Place orders containing one or more items
* Retrieve details of orders

The API uses Django REST Framework serializers and views to handle data input and output.

## Installation

You are welcome to install the Brew Ha Ha API for local testing and exploration. To install the API, follow these steps.

### Step 1: Clone the Brew Ha Ha API repository

To clone the repository, run the following command:

```bash
git clone https://github.com/itsdeannat/the-brew-ha-ha-api.git
```

### Step 2: Install packages

This project uses `pipenv` for package management. If you do not have `pipenv`, visit the [documentation](https://pipenv.pypa.io/en/latest/) for installation instructions.

After you install pipenv, run this command to install project dependencies:

```py
pipenv install
```

### Step 3: Start the Django server 

To start the Django server, run this command:

```py
python manage.py runserver
```

## Documentation 

The Brew Ha Ha API documentation contains a quick start guide, feature guides, and API reference content. The API reference documentation uses Redocly. You can find the API documentation at [https://brew-ha-ha.netlify.app/](https://brew-ha-ha.netlify.app).

![An image of the Brew Ha Ha API docs](/images/docs-homepage.png)

## Changelog 

You can see the full development history of the Brew Ha Ha API in the [repository](https://github.com/itsdeannat/the-brew-ha-ha-api).