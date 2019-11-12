UIDIR:=uifiles
UIFILES:=$(wildcard $(UIDIR)/*.ui)
PYUI=$(patsubst %.ui,%.py,$(UIFILES))

hoge: $(PYUI)

$(UIDIR)/%.py: $(UIDIR)/%.ui
	python3 -m PyQt5.uic.pyuic -x $^ -o $@

install-requirements:
	pip install -r requirements.txt

clean:
	$(RM) $(PYUI)
