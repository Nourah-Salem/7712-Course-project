
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

## Usage Example
1. We used the longest common substring algorithm implemented in the **Longest_Contig_spanning_query/matching_range.py** to measure the overlap of the reads list (124520 reads) with the query. 
2. We then decided to filter the reads by the number of matchs they made with the query, becasue it is possible that many of the small range match can actually be present in many DNA fragments (reads), therefore considering such reads is not helpful.
3. we made a series of trail for the best threshold that allows for lowering the redunduncy of match and maintain the query coverage as well:

|Length of Alignment Threshold (bases) |Number of reads per contig |Do they cover the whole query range? |
| :----------------------------------- |:-------------------------:| -----------------------------------:|
| > 13                                 |153                        |True                                 |
| :----------------------------------- |:-------------------------:| -----------------------------------:|
| > 45                                 |127                        |True                                 |
| :----------------------------------- |:-------------------------:| -----------------------------------:|
| > 90                                 |82                         |True                                 |
| :----------------------------------- |:-------------------------:| -----------------------------------:|
| > 130                                |43                         |True                                 |
|  ----------------------------------- | ------------------------- | ----------------------------------- |
| > 140                                |24                         |False                                |

Once we found that setting the threshold for the match length (140 characters and more) generated a 24 reads and those reads are not spanning the whole query (meaning that part of the query in not found or covered by any of those 24 reads), we decided that our thresholds for the matchs between the reads and the query is 130.
Meaning that those **43 reads** that we able to make alignment with the query with **130 bases match or more** were selected as our **contig** building blocks and **query carriers** as well
## Installation
make sure you have python 3.6 and 
install the folling packages before running
```python
pip install pandas
pip install seaborn
pip install -U matplotlib
pip install numpy

## Running scripts

## Please make sure to download the repo 
## so that the data files are in the right place
## then run:

Python EDA_sample_prep.Py
Python query copy.py
## Screenshots



