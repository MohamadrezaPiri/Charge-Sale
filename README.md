# Charge Sale
A Django app for charge selling. Each seller must charge his credit at first, and then they will be able to charge phone numbers. They can also withdraw their credit.
All transactions including charge sale, deposit, and withdraw will be recorded.
## Technologies Used:
![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![image](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
## Installation
- Clone the project:
```
git clone https://github.com/MohamadrezaPiri/Charge-Sale.git
```
- Create a virtual environment:
```
py -m venv YourVirtualEnvironment
```
- Then activate it:
```
YourVirtualEnvironment/Scripts/activate
```
- Using the command below, install all the packages in ```requirements.txt``` file:
```
pip install -r requirements.txt
```
- And finally:
```
py manage.py migrate
```
- Now it's time to run the server:
```
py manage.py runserver
```

