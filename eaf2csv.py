#! /Users/steven/anaconda3/bin/python3
# What: python script was generated manually by S Elmlinger February in 2019

# Why: Convert all ELAN (.eaf) files in a directory to csv files

#
#
# step 1: load packages
#
#

import glob     # Import glob to easily loop over files
import pympi    # Import pympi to work with elan files
import os
import pandas as pd
import numpy as np

#
#
# step 2: load data
#
#

# subject list
subjectarray = np.array([2, 3, 4, 5, 7, 9, 10, 12, 14, 16, 18, 22, 24,
                         25, 28, 29, 30, 33, 45, 46, 48, 50, 51, 53, 55, 84])
'''
Enter in all of the subject IDs into the variable above, comma separated.
'''

# Define variables
corpus_root = '/Users/steven/Dropbox/Cornell/Spring_2019/Projects/Nat_Stats_Causality/preprocessing/ELAN_files_synced/'
output_path = '/Users/steven/Dropbox/Cornell/Spring_2019/Projects/Nat_Stats_Causality/analyses/data/'
ort_tier_names = ['final_infraphonology','Parent']
directory = os.fsencode('{}/eaf/'.format(corpus_root))

#
#
# step 3: Initialize aggregator
#
#

columns = ['sub', 'onset', 'offset', 'cat','tier']
output = pd.DataFrame(columns=columns)

for a in range(len(subjectarray)):
    sub = subjectarray[a]
    flag = -1
# Loop over all elan files the corpusroot subdirectory called eaf
    for file_path in glob.glob('{}/eaf/*.eaf'.format(corpus_root)):
        # Initialize the elan file
        flag = flag + 1
        filename = os.listdir(directory)[flag]
        # correct for .DS_store files
        if filename.decode('utf-8') == '.DS_Store':
            os.remove(os.path.join(directory.decode('utf-8'), filename.decode('utf-8')))
            break
        file = os.fsdecode(filename)
        if file == "s%d_sync_check.eaf" % sub:
            eafob = pympi.Elan.Eaf(file_path)
            # Loop over all the defined tiers that contain orthography
            for ort_tier in ort_tier_names:
                # If the tier is not present in the elan file spew an error and
                # continue. This is done to avoid possible KeyErrors
                # If tier is present we can loop through the annotation data
                counter = -1
                all_utt = pd.DataFrame(np.nan, index=[0], columns=columns)
                for annotation in eafob.get_annotation_data_for_tier(ort_tier):
                    # We are only interested in the utterance
                    counter = counter + 1
                    all_utt.loc[counter, 'sub'] = sub
                    all_utt.loc[counter, 'onset'] = annotation[0] / 1000
                    all_utt.loc[counter, 'offset'] = annotation[1] / 1000
                    all_utt.loc[counter, 'cat'] = annotation[2]
                    all_utt.loc[counter, 'tier'] = ort_tier
                output = output.append(all_utt)
#
#
# step 4: output individual .csv files
#
#

output.to_csv('{}/inf_voc_and_parent_utt_VSIM.csv'.format(output_path))
