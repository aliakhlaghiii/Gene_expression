'''in this assignment, we need just 3 modules among the whole modules of the standard statistics library. so,
I imported just the mean, standard deviation and median to save the memory'''
from statistics import mean, median, stdev   # call statistics library

'''I have made a class to do some statistical operations. Also, I 
made an object(gene_data) of GeneExpressionData class as a parameter of statisticalAnalysis class'''
class StatisticalAnalysis:
    def __init__(self, gene_data):   # initializing with gene_data(as an instance).
        self.gene_data = gene_data

    '''a function to calculate the mean of gene values(expressions)
    all of them do the same work. if the gene exists, do a task, otherwise return None'''
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

    def above_threshold(self, gene, threshold):
        '''with enumerate method I combine the samples with gene expressions if the gene expression is greater
        than the threshold enter by user'''
        self.above_threshold_values = [
            (self.gene_data.samples[i], value)
            for i, value in enumerate(self.gene_data.gene_exp[gene])
            if value > threshold
        ]
        return self.above_threshold_values
