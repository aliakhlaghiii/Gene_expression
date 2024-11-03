class AnalysisReport:
    """Manage the display and output of analysis results in a suitable format."""

    def __init__(self, destination):
        """Initialize the report with a destination (screen or file).

        Args:
            destination (str): Output destination, either 'screen' or a file path.
        """
        self.destination = destination

    def display(self, analysis, gene, threshold):
        """Display or save the results of statistical analysis for a specific gene.

        Args:
            analysis (StatisticalAnalysis): Analysis object for performing statistical calculations.
            gene (str): The gene identifier for analysis.
            threshold (float): Threshold value for filtering results.
        """
        mean_val = analysis.calculate_mean(gene)
        median_val = analysis.calculate_median(gene)
        sd_val = analysis.calculate_sd(gene)
        differential_val = analysis.calculate_differential(gene)

        # List of results as tuples with labels and values
        results = [
            ("Mean", mean_val),
            ("Median", median_val),
            ("Standard Deviation", sd_val),
            ("Differential Expression (Normal - HCC)", differential_val),
        ]

        # Display or save each result
        for analysis_type, result in results:
            result_str = f"{result:.3f}" if result is not None else "Not found"
            output_line = f"{analysis_type} for {gene}: {result_str}\n"
            self._output(output_line)

        # Threshold results
        threshold_results = analysis.above_threshold(gene, threshold)
        if threshold_results:
            above_threshold_str = "\n".join(
                f"{sample}: {value:.3f}" for sample, value in threshold_results
            )
            output_line = f"Values above threshold {threshold} for {gene}:\n{above_threshold_str}\n"
        else:
            output_line = f"No values above threshold {threshold} for {gene}.\n"
        
        self._output(output_line)

    def _output(self, message):
        """Output message to the specified destination.

        Args:
            message (str): The message to be output.
        """
        if self.destination == 'screen':
            print(message)
        else:
            with open(self.destination, 'a') as file:
                file.write(message)
