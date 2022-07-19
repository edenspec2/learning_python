# level 0 - Finished documentation

class DataValidtor():
    assertion_referal = {}

    def assert_df(self, input_var, error_message = 'Input must be in a form of dataframe'):
        """
        A function that checks whether the input it has recieved is a pandas dataframe or not
    
        Parameters
        ----------

        input_var : any
            A varible whos type and value are unknown

        error_message : str, default 'Input must be in a form of dataframe'
 
        Returns
        -------

        Assertion
            No output if the input is valid, and assertion error message otherwise
        
        Examples
        --------

        >>> data_validator = DataValidtor()
        >>> test_var = {1: [0, 1], 2: [2, 3]}
        >>> data_validator.assert_df(test_var)
        AssertionError: Input must be in a form of dataframe
        >>> import pandas as pd
        >>> test_var = pd.DataFrame({1: [0, 1], 2: [2, 3]})
        >>> data_validator.asser_df(test_var)
        None
        """
        import pandas as pd
        assert type(input_var) == pd.core.frame.DataFrame, error_message

    def assert_estimator(self, input_var, error_message = 'Input must be a sklearn friendly estimator'):
        """
        A function that checks whether the input it has recieved is an estimator (sklearn compatible) or not 
    
        Parameters
        ----------

        input_var : any
            A varible whos type and value are unknown

        error_message : str, default 'Input must be a sklearn friendly estimator'
 
        Returns
        -------

        Assertion
            No output if the input is valid, and assertion error message otherwise
        
        Examples
        --------

        >>> data_validator = DataValidtor()
        >>> test_var = {1: [0, 1], 2: [2, 3]}
        >>> data_validator.assert_df(test_var)
        AssertionError: Input must be a sklearn friendly estimator
        >>> from sklearn.ensemble import RandomForestClassifier
        >>> test_var = RandomForestClassifier()
        >>> data_validator.asser_df(test_var)
        None
        """
        from sklearn.utils.estimator_checks import check_estimator
        try:
            check_estimator(input_var)
        except:
            raise AssertionError(error_message)

    def assert_int_iterable(self, input_var, error_message = 'Input must contain only int numbers'):
        """
        A function that checks whether the input it has recieved is an iterable of int numbers or not 
    
        Parameters
        ----------

        input_var : any
            A varible whos type and value are unknown

        error_message : str, default 'Input must contain only int numbers'
 
        Returns
        -------

        Assertion
            No output if the input is a valid, and assertion error message otherwise
        
        Examples
        --------

        >>> data_validator = DataValidtor()
        >>> test_var = [0.0, 1, 1, 2, 3, 5]
        >>> data_validator.assert_df(test_var)
        AssertionError: Input must contain only int numbers
        >>> test_var = [0, 1, 1, 2, 3, 5]
        >>> data_validator.asser_df(test_var)
        None
        """
        for number in input_var:
            assert isinstance(number, int), error_message

    def assert_column_names_exists(self, df, names, error_message = ' is not a cloumn in the dataframe'):
        """
        A function that get a pandas dataframe and an iterable of names, and checks whether the names are part of the columns of dataframe or not 
    
        Parameters
        ----------

        df : DataFrame
            A dataframe that is will be checked for the column names

        names : Iterable
            An iterable that holds possible column names

        error_message : str, default 'Column name not in dataframe'
 
        Returns
        -------

        Assertion
            No output if the input is a valid, and assertion error message otherwise
        
        Examples
        --------

        >>> import pandas as pd
        >>> data_validator = DataValidtor()
        >>> test_df = pd.DataFrame({1: [0, 1], 2: [2, 3]})
        >>> data_validator.assert_column_names_exists(test_df, [3])
        AssertionError: 3 is not a cloumn in the dataframe
        >>> data_validator.assert_column_names_exists(test_df, [2])
        None
        """
        self.assert_df(df)
        actual_columns = df.columns
        for column_name in names:
            assert column_name in actual_columns, str(column_name)+error_message

    def assert_value_is_allowed (self, value, allowed_values, error_message='given value was not found'):
        """
        A function that get a value and set of allowed values, and checks whether the value is part of the allowed values or not 
    
        Parameters
        ----------

        value: str
            The value that needs to be checked

        allowed_values: Iterable
            An iterable of possible allowed values

        error_message: str, default 'given value was not found'
 
        Returns
        -------

        Assertion
            No output if the input is a valid, and assertion error message otherwise
        
        Examples
        --------

        >>> data_validator = DataValidtor()
        >>> allowed_values = ('A', 'B', 'C')
        >>> data_validator.assert_value_is_allowed('a', allowed_values)
        AssertionError: given value was not found
        >>> data_validator.assert_value_is_allowed('A', allowed_values)
        None
        """
        assert value in allowed_values, error_message

    def assert_str(self):
        pass

    def assert_iterable(self):
        pass

# level 1 - Finished documentation
class ColumnsInfoCollector(DataValidtor):
    column_codes = {'couples' : 'get_lower_triangular_pairs', 'all': 'get_all_columns'}

    def get_all_columns(self, df):
        """
        Given a pandas dataframe, returns a list of all column names. 
    
        Parameters
        ----------
        df : DataFrame
            A pamdas dataframe
 
        Returns
        -------
        List
            A list containing the dataframe column names.
        
        Examples
        --------
        >>> columns_info_collector = ColumnsInfoCollector()
        >>> import pandas as pd
        >>> df = pd.DataFrame({'col_A': [1, 2], 'col_B': [1, 2], 'col_C': [1, 2]})       
          col_A	  col_B	    col_C
        0	1	    1	    1
        1	2	    2	    2
        >>> columns_info_collector.get_all_columns(df)
            ['col_A', 'col_B', 'col_C']
        """
        self.assert_df(df)
        return list(df.columns)

    def get_lower_triangular_pairs(self, df, include_diagonal=False):
        """
        Given a pandas dataframe, returns a set of column names couples by going over the lower triangular part of the martix columns-columns. 
    
        Parameters
        ----------

        df : DataFrame
            A pamdas dataframe

        include_diagonal : bool, default False
            A parameter that determines whether the digonal in columns-columns matrix will be taken.
            If 'False' is choosen, the result won't include the diagonal. 
            If 'True' is choosen, the result will include the diagonal. 
 
        Returns
        -------
        
        Set
            A set containing column pairs names.
        
        Examples
        --------

        >>> import pandas as pd
        >>> columns_info_collector = ColumnsInfoCollector()
        >>> df = pd.DataFrame({'col_A': [1, 2], 'col_B': [1, 2], 'col_C': [1, 2]})
            col_A	col_B	col_C
        0	1	`   1	    1
        1	2	    2	    2
        >>> columns_info_collector.get_lower_triangular_pairs(df, include_diagonal=False)
            {('col_B', 'col_A'), ('col_C', 'col_A'), ('col_C', 'col_B')}
        >>> columns_info_collector.get_lower_triangular_pairs(df, include_diagonal=True) 
            {('col_A', 'col_A'), ('col_B', 'col_A'), ('col_B', 'col_B'), ('col_C', 'col_A'), ('col_C', 'col_B'), ('col_C', 'col_C')}
        """
        self.assert_df(df)
        pairs = set()
        cols = df.columns
        for i in range(0, df.shape[1]):
            for j in range(0, i+int(include_diagonal)):
                pairs.add((cols[i], cols[j]))
        return pairs

