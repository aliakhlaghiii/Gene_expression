"""
main.py: This script runs statistical analyses on gene expression data.
It reads input from a file, performs various statistical analyses, 
and outputs the results either to the screen or a file.
"""
import argparse
from GeneExpressionData import GeneExpressionData
from StatisticalAnalysis import StatisticalAnalysis
from AnalysisReport import AnalysisReport


def main(file_path, destination, gene_list, threshold):
    """
    Main function to perform statistical analysis on gene expression data.

    Args:
        file_path (str): Path to the gene expression data file.
        destination (str): Output destination ('screen' or a file path').
        gene_list (list of str): List of gene names to analyze.
        threshold (float): Threshold for gene expression filtering.
    """
    try:
        gene_data = GeneExpressionData(file_path)
        gene_data.read_file()
        print(gene_data)
        analysis = StatisticalAnalysis(gene_data)
        report = AnalysisReport(destination)

        for gene in gene_list:
            report.display(analysis, gene, threshold)

    except FileNotFoundError as file_err:
        print(f"Error: File not found. {file_err}")
        return 1
    except ValueError as value_err:
        print(f"Error: Invalid value. {value_err}")
        return 1
    except Exception as general_err:
        print(f"An unexpected error occurred: {general_err}")
        return 2
    return 0


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        description="Analyze gene expression data and perform statistical analysis."
    )

    parser.add_argument("file_path", type=str, help="Path to the gene expression data file.")
    parser.add_argument("destination", type=str, help="Output destination ('screen' or a file path).")
    parser.add_argument("threshold", type=float, help="Threshold for gene expression filtering.")

    # Accept multiple gene names
    parser.add_argument(
        "gene_names",
        type=str,
        nargs='+',
        help="Gene names to analyze (separate multiple names with a space)."
    )

    args = parser.parse_args()

    main(args.file_path, args.destination, args.gene_names, args.threshold)
