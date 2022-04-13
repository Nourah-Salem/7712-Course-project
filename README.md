
# Constructing the Longest Conting (Containing a Specific Query) from DNA Reads 


![Screenshot](https://user-images.githubusercontent.com/65971542/163244901-d894f431-e30f-483a-a580-a29a160a6194.png)
[https://ec.europa.eu/research-and-innovation/en/horizon-magazine/new-braking-systems-and-satellite-navigation-help-more-trains-run-europes-tracks]

![Screenshot2](https://user-images.githubusercontent.com/65971542/163245219-c43f2fd1-6479-470a-8801-9b470b5ef729.png)

In this project, we have a list of DNA reads and a spcific query, nad we aim at building the longest possible contig by overlapping the reads and at the same time the contig must contain the given query.

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
1. long string (contig) that carries the query inside
2. a list of the overlapping reads with their matching indecies
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



