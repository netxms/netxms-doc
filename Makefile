all:
	@echo Select target: html or pdf

html:
	make -C adminguide html
	make -C conceptguide html
	make -C developguide html

pdf:
	make -C adminguide latexpdf
	make -C conceptguide latexpdf
	make -C developguide latexpdf

man:
	make -C adminguide man
	make -C conceptguide man
	make -C developguide man

clean:
	make -C adminguide clean
	make -C conceptguide clean
	make -C developguide clean
