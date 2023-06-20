# Import required modules
import pympi
import pandas as pd

def convert_elan_to_csv(file_paths, tiers, output_csv_path):
    df_list = []
    tiers = tiers.split(',')
    
    for file_path in file_paths:
        eaf = pympi.Elan.Eaf(file_path)
        file_name = eaf.get_file_path().split('/')[-1]
        
        for tier in tiers:
            annotations = eaf.get_annotation_data_for_tier(tier)
            for annotation in annotations:
                df_list.append({
                    'filename': file_name,
                    'index': annotation[0],
                    'onset': annotation[2],
                    'offset': annotation[3],
                    'tier': tier,
                    'annotation': annotation[1]
                })
    
    df = pd.DataFrame(df_list)
    df.to_csv(output_csv_path, index=False)
