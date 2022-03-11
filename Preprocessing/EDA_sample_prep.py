

import pandas as pd

def FASTA2DF (file):
    # The function takes the FASTA file, convert it 2-column dataframe (one for the ID, one for the read)
    
    # open file and iterate through the lines, composing each single line as we go
    id_lines = []
    seq_lines = []
    with open(file) as fp:
         for line in fp:
             if line.startswith('>'):
                 id_lines.append(line)
             else:
                 line.replace('\n', "")
                 seq_lines.append(line)
    
    # Calling DataFrame constructor after zipping
    # both lists, with columns specified
    df = pd.DataFrame(list(zip(id_lines, seq_lines)),
                   columns =['id', 'read']).replace(r'\n','', regex=True)
    
    #Calculates the length of each read, append the length
    df1= df.read.str.len().tolist()
    df1 = pd.Series(df1 , name = 'length')
    
    
    #Sort the reads descendingly
    df2 = pd.concat([df, df1], axis=1, join="inner").sort_values("length",ascending=False)
    df2.reset_index(drop=True, inplace=True)
    
        
    return df2



import seaborn as sns
import matplotlib.pyplot as plt


def view_len(df):
    sns.set_style("white")
    # Import data
    x1 = df["length"]
    # Plot
    kwargs = dict(alpha=0.8, bins=20)
    plt.figure(figsize=(10,7), dpi= 85)
    plt.hist(x1, **kwargs, color='g', label='Ideal')
    plt.gca().set(title='Reads Length Frequency', ylabel='Frequency');




def modify_reads (df):
    
    small_df = df.iloc[:100].copy()
    
    #Modifications in the reads to allow overlap
    modf1 = "AGAAGTC"
    modf2 = "CCCTAA"
    mosmall_df = "GTCGGTT"
    modf4 = "TTCCGAGCCT"
    
    
    sample_query = small_df.at[2,'read'][:-len(modf1)] + modf1 + small_df.at[76,'read'][:-len(modf2)] + modf2 + small_df.at[49,'read'][:-len(mosmall_df)] + mosmall_df + small_df.at[25,'read'][:-len(modf4)] + modf4 + small_df.at[99,'read']
                
    
    
    small_df.at[2,"read"] = small_df.at[2,'read'][:-len(modf1)] + modf1
    
    small_df.at[76,"read"] = modf1 + small_df.at[76,'read'][len(modf1):-len(modf2)] + modf2
    
    small_df.at[49,"read"] = mosmall_df[::-1] + small_df.at[49,'read'][len(modf2):-len(mosmall_df)][::-1] + modf2[::-1]
    
    small_df.at[25,"read"] = mosmall_df + small_df.at[25,'read'][len(mosmall_df):-len(modf4)] + modf4
    
    small_df.at[99,"read"] = modf4 + small_df.at[99,'read'][len(modf4):]
    print ("sample query: ", sample_query)
    return sample_query    


        
if __name__ == "__main__":
    df = FASTA2DF("./Data/READS.fasta")
    view_len(df)
    sample_query = modify_reads(df)

