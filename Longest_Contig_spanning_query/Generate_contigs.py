# Generating top 4 contig

import pandas as pd

df3 = pd.read_csv("./output/results.csv")

# create the top 2 contig list:
contig1 = df3.drop_duplicates(subset= ['read_start','read_end'],keep='first')
contig1 = contig1.drop_duplicates(subset= 'num_match_char',keep='first')
contig1.reset_index(drop=True, inplace=True)
contig1['contig_id'] = 'contig1'
col = contig1.pop("contig_id")
contig1.insert (1, "contig_id", col)

contig2 = contig1.drop_duplicates(subset= 'num_match_char',keep='last')
contig2.reset_index(drop=True, inplace=True)
contig2['contig_id'] = 'contig2'
col = contig2.pop("contig_id")
contig2.insert (1, "contig_id", col)


contig3 = df3.drop_duplicates(subset= ['read_start','read_end'],keep='last')
contig3 = contig3.drop_duplicates(subset= 'num_match_char',keep='first')
contig3.reset_index(drop=True, inplace=True)
contig3['contig_id'] = 'contig3'
col = contig3.pop("contig_id")
contig3.insert (1, "contig_id", col)


contig4 = contig3.drop_duplicates(subset= 'num_match_char',keep='last')
contig4.reset_index(drop=True, inplace=True)
contig4['contig_id'] = 'contig4'
col = contig4.pop("contig_id")
contig4.insert (1, "contig_id", col)




contig1["candidate_read"].to_csv("D:/PhD at Anschutz/semester2/7712/Day3/module3/ALLELES.fasta", index = False, header=False)

frames = [contig1, contig2, contig3, contig4]
final_file = pd.concat(frames, ignore_index=True)  
final_file['read_id'] = final_file['read_id'].map(lambda x: x.lstrip('>'))



final_file.to_csv("./output/ALLELES.aln")
final_file.to_csv("./output/ALLELES.csv")
