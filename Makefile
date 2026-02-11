DOCKER_IMAGE ?= ghcr.io/netxms/netxms-doc-builder:latest

all:
	@echo Select target: html, pdf, man, clean, docker

html:
	make -C admin html
	make -C concept html
	make -C developer html
	make -C user html

pdf:
	make -C admin latexpdf
	make -C concept latexpdf
	make -C developer latexpdf
	make -C user latexpdf

gettext:
	make -C admin gettext
	make -C concept gettext
	make -C developer gettext
	make -C user gettext

man:
	make -C manpages man

clean:
	make -C admin clean
	make -C concept clean
	make -C developer clean
	make -C manpages clean
	make -C user clean

docker:
	docker build -f docker/Dockerfile -t $(DOCKER_IMAGE) .

docker-push:
	docker buildx build --platform linux/amd64,linux/arm64 \
		-f docker/Dockerfile -t $(DOCKER_IMAGE) --push .

.PHONY: all html pdf gettext man clean docker docker-push
