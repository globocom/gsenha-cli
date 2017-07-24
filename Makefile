.PHONY: install clean dist

ROOT_PATH=$(shell pwd)

clean:
	-@rm -rf $(ROOT_PATH)/dist
	-@rm -rf $(ROOT_PATH)/build 
	-@rm -rf $(ROOT_PATH)/*.spec 

install:
	@pip install -r requirements.txt

dist: clean install
	@pyinstaller src/cli.py --onefile --name gsenha