import pympi

# create empty file
elan_file = pympi.Elan.Eaf(file_path='GL_master.eaf', author='Steven Elmlinger')

# media file name
corpus_root = '/Volumes/RAID/path/to/study/video/file/folder/'
media_name = 'Gl-cc-f31-s8-B1'
# remove linked media
elan_file.remove_linked_files()
# add media_files
elan_file.add_linked_file('%s%snormalized.wav' % (corpus_root,media_name))
elan_file.add_linked_file('%s%s.mov' % (corpus_root,media_name), mimetype='mov')
# save new file
elan_file.to_file(file_path="%s%s.eaf" % (corpus_root,media_name))
