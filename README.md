# ClickBank: A Flask Banking Management System

ClickBank is a simple banking management system that allows users to create accounts, deposit, withdraw, and transfer money between accounts.ClickBank is built using Flask, a Python web framework. ClickBank uses MySQL as it's database. The web application is built using HTML, CSS, and Bootstrap.

## Features of ClickBank

* Login/Register - Logout functionality
* Create/Update/Delete Customer functionality
* Create/Delete Account
* Amount Withdraw/Deposit/Transfer
* Customer/Account Status Listing page with activity
* Transaction history with excel export

## Table of Contents

- [Technologies Used](#technologies-used)
- [Python Setup](#python-setup)
- [Git setup](#git-setup)
- [Activate Virtual Environment](#activate-virtual-environment-help)
- [Install the required dependencies](#install-the-required-dependencies)
- [Setup Mysql Database](#setup-mysql-database)
- [Change Configuration file](#change-configuration-file)
- [Create a database named `banking`](#create-a-database-named-banking)
- [Load the `banking.sql` file](#load-the-bankingsql-file)
- [Running The Flask Project](#run-the-flask-project)

## Technologies Used

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [MySQL](https://www.mysql.com/)
* [HTML](https://html.spec.whatwg.org/multipage/)
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
* [Bootstrap](https://getbootstrap.com/)


## Python Setup

Install [Python](https://www.python.org/downloads/)

## Git setup

Install [Git](https://git-scm.com/)

Go to a directory you want to work on

**Clone the repository:**

```bash
git clone git@github.com:Tafara-N/ClickBank.git
```

## Activate Virtual Environment, [help](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Install the required dependencies.**

```bash
pip install -r requirements.txt
```

> **Download all dependency if any missing:**

**Setup Mysql Database:**

- Install [MySQL Community](https://dev.mysql.com/downloads/)
____

**Change Configuration file:**

- In ClickBank/.flaskenv change SQLALCHEMY_DATABASE_URI path with your MySQL credentials example:

    - Database name: banking
    - Username:your-username
    - Password:your-password

```bash
SQLALCHEMY_DATABASE_URI='mysql+pymysql://<user>:<password>@localhost/banking'
```
____

**Create a database named `banking`**

```bash
echo "CREATE DATABASE banking;" | mysql -u root -p
```

**Load the `banking.sql` file:**

- Creates the tables and inserts some dummy data into the tables.

```sql
mysql> USE banking;
mysql> SOURCE banking.sql;
```

OR

```bash
mysql -u root -p banking < banking.sql
```
____

## Run The Flask Project

**From the root directory of the project, run the following command:**

- In `ClickBank/`

```bash
flask run
```

**Open the browser and go to the following URL:**

- [http://localhost:5000/](http://localhost:5000/)
____

## Authors

- **Anoona Sithole - [Github](https://github.com/Anoonaa) / [Twitter](https://twitter.com/AnoonaSithole)**
- **Tafara Nyamhunga - [Github](https://github.com/Tafara-N) / [Twitter](https://twitter.com/tafaranyamhunga)**
