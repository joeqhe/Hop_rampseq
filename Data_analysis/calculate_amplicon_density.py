#!/usr/bin/python

# This file located at /home/hejoe/git_repos/Hop_rampseq/Data_analysis/calculate_amplicon_density.py

# 11542_6815_60.0-24312_9039_55.0 is target amplicon to look for in hop genome


import os

data_dir = "/oldhpc/data/scratch/armita/hop_genomics/rampseq/primer_design/locations/H.lupulus/cascade/split"
contig_size_file = "/home/hejoe/git_repos/Hop_rampseq/Data_analysis/contig_sizes.tsv"

file_end_pattern = "_kmer_pairs.tsv"

amplicon_code = "11542_6815_60.0-24312_9039_55.0"


out_file = "/home/hejoe/git_repos/Hop_rampseq/Data_analysis/For_plotting/%s_amplicon_distribution.csv" % (amplicon_code)
os.remove (out_file)



os.chdir (data_dir)



def function_count_amplicon_code (file_path, amplicon_code):
	amplicon_count = 0
	file_in = open (file_path)
	for line in file_in:
		if line.startswith (amplicon_code):
			amplicon_count += 1
	file_in.close ()
	return amplicon_count

tot_file_count = 0


for contig in os.listdir (data_dir):
	if contig.endswith (file_end_pattern):
		tot_file_count += 1

file_out = open (out_file, "w+")
os.chmod (out_file, 0777)


this_file_count = 0

file_in_size = open (contig_size_file)

for contig in os.listdir (data_dir):
	if contig.endswith (file_end_pattern):
		amplicon_count = function_count_amplicon_code (contig, amplicon_code)
		this_file_count += 1
		file_out.write (contig + "," + str (amplicon_count) + "\n")
		print "searched through %d of %d" % (this_file_count, tot_file_count)

file_out.close ()




# in_file=/oldhpc/home/hajduk/funsies/hop_rampseq/assembly_klari/reference_klari/Hum_lup_klari/cascade_klari/hopbase_klari/cascadePrimary.fasta
# out_file=/home/hejoe/git_repos/Hop_rampseq/Data_analysis/contig_sizes.tsv
# cat $in_file | awk '$0 ~ ">" {print c; c=0;printf substr($0,2,100) "\t"; } $0 !~ ">" {c+=length($0);} END { print c; }' >> $out_file
# cat $in_file | awk '$0 ~ ">" {print c; c=0;printf substr($0,2,100) "\t"; } $0 !~ ">" {c+=length($0);} END { print c; }'
