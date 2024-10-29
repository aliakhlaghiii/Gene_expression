import argparse   # import argparse to handle the command line arguments
'''since the class name is as same as the file name, I used from-import'''
from GeneExpressionData import GeneExpressionData
from StatisticalAnalysis import StatisticalAnalysis
from AnalysisReport import AnalysisReport

def main(file_path, destination):   # main of the program
    try:   # if the file path and destination are correct and exist, try.
        # Initialize classes and read data
        gene_data = GeneExpressionData(file_path)   # gene_data is an object of GeneExpressionData class
        gene_data.read_file()   # call read_file function 
        analysis = StatisticalAnalysis(gene_data)   # make an object of StatisticalAnalysis class named analysis.
        report = AnalysisReport(destination)   # make an object of AnalysisReport class named report.

        # Display analysis report
        report.display(analysis)   # call display method in report object

    except FileNotFoundError as e:   # if the file path does not exist, it shows a standard error
        print(f"Error: {e}")

if __name__ == "__main__":   # run directly
    # Initialize ArgumentParser object(parser)
    parser = argparse.ArgumentParser(description="Analyse gene expression data and perform some statistical analysis.")
    
    '''with add_argument method, I determine the positional arguments. In this case, both of them are str'''
    parser.add_argument("file_path", type=str, help="Path to the gene expression data file.")
    parser.add_argument("destination", type=str, help="Output destination (type 'screen' for screen output or provide file path).")

    args = parser.parse_args()   # according to the arguments above, they are stored in args

    # main function with parsed arguments
    main(args.file_path, args.destination)
