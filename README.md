
# Constructing the Longest Conting (Containing a Specific Query) from DNA Reads 


![Screenshot2](https://user-images.githubusercontent.com/65971542/163245219-c43f2fd1-6479-470a-8801-9b470b5ef729.png)

[https://ec.europa.eu/research-and-innovation/en/horizon-magazine/new-braking-systems-and-satellite-navigation-help-more-trains-run-europes-tracks]

DNA sequencing into small fragments is an important step for studing the genetic material. This allows to find the associations between modifications within the gene and potential phenotypic changes. Genome assembly refers to the process of putting small nucleotide sequence (reads) into the correct order. at the end of sequencing, assembly is required, as the sequence read lengths are much shorter than most genomes or even most genes. therefore, analyzing them requires assembly. And the process of assembly requires reconstructing the larger size of sequence is called contig. However, the process of reassembly  -within the genetic context- is not a straightforward process. it is similar to a complex train trafic lines that intersect with each other! 
##

In this project, we have a list of DNA reads that we want to make a longer query from and a spcific query, and we aim at building the longest contig spanning the given query, this could achieved via the overlapping the sequences and those that allow for certain range of alignment with each other are good candidates for building the contig. Such overlaps are specifically between the reads and the query. 

![Screenshot3](https://user-images.githubusercontent.com/65971542/163247740-ab9fdc49-9b2f-4fe4-afb4-382091e84efb.png)

We allowed for all possible overlaps between the query and all reads we have using Longest common substring algorithm implemented in a dynamic programming frame. We then selected the candidate reads by the length of match they can make with the query. We used a threshold of 130 and more bases matching between the query and the reads. We also validated that the 43 selected for making the longest contig are unique and are covering the whole query through the following scripts (respectively):
1. Generate_contigs.py
2. matching_range.py 

## Inputs
1. List of reads (str), in a FASTA format
2. Query (str), in FASTA format
## Outputs
1. Long strings ( 4 candidate contigs) that carries the query inside: ALLELES.fasta
2. Long string (candidate contigs) that carries the query inside: results.fasta
3. A detailed list of the overlapping reads with the query their matching indecies: ALLELES.aln
4. A detailed list of the overlapping reads with the query their matching indecies: ALLELES.CSV

## Main Steps:
1. We used the longest common substring algorithm implemented in the **/Longest_Contig_spanning_query/matching_range.py** (LCS function) to measure the overlap of the reads list (124520 reads) with the query. **in fact**, we made an initial trial of 10,000 reeds and looked at the range of characters (match length) that match to the query. from that, we had an initial assumption about the legit alignments versus those that can happen at random the following graph shows a sample of 10,000 reads aligned to the query. 

![Figure1](https://user-images.githubusercontent.com/65971542/163258552-2b2fc827-47c9-4e50-a754-9818a948e44d.png)

2. We can see this spike in the graph tells us that the majority of the alignments were too short that they might be seen as random matches. Their lengths were from 7 character match to 13 characters. Therefore, then decided to filter the reads by the number of matchs they made with the query, becasue it is possible that many of the small range match can actually be present in many DNA fragments (reads), therefore considering such reads is not helpful.
3. we made a series of trail for the best threshold that allows for lowering the redunduncy of match and maintain the query coverage as well:

|Length of Alignment Threshold (bases) |Number of reads per contig |Do they cover the whole query range? |
| :----------------------------------- |:-------------------------:| -----------------------------------:|
| > 13                                 |153                        |True                                 |
| > 45                                 |127                        |True                                 |
| > 90                                 |82                         |True                                 |
| > 130                                |43                         |True                                 |
| > 140                                |24                         |False                                |

Once we found that setting the threshold for the match length (140 characters and more) generated a 24 reads and those reads are not spanning the whole query (meaning that part of the query in not found or covered by any of those 24 reads), we decided that our thresholds for the matchs between the reads and the query is 130.

Meaning that those **43 reads** that we able to make alignment with the query with **130 bases match or more** were selected as our **contig** building blocks and **query carriers** as well

# Example of the output
As we selected the best charcter match range and the number of candidate reads, we validated that those reads are able to cover the whole query using **/Longest_Contig_spanning_query/matching_range.py** (np.logical_or function). This is a smaple of one detailed output file:

![Screenshot4](https://user-images.githubusercontent.com/65971542/163257747-81e9e0b9-c953-41cb-a00d-d50a903dab9c.png)

This table shows a smple of the reads that can make contig1, their start and end indecies and the start and end indecies of the parts of the query matching 

## Installation
make sure you have python 3.6 and 
install the folling packages before running
```python
pip install pandas
pip install seaborn
pip install -U matplotlib
numpy
unittest
```
## Usage 
A. Please make sure to download the repo so that the data files are in the right place
B. For converting the input FASTA files to CSV and generate sample data, please run:
```python
python EDA_sample_prep.Py
```
This will return 
1. A **CSV** file of our input reads
2. sample_query: 
GGGTGGTCTCCTTTACTTGTAACTTGTCCTAAGTCGTTTCTTTAGCCCATGGTGTTGGTGGGGTTCACAGAAACACCCAGAGTTCACCTGAGCCTTTAACCAATCCCAGCCAGGAGCCAGAGCCCAGGCACAGGTGCAGGACCACGGCAGGCCCAGTATTTGGCTTCCACAGAAGCTACGGCATCAGAAGTCGTGTTTAATTGTTCTTCTGCTTCTTCCTGTCTCTCGGTGGCTCCTTGAGGGCTTTGATGATCAGGCTGACCCTAAAATATTGTAAAAAGCTAACAGTTTACCATTTTCCCAGCGTGAAAGTCCATCCCTAGCTGAGCTGTTTGAGGAACACAGAGGAAGCAGCGACTGGACCGAAGGTTGCTTTACTTTGGTCCTGTCGGTTCTCCCCTCAACTCAGCCTGGGCCTGCCCTGGGCCTATTCACGTCATGGCAAATTACATTTCTTTTCCGAGCCTGTCCCGATGAAGATGCGGCCGTCCTGCAGGATGCACCTCATCCTGTAGTCAATGTGCTGCAGCATCTTGCTGCTCTTGCCCACCGTCATGGTGGCGGCTCGGATGGCTCAGATTCCCGCCGGATTCTCTGCACAGAGCGCAGTCGCCAG

C. For Comparing the reads to the query and selecting the reads that can make the longest contig spanning the query, please run:
```python
python matching_range.py 
```
This will return:
the full version of the table in the **Example of the output** section

D. To genetare the assgignment output files for the 4 longest candidate contig, please run:
```python
python PythonGenerate_contigs.py
```
This will return:
1. all the output files requiered in the assignment
These files are available in the **Output** folder

E. To plot the histogram of the match reages, please reun: 
```python
python Histogam_plot.py
```
## Unit Testing
We focused on the correctness of the input data though the **class TestLCS** in the **testing_matching_range.py** file.
we tested:
```python 1.test_LCS_input_type
2. test_UpperCase
3. test_non_empty_input
```
