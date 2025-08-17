#!/bin/bash

declare -a method_arr=("RLS" "BFOP" "2POP")

for method in "${method_arr[@]}"
do
    for i in {1..1000};
    do
        echo ${method}        
        if test -e output_GDC/output/${i}.csv; then
          echo "File exists: "output/output/${i}.csv
        else
          python3 main.py -i ../GDC_notes_analysis/clinical_notes_descriptive_1000/${i}.txt -m ${method} -o output_GDC/output_gemma_${method}/${i} --huggingface "Y" --model_card "google/gemma-7b-it" --huggingface_api  "abc"
        fi  
    done
done
