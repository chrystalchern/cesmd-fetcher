SHELL=/usr/bin/bash

for CEfolder in CE*; do \
    # deconcatenate
    cp deconcat.sh $CEfolder/deconcat.sh; \
    cd $CEfolder; \
    bash deconcat.sh; \
    rm deconcat.sh; \
    # make summaries
    mkdir -p CSMIP_summaries; \
    for ziprecord in *.zip; do \
        python -m quakeio -Stjson $ziprecord > CSMIP_summaries/${ziprecord/%.zip/.json}; \
    done; \
    cd ..; \
done