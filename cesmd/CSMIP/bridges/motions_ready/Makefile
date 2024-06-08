SHELL=/usr/bin/bash

# Before this, make all .ZIP into .zip:
# - mkdir lowercase
# - for i in *.[zZ][iI][pP]; do mv $i lowercase/${i,,}; done
# - cd lowercase
# - for i in *; do mv $i ../$i; done
# - cd ..
# - rm -d lowercase

# <pattern> : <patterns>... 
# 	command
# 	command
# 	...
# 	command


# make nc73580646_ce58658p.zip
# for i in *.zip; do make $i; done
%.zip: Makefile
	mkdir temp
	cp $@ temp/$@
	unzip $@ -d temp
	if [[ $$(ls temp/*.[vV]2 -1 | wc -l) == 1 ]]; then \
		mkdir -p concat_originals; \
		mv $@ concat_originals/$@; \
		echo -e "\n\n Deconcatenating record. \n\n"; \
		mkdir temp/deconcat; \
		for i in temp/*.[vV]2; do \
			cp $$i temp/deconcat/temp.v2; \
			grep '/&' temp/deconcat/temp.v2 > channel_number_lines.txt; \
			grep -o '[0-9] \|[0-9][0-9] ' channel_number_lines.txt > channel_numbers.txt; \
			while read -r line; do \
				echo CHAN0$$(printf '%02d' $$line).v2; \
				sed '0,/\/\&/!d' temp/deconcat/temp.v2 > temp/deconcat/CHAN0$$(printf '%02d' $$line).v2; \
				sed -i '0,/\/\&/d' temp/deconcat/temp.v2; \
				done \
				< channel_numbers.txt; \
			rm channel_number_lines.txt channel_numbers.txt temp/deconcat/temp.v2; \
		done; \
		zip -j $@ temp/deconcat/*; \
		for i in temp/deconcat/*; do rm $$i; done; \
		rm -d temp/deconcat; \
	else \
		echo -e "\n\n Record already deconcatenated. \n\n"; \
	fi
	for i in temp/*; do rm $$i; done
	rm -d temp
