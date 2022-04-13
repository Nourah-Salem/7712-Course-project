
# Constructing the Longest Conting (Containing a Specific Query) from DNA Reads 


![Screenshot2](https://user-images.githubusercontent.com/65971542/163245219-c43f2fd1-6479-470a-8801-9b470b5ef729.png)

[https://ec.europa.eu/research-and-innovation/en/horizon-magazine/new-braking-systems-and-satellite-navigation-help-more-trains-run-europes-tracks]

DNA sequencing into small fragments is an important step for studing the genetic material. This allows to find the associations between modifications within the gene and potential phenotypic changes. Genome assembly refers to the process of putting small nucleotide sequence (reads) into the correct order. Assembly is required, as the sequence read lengths are much shorter than most genomes or even most genes. therefore, analyzing them requires assembly. And the process of assembly requires reconstructing the larger size of sequence is called contig. 

In this project, we have a list of DNA reads and a spcific query, nad we aim at building the longest contig spanning the given query, this is achieved via the overlapping the reads. such overlaps are specifically between the reads and the query. 

![Screenshot3](https://user-images.githubusercontent.com/65971542/163247740-ab9fdc49-9b2f-4fe4-afb4-382091e84efb.png)

Herein, we allowed four all possible overlaps between the query and all reads we have. for that we made an initial trial of 10,000 reeds and looked at the range of characters (match length) that match to the query. from that, we had an initial assumption about the legit alignments versus those that can happen at random the following graph shows a sample of 10,000 reads aligned to the query.


The first part of the project is to apply simple preprocesdatasing on the 
then, recontruct the query from the reads list. 
once the query is constructed, we can extend it from both sides to make the longest contig.

The algorithm is still being built and by the end of the 7712 course, we will have it complete with the proper test units.

Curretly, we can: 
    
    1. Preprocess the inputs and apply EDA
    2. Creat small smaples for testing purposes (reads and query)
    3. Build the query from the reads list 
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



