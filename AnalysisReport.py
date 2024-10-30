'''Manage the display and output of analysis results in a suitable format'''
class AnalysisReport:
    def __init__(self, destination):   # initialize by destination(screen or file)
        self.destination = destination
    '''a function to show the results of statistical works'''
    def display(self, analysis, gene, threshold):   # initialize
        mean_val = analysis.calculate_mean(gene)   # keep the value of mean
        median_val = analysis.calculate_median(gene)   # keep the value of median
        sd_val = analysis.calculate_sd(gene)   # keep the value of standard deviation
        differential_val = analysis.calculate_differential(gene)   # keep the value of differential

        '''results is a list of tuples keep the values corresponding with type '''
        results = [
            ("Mean", mean_val),
            ("Median", median_val),
            ("Standard Deviation", sd_val),
            ("Differential Expression (Normal - HCC)", differential_val),
        ]

        '''Scan the results list. If type and result exist, it shows the result in 3 digits float format, otherwise
        it shows Not found'''
        for analysis_type, result in results:
            result_str = f"{result:.3f}" if result is not None else "Not found"
            if self.destination == 'screen':   # check the destination
                print(f"{analysis_type} for {gene}: {result_str}")   # use f-string to show the result
            else:   # if the destination is a file, this snippet code can write a file into the path the user enters
                with open(self.destination, 'w') as file:
                    file.write(f"{analysis_type} for {gene}: {result_str}\n")

        '''keep the value of above threshold function into a variable'''
        threshold_results = analysis.above_threshold(gene, threshold)
        '''while sample and its value is in threshold_result, it shows the name of sample and its value 
        in 3 digits float format'''
        if threshold_results:
            above_threshold_str = "\n".join(
                f"{sample}: {value:.3f}" for sample, value in threshold_results
            )
            if self.destination == 'screen':   # check the destination
                print(f"Values above threshold {threshold} for {gene}:\n{above_threshold_str}")
            else:
                with open(self.destination, 'w') as file:
                    file.write(f"Values above threshold {threshold} for {gene}:\n{above_threshold_str}\n")
        else:
            if self.destination == 'screen':
                print(f"No values above threshold {threshold} for {gene}.")
            else:
                with open(self.destination, 'a') as file:
                    file.write(f"No values above threshold {threshold} for {gene}.\n")
