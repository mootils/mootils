import numpy as np
import pandas as pd
from pandas.plotting import parallel_coordinates

from moutils.visualization import Plot


class ParallelCoordinates(Plot):

    def __init__(self, **kwargs):
        """ Shows a parallel coordinates plot for high dimensional spaces.
        """
        super().__init__(**kwargs)

    def plot(self, values: np.array, **kwargs):
        """ Generate the parallel coordinates plot. Each solution is represented as a polyline with
        vertices on the axes, while each vertical line represents to that objective value. """
        self.initialize()

        # keyword arguments
        axis_labels = kwargs.get('axis_labels', None)
        normalize = kwargs.get('normalize', False)

        self.n_dim = values.shape[0]

        # transform data to frame
        #  the first column will be used as class column, and thus will not be shown in the plot
        values = np.insert(values, 0, np.arange(self.n_dim), axis=1)
        points = pd.DataFrame(values)

        # configure axis labels
        if axis_labels:
            try:
                axis_labels.insert(0, 'class_column')
                points.columns = axis_labels
            except ValueError:
                raise AttributeError(f'parameter axis_labels must contains exactly {values.shape[1] - 1} elements')

        # normalize every axis to [0,1]
        if normalize:
            points = (points - points.min()) / (points.max() - points.min())

        ax = self._figure.gca()
        parallel_coordinates(points, class_column='class_column', ax=ax, color='#236FA4')

        ax.get_legend().remove()

    def show(self):
        """ Shows the current figure.
        """
        self._figure.show()

    def save(self, filename: str, output_format: str = 'eps'):
        """ Saves the current figure to a file.
        """
        self._figure.savefig(f'{filename}.{output_format}', format=output_format, dpi=1000)


if __name__ == '__main__':
    pcp = ParallelCoordinates(title='my title', subtitle='my subtitle')
    pcp.plot(values=np.array([[1.0, 3.0, 3.2], [2.1, 3.3, 4.3], [2.4, 2.1, 2.1], [2.1, 2.3, 4.2]]),
             axis_labels=['f1', 'f2', 'f3'],
             normalize=True)
    pcp.show()
