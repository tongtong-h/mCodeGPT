import pandas as pd
import openai

import openai

openai.api_key = "abc"
openai.api_base = "abc" # your endpoint should look like the following
openai.api_type = 'azure'
openai.api_version = '2023-05-15'  # this may change in the future
deployment_name = "mcodegpt_gpt_35_16k"   # This will correspond to the custom name you chose for your deployment when you deployed a model.

SAVE_DIRECTORY_groundtruth = "clinical_notes/"
SAVE_DIRECTORY_description = "ground_truth/"

import os

# Check if the directories exist, and if not, create them
if not os.path.exists(SAVE_DIRECTORY_description):
    os.makedirs(SAVE_DIRECTORY_description)

if not os.path.exists(SAVE_DIRECTORY_groundtruth):
    os.makedirs(SAVE_DIRECTORY_groundtruth)
    
import os
import random

    
def save_note_to_file(note, filename):
    with open(filename, 'w') as file:
        file.write(note)

def main():
    if not os.path.exists(SAVE_DIRECTORY_description):
        os.makedirs(SAVE_DIRECTORY_description)
    if not os.path.exists(SAVE_DIRECTORY_groundtruth):
        os.makedirs(SAVE_DIRECTORY_groundtruth)
    
    for i in range(1,1000): 
        try:
            gt_df = pd.read_csv(os.path.join(SAVE_DIRECTORY_groundtruth, '{}.csv'.format(i)))
        except Exception as e:
            print(i, e)
            
        notes = str(gt_df.loc[0].to_dict())
        
        # 2. descriptive format 
        response = openai.ChatCompletion.create(
            deployment_id = deployment_name,
            messages=[
                {
                    "role": "user",
                    "content": "Convert the EHR table to narratives. You need to write several paragraphs of a cancer report for a patient based on the following list of information. You need to use all the information present in the list. Do not give me a list, use descriptive language. "  + notes
                },
            ],
            max_tokens=4096*2)
        notes_descriptive = response.choices[0].message.content
        
        filename = os.path.join(SAVE_DIRECTORY_description, f"{i}.txt")
        save_note_to_file(notes_descriptive, filename)
        print(f"Saved {filename}")
            
if __name__ == "__main__":
    main()