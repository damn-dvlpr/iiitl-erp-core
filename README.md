# iiitl-erp-core
## Set Up Instructions
```bash
git clone https://github.com/damn-dvlpr/iiitl-erp-core.git
cd iiitl-erp-core
python3 -m venv venv
. venv/bin/activate
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
## Activating the virtual environment
```bash
. venv/bin/activate
```
