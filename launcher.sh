if [ ! -d env ]; then
	echo "Installing dependencies for the first launch..."
	python3.12 -m venv env
	source env/bin/activate
	pip install -r requirements.txt
fi
source env/bin/activate
python src/main.py
