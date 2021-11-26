git pull https://github.com/murillenda/M2A_Project.git

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py seed