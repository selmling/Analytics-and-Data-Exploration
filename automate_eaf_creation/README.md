# `create_eaf.py` will create a new eaf file from a template eaf file

To use:

1. Create the master.eaf file (called `'GL_master.eaf'` in the script but you can call it whatever you want)

    - This master.eaf file should eaf file should contain all the tiers and controlled vocabulary you want

2. Change the `corpus_root` variable to the path where your raw video/audio are stored

3. Change the `media_name` variable to the name of the media you'll be linking to your eaf (ELAN) file

    - note that if a *normalized* version of the audio has not been created, this will not work

4. Drag the `create_eaf.py` script to the same folder as the `master.eaf` file saved to `elan_file` variable

5. Run the script (see [this video](https://drive.google.com/file/d/1kTSkCxr2I8l1b1GuFXpeoelC1sRTaS4M/preview) to learn how to run a python script)

Note: if you want to run this on multiple subjects in the same directory, you'll just complete step 3 and step 5 again for the new subjects.
