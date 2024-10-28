'''from GeneExpressionData file, import GeneExpressionData class, since the class name  is as same as the file name'''
from GeneExpressionData import GeneExpressionData
from StatisticalAnalysis import StatisticalAnalysis
from AnalysisReport import AnalysisReport

if __name__ == "__main__":   # run directly
    try:   # I used try-except in order to if user enters a wrong path file, the system shows an standard error
        path_file = input("Enter the file path: ")
        destination = input("Enter output destination (type 'screen' for screen or provide file path): ")

        # Initialize classes and read data
        gene_data = GeneExpressionData(path_file)
        gene_data.read_file()
        analysis = StatisticalAnalysis(gene_data)
        report = AnalysisReport(destination)  # report is obj of AnalysisReport class that initialized by a destination

        # Display analysis report
        report.display(analysis)

    except FileNotFoundError as e:
        print(e)
