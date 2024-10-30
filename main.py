import argparse   # import argparse to handle the command line arguments
from GeneExpressionData import GeneExpressionData
from StatisticalAnalysis import StatisticalAnalysis
from AnalysisReport import AnalysisReport

def main(file_path, destination, gene_name, threshold):  # main with 4 parameters
    try:
        gene_data = GeneExpressionData(file_path)   # gene_data is an object of GeneExpressionData class
        gene_data.read_file()   # call read_file function
        analysis = StatisticalAnalysis(gene_data)   # make an object of StatisticalAnalysis class named analysis.
        report = AnalysisReport(destination)   # make an object of AnalysisReport class named report.

        # Display analysis report
        report.display(analysis, gene_name, threshold)  # Pass gene_name and threshold

    except FileNotFoundError as e:   # if the file path does not exist, it shows a standard error
        print(e)

if __name__ == "__main__":   # run directly
# Initialize ArgumentParser object(parser), also the user can see this description when the user enter -h for help'''
    parser = argparse.ArgumentParser(description="Analyse gene expression data and perform some statistical analysis.")

    # Define positional arguments
    parser.add_argument("file_path", type=str, help="Path to the gene expression data file.")
    parser.add_argument("destination", type=str, help="Output destination (type 'screen' for screen output or provide file path).")
    parser.add_argument("gene_name", type=str, help="Gene name to analyze.")
    parser.add_argument("threshold", type=float, help="Threshold for gene expression filtering.")

    # Parse arguments respectively
    args = parser.parse_args()

    # Call main function with parsed arguments
    main(args.file_path, args.destination, args.gene_name, args.threshold)
