NAME=Thesis
all : 
	pdflatex ${NAME}.tex
	for mpfile in *.mp; do mpost $mpfile; done
	pdflatex ${NAME}.tex
	bibtex ${NAME}
	pdflatex ${NAME}.tex
	pdflatex ${NAME}.tex
	pdflatex ${NAME}.tex
clean :
	rm -f *.pdf *.aux *.log *.out *.toc *.bbl
