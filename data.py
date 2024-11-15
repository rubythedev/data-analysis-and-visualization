'''data.py
Reads CSV files, stores data, access/filter data by variable name
Ruby Nunez
'''

import csv
import numpy as np


class Data:
    def __init__(self, filepath=None, headers=None, data=None, header2col=None):
        '''Data object constructor

        Parameters:
        -----------
        filepath: str or None. Path to data .csv file
        headers: Python list of strings or None. List of strings that explain the name of each
            column of data.
        data: ndarray or None. shape=(N, M).
            N is the number of data samples (rows) in the dataset and M is the number of variables
            (cols) in the dataset.
            2D numpy array of the dataset’s values, all formatted as floats.
        header2col: Python dictionary or None.
                Maps header (var str name) to column index (int).
                Example: "sepal_length" -> 0
        '''
        # declaring and initializing variables
        self.filepath = filepath
        self.headers = headers
        self.data = data
        self.header2col = header2col

        # If `filepath` isn't None, call the `read` method
        if filepath != None:
            self.read(self.filepath)


    def read(self, filepath):
        '''Read in the .csv file `filepath` in 2D tabular format. Convert to numpy ndarray called
        `self.data` at the end.

        Format of `self.data`:
            Rows should correspond to i-th data sample.
            Cols should correspond to j-th variable / feature.

        Parameters:
        -----------
        filepath: str or None. Path to data .csv file

        Returns:
        -----------
        None. (No return value).
        '''
        
        # Read in the .csv file `filepath` to set `self.data`.
        # Parse the file to only store numeric columns of data in a 2D tabular format

        header2col_dictionary = {}

        data_type_list = ['numeric', 'enum', 'string', 'date']

        data_list = []
        header_list = []
        numeric_header_list = []
        index_row_2_list = []

        with open(filepath) as csv_file:

            csv_reader = csv.reader(csv_file, skipinitialspace=True)

            row_count = 0

            for row in csv_reader:
                if row_count == 0:
                    for col in row:
                        col = col.strip(' ')
                        col = col.strip('\n')
                        header_list.append(col)

                if row_count == 1:
                    if row[0] not in data_type_list:
                        print("Error: there are no data types in second row")
                    else:
                        for a in range(len(row)):
                            if row[a] == 'numeric':
                                index_row_2_list.append(a)

                if row_count > 1:
                    data_row = []
                    for i in index_row_2_list:                    
                        stripped_row = row[i].strip(' ')
                        stripped_row = row[i].strip('\n')
                        data_row.append(float(stripped_row))
                    data_list.append(data_row)

                row_count +=1
        
        # creating headers of numeric data
        for i in index_row_2_list:
            numeric_header_list.append(header_list[i])
        
        # creating dictionary for headers of numeric data
        for i in numeric_header_list:
            header2col_dictionary[i] = numeric_header_list.index(i)
        
        self.headers = numeric_header_list
        self.data = data_list
        self.data = np.array(self.data)
        self.header2col = header2col_dictionary
        self.filepath = filepath


    def __str__(self):
        '''toString method

        Returns:
        -----------
        str. A nicely formatted string representation of the data in this Data object.
            Only shows the 1st 5 rows of data
        '''

        divider = '-------------------------------\n'
        filepath_and_dimensions_string = '' + self.filepath + ' (' + str(self.get_num_samples()) + 'x' + str(self.get_num_dims()) + ')\n'
        header_label_string = 'Headers:\n  '
        headers_string = '    '.join(self.headers) + '\n'
        showing_rows_string = 'Showing first 5/150 rows.\n'
        data_string = ''
        if self.get_num_samples() < 5:
            for i in range(self.get_num_samples()):
                for j in range(self.get_num_dims()):
                    data_string += str(self.data[i][j]) + '    '
                data_string += '\n'

        else:
            for i in range(5):
                for j in range(self.get_num_dims()):
                    data_string += str(self.data[i][j]) + '    '
                data_string += '\n'
            

        string = divider + filepath_and_dimensions_string + header_label_string + headers_string + divider + showing_rows_string + data_string

        return string


    def get_headers(self):
        '''Get method for headers

        Returns:
        -----------
        Python list of str.
        '''

        return self.headers


    def get_mappings(self):
        '''Get method for mapping between variable name and column index

        Returns:
        -----------
        Python dictionary. str -> int
        '''

        return self.header2col


    def get_num_dims(self):
        '''Get method for number of dimensions in each data sample

        Returns:
        -----------
        int. Number of dimensions in each data sample. Same thing as number of variables.
        '''

        return len(self.headers)


    def get_num_samples(self):
        '''Get method for number of data points (samples) in the dataset

        Returns:
        -----------
        int. Number of data samples in dataset.
        '''

        return len(self.data)


    def get_sample(self, rowInd):
        '''Gets the data sample at index `rowInd` (the `rowInd`-th sample)

        Returns:
        -----------
        ndarray. shape=(num_vars,) The data sample at index `rowInd`
        '''

        return self.data[rowInd]


    def get_header_indices(self, headers):
        '''Gets the variable (column) indices of the str variable names in `headers`.

        Parameters:
        -----------
        headers: Python list of str. Header names to take from self.data

        Returns:
        -----------
        Python list of nonnegative ints. shape=len(headers). The indices of the headers in `headers`
            list.
        '''

        header_indices_list = []
        for i in headers:
            if i in self.header2col:
                header_indices_list.append(self.header2col[i])
        return header_indices_list

    
    def get_all_data(self):
        '''Gets a copy of the entire dataset

        Returns:
        -----------
        ndarray. shape=(num_data_samps, num_vars). A copy of the entire dataset.
        '''
        
        data_copy = np.copy(self.data)

        return data_copy
        

    def head(self):
        '''Return the 1st five data samples (all variables)

        Returns:
        -----------
        ndarray. shape=(5, num_vars). 1st five data samples.
        '''
        
        if 0 < self.get_num_samples() < 2:
            row1 = self.get_sample(0)

            head_list = [row1]
        
        if 1 < self.get_num_samples() < 3:
            row1 = self.get_sample(0)
            row2 = self.get_sample(1)

            head_list = [row1,row2]
        
        if 2 < self.get_num_samples() < 4:
            row1 = self.get_sample(0)
            row2 = self.get_sample(1)
            row3 = self.get_sample(2)

            head_list = [row1,row2,row3]

        if 3 < self.get_num_samples() < 5:
            row1 = self.get_sample(0)
            row2 = self.get_sample(1)
            row3 = self.get_sample(2)
            row4 = self.get_sample(3)

            head_list = [row1,row2,row3,row4]

        if self.get_num_samples() >= 5:
            row1 = self.get_sample(0)
            row2 = self.get_sample(1)
            row3 = self.get_sample(2)
            row4 = self.get_sample(3)
            row5 = self.get_sample(4)

            head_list = [row1,row2,row3,row4,row5]

        head_array = np.array(head_list)

        return head_array


    def tail(self):
        '''Return the last five data samples (all variables)

        Returns:
        -----------
        ndarray. shape=(5, num_vars). Last five data samples.
        '''
        
        if 0 < self.get_num_samples() < 2:
            last_row1 = self.get_sample(-1)

            tail_list = [last_row1]
        
        if 1 < self.get_num_samples() < 3:
            last_row1 = self.get_sample(-2)
            last_row2 = self.get_sample(-1)

            tail_list = [last_row1,last_row2]
        
        if 2 < self.get_num_samples() < 4:
            last_row1 = self.get_sample(-3)
            last_row2 = self.get_sample(-2)
            last_row3 = self.get_sample(-1)

            tail_list = [last_row1,last_row2,last_row3]

        if 3 < self.get_num_samples() < 5:
            last_row1 = self.get_sample(-4)
            last_row2 = self.get_sample(-3)
            last_row3 = self.get_sample(-2)
            last_row4 = self.get_sample(-1)

            tail_list = [last_row1,last_row2,last_row3,last_row4]

        if self.get_num_samples() >= 5:
            last_row1 = self.get_sample(-5)
            last_row2 = self.get_sample(-4)
            last_row3 = self.get_sample(-3)
            last_row4 = self.get_sample(-2)
            last_row5 = self.get_sample(-1)

            tail_list = [last_row1,last_row2,last_row3,last_row4,last_row5]

        tail_array = np.array(tail_list)

        return tail_array


    def limit_samples(self, start_row, end_row):
        '''Update the data so that this `Data` object only stores samples in the contiguous range:
            `start_row` (inclusive), end_row (exclusive)
        Samples outside the specified range are no longer stored.

        '''
        
        limited_data = self.data[start_row:end_row,:]
        self.data = limited_data
        

    def select_data(self, headers, rows=[]):
        '''Return data samples corresponding to the variable names in `headers`.
        If `rows` is empty, return all samples, otherwise return samples at the indices specified
        by the `rows` list.

        Parameters:
        -----------
            headers: Python list of str. Header names to take from self.data
            rows: Python list of int. Indices of subset of data samples to select.
                Empty list [] means take all rows

        Returns:
        -----------
        ndarray. shape=(num_data_samps, len(headers)) if rows=[]
                 shape=(len(rows), len(headers)) otherwise
            Subset of data from the variables `headers` that have row indices `rows`.

        '''
        
        if isinstance(headers, str):
           headers = [headers]
        headinds = self.get_header_indices(headers)
        npix = np.ix_(rows, headinds)
        if len(rows) == 0:
            return self.data[:,headinds]
        return self.data[npix]
