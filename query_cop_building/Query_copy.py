

import numpy as np

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
    shape=lcs_arr.shape
    max_pos = np.where(lcs_arr == np.nanmax(lcs_arr)) #may produce problem 
                                                      # if max is not in the last column
    
    # here we select the read that has the longest match with the query
    # and that match is at the end of the read 
    if max_pos[1][0]+1 == shape[1] and max_pos[0][0] == result:
        return result,True, read, LCS_mat
    else:
        return 0,False, '', LCS_mat
        
    
def cut_query(query,result):
    # cut each matching part of the query and allow for begining match all the time
    return query[result:]

    
if __name__ == "__main__":

    #calling the functions
    query = 'AAATTTCCCTTTGGGTAGTGTT'
    print ('Query: ', query)
    reads = ["AAATT",'BBBBBBBAAATTTCCC' ,"IJLKMLIJL", "TTTGGGT", "AGTGTT"]
    
    
    accepted_reads = []
    while len (query) > 0: 
        candidate_reads=[]
        mtch_results = []
        for seq in reads:
            # each comparison, we return the max letter match number
            # we return the read that made the max match
            # and its matrix match
            result, flag, read, LCS_mat = LCS(query, seq)
            if flag:
                mtch_results.append(result)
                candidate_reads.append(read)
            mtch_results.sort()
            sorted_reads = [x for _,x in sorted(zip(mtch_results,candidate_reads))]
        query = cut_query(query, mtch_results[-1])
        reads.remove(sorted_reads[-1])
        accepted_reads.append(sorted_reads[-1])
    print ("query building reads: ", accepted_reads) 


#please uncomment this part if you would like to view the matching matrix

# from tabulate import tabulate
# print(tabulate(LCS_mat))
