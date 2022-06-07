#!/bin/sh

.PHONY: all

all: out/00-intro.tex out/10-context.tex out/20-analysis.tex out/tab_test_overview.tex img/barplot.pdf out/80-evaluation.tex out/thesis.pdf

.PHONY: all clean spelling

out/00-intro.tex: content/00-intro.md chapter.tpl.tex
	mkdir -p out/src
	pandoc --to latex --template chapter.tpl.tex content/00-intro.md >out/00-intro.tex
	echo "\\input{out/00-intro.tex}" >>out/chapters.tex

out/10-context.tex: content/10-context.md chapter.tpl.tex
	pandoc --to latex --template chapter.tpl.tex content/10-context.md >out/10-context.tex
	echo "\\input{out/10-context.tex}" >>out/chapters.tex

out/20-analysis.tex: content/20-analysis.md chapter.tpl.tex
	pandoc --to latex --template chapter.tpl.tex content/20-analysis.md >out/20-analysis.tex
	echo "\\input{out/20-analysis.tex}" >>out/chapters.tex

out/tab_test_overview.tex: src/tab_test_overview.tex
	cp src/tab_test_overview.tex out/tab_test_overview.tex

img/barplot.pdf: data/tests.csv pyplot.py
	./pyplot.py

out/80-evaluation.tex: content/80-evaluation.md chapter.tpl.tex data/tests.csv
	pandoc --to latex --template chapter.tpl.tex content/80-evaluation.md >out/80-evaluation.tex
	echo "\\input{out/80-evaluation.tex}" >>out/chapters.tex

out/thesis.pdf: thesis.tex out/00-intro.tex out/10-context.tex out/20-analysis.tex out/80-evaluation.tex img/barplot.pdf out/tab_test_overview.tex
	latexmk -pdf -outdir=out thesis.tex

#clears everything from "out" dir
clean:
	rm -rf out/*

#checks mistakes in spelling
spelling:
	aspell --lang=en_gb --mode=markdown -c content/00-intro.md
	aspell --lang=en_gb --mode=markdown -c content/10-context.md
	aspell --lang=en_gb --mode=markdown -c content/20-analysis.md
	aspell --lang=en_gb --mode=markdown -c content/80-evaluation.md

