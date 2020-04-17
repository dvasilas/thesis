TEX = pdflatex
BIB = bibtex
DOC = main

.PHONY: help $(DOC).pdf all show clean

# https://gist.github.com/prwhite/8168133
help:           ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

all:            ## Build all
all: $(DOC).pdf

show:           ## Build and open the document
show: $(DOC).pdf
	make $(DOC).pdf
	open $(DOC).pdf

$(DOC).pdf: $(DOC).tex
	latexmk -recorder -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make -g $(DOC).tex

clean:
	latexmk -CA