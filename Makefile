TEX = pdflatex
BIB = bibtex
DOC = thesis

.PHONY: help all $(DOC).pdf clean

# https://gist.github.com/prwhite/8168133
help:           ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

all:            ## Build all
all: $(DOC).pdf

$(DOC).pdf: $(DOC).tex refs.bib
	latexmk -bibtex -recorder -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make -pvc -g $(DOC).tex

clean:
	latexmk -CA
