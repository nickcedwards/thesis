NAME=Thesis

all : ${NAME}.pdf

%.pdf : %.tex
	pdflatex $<.tex
	./makeFeynDiagrams.sh
	pdflatex $<.tex
	bibtex $<
	pdflatex $<.tex
	pdflatex $<.tex
	pdflatex $<.tex

Backup: Backup.pdf

clean :
	rm -f ${NAME}.pdf *.aux *.log *.out *.toc *.bbl *.1 *.mp
