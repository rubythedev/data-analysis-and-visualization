'''analysis.py
Run statistical analyses and plot Numpy ndarray data
Ruby Nunez
'''

import numpy as np
import matplotlib.pyplot as plt
from data import *


class Analysis:
    def __init__(self, data):
        ''' Initialize data object

        Parameters:
        -----------
        data: Data object. Contains all data samples and variables in a dataset.
        '''

        self.data = data

        # Make plot font sizes legible
        plt.rcParams.update({'font.size': 18})


    def set_data(self, data):
        '''Method that re-assigns the instance variable `data` with the parameter.
        Convenience method to change the data used in an analysis without having to create a new
        Analysis object.

        Parameters:
        -----------
        data: Data object. Contains all data samples and variables in a dataset.
        '''
        
        self.data = data


    def min(self, headers, rows=[]):
        '''Computes the minimum of each variable in `headers` in the data object.
        (i.e. the minimum value in each of the selected columns)

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of min over, or over all indices
            if rows=[]

        Returns
        -----------
        mins: ndarray. shape=(len(headers),)
            Minimum values for each of the selected header variables
        '''
        
        min_data = self.data.select_data(headers, rows)
        mins = np.min(min_data, axis = 0 )
        
        return mins


    def max(self, headers, rows=[]):
        '''Computes the maximum of each variable in `headers` in the data object.

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of max over, or over all indices
            if rows=[]

        Returns
        -----------
        maxes: ndarray. shape=(len(headers),)
            Maximum values for each of the selected header variables
        '''
        
        max_data = self.data.select_data(headers, rows)
        maxes = np.max(max_data, axis = 0 )
        
        return maxes


    def range(self, headers, rows=[]):
        '''Computes the range [min, max] for each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of min/max over, or over all indices
            if rows=[]

        Returns
        -----------
        mins: ndarray. shape=(len(headers),)
            Minimum values for each of the selected header variables
        maxes: ndarray. shape=(len(headers),)
            Maximum values for each of the selected header variables
        '''
        
        mins = self.min(headers, rows)
        maxes = self.max(headers, rows)
        
        return mins, maxes


    def mean(self, headers, rows=[]):
        '''Computes the mean for each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`).

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of mean over, or over all indices
            if rows=[]

        Returns
        -----------
        means: ndarray. shape=(len(headers),)
            Mean values for each of the selected header variables
        '''
        
        mean_data = self.data.select_data(headers, rows)
        num_rows = len(mean_data)
        sum_data = np.sum(mean_data, axis = 0 )
        means = np.divide(sum_data, num_rows)
        
        return means


    def var(self, headers, rows=[]):
        '''Computes the variance for each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of variance over, or over all indices
            if rows=[]

        Returns
        -----------
        vars: ndarray. shape=(len(headers),)
            Variance values for each of the selected header variables
        '''
        
        vars_data = self.data.select_data(headers, rows)
        num_rows = len(vars_data)
        subtract_mean_squared = (vars_data - self.mean(headers, rows)) ** 2
        sum_data = np.sum(subtract_mean_squared, axis = 0 )
        vars = np.divide(sum_data, num_rows - 1)
        
        return vars


    def std(self, headers, rows=[]):
        '''Computes the standard deviation for each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of standard deviation over,
            or over all indices if rows=[]

        Returns
        -----------
        vars: ndarray. shape=(len(headers),)
            Standard deviation values for each of the selected header variables
        '''
        vars = (self.var(headers, rows)) ** .5
        
        return vars


    def show(self):
        '''Simple wrapper function for matplotlib's show function.
        '''
        
        plt.show()


    def scatter(self, ind_var, dep_var, title):
        '''Creates a simple scatter plot with "x" variable in the dataset `ind_var` and
        "y" variable in the dataset `dep_var`. Both `ind_var` and `dep_var` should be strings
        in `self.headers`.

        Parameters:
        -----------
        ind_var: str.
            Name of variable that is plotted along the x axis
        dep_var: str.
            Name of variable that is plotted along the y axis
        title: str.
            Title of the scatter plot

        Returns:
        -----------
        x. ndarray. shape=(num_data_samps,)
            The x values that appear in the scatter plot
        y. ndarray. shape=(num_data_samps,)
            The y values that appear in the scatter plot
        '''
        
        x = self.data.select_data(ind_var)
        y = self.data.select_data(dep_var)
        
        plt.figure(figsize=(12,8))
        plt.plot(x, y, '*r')
        plt.title(title)
        plt.xlabel(ind_var)
        plt.ylabel(dep_var)
        
        return x, y


    def pair_plot(self, data_vars, fig_sz=(12, 12), title=''):
        '''Create a pair plot: grid of scatter plots showing all combinations of variables in
        `data_vars` in the x and y axes.

        Parameters:
        -----------
        data_vars: Python list of str.
            Variables to place on either the x or y axis of the scatter plots
        fig_sz: tuple of 2 ints.
            The width and height of the figure of subplots. Pass as a paramter to plt.subplots.
        title. str. Title for entire figure (not the individual subplots)

        Returns:
        -----------
        fig. The matplotlib figure.
            1st item returned by plt.subplots
        axes. ndarray of AxesSubplot objects. shape=(len(data_vars), len(data_vars))
            2nd item returned by plt.subplots
        '''
        
        title_font = {'family': 'serif', 'color': 'blue', 'fontsize': 20}
        axis_font = {'family': 'serif', 'color': 'darkred', 'fontsize': 10}

        # Initialize figure
        fig = plt.figure(figsize=fig_sz)
        fig.suptitle(title, fontdict=title_font, y=0.95)

        # Create a grid of subplots and plot each combination
        num_vars = len(data_vars)
        axes = []

        for i, x_var in enumerate(data_vars):
            x = self.data.select_data(x_var)
            row_axes = []
            for j, y_var in enumerate(data_vars):
                y = self.data.select_data(y_var)
                
                # Create subplot at the i-th row and j-th column
                ax = fig.add_subplot(num_vars, num_vars, i * num_vars + j + 1)
                ax.scatter(x, y, color='red', s=2)  # Plot within the axes grid
                ax.tick_params(axis='both', labelsize=8)
                
                # Set axis labels only on edges to avoid clutter
                if j == 0:
                    ax.set_ylabel(x_var, fontdict=axis_font)
                if i == num_vars - 1:
                    ax.set_xlabel(y_var, fontdict=axis_font)

                row_axes.append(ax)

            axes.append(row_axes)

        # Convert axes to an array to match expected output type
        axes = np.array(axes)
        plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust layout to fit title
        return fig, axes