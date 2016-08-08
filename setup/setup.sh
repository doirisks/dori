cd /src/setup

./models.py

./CUIs.py

./dockerwriter.py

# overwrites itself in the containers so that it will only be activated once
echo "#cd /src/setup
#./models.py
#./CUIs.py
#./dockerwriter.py" > ./setup.sh
