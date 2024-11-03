import argparse
from GeneExpressionData import GeneExpressionData
from StatisticalAnalysis import StatisticalAnalysis
from AnalysisReport import AnalysisReport

def main(file_path, destination, gene_name, threshold):
    """Perform statistical analysis on gene expression data and display results.

    Args:
        file_path (str): Path to the gene expression data file.
        destination (str): Output destination, either 'screen' or a file path.
        gene_name (str): Name of the gene to analyze.
        threshold (float): Threshold for gene expression filtering.
    """
    try:
        gene_data = GeneExpressionData(file_path)
        gene_data.read_file()
        
        analysis = StatisticalAnalysis(gene_data)
        report = AnalysisReport(destination)

        # Display analysis report
        report.display(analysis, gene_name, threshold)

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyze gene expression data and perform statistical analysis."
    )

    # Define positional arguments
    parser.add_argument("file_path", type=str, help="Path to the gene expression data file.")
    parser.add_argument("destination", type=str, help="Output destination ('screen' or a file path).")
    parser.add_argument("gene_name", type=str, help="Gene name to analyze.")
    parser.add_argument("threshold", type=float, help="Threshold for gene expression filtering.")

    # Parse arguments
    args = parser.parse_args()

    # Call main function with parsed arguments
    main(args.file_path, args.destination, args.gene_name, args.threshold)
