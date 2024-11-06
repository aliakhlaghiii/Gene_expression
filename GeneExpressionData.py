'''In this class, I try to manipulate, store and read the data'''
class GeneExpressionData:
    def __init__(self, file_path):   # initialize with file path
        self.file_path = file_path
        self.gene_exp = {}   # a dictionary to keep values of each gene regardless of type(normal or HCC)
        self.normal_dict = {}   # a dictionary to divide gene expressions corresponding to 'normal' type
        self.hcc_dict = {}   # a dictionary to divide gene expressions corresponding to 'HCC' type
        self.samples = []  # list to store sample names

    '''function to read the file and store data'''
    def read_file(self):
        with open(self.file_path, 'r', encoding='ascii') as file:   # open file in read mode with ascii encoder
            lines = file.readlines()   # read the whole lines
            headers = lines[0].strip().split(',')   # assume the first line split by ',' as the header
            '''keep the sample values split by ',' in self.samples list(the first element of each line)'''
            self.samples = [line.split(',')[0] for line in lines[1:]]   # lines[1:] refers to after header row.

            '''in the header, from the third cell to the end, I assumed to gene name(header). each column has
             expressions and values for each gene. so, I'm going to make an empty list(as values of the dictionary) to
              scan the rows one by one, and based on its index, I allocate them to each gene name. finally,
              I have columns with a header(gene name)'''
            self.gene_exp = {header: [] for header in headers[2:]}   # Creates an empty list for value of each header

            for line in lines[1:]:   # read the file line by line
                values = line.strip().split(',')
                sample_type = values[1]   # Assume the second column is gene type
                ''' complete the dictionary with headers(keys) and append the values to that empty list '''
                for key, value in zip(headers[2:], values[2:]):
                    self.gene_exp[key].append(float(value)) #append the floated values as value of gene_exp dictionary


                if sample_type == 'normal':   # check the type
                    for key, value in zip(headers[2:], values[2:]):
                        ''' if gene name doesn't exist, make an empty list to put the values in it '''
                        if key not in self.normal_dict:
                            self.normal_dict[key] = []   # if the gene name does not exist, make a new one
                        ''' if gene name exists, just append its values '''
                        self.normal_dict[key].append(float(value))   # in any case, append it
                elif sample_type == 'HCC':   # as same as Normal, I checked HCC conditions
                    for key, value in zip(headers[2:], values[2:]):
                        if key not in self.hcc_dict:
                            self.hcc_dict[key] = []   # make a new key
                        self.hcc_dict[key].append(float(value))    # in any case, append it
        ''' return the values'''
        return self.gene_exp, self.normal_dict, self.hcc_dict
