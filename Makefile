# Run in sudo
setup:
	sudo apt-get install python 
# add js later
	pip install redis fastapi

run:	
	python srcpy/__init__.py &
