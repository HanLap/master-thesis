FILE ?= topic-thoughts.adoc
BIN ?= asciidoctor-pdf

.PHONY: all
all:
	$(BIN) $(FILE)

.PHONY: watch
watch:
	while inotifywait -e close_write $(FILE); do $(BIN) -a pdf-theme=adoc-theme.yml $(FILE); done
