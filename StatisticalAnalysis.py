'''in this assignment, we need just 3 modules among the whole modules of standard statistics library. so,
I imported just mean, standard deviation and median to save the memory'''
from statistics import mean, median, stdev

'''I have made a class in order to do some statistical operations. Also, I 
made an object(gene_data) of GeneExpressionData class as a parameter of statisticalAnalysis class'''
class StatisticalAnalysis:
    def __init__(self, gene_data):   # initializing
        self.gene_data = gene_data
        self.above_threshold_values = []  # a list that can keep the values of genes that are above threshold

    '''a function to calculate the mean of gene values(expressions)
    all of them do the same works. if the gene exists, do a task, otherwise return None'''
    def calculate_mean(self, gene):
        return mean(self.gene_data.gene_exp[gene]) if gene in self.gene_data.gene_exp else None

    '''a function to calculate the standard deviation of gene values(expressions)'''
    def calculate_sd(self, gene):
        return stdev(self.gene_data.gene_exp[gene]) if gene in self.gene_data.gene_exp else None

    '''a function to calculate the median of gene values(expressions)'''
    def calculate_median(self, gene):
        return median(self.gene_data.gene_exp[gene]) if gene in self.gene_data.gene_exp else None

    '''a function to calculate the differential of gene values(normal - hcc)'''
    def calculate_differential(self, gene):
        if gene in self.gene_data.normal_dict and gene in self.gene_data.hcc_dict:   # if gene exists
            normal_mean = mean(self.gene_data.normal_dict[gene])
            hcc_mean = mean(self.gene_data.hcc_dict[gene])
            return normal_mean - hcc_mean
        return None
    '''according to the threshold value that user enters, compares the gene expressions from gene_exp 
    dictionary. if the value is greater than threshold, return its value and add it to the list'''
    def above_threshold(self, gene, threshold):
        self.above_threshold_values = [value for value in self.gene_data.gene_exp[gene] if value > threshold]
        return self.above_threshold_values
