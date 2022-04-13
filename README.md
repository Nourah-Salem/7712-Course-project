
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



