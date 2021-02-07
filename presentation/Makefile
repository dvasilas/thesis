## Author: SmallEndian

TEX = pdflatex
BIB = bibtex
SOURCE = presentation.tex
PVC =

.PHONY: help all  clean

all: $(SOURCE:.tex=.pdf) ## Builds once

# https://gist.github.com/prwhite/8168133
help:           ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'


%.pdf: %.tex
	latexmk -recorder -pdf -pdflatex="pdflatex -interaction=batchmode" -use-make $(PVC) -g $<

watch: ## Rebuild on changes
	make all PVC="-pvc"


clean:
	latexmk -CA
