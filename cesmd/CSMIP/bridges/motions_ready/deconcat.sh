SHELL=/usr/bin/bash

# make all .ZIP files into .zip files
mkdir lowercase
for i in *.ZIP; do mv $i lowercase/${i,,}; done
cd lowercase
for i in *; do mv $i ../$i; done
cd ..
rm -d lowercase

# unzip all records and look inside
for ziprecord in *.zip; do \
    mkdir temp; \
    unzip $ziprecord -d temp; \
    # if there is only one .v2 file, then we know it's a concatenated record. deconcatenate it.
    if [[ $(ls temp/*.[vV]2 -1 | wc -l) == 1 ]]; then \
        # move the original record into the concat_originals folder
        mkdir -p concat_originals; \
        mv $ziprecord concat_originals/$ziprecord; \
        # start deconcatenating
        echo -e "\n\n Deconcatenating record. \n\n"; \
        mkdir temp/deconcat; \
        # copy the single .v2 file to temp/deconcat/temp.v2
        for i in temp/*.[vV]2; do \
            cp $i temp/deconcat/temp.v2; \
            # get the channel numbers
            grep '/&' temp/deconcat/temp.v2 > channel_number_lines.txt; \
            grep -o '[0-9] \|[0-9][0-9] ' channel_number_lines.txt > channel_numbers.txt; \
            # for each channel, extract its data from temp/deconcat/temp.v2, then delete its data from temp/deconcat/temp.v2
            while read -r line; do \
                echo CHAN0$(printf '%02d' $line).v2; \
                sed '0,/\/\&/!d' temp/deconcat/temp.v2 > temp/deconcat/CHAN0$(printf '%02d' $line).v2; \
                sed -i '0,/\/\&/d' temp/deconcat/temp.v2; \
                done \
                < channel_numbers.txt; \
            rm channel_number_lines.txt channel_numbers.txt temp/deconcat/temp.v2; \
        done; \
        # zip up the channel data and name it the same as the original .zip
        zip -j $ziprecord temp/deconcat/*; \
        for i in temp/deconcat/*; do rm $i; done; \
        rm -d temp/deconcat; \
    else \
        echo -e "\n\n Record already deconcatenated. \n\n"; \
    fi; \
    for i in temp/*; do rm $i; done; \
    rm -d temp; \
done