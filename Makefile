UIDIR:=uifiles
UIFILES:=$(wildcard $(UIDIR)/*.ui)
PYUI=$(patsubst %.ui,%.py,$(UIFILES))

all: dist pyfiles
release: dist.zip

dist.zip: dist files
	zip -r $@ $<

dist: game.py dist/data dist/data/test_data.csv
	pyinstaller game.py --onefile

dist/data:
	mkdir -p $@

dist/data/test_data.csv: data/test_data.csv
	cp $^ $@

pyfiles:  $(PYUI)

$(UIDIR)/%.py: $(UIDIR)/%.ui
	python3 -m PyQt5.uic.pyuic -x $^ -o $@

install-requirements:
	pip install -r requirements.txt

clean:
	$(RM) $(PYUI)

#TODO: delete
run:
	python.exe game.py
