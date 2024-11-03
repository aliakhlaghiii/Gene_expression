from statistics import mean, median, stdev  # Importing specific functions

class StatisticalAnalysis:
    """Class to perform statistical analyses on gene expression data."""

    def __init__(self, gene_data):
        """Initialize with gene_data instance."""
        self.gene_data = gene_data

    def calculate_mean(self, gene):
        """Calculate the mean of gene expression values.
        
        Args:
            gene (str): Gene identifier.
        
        Returns:
            float or None: Mean of expression values if gene exists, else None.
        """
        return mean(self.gene_data.gene_exp[gene]) if gene in self.gene_data.gene_exp else None

    def calculate_sd(self, gene):
        """Calculate the standard deviation of gene expression values.

        Args:
            gene (str): Gene identifier.
        
        Returns:
            float or None: Standard deviation if gene exists, else None.
        """
        return stdev(self.gene_data.gene_exp[gene]) if gene in self.gene_data.gene_exp else None

    def calculate_median(self, gene):
        """Calculate the median of gene expression values.

        Args:
            gene (str): Gene identifier.
        
        Returns:
            float or None: Median if gene exists, else None.
        """
        return median(self.gene_data.gene_exp[gene]) if gene in self.gene_data.gene_exp else None

    def calculate_differential(self, gene):
        """Calculate differential expression between normal and HCC conditions.

        Args:
            gene (str): Gene identifier.
        
        Returns:
            float or None: Differential if gene exists in both dictionaries, else None.
        """
        if gene in self.gene_data.normal_dict and gene in self.gene_data.hcc_dict:
            normal_mean = mean(self.gene_data.normal_dict[gene])
            hcc_mean = mean(self.gene_data.hcc_dict[gene])
            return normal_mean - hcc_mean
        return None

    def above_threshold(self, gene, threshold):
        """Get samples where gene expression exceeds a specified threshold.

        Args:
            gene (str): Gene identifier.
            threshold (float): Threshold value to compare against.
        
        Returns:
            list of tuples: Sample names and values where expression > threshold.
        """
        return [
            (self.gene_data.samples[i], value)
            for i, value in enumerate(self.gene_data.gene_exp.get(gene, []))
            if value > threshold
        ]
