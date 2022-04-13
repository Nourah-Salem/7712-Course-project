

import numpy as np
import pandas as pd

def LCS(query,read):
    #Compares two sequences, outputs longest string length and matching reads
    m=len(query)
    n=len(read)
    # constructure an nXm matrix
    LCS_mat = [[0 for k in range(n+1)] for l in range(m+1)]
    result=0
    
    # filling the matrix
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                LCS_mat[i][j] = 0
            elif (query[i-1] == read[j-1]):
                LCS_mat[i][j] = LCS_mat[i-1][j-1] + 1
                result = max(result, LCS_mat[i][j])
            else:
                LCS_mat[i][j] = 0
    lcs_arr = np.array(LCS_mat)
    max_pos = np.where(lcs_arr == np.nanmax(lcs_arr)) 
    return result,True, read, LCS_mat, max_pos
        
    
if __name__ == "__main__":

    #calling the functions
    query = 'GGGATCGGCCATTGAACAAGATGGATTGCACGCAGGTTCTCCGGCCGCTTGGGTGGAGAGGCTATTCGGCTATGACTGGGCACAACAGACAATCGGCTGCTCTGATGCCGCCGTGTTCCGGCTGTCAGCGCAGGGGCGCCCGGTTCTTTTTGTCAAGACCGACCTGTCCGGTGCCCTGAATGAACTGCAGGACGAGGCAGCGCGGCTATCGTGGCTGGCCACGACGGGCGTTCCTTGCGCAGCTGTGCTCGACGTTGTCACTGAAGCGGGAAGGGACTGGCTGCTATTGGGCGAAGTGCCGGGGCAGGATCTCCTGTCATCTCACCTTGCTCCTGCCGAGAAAGTATCCATCATGGCTGATGCAATGCGGCGGCTGCATACGCTTGATCCGGCTACCTGCCCATTCGACCACCAAGCGAAACATCGCATCGAGCGAGCACGTACTCGGATGGAAGCCGGTCTTGTCGATCAGGATGATCTGGACGAAGAGCATCAGGGGCTCGCGCCAGCCGAACTGTTCGCCAGGCTCAAGGCGCGCATGCCCGACGGCGATGATCTCGTCGTGACCCATGGCGATGCCTGCTTGCCGAATATCATGGTGGAAAATGGCCGCTTTTCTGGATTCATCGACTGTGGCCGGCTGGGTGT'
    print ('Query: ', query)
    df = pd.read_csv("D:/PhD at Anschutz/semester2/7712/Day3/assignment material/samples for test/READS.csv")
    
    reads = df['read'].tolist()    
    accepted_reads = []
    cadndidate_read_count =1
    candidate_reads=[]
    mtch_results = []
    read_id =[]
    sstart = []
    send = []
    qstart= []
    qend = []
    for seq in reads:
        # each comparison, we return the max letter match number
        # we return the read that made the max match
        # and its matrix match
        result, flag, read, LCS_mat, max_pos = LCS(query, seq)
        if flag:
            mtch_results.append(result)
            candidate_reads.append(read)
            read_id.append(df["id"][cadndidate_read_count])
            sstart.append(max_pos[0][0]-result)
            send.append(max_pos[0][0])
            qstart.append(max_pos[1][0]-result)
            qend.append(max_pos[1][0])
            print ("candidate read", cadndidate_read_count, ":")
            print (read)
            print ("number of char match:", result)
            print ("-------------------------------")
        cadndidate_read_count+=1
        





#please uncomment this part if you would like to view the matching matrix
# from tabulate import tabulate
# print(tabulate(LCS_mat))


# combine all the created list into one dataframe
df2 = pd.DataFrame(list(zip(read_id, candidate_reads, mtch_results,sstart, send, qstart,qend)),
               columns =['read_id', 'candidate_read', "num_match_char", "read_start", "read_end", "query_start", "query_end"]).replace(r'\n','', regex=True)


# sort the dataframe base on the number of char match between each raed and the query 
from natsort import index_natsorted
df3 = df2.sort_values(by=['num_match_char'], key=lambda x:np.argsort(index_natsorted(df2["num_match_char"])))[::-1]
df3.reset_index(drop=True, inplace=True)


# select threshold for alignment lengthins
df3 = df3[df3.num_match_char > 130]
df3.to_csv("./output/results.csv")


# create the top 2 contig list:
contig1 = df3.drop_duplicates(subset= ['read_start','read_end'],keep='first')
contig1 = contig1.drop_duplicates(subset= 'num_match_char',keep='first')
contig1.reset_index(drop=True, inplace=True)
contig1['contig_id'] = 'contig1'
col = contig1.pop("contig_id")
contig1.insert (1, "contig_id", col)




# check the coverage of the query with the selected candidate reads
Q_bolean =  [False for i in range(len(query))]

obj = {}
for i in range(len(contig1.candidate_read.tolist())):
     obj['l'+str(read_id[i])] = [False for i in range(len(query))]

# build a Boolean operator OR to check if the query list is all covered by the candidate reads
candidates = pd.DataFrame()
c = 0
for key in obj:     
    print (contig1.candidate_read[c])
    obj[key][contig1.read_start[c]:contig1.read_end[c]] = [True for i in range(contig1.read_start[c],contig1.read_end[c])]    
    for i,char_r in enumerate(obj[key]):
        if np.logical_or(Q_bolean[i],char_r) == True:
            Q_bolean[i] = True
    candidates = candidates.append(contig1.iloc[[c]])
    c+=1
print (Q_bolean)











