TEX = pdflatex
BIB = bibtex
DOC = main

.PHONY: help $(DOC).pdf all show ch2 ch3 clean

# https://gist.github.com/prwhite/8168133
help:           ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

all:            ## Build all
all: $(DOC).pdf

show:           ## Build and open the document
show: $(DOC).pdf
	make $(DOC).pdf
	open $(DOC).pdf

$(DOC).pdf: $(DOC).tex refs.bib
	latexmk -bibtex -recorder -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make -g $(DOC).tex


ch2: chapter-builds/ch2.tex refs.bib
	latexmk -bibtex -recorder -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make -g chapter-builds/ch2.tex
	open ch2.pdf

ch3: chapter-builds/ch3.tex refs.bib
	latexmk -bibtex -recorder -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make -g chapter-builds/ch3.tex
	open ch3.pdf

clean:
	latexmk -CA