class DataPlotter(DataValidtor):
    import numpy as np
    mask_matrix_dict = {'upper_triangle': np.triu, 'lower_triangle': np.tril}
    possible_plots = ('scatter', 'line')

    def scatter_plot (self, X_label, y_label, df, ax):
        """
        Function that excutes a scatter plot on a given axis, provided a dataframe and specified X and y labels. 
    
        Parameters
        ----------

        X_label: str
            The name of column in the dataframe used for the scatter plot as X.

        y_label: str
            The name of column in the dataframe used for the scatter plot as y.
            
        df: DataFrame
            A pamdas dataframe containing the X_label and y_label columns with data.

        ax: axis
            The axis on which the scatter plot will be presented on.

 
        Returns
        -------
        None
            No return value, the plot will just be presented
        
        Examples
        --------
        >>> import pandas as pd
        >>> import matplotlib as plt
        >>> data_plotter = DataPlotter()
        >>> df = pd.DataFrame({'A': [-2, -1, 0, 1, 2], 'B': [4, 1, 0, 1, 4]})
        	A	B
        0	-2	4
        1	-1	1
        2	0	0
        3	1	1
        4	2	4
        >>> fig, ax = plt.subplots()
        >>> data_plotter.scatter_plot('A', 'B', df, ax)
        """
        ax.scatter(X_label, y_label, data=df)

    def line_plot (self, X_label, y_label, df, ax):
        """
        Function that excutes a line plot on a given axis, provided a dataframe and specified X and y labels. 
    
        Parameters
        ----------

        X_label: str
            The name of column in the dataframe used for the line plot as X.

        y_label: str
            The name of column in the dataframe used for the line plot as y.
            
        df: DataFrame
            A pamdas dataframe containing the X_label and y_label columns with data.

        ax: axis
            The axis on which the line plot will be presented on.

 
        Returns
        -------
        None
            No return value, the plot will just be presented
        
        Examples
        --------
        >>> import pandas as pd
        >>> import matplotlib as plt
        >>> data_plotter = DataPlotter()
        >>> df = pd.DataFrame({'A': [-2, -1, 0, 1, 2], 'B': [4, 1, 0, 1, 4]})
        	A	B
        0	-2	4
        1	-1	1
        2	0	0
        3	1	1
        4	2	4
        >>> fig, ax = plt.subplots()
        >>> data_plotter.scatter_plot('A', 'B', df, ax)
        """
        ax.plot(X_label, y_label, data=df)

    def plot_on_ax (self, X_label, y_label, df, ax, plot_type = 'scatter'):
        """
        Function that excutes a plot (according to plot_type) on a given axis, provided a dataframe and specified X and y labels. 
    
        Parameters
        ----------

        X_label: str
            The name of column in the dataframe used for the plot as X.

        y_label: str
            The name of column in the dataframe used for the plot as y.
            
        df: DataFrame
            A pamdas dataframe containing the X_label and y_label columns with data.

        ax: axis
            The axis on which the plot will be presented on.

        plot_type: str, default 'scatter'
            A parameter that determines the type of plot.
 
        Returns
        -------
        None
            No return value, the plot will just be presented
        
        Examples
        --------
        >>> import pandas as pd
        >>> import matplotlib.pyplot as plt
        >>> data_plotter = DataPlotter()
        >>> df = pd.DataFrame({'A': [-2, -1, 0, 1, 2], 'B': [4, 1, 0, 1, 4]})
        	A	B
        0	-2	4
        1	-1	1
        2	0	0
        3	1	1
        4	2	4
        >>> fig, ax = plt.subplots()
        >>> data_plotter.plot_on_ax('A', 'B', df, ax)
        """
        self.assert_value_is_allowed(plot_type, self.possible_plots, error_message='plot_type not found')
        getattr(self, plot_type+'_plot')(X_label, y_label, df, ax)
        ax.set_xlabel(X_label)
        ax.set_ylabel(y_label)

    def plot_on_subplots(self, variable_list, df, row_number = 2, fig_size=(15,15), plot_type = 'scatter'):
        """
        Function that excutes a series of plots (according to plot_type) as subplot. This series of plots will be all possible couple combinations (order doesn't matter)
        of labels listed in variable_list, provided a dataframe containing all possible labels. 
    
        Parameters
        ----------

        variable_list: list
            A list of labels in the dataframe, where all couple combinations made from this list will be plotted.
            
        df : DataFrame
            A pamdas dataframe containing the variable_list column labels with data.

        row_number: int, default 2
            The number of rows in the subplots figure that will be presented.

        fig_size: tuple, default (15,15)
            The figure size of each subplot.

        plot_type: str, default 'scatter'
            A parameter that determines the type of plot.
 
        Returns
        -------
        None
            No return value, the plot will just be presented
        
        Examples
        --------

        >>> import pandas as pd
        >>> data_plotter = DataPlotter()
        >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [2, 3, 4], 'C': [3, 4, 5], 'D': [4, 5, 6]})
        	A	B	C	D
        0	1	2	3	4
        1	2	3	4	5
        2	3	4	5	6
        >>> data_plotter.plot_scatter_on_subplots(['A', 'B', 'D'], df)
        """
        import matplotlib.pyplot as plt
        self.assert_column_names_exists(df, variable_list)
        num_of_plots = len(variable_list)-1
        fig, axs = plt.subplots(row_number, 1+(num_of_plots//row_number), figsize=fig_size)
        for variable_index, loop_variable in enumerate(variable_list[1:]):
            self.plot_on_ax(variable_list[0], loop_variable, df, axs[variable_index % row_number][variable_index // row_number], plot_type)


    def plot_corr_heatmap (self, df, figure_size = (15, 15), mask = 'upper_triangle', **heatmap_kwargs):
        """
        Function that plots a corrlation relations plot based on the seaborn heatmap plot on a given axis, provided a dataframe. 
    
        Parameters
        ----------
            
        df: DataFrame
            A pamdas dataframe with data to be plotted.

        figure_size: tuple, default (15, 15)
            A (x, y) size tuple

        mask: str, default 'upper_triangle'
            A mask matrix instructions that will reduce the heatmap.

        heatmap_kwargs: kwargs
            Keyword arguments that be provided to seaborn heatmap function

 
        Returns
        -------
        None
            No return value, the plot will just be presented
        
        Examples
        --------
        >>> from sklearn import datasets
        >>> import pandas as pd
        >>> iris = datasets.load_iris()
        >>> X = pd.DataFrame(iris.data, columns=['feature_'+str(i) for i in range(4)])
        >>> data_plotter = DataPlotter()
        >>> data_plotter.plot_corr_heatmap(X, annot = True, cmap='coolwarm', linewidths=3, linecolor='black')
        """
        import matplotlib.pyplot as plt
        import seaborn as sns
        self.assert_df(df)
        self.assert_value_is_allowed(mask, self.mask_matrix_dict.keys(), error_message='mask matrix type not found')
        fig, ax = plt.subplots(figsize=figure_size)
        mask_matrix = self.mask_matrix_dict.get(mask)(df.corr())
        sns.heatmap(df.corr(), mask=mask_matrix, **heatmap_kwargs)

class MetricsInterpeter (DataValidtor):

    from sklearn.metrics import r2_score, mean_squared_error, accuracy_score, recall_score, precision_score, f1_score
    bigger_the_better_metrics = ('R2', 'recall', 'accuracy', 'precision', 'f1')
    smaller_the_better_metrics = ('MSE')
    metric_interperter = {'MSE_loss': mean_squared_error, 'R2_score': r2_score, 'recall_score': recall_score, 'accuracy_score': accuracy_score, 'precision_score': precision_score, 'f1_score': f1_score}

    def correct_metric_name(self, metric):
        """
        Function that recieves an metric names and adds a suffix to it accoring to it's goal.
        If the goal of the metric is 'bigger the better' the suffix will be '_score', if the goal is 'smaller the better' the suffix will be '_loss'.
    
        Parameters
        ----------

        metric: str
            The name of the metric.


        Returns
        -------
        Str
            A str of the metric name with appropriate suffix. 
        
        Examples
        --------
        >>> metric_interpeter = MetricsInterpeter()
        >>> metric_interpeter.correct_metric_name('MSE')
        'MSE_loss'
        >>> metric_interpeter.correct_metric_name('f1')
        'f1_score'
        """
        if metric in self.bigger_the_better_metrics:
            return metric+'_score'
        if metric in self.smaller_the_better_metrics:
            return metric+'_loss'

    def create_metric_function(self, metric):
        """
        Function that recieves a metric name and returns the appropriate metric fuction.
    
        Parameters
        ----------

        metric: str
            The name of the choosen metric. must have a suffix of '_score' or '_loss'.
 

        Returns
        -------
        Object
            A metric function 
        
        Examples
        --------
        >>> metric_interpeter = MetricsInterpeter()
        >>> metric_interpeter.create_metric_function('RMSE_loss')
        <function __main__.MetricsInterpeter.<lambda>>
        >>> metric_interpeter.create_metric_function('f1_score')
        <function sklearn.metrics._classification.f1_score>
        """
        self.assert_value_is_allowed(metric, self.metric_interperter.keys(), 
                                     error_message = 'The metric '+metric.split('_')[0]+' was not found. known metrics are:\n'+'\n'.join(self.metric_interperter.keys()))
        return self.metric_interperter.get(metric)


    def interpert_metrics(self, metrics):
        """
        Function that recieves an iterable of metric names and returns the appropriate metric fuctions.
    
        Parameters
        ----------

        metrics: iterable of str
            The names of the choosen metrics.


        Returns
        -------
        List
            A list of metric functions 
        
        Examples
        --------
        >>> metric_interpeter = MetricsInterpeter()
        >>> metric_interpeter.interpert_metrics(['MSE', 'f1'])
        {'MSE_loss': <function sklearn.metrics._regression.mean_squared_error>,
        'f1_score': <function sklearn.metrics._classification.f1_score>}
        """
        corrected_metric_names = [self.correct_metric_name(metric) for metric in metrics]
        selected_metrics = {metric: self.create_metric_function(metric) for metric in corrected_metric_names}
        return selected_metrics

# level 2 - Finished documentation
class Utils (MetricsInterpeter, ColumnsInfoCollector, DataPlotter):

    def build_loop_range (self, start_num, end_num, error_message='Input must contain only int numbers'):
        """
        Compute a simple iterable range for loops, the main difference between it and simple 'range(start_num, end_num)' is that
        in case of start_num == end_num this function still returns an iterable
    
        Parameters
        ----------

        start_num: int
            Inital value for iteration.

        end_num: int
            End value for iteration.

        error_message: str, default 'Input must contain only int numbers'
            In case of invalid enrty, this will the presented error message to the user.
 
        Returns
        -------

        Iterable
            Iterable in the range of start_num to end_num.
        
        Examples
        --------

        >>> operating_tool = Utils()
        >>> operating_tool.build_loop_range(5, 8)
            range(5, 8)
        >>> operating_tool.build_loop_range(6, 6)
            [6]
        """
        
        self.assert_int_iterable ([start_num, end_num], error_message)
        if start_num == end_num:
            return [start_num]
        return range(start_num, end_num)

    def merge_dicts (self, *dicts):
        """
        Given dictionaries, returns a merge dictionary with all the items combined. the function assumes that is no joint keys
    
        Parameters
        ----------

        dicts: dict kargs
            The dictionaries intended for merging
 
        Returns
        -------

        Dictionary
            Dictionary with all the items from the given dictionaries
        
        Examples
        --------

        >>> operating_tool = Utils()
        >>> dict_1 = {'a': 1, 'b': 2}
        >>> dict_2 = {'c': 3}
        >>> dict_3 = {'d': 4, 'e': 5, 'f': 6}
        >>> operating_tool.merge_dicts(dict_1, dict_2, dict_3)
            {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
        """
        merged_dict = {k: v for d in dicts for k, v in d.items()}
        return merged_dict

    def flatten_list_of_lists (self, list_of_lists):
        """
        Given a list where are all the items are list themselves, returns a single list where the items are the items of the inner lists
    
        Parameters
        ----------

        list_of_lists: list
            List of lists, meaning that items of the list are lists as well.
 
        Returns
        -------

        List
            List where all the items are the items of the inner lists
        
        Examples
        --------

        >>> operating_tool = Utils()
        >>> list_of_lists [[6, 5], [8, 9], [2]]
        >>> operating_tool.flatten_list_of_lists(list_of_lists)
            [6, 5, 8, 9, 2]
        """
        return [item for sublist in list_of_lists for item in sublist]

    def merge_lists (self, lists, joining_parameter = 'union'):
        """
        Given an iterable where every item in the is a list and a joining_parameter that could be
        either 'union' or 'intersection', return a merged list of the inner lists.
        If 'union' is choosen, the result will contain all the unique values in all the inner lists.
        If 'intersection' is choosen, the result will contain the unique items that appear in all the inner lists. 
    
        Parameters
        ----------

        lists: iterable
            An iterable that all its items are lists

        joining_parameter: str, default 'union'
            A parameter that determines how the merging will be.
            If 'union' is choosen, the result will contain all the unique values in all the inner lists.
            If 'intersection' is choosen, the result will contain the unique items that appear in all the inner lists. 
 
        Returns
        -------

        List
            A list with the merged items of the inner lists.
        
        Examples
        --------

        >>> operating_tool = Utils()
        >>> lists = [[1, 2, 3], [2, 3, 4], [3, 4, 5, 6]]
        >>> operating_tool.merge_lists(lists, joining_parameter = 'union') 
            [1, 2, 3, 4, 5, 6]
        >>> operating_tool.merge_lists(lists, joining_parameter = 'intersection') 
            [3]
        """
        if joining_parameter == 'union':
            final_list = list(set(self.flatten_list_of_lists(lists)))
        if joining_parameter == 'intersection':
            final_list = list(set(lists[0]).intersection(*lists[1:]))
        return final_list

    def get_value_frequency_from_tuples_iterable (self, tuple_iterable, value):
        """
        Given an iterable where every item in the iterable is a tuple and a value.
        The function returns the number of times this value appers in the inner tuples. 
    
        Parameters
        ----------

        tuple_iterable: iterable
            An iterable that all its items are tuples.
            the lentgh of each tuple has to be at least 2, as it searches the first two items only.

        value: any
            The value that will be searched in the inner tuple of the iterable. 
 
        Returns
        -------

        Int
            The frequency of the value in the iterable.
        
        Examples
        --------

        >>> operating_tool = Utils()
        >>> tuple_list = [(1, 2), (3, 1), (2, 3), (1, 1)]
        >>> operating_tool.get_item_frequency_from_tuples_iterable(tuple_list, value=1)
            4
        """
        from collections import Counter
        return Counter(i[0] for i in tuple_iterable)[value] + Counter(i[1] for i in tuple_iterable)[value]

    def get_values_ordered_by_frequency_from_tuples_iterable (self, tuple_iterable):
        """
        Given an iterable where every item in the iterable is a tuple, returns a list of unique value of the inner tuples,
        ordered by their frequency. 
    
        Parameters
        ----------

        tuple_iterable: iterable
            An iterable that all its items are tuples.
            the lentgh of each tuple has to be at least 2, as those are only value that will count.

 
        Returns
        -------

        Int
            The frequency of the value in the iterable.
        
        Examples
        --------

        >>> operating_tool = Utils()
        >>> tuple_list = [(1, 2), (3, 1), (2, 3), (1, 1)]
        >>> operating_tool.get_values_ordered_by_frequency_from_tuples_iterable(tuple_list)
            [1, 2, 3]
        """
        values_and_frequencies = {value : self.get_value_frequency_from_tuples_iterable(tuple_iterable, value) for value_tuple in tuple_iterable for value in value_tuple}
        sorted_tuples = sorted(values_and_frequencies.items(), key=lambda x: x[1], reverse=True)
        sorted_values_list = [value_tuple[0] for value_tuple in sorted_tuples]
        return sorted_values_list

    def get_paired_value_from_tuple (self, single_tuple, value):
        """
        Given an tuple that has 2 values and value. 
        If this value is found in the tuple, the function returns the other value from the tuple, otherwise rises an error.
    
        Parameters
        ----------

        single_tuple: tuple
            A tuple in a length of 2.
        
        value: any
            The value that will be searched in the tuple.

        Returns
        -------

        Any
            The pair value from the tuple.
        
        Examples
        --------

        >>> operating_tool = Utils()
        >>> single_tuple = (1, 2)
        >>> operating_tool.get_paired_value_from_tuple (single_tuple, value=3)
        AssertionError: Value not found in the tuple
        >>> operating_tool.get_paired_value_from_tuple (single_tuple, value=1)
            2
        """
        self.assert_value_is_allowed(value, single_tuple, 'Value not found in the tuple')
        if value == single_tuple[0]:
            return single_tuple[1]
        if value == single_tuple[1]:
            return single_tuple[0]
        
    def get_all_paired_values_from_tuple_iterable (self, tuple_iterable, value, save_reminders = False, save_reminders_attr_name=''):
        """
        Given an iterable where every item in the is a tuple and a value.
        The function returns the all of the paired items in the inner tuples (including the inital value)
    
        Parameters
        ----------

        tuple_iterable: iterable
            An iterable that all its items are tuples.
            the lentgh of each tuple has to be at least 2, as it searches the first two items only.

        value: any
            The value that will be searched in the inner tuple of the iterable.

        save_reminders: bool, default False
            optinal feature of this function. If True, all the values that were paired to the given value
            will be removed from a list (an attribute in the object).

        save_reminders_attr_name: str, default ''
            The name of the attribute that holds a list of values, and it will be reduced from all
            the values that were returned by this function. 
 
        Returns
        -------

        List
            A list of all paired values of the given value (inculding the given value)
        
        Examples
        --------

        >>> operating_tool = Utils()
        >>> tuple_list = [(1, 2), (3, 1), (2, 3), (1, 1)]
        >>> operating_tool.get_all_paired_values_from_tuple_iterable(tuple_list, value=3)
            [3, 1, 2]
        """
        paired_values = [value] + [self.get_paired_value_from_tuple(single_tuple, value) for single_tuple in tuple_iterable if value in single_tuple]
        if save_reminders:
            inital_reminders = getattr(self, save_reminders_attr_name)
            setattr(self, save_reminders_attr_name, [value for value in inital_reminders if not value in paired_values])
        return paired_values

    def get_core_string(self, inital_str):
        """
        A function that gets a string that can have a serial number at the end, and returns a string without a serial number
    
        Parameters
        ----------

        inital_str: str
            A string that can have a serial number at the end.

 
        Returns
        -------

        String
            A string withour a serial number at the end.
        
        Examples
        --------

        >>> operating_tool = Utils()
        >>> operating_tool.get_core_string('B_5')
        'B'
        >>> operating_tool.get_core_string('meow')
        'meow'
        >>> operating_tool.get_core_string('k_best_8')
        'k_best'
        """
        split_result = inital_str.split('_')
        if split_result[-1].isdigit():
            return '_'.join(split_result[:-1])
        else:
            return inital_str

    def set_attributes(self, estimator, **kwargs):
        """
        Given an estimator and key arguments for the estimator , returns an estimator with the attributes set
    
        Parameters
        ----------
        estimator : object
            An object.

        kwargs : keywords
 
        Returns
        -------
        Object
            The given estimator with attributes set.
        
        Examples
        --------
        >>> from sklearn.neighbors import KNeighborsClassifier
        >>> operating_tool = Utils()
        >>> operating_tool.set_attributes(KNeighborsClassifier(), n_neighbors = 8, leaf_size = 20, p = 1) 
            KNeighborsClassifier(algorithm='auto', leaf_size=20, metric='minkowski',
                                 metric_params=None, n_jobs=None, n_neighbors=8, p=1,
                                 weights='uniform')
        >>> operating_tool.set_attributes(KNeighborsClassifier(), **{'n_neighbors': 2, 'weights': 'distance'}) 
            KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
                                 metric_params=None, n_jobs=None, n_neighbors=2, p=2,
                                 weights='distance')
        """
        # self.assert_estimator(estimator)
        new_estimator = estimator
        for attr_name, attr_value in kwargs.items():
            setattr(new_estimator, attr_name, attr_value)
        return new_estimator

# level 3 - Finished documnetation

class CorrlationAnalyzer (Utils):
        
    def get_top_correlations (self, df, correlation_limit=0.8, abs_factor=True):        
        """
        A fucntion that gets a df and return the top_correlations of the dataframe based on the correlation limit and abs_factor
    
        Parameters
        ----------

        df: DataFrame
            A pandas dataframe with the data for analysis.

        correlation_limit: float, default 0.8
            A corrleation limit for analysis. if the correlation between two factors is below this limit the paired columns won't be considered correlated.

        abs_factor: bool, default True
            A bool factor that will determine whether to apply abs on the correlation values.

        Returns
        -------

        Dataframe
            A dataframe (full version) detailing the top correlations of df.
        
        Examples
        --------

        >>> import pandas as pd
        >>> from sklearn import datasets
        >>> corrlation_analyzer = CorrlationAnalyzer()
        >>> iris = datasets.load_iris()
        >>> X = pd.DataFrame(iris.data, columns=['feature_'+str(i) for i in range(4)])
        >>> corrlation_analyzer.get_top_correlations(X)
        feature_0  feature_0    1.000000
                   feature_1         NaN
                   feature_2    0.871754
                   feature_3    0.817941
        feature_1  feature_0         NaN
                   feature_1    1.000000
                   feature_2         NaN
                   feature_3         NaN
        ...
        """
        self.assert_df(df)
        if abs_factor == True:
            corr_matrix = df.corr().abs()
        else:
            corr_matrix = df.corr()
        return corr_matrix[corr_matrix>=correlation_limit].unstack()

    def get_top_correlated_pairs(self, df, correlation_limit=0.8, abs_factor=True):
        """
        A fucntion that gets a df and return the top_correlations of the dataframe based on the correlation limit and abs_factor
    
        Parameters
        ----------

        df: DataFrame
            A pandas dataframe with the data for analysis.

        correlation_limit: float, default 0.8
            A corrleation limit for analysis. if the correlation between two factors is below this limit the paired columns won't be considered correlated.

        abs_factor: bool, default True
            A bool factor that will determine whether to apply abs on the correlation values.

        Returns
        -------

        Dataframe
            A dataframe (reduced version) detailing the top correlations of df.
        
        Examples
        --------

        >>> import pandas as pd
        >>> from sklearn import datasets
        >>> corrlation_analyzer = CorrlationAnalyzer()
        >>> iris = datasets.load_iris()
        >>> X = pd.DataFrame(iris.data, columns=['feature_'+str(i) for i in range(4)])
        >>> corrlation_analyzer.get_top_correlated_pairs(X)
        feature_2  feature_3    0.962865
        feature_0  feature_2    0.871754
                   feature_3    0.817941
        dtype: float64
        """
        corr_matrix = self.get_top_correlations(df, correlation_limit, abs_factor)
        labels_to_drop = self.get_lower_triangular_pairs(df, include_diagonal=True)
        corr_pairs = corr_matrix.drop(labels=labels_to_drop).sort_values(ascending=False)
        return corr_pairs.dropna()

    def get_corr_features_groups (self, df, correlation_limit=0.8, abs_factor=True):
        """
        A fucntion that gets a df and return the correlation groups (grouped pairs with a common correlated features)
        of the dataframe based on the correlation limit and abs_factor
    
        Parameters
        ----------

        df: DataFrame
            A pandas dataframe with the data for analysis.

        correlation_limit: float, default 0.8
            A corrleation limit for analysis. if the correlation between two factors is below this limit the paired columns won't be considered correlated.

        abs_factor: bool, default True
            A bool factor that will determine whether to apply abs on the correlation values.

        Returns
        -------

        List
            A list where every item is a group of features who are correlated.
        
        Examples
        --------

        >>> import pandas as pd
        >>> from sklearn import datasets
        >>> corrlation_analyzer = CorrlationAnalyzer()
        >>> iris = datasets.load_iris()
        >>> X = pd.DataFrame(iris.data, columns=['feature_'+str(i) for i in range(4)])
        >>> corrlation_analyzer.get_corr_features_groups(X)
        [['feature_2', 'feature_3', 'feature_0']]
        """
        feature_pairs = self.get_top_correlated_pairs(df, correlation_limit, abs_factor).index
        ordered_features = self.get_values_ordered_by_frequency_from_tuples_iterable(feature_pairs)
        self.left_features = ordered_features.copy()
        corr_groups = [self.get_all_paired_values_from_tuple_iterable(feature_pairs, feature, save_reminders=True, save_reminders_attr_name='left_features') for feature in ordered_features if feature in self.left_features]
        delattr(self, 'left_features')
        return corr_groups

    def plot_correlated_groups (self, df, correlation_limit=0.8, abs_factor=True, plot_type='scatter'):
        """
        A fucntion that gets a df and return the correlation groups (grouped pairs with a common correlated features)
        of the dataframe based on the correlation limit and abs_factor
    
        Parameters
        ----------

        df: DataFrame
            A pandas dataframe with the data for analysis.

        correlation_limit: float, default 0.8
            A corrleation limit for analysis. if the correlation between two factors is below this limit the paired columns won't be considered correlated.

        abs_factor: bool, default True
            A bool factor that will determine whether to apply abs on the correlation values.

        plot_type: str, default 'scatter'
            A parameter given to the plot_on_subplots method and determines the type of plot drawn.

        Returns
        -------

        None
            No return value, the plot will just be presented.
        
        Examples
        --------

        >>> import pandas as pd
        >>> from sklearn import datasets
        >>> corrlation_analyzer = CorrlationAnalyzer()
        >>> iris = datasets.load_iris()
        >>> X = pd.DataFrame(iris.data, columns=['feature_'+str(i) for i in range(4)])
        >>> corrlation_analyzer.plot_correlated_groups(X)
        """
        corr_groups = self.get_corr_features_groups(df, correlation_limit, abs_factor)
        for corr_group in corr_groups:
            self.plot_on_subplots(corr_group, df, plot_type=plot_type)

class NewFeaturesAdder(Utils):
    addition_features_selector = {'polynomial': 'add_polynomial_features',
                                  'interaction': 'add_interaction_features',
                                  'fitted': 'add_fitted_features'}

    def interpert_addition_instructions(self, df, addition_instructions):
        """
        Function that takes the addition instruction provided by the user and translates any column codes to actual columns in the df.
        Column codes:
        'all' - returns all the columns in the df
        'couples' - returns all possible combinations of couples from the df columns pool. 
    
        Parameters
        ----------

        df: DataFrame
            A pamdas dataframe containing the column that the polynomial features will be based on.

        addition_instructions: list
            list of tuples, where every tuple represent an addition instruction. the first item in the tuple is the target column/s
            and the second item is either a function (interaction/fitting) or int number (polynomial).

        Returns
        -------

        List
            An updated version of the given addition instruction. If the instruction didn't contain any 'column codes' the final result will be identical to original input,
            and if codes were used then they will be replaced with the actual column names from the df
        
        Examples
        --------
        >>> import pandas as pd
        >>> from sklearn import datasets
        >>> def interaction_func (x):
        >>>     return x[0]*x[-1]
        >>> new_features_tool = NewFeaturesAdder()
        >>> iris = datasets.load_iris()
        >>> X = pd.DataFrame(iris.data, columns=['feature_'+str(i) for i in range(4)])
        >>> polynomial_instructions = [('all', 2), (['feature_3'], 3)]
        >>> new_features_tool.interpert_addition_instructions(X, polynomial_instructions)
        [(['feature_0'], 2),
        (['feature_1'], 2),
        (['feature_2'], 2),
        (['feature_3'], 2),
        (['feature_3'], 3)]
        >>> interaction_instructions = [('couples', interaction_func)]
        >>> new_features_tool.interpert_addition_instructions(X, interaction_instructions)
        [(('feature_1', 'feature_0'), <function __main__.interaction_func>),
        (('feature_3', 'feature_0'), <function __main__.interaction_func>),
        (('feature_3', 'feature_1'), <function __main__.interaction_func>),
        (('feature_2', 'feature_1'), <function __main__.interaction_func>),
        (('feature_3', 'feature_2'), <function __main__.interaction_func>),
        (('feature_2', 'feature_0'), <function __main__.interaction_func>)]
        """
        interpeted_instructions = []
        for (columns, addition_value) in addition_instructions:
            if type(columns) == list:
                interpeted_instructions.append((columns, addition_value))
            elif columns == 'all':
                interpeted_instructions = interpeted_instructions +  [([columns_interp], addition_value) for columns_interp in getattr(self, self.column_codes.get(columns))(df)]
            elif columns == 'couples':
                interpeted_instructions = interpeted_instructions +  [(columns_interp, addition_value) for columns_interp in getattr(self, self.column_codes.get(columns))(df)]
        return interpeted_instructions

    def polynomial_feature (self, df, column_name, polynomial_degree, new_column_name = None):
        """
        Function that add polynomial features of a dataframe column. 
    
        Parameters
        ----------

        df : DataFrame
            A pamdas dataframe containing the column that the polynomial features will be based on.

        column_name: str
            The label of the column in the dataframe used for the polynominal features.

        polynomial_degree: int
            The maximum degree of polynominal features, all degrees prior to that degree will be created.

        new_column_names: list, default None
            The names given to the new columns that will be created.
            If None, the column name for each column will be the a concatenation of the original name
            with '**poly_degree' for each poly_degree created respectively
 
        Returns
        -------
        DataFrame
            A dataframe contianing all the original columns of the provided df with the polynominal features added
        
        Examples
        --------
        >>> new_features_tool = NewFeaturesAdder()
        >>> import pandas as pd
        >>> df = pd.DataFrame({'A': [-2, -1, 0, 1, 2], 'B': [4, 1, 0, 1, 4]})
        	A	B
        0	-2	4
        1	-1	1
        2	0	0
        3	1	1
        4	2	4
        >>> new_features_tool.polynomial_feature(df, 'A', 4)        
            A	B	A**2	A**3	A**4
        0	-2	4	4	    -8	    16
        1	-1	1	1	    -1	    1
        2	0	0	0	    0	    0
        3	1	1	1	    1	    1
        4	2	4	4	    8	    16
        >>> new_features_tool.polynomial_feature(df, 'B', 3, ['B_squared', 'B_cubed'])        
            A	B	B_squared	B_cubed
        0	-2	4	16	        64
        1	-1	1	1	        1
        2	0	0	0	        0
        3	1	1	1	        1
        4	2	4	16	        64
        """
        new_df = df.copy()
        loop_range = self.build_loop_range (2, polynomial_degree+1, 'polynomial degree must be integer')
        if new_column_name == None:
            new_column_name = [column_name+'**'+str(degree) for degree in loop_range]
        for loop_index, degree in enumerate(loop_range):
            new_df[new_column_name[loop_index]] = new_df[column_name].apply(lambda x: x**degree)
        return new_df

    def add_polynomial_features(self, df, polynomial_instructions):
        """
        Function that add polynomial features of a dataframe columns according to the polynomial instructions. 
    
        Parameters
        ----------

        df: DataFrame
            A pamdas dataframe containing the column that the polynomial features will be based on.

        polynomial_instructions: list
            List of tuples, where every tuple represent a polynomial instruction. 
            The first item in the tuple is the target column, and the second item is int number representing the maximum
            polynomial degree (all degrees up to this number it will be created).

        Returns
        -------

        DataFrame
            A dataframe contianing all the original columns of the provided df with the polynominal features added
        
        Examples
        --------

        >>> new_features_tool = NewFeaturesAdder()
        >>> import pandas as pd
        >>> df = pd.DataFrame({'A': [-2, -1, 0, 1, 2], 'B': [4, 1, 0, 1, 4]})
        	A	B
        0	-2	4
        1	-1	1
        2	0	0
        3	1	1
        4	2	4
        >>> polynomial_instructions=[(['A'], 4), (['B'], 3)]
        >>> new_features_tool.add_polynomial_features(df, polynomial_instructions)                
            A	B	A**2	A**3	A**4	B**2	B**3
        0	-2	4	4	    -8	    16	    16	    64
        1	-1	1	1	    -1	    1	    1	    1
        2	0	0	0	    0	    0	    0	    0
        3	1	1	1	    1	    1	    1	    1
        4	2	4	4	    8	    16	    16	    64
        """
        self.assert_df(df)
        updated_instructions = self.interpert_addition_instructions(df, polynomial_instructions)
        new_df = df.copy()
        for (columns, polynomial_degree) in updated_instructions:
            self.assert_column_names_exists(new_df, columns)
            for column_name in columns:
                new_df = self.polynomial_feature(new_df, column_name, polynomial_degree)
        return new_df

    def interaction_feature (self, df, columns, interaction_function, new_column_name = None):
        """
        Function that add interaction feature of a dataframe column pair. 
    
        Parameters
        ----------

        df: DataFrame
            A pamdas dataframe containing the column pair that the interaction feature will be based on.

        columns: list
            List containing the labels of the columns in the dataframe used for the interaction feature.

        interaction_function: callable object
            The interaction function that will used to create the interaction feature.
            This function must be in one variable, where each variable contains a number of data points
            in respect to to the number of columns and in respect to their location in the columns list. 

        new_column_names: str, default None
            The name given to the new column that will be created.
            If None, the column name will be a concatenation of the original names
 
        Returns
        -------
        DataFrame
            A dataframe contianing all the original columns of the provided df with the interaction feature added
        
        Examples
        --------
        >>> new_features_tool = NewFeaturesAdder()
        >>> import pandas as pd
        >>> def interaction_func (x):
        >>>     return x[0]*x[-1]
        >>> df = pd.DataFrame({'A': [-2, -1, 0, 1, 2], 'B': [4, 1, 0, 1, 4]})
        	A	B
        0	-2	4
        1	-1	1
        2	0	0
        3	1	1
        4	2	4
        >>> new_features_tool.interaction_feature(df, ['A', 'B'], interaction_func)
        	A	B	A_B
        0	-2	4	-8
        1	-1	1	-1
        2	0	0	0
        3	1	1	1
        4	2	4	8
        """
        new_df = df.copy()
        if new_column_name == None:
            new_column_name = '_'.join(columns) # columns[0]+'_'+columns[-1]
        new_df[new_column_name] = new_df[list(columns)].apply(interaction_function, axis=1)
        return new_df

    def add_interaction_features (self, df, interaction_instructions):
        """
        Function that add interaction features of a dataframe according to the interaction instructions. 
    
        Parameters
        ----------

        df: DataFrame
            A pamdas dataframe containing the columns that the interaction features will be based on.

        interaction_instructions: list
            List of tuples, where every tuple represent an interaction instruction. 
            The first item in the tuple is a list of columns for the interaction, and the second item is a callable function that will be applied on
            the provided columns. This function must be in one variable, where each variable contains a number of data points
            in respect to to the number of columns and in respect to their location in the columns list. 
 
        Returns
        -------
        DataFrame
            A dataframe contianing all the original columns of the provided df with the interaction features added
        
        Examples
        --------
        >>> new_features_tool = NewFeaturesAdder()
        >>> import pandas as pd
        >>> def interaction_func (x):
        >>>     return x[0]*x[-1]
        >>> df = pd.DataFrame({'A': [-2, -1, 0, 1, 2], 'B': [4, 1, 0, 1, 4]})
        	A	B
        0	-2	4
        1	-1	1
        2	0	0
        3	1	1
        4	2	4
        >>> interaction_instructions=[(['A', 'B'], interaction_func)]
        >>> new_features_tool.add_interaction_features(df, interaction_instructions)
        	A	B	A_B
        0	-2	4	-8
        1	-1	1	-1
        2	0	0	0
        3	1	1	1
        4	2	4	8
        """
        self.assert_df(df)
        updated_instructions = self.interpert_addition_instructions(df, interaction_instructions)
        new_df = df.copy()
        for (columns, interaction_function) in updated_instructions:
            self.assert_column_names_exists(new_df, columns)
            new_df = self.interaction_feature(new_df, columns, interaction_function)
        return new_df

    def fitted_feature (self, df, columns, fit_function, new_column_name = None):
        """
        Function that add fitted feature of a dataframe given columns and a fit function. 
    
        Parameters
        ----------

        df: DataFrame
            A pamdas dataframe containing the columns that the fitted feature will be based on.

        columns: list
            List containing the labels of the columns in the dataframe used for the fitted feature.
            The order should [X_label, y_label]

        fit_function: callable object
            The fit function that will used to create the fitted feature.
            This must be a function in one variable(x) and coefficients 

        new_column_names: str, default None
            The name given to the new column that will be created.
            If None, the column name will be a concatenation of the X_label with '_fitted'
 
        Returns
        -------
        DataFrame
            A dataframe contianing all the original columns of the provided df with the fitted feature added
        
        Examples
        --------
        >>> new_features_tool = NewFeaturesAdder()
        >>> import pandas as pd
        >>> def poly_3(x, a, b, c, d):
        >>>     return round(a + b*x + c*(x**2) + d*(x**3),2)
        >>> df = pd.DataFrame({'A': [-2, -1, 0, 1, 2], 'B': [4, 1, 0, 1, 4]})
        	A	B
        0	-2	4
        1	-1	1
        2	0	0
        3	1	1
        4	2	4
        >>> new_features_tool.fitted_feature(df, ['A', 'B'], poly_3)
        	A	B	A_fitted
        0	-2	4	-8
        1	-1	1	-1
        2	0	0	0
        3	1	1	1
        4	2	4	8
        """
        from scipy.optimize import curve_fit
        new_df = df.copy()
        if new_column_name == None:
            new_column_name = columns[0]+'_fitted'
        fit_coef, _ = curve_fit(fit_function, df[columns[0]], df[columns[1]])
        new_df[new_column_name] = new_df[columns[0]].apply(fit_function, args=tuple(fit_coef)) # Solve issue with posi args
        return new_df

    def add_fitted_features (self, df, fitting_instructions):
        """
        Function that add fitted features of a dataframe according to the fitting instructions. 
    
        Parameters
        ----------

        df: DataFrame
            A pamdas dataframe containing the columns that the fitting features will be based on.

        fitting_instructions: list
            List of tuples, where every tuple represent a fitting instruction. 
            The first item in the tuple is a list of columns for the fitting, and the second item is a callable function that fitting will
            be based on. This function must be in one variable(x), and the rest of the arguments will be the coefficients. 
 
        Returns
        -------
        DataFrame
            A dataframe contianing all the original columns of the provided df with the fitted features added
        
        Examples
        --------
        >>> new_features_tool = NewFeaturesAdder()
        >>> import pandas as pd
        >>> def poly_3 (x, a, b, c, d):
        >>>     return round(a + b*x + c*(x**2) + d*(x**3),2)
        >>> df = pd.DataFrame({'A': [-2, -1, 0, 1, 2], 'B': [4, 1, 0, 1, 4]})
        	A	B
        0	-2	4
        1	-1	1
        2	0	0
        3	1	1
        4	2	4
        >>> fitting_instructions=[(['A', 'B'], poly_3)]
        >>> new_features_tool.add_fitted_features(df, fitting_instructions)
        	A	B	A_fitted
        0	-2	4	-8
        1	-1	1	-1
        2	0	0	0
        3	1	1	1
        4	2	4	8
        """
        self.assert_df(df)
        updated_instructions = self.interpert_addition_instructions(df, fitting_instructions)
        new_df = df.copy()
        for (columns, fit_function) in updated_instructions:
            self.assert_column_names_exists(new_df, columns)
            new_df = self.fitted_feature(new_df, columns, fit_function)
        return new_df

    def add_new_features (self, instructions, df, *_):
        """
        Function that add can add polynomial, interaction and fitted features of a dataframe according to the given addition instructions. 
    
        Parameters
        ----------

        instructions: dictionary
            Dictionary containing all addition insturction for the new features. the keys will represent the type of features
            (like 'polynomial', 'interaction' or 'fitted') and according to every individual instructions adds features accordingly.
            For example: {'interaction': interaction_instructions, 'polynomial': polynomial_instructions, 'fitted': fitting_instructions}
            
            polynomial instructions
            List of tuples, where every tuple represent a polynomial instruction. 
            The first item in the tuple is the target column, and the second item is int number representing the maximum
            polynomial degree (all degrees up to this number it will be created).

            interaction instructions
            List of tuples, where every tuple represent an interaction instruction. 
            The first item in the tuple is a list of columns for the interaction, and the second item is a callable function that will be applied on
            the provided columns. This function must be in one variable, where each variable contains a number of data points
            in respect to to the number of columns and in respect to their location in the columns list.

            fitting insturctions
            List of tuples, where every tuple represent a fitting instruction. 
            The first item in the tuple is a list of columns for the fitting, and the second item is a callable function that fitting will
            be based on. This function must be in one variable(x), and the rest of the arguments will be the coefficients. 

        df: DataFrame
            A pamdas dataframe containing the columns that the new features will be based on.

 
        Returns
        -------
        DataFrame
            A dataframe contianing all the original columns of the provided df with the new features added
        
        Examples
        --------
        >>> new_features_tool = NewFeaturesAdder()
        >>> import pandas as pd
        >>> def interaction_func (x):
        >>>     return x[0]*x[-1]
        >>> def poly_3 (x, a, b, c, d):
        >>>     return round(a + b*x + c*(x**2) + d*(x**3),2)
        >>> df = pd.DataFrame({'A': [-2, -1, 0, 1, 2], 'B': [4, 1, 0, 1, 4]})
        	A	B
        0	-2	4
        1	-1	1
        2	0	0
        3	1	1
        4	2	4
        >>> polynomial_instructions=[(['A'], 4), (['B'], 3)]
        >>> interaction_instructions=[(['A', 'B'], interaction_func)]
        >>> fitting_instructions=[(['A', 'B'], poly_3)]
        >>> addition_instructions={'interaction': interaction_instructions, 'polynomial': polynomial_instructions, 'fitted': fitting_instructions}
        >>> new_features_tool.add_new_features(addition_instructions, df)
            A	B	A_B	A**2	A**3	A**4	B**2	B**3	A_fitted
        0	-2	4	-8	4	    -8	    16	    16	    64	    -5.0
        1	-1	1	-1	1	    -1	    1	    1	    1	    0.0
        2	0	0	0	0	    0	    0	    0	    0	    1.0
        3	1	1	1	1	    1	    1	    1	    1	    4.0
        4	2	4	8	4	    8	    16	    16	    64	    15.0
        """
        new_df = df.copy()
        for feature_type, type_instructions in instructions.items():
            self.assert_value_is_allowed(feature_type, self.addition_features_selector.keys(), error_message='Addition feature type not found')
            new_df = getattr(self, self.addition_features_selector.get(feature_type))(new_df, type_instructions)
        return new_df

class FeaturesScaler(Utils):
    from sklearn.preprocessing import MinMaxScaler, StandardScaler, OneHotEncoder, LabelBinarizer
    scaling_interpeter = {'normalize': StandardScaler(), 'min_max': MinMaxScaler(), 'onehot': OneHotEncoder(), 'label_binarize': LabelBinarizer()}

    def interpert_scaling_instructions(self, df, scaling_instructions):
        """
        Function that takes the scaling instruction provided by the user and translates any column codes to actual columns in the df.
        Column codes:
        'all' - returns all the columns in the df
        'couples' - returns all possible combinations of couples from the df columns pool. 
    
        Parameters
        ----------

        df: DataFrame
            A pamdas dataframe containing the column that the polynomial features will be based on.

        scaling_instructions: dictionary
            A dictionart containing scaling instruction. The keys will be the scaler(codes or actual scalers) the values will be
            a list of columns or column codes that the scaler should be activated on.

        Returns
        -------

        Dictionary
            An updated version of the given scaling instruction. If the instruction didn't contain any 'column codes' the final result will be identical to original input,
            and if codes were used then they will be replaced with the actual column names from the df
        
        Examples
        --------

        >>> features_scaler = FeaturesScaler()
        >>> import pandas as pd
        >>> df = pd.DataFrame({'A': [-2, -1, 0, 1, 2], 'B': [4, 1, 0, 1, 4]})
        >>> scaling_instructions = {'min_max': 'all'}
        >>> features_scaler.interpert_scaling_instructions(X, scaling_instructions)
        {'min_max': ['A', 'B']}
        """
        interpeted_instructions = {}
        for scaler, columns in scaling_instructions.items():
            if type(columns) == list:
                interpeted_instructions.update({scaler: columns})
            elif columns in self.column_codes.keys():
                interpeted_instructions.update({scaler: [columns_interp for columns_interp in getattr(self, self.column_codes.get(columns))(df)]})
        return interpeted_instructions


    def build_scaling_transformer(self, df, scaling_instructions, **column_transformer_kwargs):
        """
        A function that gets a dataframe, scaling instructions and possible kwargs for the make_column_transformer.
        The function constructs and returns a column transformer object built by the instructions 
    
        Parameters
        ----------

        df: DataFrame
            A pandas dataframe that contains all the columns that require scaling.

        scaling_instructions: dictionary
            A dictionart containing scaling instruction. The keys will be the scaler(codes or actual scalers) the values will be
            a list of columns or column codes that the scaler should be activated on.

        column_transformer_kwargs: kwargs
            kwargs that will be given to the make_column_transformer function.
 
        Returns
        -------

        ColumnTransformer
            A column transformer object created by the make_column_transformer function

        List
            A list containing the columns names that will be edited by the column transformer
        
        Examples
        --------

        >>> features_scaler = FeaturesScaler()
        >>> import pandas as pd
        >>> df = pd.DataFrame({'A': [-2, -1, 0, 1, 2], 'B': [4, 1, 0, 1, 4]})
        	A	B
        0	-2	4
        1	-1	1
        2	0	0
        3	1	1
        4	2	4
        >>> scaling_instructions = {'min_max': ['A'], 'normalize': ['B']}
        >>> features_scaler.build_scaling_transformer(df, scaling_instructions)
        (ColumnTransformer(n_jobs=None, remainder='drop', sparse_threshold=0.3,
                           transformer_weights=None,
                           transformers=[('minmaxscaler',
                                          MinMaxScaler(copy=True, feature_range=(0, 1)),
                                          ['A']),
                                         ('standardscaler',
                                          StandardScaler(copy=True, with_mean=True,
                                                         with_std=True),
                                          ['B'])],
                           verbose=False),
        ['A', 'B'])
        >>> scaling_instructions = {'min_max': 'all'}
        >>> features_scaler.build_scaling_transformer(df, scaling_instructions, remainder='passthrough', sparse_threshold=0)
        (ColumnTransformer(n_jobs=None, remainder='passthrough', sparse_threshold=0,
                           transformer_weights=None,
                           transformers=[('minmaxscaler',
                                          MinMaxScaler(copy=True, feature_range=(0, 1)),
                                          ['A', 'B'])],
                           verbose=False),
        ['A', 'B'])
        """
        from sklearn.compose import make_column_transformer
        updated_instructions = self.interpert_scaling_instructions(df, scaling_instructions)
        edited_columns_names = self.flatten_list_of_lists(updated_instructions.values())
        self.assert_column_names_exists(df, edited_columns_names)
        scaling_steps = [(self.scaling_interpeter.get(scaler, scaler), column_names) for scaler, column_names in updated_instructions.items()]
        column_scaler = make_column_transformer (*scaling_steps, **column_transformer_kwargs)
        return column_scaler, edited_columns_names

    def scale_features(self, instructions, df, *_):
        """
        A function that gets a dataframe and instructions for scaling and for making the make_column_transformer.
        The function constructs a column transformer object from the instructions and then activates it on the dataframe 
    
        Parameters
        ----------

        instructions: dictionary
            A dictionart containing scaling instruction. The keys will be the scaler(codes or actual scalers) the values will be
            a list of columns or column codes that the scaler should be activated on.

        df: DataFrame
            A pandas dataframe that contains all the columns that require scaling.


        Returns
        -------

        DataFrame
            A scaled version of the inital dataframe based on the scaling instructions.
        
        Examples
        --------

        >>> features_scaler = FeaturesScaler()
        >>> import pandas as pd
        >>> df = pd.DataFrame({'A': [-2, -1, 0, 1, 2], 'B': [4, 1, 0, 1, 4]})
        	A	B
        0	-2	4
        1	-1	1
        2	0	0
        3	1	1
        4	2	4
        >>> scaling_instructions = {'min_max': ['A'], 'normalize': ['B']}
        >>> features_scaler.scaling_features(scaling_instructions, df)
            A	    B
        0	0.00	1.195229
        1	0.25	-0.597614
        2	0.50	-1.195229
        3	0.75	-0.597614
        4	1.00	1.195229
        >>> scaling_instructions = {'min_max': 'all'}
        >>> features_scaler.scale_features(scaling_instructions, df)
            A	    B
        0	0.00	1.00
        1	0.25	0.25
        2	0.50	0.00
        3	0.75	0.25
        4	1.00	1.00
        """
        import pandas as pd
        self.assert_df(df)
        scaling_instructions={key: value for key, value in instructions.items() if key in self.scaling_interpeter.keys()}
        column_transformer_kwargs={key: value for key, value in instructions.items() if not key in self.scaling_interpeter.keys()}
        column_scaler, edited_columns_names = self.build_scaling_transformer(df, scaling_instructions, **column_transformer_kwargs)
        new_column_order  = edited_columns_names + [column_name for column_name in df.columns if not column_name in edited_columns_names]
        new_df = pd.DataFrame(column_scaler.fit_transform(df), columns = new_column_order)
        return new_df

class FeatureSelector(Utils):

    def init_selection_tools_and_metrics(self):
        from sklearn.feature_selection import SelectKBest, VarianceThreshold
        from sklearn.feature_selection import chi2, f_classif, f_regression
        self.selection_tool_interpeter = {'k_best': SelectKBest(), 'variance' : VarianceThreshold()}
        self.selection_metric_interpeter = {'class_if': f_classif, 'chi2': chi2, 'regression': f_regression}
    # chi2 non negetive

    def build_selection_tools(self, selection_instructions):
        """
        Function that takes feature selection instruction in codes provided by the user and translates any it to actual selection tool.
    
        Parameters
        ----------

        selection_instructions: dictionary
            Dictionary containing codes of selection tools and parameters from sklearn.feature_selection.
            Codes and meaning:
                'k_best': SelectKBest
                'variance': VarianceThreshold
                'class_if': f_classif
                'chi2': chi2
                'regression': f_regression


        Returns
        -------

        List
            An List of the actual selection tool built by the given selection instruction.
        
        Examples
        --------
        >>> feature_selector=FeatureSelector()
        >>> selection_instructions={'k_best_1': {'k': 12, 'score_func': 'chi2'}, 'k_best_2': {'k': 8}, 'variance': {'threshold': 1}}
        >>> feature_selector.build_selection_tools(selection_instructions)
        [SelectKBest(k=12, score_func=<function chi2 at 0x7f2a3dd5a7b8>),
         SelectKBest(k=8, score_func=<function f_classif at 0x7f2a3dd4eae8>),
         VarianceThreshold(threshold=1)]
        """
        selection_tools = []
        for select_tool, select_parameters in selection_instructions.items():
            self.init_selection_tools_and_metrics() 
            interperted_parameters = {key: self.selection_metric_interpeter.get(value, value) for key, value in select_parameters.items()}
            select_tool_interperted = self.selection_tool_interpeter.get(self.get_core_string(select_tool))
            selection_tool = self.set_attributes(select_tool_interperted, **interperted_parameters)
            selection_tools.append(selection_tool)
        return selection_tools

    def get_selection_results(self, X, y, selection_tools):
        """
        Function that takes a list of feature selection tool (sklearn.feature_selction tools or similar),
        activates each selection tool on the provided (X, y) data points (X must a pandas dataframe).
        and return a list where every value is a list of columns from X that is the result of selection tool, respectively.
    
        Parameters
        ----------

        X: DataFrame
            X data points.

        y: DataFrame or Series
            The target values of the given X data.

        selection_tools: list
            An List of selection tools (sklearn.feature_selection tools or similar).

        Returns
        -------

        List
            An List containing the restults of each selection tool as an individual list, resulting as list of lists.
        
        Examples
        --------
        >>> feature_selector=FeatureSelector()
        >>> import pandas as pd
        >>> from sklearn import datasets
        >>> iris = datasets.load_iris()
        >>> X = pd.DataFrame(iris.data, columns=['feature_'+str(i) for i in range(4)])
        >>> y = pd.Series(iris.target, name='target_column')
        >>> selection_instructions={'k_best': {'k': 2}, 'variance': {'threshold': 1}}
        >>> selection_tools=feature_selector.build_selection_tools(selection_instructions)
        >>> feature_selector.get_selection_results(X, y, selection_tools)
        [['feature_2', 'feature_3'], ['feature_2']]
        """
        self.assert_df(X)
        column_list = []
        for selection_tool in selection_tools:
            selection_tool.fit_transform(X, y)
            column_list.append(list(X.columns[selection_tool.get_support()]))
        return column_list

    def select_features(self, instructions, df, target_column, *_):
        """
        Function that takes a pandas dataframe, a column with target values and feature selection instruction in codes provided by the user.
        The function returns a reduced version of the df based on the feature selection steps.
    
        Parameters
        ----------

        instructions: dictionary.
            Dictionary containing codes of selection tools and parameters from sklearn.feature_selection.
            Codes and meaning:
                'k_best': SelectKBest
                'variance': VarianceThreshold
                'class_if': f_classif
                'chi2': chi2
                'regression': f_regression
            In addition, the instructions can contain a joining parameter what will determine the reduction of the output dataframe
            There are two valid options:
                'union' (default) - if a feature was selected at least by one selection tool, it will appear in the final dataframe
                'intersection' - if the feature was selected by all the selection tools, it will appeat in the final dataframe

        df: DataFrame
            A pandas dataframe containing X data points.

        target_column: DataFrame or Series
            The target values of the given X data.


        Returns
        -------

        DataFrame
            A reduced version of the inital dataframe, containing features selected by the selection parameters.
        
        Examples
        --------
        >>> feature_selector=FeatureSelector()
        >>> import pandas as pd
        >>> from sklearn import datasets
        >>> iris = datasets.load_iris()
        >>> X = pd.DataFrame(iris.data, columns=['feature_'+str(i) for i in range(4)])
        >>> y = pd.Series(iris.target, name='target_column')
        >>> selection_instructions={'k_best': {'k': 2}, 'variance': {'threshold': 1}}
        >>> feature_selector.select_features(X, y, selection_instructions)
            feature_3	feature_2
        0	0.2	        1.4
        1	0.2	        1.4
        2	0.2	        1.3
        3	0.2	        1.5
        4	0.2	        1.4
        >>> selection_instructions={'k_best': {'k': 2}, 'variance': {'threshold': 1}, 'joining_parameter': 'intersection'}
        >>> feature_selector.select_features(X, y, selection_instructions)
        	feature_2
        0	1.4
        1	1.4
        2	1.3
        3	1.5
        4	1.4
        """
        self.assert_df(df)
        new_df =df.copy()
        joining_parameter = instructions.pop('joining_parameter', 'union')
        selection_tools = self.build_selection_tools(instructions)
        column_lists = self.get_selection_results(new_df, target_column, selection_tools)
        new_df = new_df[self.merge_lists(column_lists, joining_parameter)]
        return new_df

# level 4 - finished documentation

class EstimatorDataProcessor(CorrlationAnalyzer, NewFeaturesAdder, FeaturesScaler, FeatureSelector):

    def get_predict_scores(self, estimator, X, y, metric_functions, prefix='', multiclass_classification=False):
        """
        A fucntion that gets a fitted estimator, (X, y) data points, a dictionary of metric functions,
        and a prefix for the final metric names. The function returns the scores of the estimator on the given
        data points based on the metric functions. 
    
        Parameters
        ----------
        estimator : object
            An estimator object (fitted already).

        X : array-like
            X data points.

        y : array-like
            The target values of the given X data.

        metric_functions: dictionary
            A dictionary of metric functions that will evaluate the preformance of the estimator.
            The keys of the dictionary are the names, and will be part of the scoring names as well,
            while the values are the scoring functions.

        prefix : str, default ''
            A prefix that will be added to names of the scoring functions as the keys of the final output.

        multiclass_classification: bool, default False
            A boolean flag indicating whether this is a classification problem with multi classes or not. 
 
        Returns
        -------
        Dictionary
            A dictionary of the metrics results of the given estimator with (X, y) dataset.
        
        Examples
        --------
        >>> import numpy as np
        >>> from sklearn.linear_model import LinearRegression
        >>> from sklearn.metrics import r2_score
        >>> X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
        >>> # y = 1 * x_0 + 2 * x_1 + 3
        >>> y = np.dot(X, np.array([1, 2])) + 3
        >>> reg_estimator = LinearRegression().fit(X, y)
        >>> metric_fuctions = {'R2': r2_score}
        >>> prefix = 'Test_'
        >>> estimator_data_processor = EstimatorDataProcesseor()
        >>> estimator_data_processor.get_predict_scores(reg_estimator, X, y, metric_functions, prefix)
        {'Test_R2': 1.0}
        """
        y_hat = estimator.predict(X)
        if multiclass_classification:
            score_results = {prefix+metric : round(metric_function(y, y_hat, average='micro'),2) for metric, metric_function in metric_functions.items()}
        else:
            score_results = {prefix+metric : round(metric_function(y, y_hat),2) for metric, metric_function in metric_functions.items()}
        return score_results

    def fit_and_score_estimator(self, estimator, X_train, X_test, y_train, y_test, metric_functions, multiclass_classification=False):
        """
        A fucntion that gets an estimator, (X_train, X_test, y_train, y_test) data points and a dictionary of metric functions,
        The function returns a fitted estimator (on the train data) and the train/test scores of the estimator on the given
        data points based on the metric functions. 
    
        Parameters
        ----------
        estimator : object
            An estimator object.

        X_train, X_test : array-like
            X data points.

        y_train, y_test : array-like
            The target values of the given X data.

        metric_functions: dictionary
            A dictionary of metric functions that will evaluate the preformance of the estimator.
            The keys of the dictionary are the names, and will be part of the scoring names as well,
            while the values are the scoring functions.

        multiclass_classification: bool, default False
            A boolean flag indicating whether this is a classification problem with multi classes or not. 

        Returns
        -------

        Object
            A fitted version of the given estimator

        Dictionary
            A dictionary of the evalution results of the given estimator with (X_train, X_test, y_train, y_test) dataset,
            according to the provided metrics.
        
        Examples
        --------
        >>> import numpy as np
        >>> from sklearn.linear_model import LinearRegression
        >>> from sklearn.metrics import r2_score
        >>> X_train = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
        >>> X_test = np.array([[1, 0], [0.5, 3]])
        >>> # y = 1 * x_0 + 2 * x_1 + 3
        >>> y_train = np.dot(X_train, np.array([1, 2])) + 3
        >>> # y = 1.5 * x_0 + 1.5 * x_1 + 3
        >>> y_test = np.dot(X_test, np.array([1.5, 1.5])) + 3
        >>> reg_estimator = LinearRegression()
        >>> metric_fuctions = {'R2': r2_score}
        >>> estimator_data_processor = EstimatorDataProcessor()
        >>> estimator_data_processor.get_predict_scores(reg_estimator, X_train, X_test, y_train, y_test, metric_functions)
        (LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False),
        {'Test_R2': 0.74, 'Train_R2': 1.0})
        """
        estimator.fit(X_train, y_train)
        train_scores = self.get_predict_scores(estimator, X_train, y_train, metric_functions, 'Train_', multiclass_classification)
        test_scores = self.get_predict_scores(estimator, X_test, y_test, metric_functions, 'Test_', multiclass_classification)
        return estimator, self.merge_dicts(train_scores, test_scores)

    def get_permutation_importance(self, estimator, X, y, **permutation_kwargs): # permutation_importance, permutation_n_repeats
        """
        A fucntion that gets a fitted estimator, (X, y) data points and kwargs for the permutation importance,
        The function returns ...
    
        Parameters
        ----------
        estimator : object
            An estimator object (fitted already).

        X: DataFrame
            X data points.

        y: DataFrame or Series
            The target values of the given X data.

        permutation_kwargs: kwargs
            Keywords arguments for the permutation imprortance algorithm.

        Returns
        -------

        Dictionary
            A dictionary of the permutation importance results of the given estimator with (X, y) dataset.
        
        Examples
        --------

        >>> import pandas as pd
        >>> from sklearn import datasets
        >>> from sklearn.linear_model import LinearRegression
        >>> from sklearn.model_selection import train_test_split
        >>> iris = datasets.load_iris()
        >>> X = pd.DataFrame(iris.data, columns=['feature_'+str(i) for i in range(4)])
        >>> y = pd.Series(iris.target, name='target_column')
        >>> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        >>> reg_estimator = LinearRegression().fit(X_train, y_train)
        >>> estimator_data_processor = EstimatorDataProcessor()
        >>> estimator_data_processor.get_permutation_importance(reg_estimator, X_test, y_test)
        {'Permutation importance': 'feature_3:0.74, feature_2:0.33, feature_0:0.01'}
        """
        self.assert_df(X)
        from sklearn.inspection import permutation_importance
        r = permutation_importance(estimator, X, y)
        arg_indices = r.importances_mean.argsort()[::-1][:3]
        output_str = ', '.join([feature+':'+str(round(r.importances_mean[arg_indices][index],2)) for index, feature in enumerate(X.columns[arg_indices])])
        return {'Permutation importance': output_str}

    def get_estimator_data (self, estimator, X_train, X_test, y_train, y_test, metrics, multiclass_classification=False, permutation_importance=False, **permutation_kwargs):
        """
        A fucntion that gets an estimator, (X_train, X_test, y_train, y_test) data points, a list of wanted metrics,
        and permutation importance algorithm parameters. The function tests the estimator on the given data points and
        returns a dictionary containing the metric evalution of the estimator
    
        Parameters
        ----------

        estimator: object
            An estimator object.

        X_train, X_test: DataFrame
            X data points.

        y_train, y_test: DataFrame or Series
            The target values of the given X data.

        metrics: iterable
            A list of metrics that will evaluate the estimator.

        multiclass_classification: bool, default False
            A boolean flag indicating whether this is a classification problem with multi classes or not. 

        permutation_importance: bool, default False
            A bool flag indicating whether to get permutation importance results as well or not.

        permutation kwargs: kwargs
            Keywords arguments for the permutation imprortance algorithm.

    
        Returns
        -------

        Dictionary
            A dictionary of the evalution results of the given estimator with (X_train, X_test, y_train, y_test) dataset,
            according to the requested metrics.
        
        Examples
        --------

        >>> import pandas as pd
        >>> from sklearn import datasets
        >>> from sklearn.linear_model import LinearRegression
        >>> from sklearn.model_selection import train_test_split
        >>> iris = datasets.load_iris()
        >>> X = pd.DataFrame(iris.data, columns=['feature_'+str(i) for i in range(4)])
        >>> y = pd.Series(iris.target, name='target_column')
        >>> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        >>> reg_estimator = LinearRegression()
        >>> metrics = ['R2', 'MSE']
        >>> estimator_data_processor = EstimatorDataProcessor()
        >>> estimator_data_processor.get_estimator_data(reg_estimator, X_train, X_test, y_train, y_test, metrics)
        {'Test_MSE_loss': 0.04,
         'Test_R2_score': 0.93,
         'Train_MSE_loss': 0.05,
         'Train_R2_score': 0.93,
         'feature_list': 'feature_0, feature_1, feature_2, feature_3',
         'parameters': {'copy_X': True,
         'fit_intercept': True,
         'n_jobs': None,
         'normalize': False}}
        """
        self.assert_df(X_train)
        estimator_data = {'feature_list': ', '.join(list(X_train.columns)), 'parameters': estimator.get_params()}
        metric_functions = self.interpert_metrics(metrics)
        estimator, train_test_scores = self.fit_and_score_estimator(estimator, X_train, X_test, y_train, y_test, metric_functions, multiclass_classification)
        permutation_importance_scores = self.get_permutation_importance(estimator, X_test, y_test, **permutation_kwargs) if permutation_importance else {}
        estimator_data.update(self.merge_dicts(train_test_scores, permutation_importance_scores))
        return estimator_data

    def build_and_test_estimator (self, estimator, X, y, metrics, test_size=0.2, random_state=42, multiclass_classification=False, permutation_importance=False, **permutation_kwargs):
        """
        A fucntion that gets an estimator, (X, y) data points, a list of wanted metrics,
        and permutation importance algorithm parameters. The function tests the estimator on the given data points and
        returns a dictionary containing the metric evalution of the estimator
    
        Parameters
        ----------

        estimator: object
            An estimator object.

        X: DataFrame
            X data points.

        y: DataFrame or Series
            The target values of the given X data.

        metrics: iterable
            A list of metrics that will evaluate the estimator.

        test_size: float, default 0.2
            A number that will determine the size of the train-test split.

        random_state: int, default 42
            A number that will determine the random state of the train-test split.

        multiclass_classification: bool, default False
            A boolean flag indicating whether this is a classification problem with multi classes or not. 

        permutation_importance: bool, default False
            A bool flag indicating whether to get permutation importance results as well or not.

        permutation kwargs: kwargs
            Keywords arguments for the permutation imprortance algorithm.

        Returns
        -------

        Dictionary
            A dictionary of the evalution results of the given estimator with (X, y) dataset, according to the requested metrics.
        
        Examples
        --------

        >>> import pandas as pd
        >>> from sklearn import datasets
        >>> from sklearn.linear_model import LinearRegression
        >>> iris = datasets.load_iris()
        >>> X = pd.DataFrame(iris.data, columns=['feature_'+str(i) for i in range(4)])
        >>> y = pd.Series(iris.target, name='target_column')
        >>> reg_estimator = LinearRegression()
        >>> metrics = ['R2', 'MSE']
        >>> estimator_data_processor = EstimatorDataProcessor()
        >>> estimator_data_processor.build_and_test_estimator(reg_estimator, X, y, metrics)
        {'Test_MSE_loss': 0.04,
        'Test_R2_score': 0.95,
        'Train_MSE_loss': 0.05,
        'Train_R2_score': 0.93,
        'feature_list': 'feature_0, feature_1, feature_2, feature_3',
        'parameters': {'copy_X': True,
                      'fit_intercept': True,
                      'n_jobs': None,
                      'normalize': False}}
        """
        self.assert_df(X)
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        return self.get_estimator_data(estimator, X_train, X_test, y_train, y_test, metrics, multiclass_classification, permutation_importance, **permutation_kwargs)

class ModelsDataProcessor(CorrlationAnalyzer, NewFeaturesAdder, FeaturesScaler, FeatureSelector):

    def get_model_with_max_key_parameter (self, models_data, key_parameter):
        """
        Function that is given the evaluation results of different estimators and a key parameter, 
        and returns the name of the model with the highest value in the key parameter.
    
        Parameters
        ----------

        models_data : dictionary
            A dictioniary contianing the evaluation results of multiple estimators, where the keys are the name of the model, and the values are dictionaries
            with the evaluation results.

        key_parameter: str
            A str that is one of the keys in the inner dictionary. This will that parameter that this function will compare between each model in the models_data.
 
        Returns
        -------

        String
            The name of the models with highest value in the key parameter.
        
        Examples
        --------

        >>> estimator_data_processor=EstimatorDataProcessor()
        >>> models_data_processor=ModelsDataProcessor()
        >>> import pandas as pd
        >>> from sklearn import datasets
        >>> from sklearn.ensemble import RandomForestClassifier
        >>> from sklearn.tree import DecisionTreeClassifier
        >>> from sklearn.neighbors import KNeighborsClassifier
        >>> from sklearn.svm import SVC
        >>> iris = datasets.load_iris()
        >>> X=pd.DataFrame(iris.data, columns=['feature_'+str(i) for i in range(4)]).drop(['feature_2', 'feature_3'], axis=1)
        >>> y=pd.Series(iris.target, name='target_column')
        >>> estimators={'Random_tree': RandomForestClassifier(),
                        'Decision_tree': DecisionTreeClassifier(),
                        'N_neighbors': KNeighborsClassifier(),
                        'SVC': SVC()}
        >>> models_data={estimator_name: estimator_data_processor.build_and_test_estimator(estimator, X, y, ['recall', 'precision', 'f1'], multiclass_classification=True) for estimator_name, estimator in estimators.items()}
        >>> models_data_processor.get_model_with_max_key_parameter(models_data, 'Test_f1_score')
        'SVC'
        """
        for index, (model_name, model_data) in enumerate(models_data.items()):
            current_value = model_data.get(key_parameter)
            if index == 0:
                self.assert_value_is_allowed(key_parameter, model_data.keys())
                max_value, best_model_name = current_value, model_name
            if current_value > max_value:
                max_value, best_model_name = current_value, model_name
        return best_model_name

    def get_model_with_min_key_parameter (self, models_data, key_parameter):
        """
        Function that is given the evaluation results of different estimators and a key parameter, 
        and returns the name of the model with the lowest value in the key parameter.
    
        Parameters
        ----------

        models_data : dictionary
            A dictioniary contianing the evaluation results of multiple estimators, where the keys are the name of the model, and the values are dictionaries
            with the evaluation results.

        key_parameter: str
            A str that is one of the keys in the inner dictionary. This will that parameter that this function will compare between each model in the models_data.
 
        Returns
        -------

        String
            The name of the models with lowest value in the key parameter.
        
        Examples
        --------

        >>> estimator_data_processor=EstimatorDataProcessor()
        >>> models_data_processor=ModelsDataProcessor()
        >>> import pandas as pd
        >>> from sklearn import datasets
        >>> from sklearn.ensemble import RandomForestClassifier
        >>> from sklearn.tree import DecisionTreeClassifier
        >>> from sklearn.neighbors import KNeighborsClassifier
        >>> from sklearn.svm import SVC
        >>> iris=datasets.load_iris()
        >>> X=pd.DataFrame(iris.data, columns=['feature_'+str(i) for i in range(4)]).drop(['feature_2', 'feature_3'], axis=1)
        >>> y=pd.Series(iris.target, name='target_column')
        >>> estimators={'Random_tree': RandomForestClassifier(),
                        'Decision_tree': DecisionTreeClassifier(),
                        'N_neighbors': KNeighborsClassifier(),
                        'SVC': SVC()}
        >>> models_data={estimator_name: estimator_data_processor.build_and_test_estimator(estimator, X, y, ['recall', 'precision', 'f1'], multiclass_classification=True) for estimator_name, estimator in estimators.items()}
        >>> models_data_processor.get_model_with_min_key_parameter(models_data, 'Test_f1_score')
        'Decision_tree'
        """
        for index, (model_name, model_data) in enumerate(models_data.items()):
            current_value = model_data.get(key_parameter)
            if index == 0:
                self.assert_value_is_allowed(key_parameter, model_data.keys())
                min_value, best_model_name = current_value, model_name
            if current_value < min_value:
                min_value, best_model_name = current_value, model_name
        return best_model_name

    def get_n_best_models(self, models_data, selected_metric, prefix='Test_', num_of_results=3):
        """
        Function that is given the evaluation results of different estimators and a key parameter, 
        and returns names of the best model with the optimum value in the selected_metric.
    
        Parameters
        ----------

        models_data : dictionary
            A dictioniary contianing the evaluation results of multiple estimators, where the keys are the name of the model, and the values are dictionaries
            with the evaluation results.

        selected_metric: str
            A str that when concatenated with the prefix is one of the keys in the inner dictionary. This will that parameter that this function will compare between each model in the models_data.
            If the selected metric ends with '_score' the optimum goal will be max value and if it ends with '_loss' the goal will be min value

        prefix: str, default 'Test_'
            A str that will be concatenated with the selected metric in order to get the exact key in the inner dictionary.

        num_of_results: int, default 3
            The number of models that will be returned
 
        Returns
        -------

        List
            A list of the model names with the optimum values in the selected metric.
        
        Examples
        --------

        >>> estimator_data_processor=EstimatorDataProcessor()
        >>> models_data_processor=ModelsDataProcessor()
        >>> import pandas as pd
        >>> from sklearn import datasets
        >>> from sklearn.ensemble import RandomForestClassifier
        >>> from sklearn.tree import DecisionTreeClassifier
        >>> from sklearn.neighbors import KNeighborsClassifier
        >>> from sklearn.svm import SVC
        >>> iris=datasets.load_iris()
        >>> X=pd.DataFrame(iris.data, columns=['feature_'+str(i) for i in range(4)]).drop(['feature_2', 'feature_3'], axis=1)
        >>> y=pd.Series(iris.target, name='target_column')
        >>> estimators={'Random_tree': RandomForestClassifier(),
                        'Decision_tree': DecisionTreeClassifier(),
                        'N_neighbors': KNeighborsClassifier(),
                        'SVC': SVC()}
        >>> models_data={estimator_name: estimator_data_processor.build_and_test_estimator(estimator, X, y, ['recall', 'precision', 'f1'], multiclass_classification=True) for estimator_name, estimator in estimators.items()}
        >>> models_data_processor.get_n_best_models(models_data, 'f1_score', num_of_results=2)
        ['SVC', 'Random_tree']
        """
        best_models_names = []
        temp_models_data = models_data.copy()
        for index in range(min(num_of_results, len(models_data))):
            if selected_metric.split('_')[-1] == 'score':
                current_best_model_name = self.get_model_with_max_key_parameter(temp_models_data, prefix+selected_metric)
            elif selected_metric.split('_')[-1] == 'loss':
                current_best_model_name = self.get_model_with_min_key_parameter(temp_models_data, prefix+selected_metric)
            best_models_names.append(current_best_model_name)
            del temp_models_data[current_best_model_name]
        return best_models_names

    def models_data_to_df (self, models_data, models_list, selected_keys, feature_list_as_dummies=False):
        """
        Function that is given the evaluation results of different estimators, a list of models names to present, and a list of keys, 
        and returns a dataframe representation of the models with the selected keys as columns.
    
        Parameters
        ----------

        models_data: dictionary
            A dictioniary contianing the evaluation results of multiple estimators, where the keys are the name of the model, and the values are dictionaries
            with the evaluation results.

        models_list: list
            A list of selected models (sub group of models_data keys) that will be included in the dataframe.

        selected_keys: list
            A list of selected keys (sub group of the inner dictionary keys) that will be presented as columns in the dataframe.
        
        feature_list_as_dummies: bool, defualt False
            A boolean indicator. if True the 'feature_list' componant of the dataframe will be broken down into dummy columns in the dataframe.
 
        Returns
        -------

        Dataframe
            A dataframe of the selected models with the selected keys as columns.
        
        Examples
        --------

        >>> estimator_data_processor=EstimatorDataProcessor()
        >>> models_data_processor=ModelsDataProcessor()
        >>> import pandas as pd
        >>> from sklearn import datasets
        >>> from sklearn.ensemble import RandomForestClassifier
        >>> from sklearn.tree import DecisionTreeClassifier
        >>> from sklearn.neighbors import KNeighborsClassifier
        >>> from sklearn.svm import SVC
        >>> iris=datasets.load_iris()
        >>> X=pd.DataFrame(iris.data, columns=['feature_'+str(i) for i in range(4)]).drop(['feature_2', 'feature_3'], axis=1)
        >>> y=pd.Series(iris.target, name='target_column')
        >>> estimators={'Random_tree': RandomForestClassifier(),
                        'Decision_tree': DecisionTreeClassifier(),
                        'N_neighbors': KNeighborsClassifier(),
                        'SVC': SVC()}
        >>> models_data={estimator_name: estimator_data_processor.build_and_test_estimator(estimator, X, y, ['recall', 'precision', 'f1'], multiclass_classification=True) for estimator_name, estimator in estimators.items()}
        >>> best_models_names=models_data_processor.get_n_best_models(models_data, 'f1_score', num_of_results=2)
        >>> selected_keys=list(models_data['SVC'].keys())
        >>> models_data_processor.models_data_to_df(models_data, best_models_names, selected_keys)
        	        feature_list	        parameters	                                        Train_recall_score	Train_precision_score	...
        SVC	        feature_0, feature_1	{'C': 1.0, 'break_ties': False, 'cache_size': ...	0.78	            0.78	                ...
        Random_tree	feature_0, feature_1	{'bootstrap': True, 'ccp_alpha': 0.0, 'class_w...	0.94	            0.94                    ...
        """
        import pandas as pd
        temp_list = []
        basic_keys = ['feature_list', 'Permutation importance']
        for model_name in models_list:
            temp_dict = {key: value for key, value in models_data.get(model_name).items() if key in selected_keys+basic_keys}
            temp_list.append(temp_dict)
        result_df = pd.DataFrame(temp_list, index=models_list)
        if feature_list_as_dummies:
            result_df = pd.concat([result_df.drop(['feature_list'], axis=1), result_df['feature_list'].str.get_dummies(sep=', ')], axis = 1)
        return result_df

# level 4 - finished documentation


class FeatureIterator(EstimatorDataProcessor, ModelsDataProcessor):
    
    def iterate_features(self, estimator, df, target_column, metrics , min_features_num=1, max_features_num=1, model_name_prefix='feature_iterator',
                         test_size=0.2, random_state=42, multiclass_classification=False, permutation_importance=False, **permutation_kwargs):
        """
        Function that is given an estimator, a dataframe, a target value and metrics.
        The function iterates over the different features combinations as set by the min_features_num and max_features_num,
        and returns the evaluation results of different features combinations based on the given metrics.
    
        Parameters
        ----------

        estimator: object
            An estimator object.

        X: DataFrame
            X data points.

        y: DataFrame or Series
            The target values of the given X data.

        metrics: iterable
            A list of metrics that will evaluate the estimator.

        model_name_prefix: str default 'feature_iterator'
            A string that will the start of every model name in the result models_data

        test_size: float, default 0.2
            A number that will determine the size of the train-test split.

        random_state: int, default 42
            A number that will determine the random state of the train-test split.

        multiclass_classification: bool, default False
            A boolean flag indicating whether this is a classification problem with multi classes or not. 

        permutation_importance: bool, default False
            A bool flag indicating whether to get permutation importance results as well or not.

        permutation_kwargs: kwargs
            Keywords arguments for the permutation imprortance algorithm. 
 
        Returns
        -------

        Dictionary
            A dictionary containing the evalution results of the different models tested by this function.


        Examples
        --------

        >>> feature_iterator=FeatureIterator()
        >>> import pandas as pd
        >>> from sklearn import datasets
        >>> from sklearn.svm import SVC
        >>> iris=datasets.load_iris()
        >>> X=pd.DataFrame(iris.data, columns=['feature_'+str(i) for i in range(4)])
        >>> y=pd.Series(iris.target, name='target_column')
        >>> estimator=SVC()
        >>> models_data=feature_iterator.iterate_features(estimator, X, y, ['recall', 'precision', 'f1'],
                                                          min_features_num=1,
                                                          max_features_num=4,
                                                          random_state=0,
                                                          multiclass_classification=True)
        >>> best_models_names=feature_iterator.get_n_best_models(models_data, 'f1_score', num_of_results=6)
        >>> selected_keys=list(list(models_data.values())[0].keys())
        >>> feature_iterator.models_data_to_df(models_data, best_models_names, selected_keys)
        	                    feature_list	                parameters	                        Train_recall_score	...
        feature_iterator_2_0	feature_2, feature_3	        {'C': 1.0, 'break_ties': False, ...	0.96	            ...
        feature_iterator_3_1	feature_0, feature_1, feature_2	{'C': 1.0, 'break_ties': False, ...	0.96	            ...
        feature_iterator_3_2	feature_0, feature_2, feature_3	{'C': 1.0, 'break_ties': False, ...	0.97	            ...
        feature_iterator_3_3	feature_1, feature_2, feature_3	{'C': 1.0, 'break_ties': False, ...	0.97	            ...
        feature_iterator_1_2	feature_3	                    {'C': 1.0, 'break_ties': False, ...	0.96	            ...
        feature_iterator_1_3	feature_2	                    {'C': 1.0, 'break_ties': False, ...	0.95	            ...
        """
        from itertools import combinations
        models_data = {}
        loop_range = self.build_loop_range (min_features_num, max_features_num, 'feature number must be integer') 
        for features_num in loop_range:
            possible_features = set(combinations(df.columns, features_num))
            for inner_index, selected_features in enumerate(possible_features):
                model_name = model_name_prefix+'_'+str(features_num)+'_'+str(inner_index)
                models_data[model_name] = self.build_and_test_estimator(estimator, df[list(selected_features)], target_column, metrics,
                                                                        test_size=test_size,
                                                                        random_state=random_state,
                                                                        multiclass_classification=multiclass_classification, 
                                                                        permutation_importance=permutation_importance, 
                                                                        **permutation_kwargs)
        return models_data

class HyperparameterTuner (EstimatorDataProcessor, ModelsDataProcessor):

    def tune_hyperparameters(self, estimator, df, target_column, metrics, parameters_to_tune, model_name_prefix = 'hyperparameter_tuner',
                             test_size=0.2, random_state=42, multiclass_classification=False, permutation_importance=False, **permutation_kwargs):
        """
        Function that is given an estimator, a dataframe, a target value and metrics, and a set of parameters to tune in the estimator.
        The function iterates over the different given parameters, and returns the evaluation results based on the given metrics.
    
        Parameters
        ----------

        estimator: object
            An estimator object.

        X: DataFrame
            X data points.

        y: DataFrame or Series
            The target values of the given X data.

        metrics: iterable
            A list of metrics that will evaluate the estimator.

        parameter_to_tune: dictionary
            A dictionary with parameters names (str) as keys and lists of parameter settings to try as values.

        model_name_prefix: str default 'hyperparameter_tuner'
            A string that will the start of every model name in the result models_data

        test_size: float, default 0.2
            A number that will determine the size of the train-test split.

        random_state: int, default 42
            A number that will determine the random state of the train-test split.

        multiclass_classification: bool, default False
            A boolean flag indicating whether this is a classification problem with multi classes or not. 

        permutation_importance: bool, default False
            A bool flag indicating whether to get permutation importance results as well or not.

        permutation_kwargs: kwargs
            Keywords arguments for the permutation imprortance algorithm. 
 
        Returns
        -------

        Dictionary
            A dictionary containing the evalution results of the different models tested by this function.


        Examples
        --------

        >>> hyperparameter_tuner=HyperparameterTuner()
        >>> import pandas as pd
        >>> from sklearn import datasets
        >>> from sklearn.svm import SVC
        >>> iris=datasets.load_iris()
        >>> X=pd.DataFrame(iris.data, columns=['feature_'+str(i) for i in range(4)]).drop(['feature_2', 'feature_3'], axis=1)
        >>> y=pd.Series(iris.target, name='target_column')
        >>> estimator=SVC()
        >>> parameters_to_tune={'kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
                                'C': [0.1, 1, 10, 100]}
        >>> models_data=hyperparameter_tuner.tune_hyperparameters(estimator, X, y, ['recall', 'precision', 'f1'], parameters_to_tune,
                                                                  random_state=0,
                                                                  multiclass_classification=True)
        >>> best_models_names=hyperparameter_tuner.get_n_best_models(models_data, 'f1_score', num_of_results=6)
        >>> selected_keys=list(list(models_data.values())[0].keys())
        >>> hyperparameter_tuner.models_data_to_df(models_data, best_models_names, selected_keys)
	                            feature_list	        parameters	                                        Train_recall_score	...
        hyperparameter_tuner_2	feature_0, feature_1	{'C': 10, 'break_ties': False, 'cache_size': 2...	0.83                ...
        hyperparameter_tuner_0	feature_0, feature_1	{'C': 0.1, 'break_ties': False, 'cache_size': ...	0.85	            ...
        hyperparameter_tuner_1	feature_0, feature_1	{'C': 1, 'break_ties': False, 'cache_size': 20...	0.84	            ...
        hyperparameter_tuner_3	feature_0, feature_1	{'C': 100, 'break_ties': False, 'cache_size': ...	0.83	            ...
        hyperparameter_tuner_4	feature_0, feature_1	{'C': 0.1, 'break_ties': False, 'cache_size': ...	0.84	            ...
        hyperparameter_tuner_5	feature_0, feature_1	{'C': 1, 'break_ties': False, 'cache_size': 20...	0.84	            ...
        """
        from itertools import product
        parameter_matrix = product(*parameters_to_tune.values())
        models_data = {}
        for inner_index, parameters in enumerate(parameter_matrix):
            current_parameters = dict(zip(parameters_to_tune.keys() ,parameters))
            tuned_estimator = self.set_attributes(estimator, **current_parameters)
            model_name = model_name_prefix+'_'+str(inner_index)
            models_data[model_name] = self.build_and_test_estimator(tuned_estimator, df, target_column, metrics,
                                                                    test_size=test_size,
                                                                    random_state=random_state,
                                                                    multiclass_classification=multiclass_classification, 
                                                                    permutation_importance=permutation_importance, 
                                                                   **permutation_kwargs)
        return models_data

class EstimatorIterator(EstimatorDataProcessor, ModelsDataProcessor):
    
    def iterate_estimators(self, estimators, df, target_column, metrics,
                           test_size=0.2, random_state=42, multiclass_classification=False, permutation_importance=False, **permutation_kwargs):
        """
        Function that is given a number of estimator, a dataframe, a target value and metrics, and the evaluation results of different estimator based on the given metrics.
    
        Parameters
        ----------

        estimators: dictionary
            A dictionary of estimator that this function will test. The keys of this dictionary will be resulting names (keys) of the models, 
            and the values are estimators that the model will test

        X: DataFrame
            X data points.

        y: DataFrame or Series
            The target values of the given X data.

        metrics: iterable
            A list of metrics that will evaluate the estimator.

        test_size: float, default 0.2
            A number that will determine the size of the train-test split.

        random_state: int, default 42
            A number that will determine the random state of the train-test split.

        multiclass_classification: bool, default False
            A boolean flag indicating whether this is a classification problem with multi classes or not. 

        permutation_importance: bool, default False
            A bool flag indicating whether to get permutation importance results as well or not.

        permutation_kwargs: kwargs
            Keywords arguments for the permutation imprortance algorithm. 
 
        Returns
        -------

        Dictionary
            A dictionary containing the evalution results of the different models tested by this function.
        
        Examples
        --------

        >>> estimator_iterator=EstimatorIterator()
        >>> import pandas as pd
        >>> from sklearn import datasets
        >>> from sklearn.svm import SVC
        >>> from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
        >>> from sklearn.tree import DecisionTreeClassifier
        >>> from sklearn.neighbors import KNeighborsClassifier
        >>> iris=datasets.load_iris()
        >>> X=pd.DataFrame(iris.data, columns=['feature_'+str(i) for i in range(4)])
        >>> y=pd.Series(iris.target, name='target_column')
        >>> estimators={'SVC': SVC(),
                        'Random forest': RandomForestClassifier(),
                        'Gradient boosting': GradientBoostingClassifier(),
                        'Ada boosting': AdaBoostClassifier(),
                        'Decision Tree': DecisionTreeClassifier(),
                        'K nearest neighbors': KNeighborsClassifier()}
        >>> models_data=estimator_iterator.iterate_features(estimators, X, y, ['recall', 'precision', 'f1'],
                                                            random_state=0,
                                                            multiclass_classification=True)
        >>> best_models_names=estimator_iterator.get_n_best_models(models_data, 'f1_score', num_of_results=6)
        >>> selected_keys=list(list(models_data.values())[0].keys())
        >>> estimator_iterator.models_data_to_df(models_data, best_models_names, selected_keys)
                            feature_list	                            parameters	                                        Train_recall_score	...
        SVC	                feature_0, feature_1, feature_2, feature_3	{'C': 1.0, 'break_ties': False, 'cache_size': ...	0.96                ...
        Gradient boosting	feature_0, feature_1, feature_2, feature_3	{'ccp_alpha': 0.0, 'criterion': 'friedman_mse'...	1.00	            ...
        Decision Tree	    feature_0, feature_1, feature_2, feature_3	{'ccp_alpha': 0.0, 'class_weight': None, 'crit...	1.00	            ...
        Random forest	    feature_0, feature_1, feature_2, feature_3	{'bootstrap': True, 'ccp_alpha': 0.0, 'class_w...	1.00	            ...
        Ada boosting	    feature_0, feature_1, feature_2, feature_3	{'algorithm': 'SAMME.R', 'base_estimator': Non...	0.96	            ...
        K nearest neighbors	feature_0, feature_1, feature_2, feature_3	{'algorithm': 'auto', 'leaf_size': 30, 'metric...	0.95	            ...
        """
        models_data = {}
        for model_name, estimator in estimators.items():
            models_data[model_name] = self.build_and_test_estimator(estimator, df, target_column, metrics,
                                                                    test_size=test_size,
                                                                    random_state=random_state,
                                                                    multiclass_classification=multiclass_classification, 
                                                                    permutation_importance=permutation_importance, 
                                                                    **permutation_kwargs)
        return models_data

# an estimator optimization tool(obj) contains several functions that are aimed at choosing features
# for a reg_model (provided) from the entire dataset. the main output of this tool is a
# dictionary called models_data that provides data about all models ran by the tool.
# a viewing function is also inculded for easy inspection in dataframe format

class EstimatorOptimizer (EstimatorIterator, FeatureIterator, HyperparameterTuner):
    def __init__(self):
        pass
            
    def get_new_df(self, df, target_column,
                   opt_instructions={'add_new_features': {'interaction': [], 'polynomial': [], 'fitted': [], 'group_mean': [], 'datetime': []},
                                     'scale_features': {'normalize': [], 'min_max': [], 'onehot': []},
                                     'select_features': {'k_best': {'k': 10}}}  
                                     ):
        new_df=df.copy()
        for opt_step, opt_step_instructions in opt_instructions.items():
            if opt_step in ('add_new_features', 'scale_features', 'select_features'):
                new_df=getattr(self, opt_step)(opt_step_instructions, new_df, target_column)
        return new_df

    def iterate_and_tune(self, estimator, df, target_column, metrics , min_features_num=1, max_features_num=1, num_models_to_tune=1, parameters_to_tune={},
                         test_size=0.2, random_state=42, multiclass_classification=False, permutation_importance=False, *_):
        # leading metric is metrics[0]
        feature_iteration_models_data=self.iterate_features(estimator, df, target_column, metrics , min_features_num, max_features_num, 'iterate_features',
                                                            test_size, random_state, multiclass_classification, permutation_importance)
        best_models_names=self.get_n_best_models(feature_iteration_models_data, self.correct_metric_name(metrics[0]), num_of_results=num_models_to_tune)
        best_models_feature_lists=[[feature_iteration_models_data.get(model_name).get('feature_list')] for model_name in best_models_names]
        tune_hyperparameters_models_data_list=[self.tune_hyperparameters(estimator, df[feature_list], target_column, metrics, parameters_to_tune, 'iterate_and_tune'+str(inner_index), 
                                                                         test_size, random_state, multiclass_classification, permutation_importance) for inner_index, feature_list in enumerate(best_models_feature_lists)]
        models_data=self.merge_dicts(feature_iteration_models_data, *tune_hyperparameters_models_data_list)   
        return models_data


    def find_opt_model(self, estimator, df, target_column,
                       opt_instructions={'add_new_features': {'interaction': [], 'polynomial': [], 'fitted': [], 'group_mean': [], 'datetime': []},
                                         'scale_features': {'normalize': [], 'min_max': [], 'onehot': []},
                                         'select_features': {'k_best': {'k': 10}},
                                         'iterate_estimators': {'metrics': ('f1', 'recall', 'precision'), 'estimators': [],
                                                                'test_size': 0.2, 'random_state':42, 'multiclass_classification': False, 'permutation_importance': False},
                                         'iterate_features': {'metrics': ('f1', 'recall', 'precision'), 'min_features_num': 1, 'max_features_num': 1,
                                                              'test_size': 0.2, 'random_state':42, 'multiclass_classification': False, 'permutation_importance': False},
                                         'tune_hyperparameters': {'metrics': ('f1', 'recall', 'precision'), 'parameters_to_tune': {},
                                                                  'test_size': 0.2, 'random_state':42, 'multiclass_classification': False, 'permutation_importance': False},
                                         'iterate_and_tune': {'metrics': ('f1', 'recall', 'precision'), 'min_features_num': 1, 'max_features_num': 1, 'num_models_to_tune': 1, 'parameters_to_tune': {},
                                                              'test_size': 0.2, 'random_state':42, 'multiclass_classification': False, 'permutation_importance': False}
                                         },
                       leading_metric='f1',
                       num_of_results=3,
                       present_results_as_df=True,
                       feature_list_as_dummies=False):
        new_df = df.copy()
        for opt_step, opt_step_instructions in opt_instructions.items():
            if opt_step in ('add_new_features', 'scale_features', 'select_features'):
                new_df=getattr(self, opt_step)(opt_step_instructions, new_df, target_column)

            if opt_step == 'iterate_estimators':
                pass
                # models_data=self.iterate_estimators()

            if opt_step == 'iterate_features':
                models_data=self.iterate_features(estimator, new_df, target_column,
                                                  **opt_step_instructions)
            if opt_step == 'tune_hyperparameters':
                models_data=self.tune_hyperparameters(estimator, new_df, target_column,
                                                      **opt_step_instructions)
            if opt_step == 'iterate_and_tune':
                models_data=self.iterate_and_tune(estimator, new_df, target_column,
                                                  **opt_step_instructions)

        best_models_names = self.get_n_best_models(models_data, self.correct_metric_name(leading_metric), num_of_results=num_of_results)
        selected_keys=list(list(models_data.values())[0].keys())
        if present_results_as_df:
            return self.models_data_to_df(models_data, best_models_names, selected_keys)
        else:
            return {model_name: model_data for model_name, model_data in models_data.items() if model_name in best_models_names} 
        # best_models_names = []
        # for opt_metric in selected_metrics:
        #     best_models_names = best_models_names + self.get_n_best_models(models_data, opt_metric, num_of_results)
        # best_models_names = set(best_models_names)
        # if present_results_as_df:
        #     return self.models_data_to_df(models_data, best_models_names, selected_keys, feature_list_as_dummies)
        # else:
        #     return {model_name: model_data for model_name, model_data in models_data.items() if model_name in best_models_names}
