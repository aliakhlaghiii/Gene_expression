'''Manages the display and output of analysis results in a suitable format'''
class AnalysisReport:
    def __init__(self, destination):   # initialize by destination(screen or file)
        self.destination = destination

    def display(self, analysis):
        while True:   # I put it in while loop to if user enter an invalid gene name and type, it repeats.
            gene = input("Enter the gene name: ").strip()
            if gene in analysis.gene_data.gene_exp:
                print("Choose the type of analysis:")
                break
            else:
                print("Gene not found. Try again\n")

        while True:   # user choice
            print("1. Mean\n2. Median\n3. Standard Deviation\n4. Differential Expression\n5. Above threshold")
            user_input = input("Enter the number corresponding to your choice: ")

            if user_input == '1':
                result = analysis.calculate_mean(gene)   # call calculate_mean function
                analysis_type = "Mean"
            elif user_input == '2':
                result = analysis.calculate_median(gene)   # call calculate_median function
                analysis_type = "Median"
            elif user_input == '3':
                result = analysis.calculate_sd(gene)   # call standard deviation function
                analysis_type = "Standard Deviation"
            elif user_input == '4':
                result = analysis.calculate_differential(gene)   # call calculate_differential function
                analysis_type = "Differential Expression (Normal - HCC)"
            elif user_input == '5':
                threshold = float(input("Enter a threshold value: "))   # assume user input as threshold value
                result = analysis.above_threshold(gene, threshold)   # call above_threshold function
                analysis_type = f"Values above threshold {threshold}"
            else:
                print("Invalid choice. Try again.")
                continue   # to the first of the loop

            if result is not None:
                if user_input == '5':
                    if not result:  # Check if the result list is empty
                        result_str = "There is no gene above threshold."
                    else:   # result exists
                        '''while value is in result, the results separated by ',' will be appeared on the screen'''
                        result_str = ', '.join(f"{val:.3f}" for val in result)
                else:
                    result_str = f"{result:.3f}"  # for other analysis types, it shows the result

                if self.destination == 'screen':
                    print(f"{analysis_type} for {gene}: {result_str}")
                else:
                    with open(self.destination, 'w') as file:
                        file.write(f"{analysis_type} for {gene}: {result_str}\n")
                        print(f"The result was added to: {self.destination}")
                break
            else:
                print(f"{analysis_type} could not be calculated. Gene data might be missing.")
