# Gene Expression Data Analysis

The goal of this code is to analyze some data from a file. This analysis causes us to find out how genes are
turned on/off in the liver affected by cancer compared to a healthy liver. Especially by calculating differential you can find that the gene is TSG(Tumor suppressor gene) or Ancogene. So, the user can enter a gene name, and the mean, median, and standard deviation of values among 357 samples can be seen using this code. Also, it is possible to calculate the differential (The numerical difference between the values of a gene when it is in a normal state and
when it is affected by cancer.
## Table of Contents
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Classes and Methods](#classes-and-methods)
- [Contact](#contact)
## Dependencies
- Python 3

Libraries:
* statistics (standard Python library)
* argparse (standard Python library)

Ensure that your Python environment is set up with the necessary modules before running the program.

## Installation

1. Clone the repository:
   ```bash
   https://github.com/aliakhlaghiii/final_assignment.git
## Usage
- python3 main.py file path, destination, gene name, threshold value

You should replace the whole arguments above with your data

- Example of command-line execution:
  python3 main.py /users/data/liver_cancer_gene_expression.csv screen 1007_s_at 5.4
## Project Structure

- GeneExpressionData.py:
In this class I try to manipulate, store and read the data(file).

- StatisticalAnalysis.py:
Make a class in order to do some statistical operations. I made an object(gene_data) of GeneExpressionData class as
a parameter of statisticalAnalysis class.
- AnalysisReport.py:
Displays and outputs analysis results in a suitable format.
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
1. read_file: Read the expression data file and store the data

### StatisticalAnalysis 
#### purpose:
A class in order to do some statistical operations. I made an object(gene_data) of GeneExpressionData class as
a parameter of statisticalAnalysis class. Also, you can find gene values that are above the threshold that the user wants.
#### Attributes:
gene_data: An object of GeneExpressionData class.
#### Methods:
1. calculate_mean(gene): Calculate the mean expression of a specific gene.
2. calculate_sd(gene): Calculate the standard deviation of expression values for a specific gene.
3. calculate_median(gene): Calculate the median expression value for a specific gene.
4. calculate_differential(gene): Calculate the differential expression of a specific gene (normal mean - HCC mean).
5. above_threshold(gene, threshold): filter the gene expressions above the threshold with its sample name.
### AnalysisReport
#### purpose:
Manages the display and output of analysis results in a suitable format.

#### Attributes:
destination: Output destination for results (screen or file path).
#### Methods:
display(analysis): Prompts user input, performs analysis, and displays or saves results.

## Contact
- Author: Ali Akhlaghi
- Email: a.akhlaghi@st.hanze.nl
