import pandas as pd
import openai
import os
import random


openai.api_key = "OPENAI_API_KEY"
openai.api_base = "https://deploymentname.openai.azure.com/" # your endpoint should look like the following
openai.api_type = 'azure'
openai.api_version = '2023-05-15'  # this may change in the future
deployment_name = "mcodegpt_gpt_35_16k"   # This will correspond to the custom name you chose for your deployment when you deployed a model.


GROUND_TRUTH_DIRECTORY = "ground_truth/"
CLINICAL_NOTES_DIRECTORY = "clinical_notes/"

def create_directory()
    # Check if the directories exist, and if not, create them  
    if not os.path.exists(CLINICAL_NOTES_DIRECTORY):
        os.makedirs(CLINICAL_NOTES_DIRECTORY)


def generate_note(ehr_dict, note_name):
    response = openai.ChatCompletion.create(
        deployment_id = deployment_name,
        messages=[
            {
                "role": "user",
                "content": f"Convert the EHR table to narratives. You need to write several paragraphs of a cancer report for a patient based on the following list of information. You need to use all the information present in the list. Do not give me a list; use descriptive language.
EHR table: \n{ehr_dict}
"
            },
        ],
        max_tokens=4096)

    
    notes_descriptive = response.choices[0].message.content
    filename = os.path.join(CLINICAL_NOTES_DIRECTORY, f"{note_name}.txt")
    save_note_to_file(notes_descriptive, filename)
    
    print(f"Saved {filename}")
        
if __name__ == "__main__":
    create_directory()
    ehr_dict = pd.read_csv(os.path.join(GROUND_TRUTH_DIRECTORY, "1.csv")).to_dict()
    generate_note(ehr_dict)