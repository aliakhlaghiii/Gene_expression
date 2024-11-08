import sys
import argparse

def get_gene_names():
    """Collect multiple gene names from the user until they enter a special character."""
    print("Enter gene names one by one. Type '#' to finish:")
    gene_names = []
    for line in sys.stdin:   
        gene = line.strip()
        if gene == "#":
            break
        gene_names.append(gene)
    return gene_names

def main(file_path, destination, gene_names, threshold):
    """Perform statistical analysis on multiple genes."""
    try:
        from GeneExpressionData import GeneExpressionData
        from StatisticalAnalysis import StatisticalAnalysis
        from AnalysisReport import AnalysisReport
        
        gene_data = GeneExpressionData(file_path)
        gene_data.read_file()

        analysis = StatisticalAnalysis(gene_data)
        report = AnalysisReport(destination)

        for gene in gene_names:
            print(f"\nAnalysis for gene: {gene}")
            report.display(analysis, gene, threshold)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze gene expression data.")
    parser.add_argument("file_path", type=str, help="Path to the gene expression data file.")
    parser.add_argument("destination", type=str, help="Output destination ('screen' or a file path).")
    parser.add_argument("threshold", type=float, help="Threshold for gene expression filtering.")
    
    args = parser.parse_args()

    # Collect multiple gene names from the user
    gene_names = get_gene_names()

    # Call main with all arguments
    main(args.file_path, args.destination, gene_names, args.threshold)
