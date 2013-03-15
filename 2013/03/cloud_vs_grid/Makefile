CLEAN=xxxx.log xxxx.nav xxxx.out xxxx.pdf xxxx.snm xxxx.toc xxxx.aux
COMPILER=texi2pdf

OUT=cloud_vs_grid

LIXO=$(patsubst xxxx%,$(OUT)%,$(CLEAN))

all: $(OUT).pdf

%.pdf : %.tex
	@echo 
	@echo $<
	$(COMPILER) $<

see: all
	xpdf -fullscreen $(OUT).pdf

clean:
	rm -rf $(LIXO)

