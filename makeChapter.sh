if [ $# -ne 1 ]
then
    echo "Please specify chaper name"
    return -1
fi

CHAPTER=${1}
mkdir Chapters/$CHAPTER
mkdir Chapters/$CHAPTER/Figures
echo -e "\\graphicspath{{Chapters/$CHAPTER/Figures/}}\n\\\\chapter{$CHAPTER}\n\\label{chap:$CHAPTER}" >> Chapters/$CHAPTER/$CHAPTER.tex
echo -e "\n%\\include{Chapters/$CHAPTER/$CHAPTER}" >> Thesis.tex

