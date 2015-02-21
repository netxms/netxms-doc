all:
	@echo Select target: html, pdf, man, clean

html:
	make -C admin html
	make -C concept html
	make -C developer html

pdf:
	make -C admin latexpdf
	make -C concept latexpdf
	make -C developer latexpdf

gettext:
	make -C admin gettext
	make -C concept gettext
	make -C developer gettext

man:
	make -C manpages man

clean:
	make -C admin clean
	make -C concept clean
	make -C developer clean
	make -C manpages clean
