# Gene Expression Data Analysis

The goal of this code is to analyze some data from a file. This analysis causes us to find out how genes are
turned on/off in liver affected by cancer compared to healthy liver. So, the user can enter a gene name and,
by this code, can see the mean, median, and standard deviation of values among 357 samples. Also, it is possible to
calculate the differential (The numerical difference between the values of a gene when it is in a normal state and
when it is affected by cancer.)
## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Classes and Methods](#classes-and-methods)
- [Contact](#contact)
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aliakhlaghiii/final-assignment.git
## Usage
python3 main.py
## Project Structure

- GeneExpressionData.py:
In this class I try to manipulate, store and read the data(file).

- StatisticalAnalysis.py:
Make a class in order to do some statistical operations. I made an object(gene_data) of GeneExpressionData class as
a parameter of statisticalAnalysis class.
- AnalysisReport.py:
Displays and outputs analysis results in suitable format.
- main.py:
Main script to run the program
- README.md:
Project documentation and help
## Classes and Methods
### GeneExpressionData 
#### purpose:
Reads, manipulates, and stores gene expression data from a CSV file(Liver_GSE14520_U133A)
#### Attributes:
1. file_path: As the problem said, I put file_path as a parameter to initialize
2. samples: A list to keep the first column(samples)
3. types: A list to keep the second column(type)
4. gene_exp: A dictionary to keep values of each gene regardless of type(normal or HCC)
5. normal_dict: A dictionary to divide gene expressions corresponding to 'normal' type
6. hcc_dict: A dictionary to divide gene expressions corresponding to 'HCC' type
#### Methods:
1. read_file: Read expression data file and stores the data

### StatisticalAnalysis 
#### purpose:
A class in order to do some statistical operations. I made an object(gene_data) of GeneExpressionData class as
a parameter of statisticalAnalysis class. Also, you can find gene values that are above threshold that user wants.
#### Attributes:
gene_data: An object of GeneExpressionData class.
#### Methods:
1. calculate_mean(gene): Calculate the mean expression of a specific gene.
2. calculate_sd(gene): Calculate the standard deviation of expression values for a specific gene.
3. calculate_median(gene): Calculate the median expression value for a specific gene.
4. calculate_differential(gene): Calculate the differential expression of a specific gene (normal mean - HCC mean).
5. above_threshold(gene, threshold): filter the genes that their values are above the threshold.
### AnalysisReport
#### purpose:
Manages the display and output of analysis results in a suitable format.

#### Attributes:
destination: Output destination for results (screen or file path).
#### Methods:
display(analysis): Prompts user input, performs analysis, and displays or saves results.

## Contact
- Maintainer: Ali Akhlaghi
- Email: a.akhlaghi@st.hanze.nl
