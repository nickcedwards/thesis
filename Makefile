NAME=Thesis

all : ${NAME}.pdf

%.pdf : %.tex
	pdflatex $<
	./makeFeynDiagrams.sh
	pdflatex $<.tex
	bibtex $<
	pdflatex $<
	pdflatex $<
	pdflatex $<

Backup: Backup.pdf

clean :
	rm -f ${NAME}.pdf *.aux *.log *.out *.toc *.bbl *.1 *.mp
