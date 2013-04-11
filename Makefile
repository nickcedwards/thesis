NAME=Thesis

all : ${NAME}.pdf

%.pdf : %.tex
	pdflatex ${NAME}.tex
	./makeFeynDiagrams.sh
	pdflatex ${NAME}.tex
	bibtex ${NAME}
	pdflatex ${NAME}.tex
	pdflatex ${NAME}.tex
	pdflatex ${NAME}.tex

backup: backup.pdf

clean :
	rm -f ${NAME}.pdf *.aux *.log *.out *.toc *.bbl *.1 *.mp
