import importlib

import numpy as np

from moutils.visualization import Plot


class ScatterPlot(Plot):

    def __init__(self, **kwargs):
        """ Shows a scatter plot in a 2D-3D space.
        """
        super().__init__(**kwargs)

    def plot(self, values: np.array, **kwargs):
        """ Initialize a figure to plot data in 2D or 3D space.
        """
        self.initialize()

        self.n_dim = values.shape[0]
        if self.n_dim == 2:
            self._two_dim(values)
        else:
            self._three_dim(values)

    def add(self, values: np.array, **kwargs) -> None:
        """ Append values to figure.

        :param values: Data point(s).
        :type values: ``np.array``
        :key label: ``str`` -- Axis label (defaults to ``None``).
        :key color: ``str`` -- Point(s) color (defaults to ``default_color``).
        :key axline: ``bool`` -- Show or hide the axis lines for single points in 2D space (defaults to ``False``).
        """
        assert self._figure, \
            AssertionError('figure has not been initialized')
        assert self.n_dim == values.shape[0], \
            AttributeError('input values\' dimension does not match to current figure')

        # keyword arguments
        label = kwargs.get('label', None)
        color = kwargs.get('color', self.default_color)
        axline = kwargs.get('axline', False)

        # get current axis
        ax = self._figure.gca()

        if self.n_dim == 2:
            ax.scatter(values[0], values[1], color=color, label=label)

            if axline:
                ax.axvline(x=values[0], color=color, linestyle=':')
                ax.axhline(y=values[1], color=color, linestyle=':')
        else:
            ax.scatter(values[0, :], values[1, :], values[2, :], color=color, label=label)
            # todo Add axlines

        # activate legend
        self._figure.legend(loc=1)

    def _two_dim(self, values: np.array) -> None:
        """ Scatter plot matrix in 2D space.
        """
        ax = self._figure.gca()
        ax.scatter(values[0, :], values[1, :], color=self.default_color, label='front')
        ax.set_title(self.subtitle)

    def _three_dim(self, values: np.array) -> None:
        """ Scatter plot matrix in 3D space.
        """
        # this import registers the 3D projection, but is otherwise unused
        importlib.import_module("mpl_toolkits.mplot3d")

        ax = self._figure.gca(projection='3d')
        ax.scatter(values[0, :], values[1, :], values[2, :], color=self.default_color, label='front')
        ax.set_title(self.subtitle)

    def show(self):
        """ Shows the current figure.
        """
        self._figure.show()

    def save(self, filename: str, output_format: str = 'eps'):
        """ Saves the current figure to a file.
        """
        self._figure.savefig(f'{filename}.{output_format}', format=output_format, dpi=1000)


if __name__ == '__main__':
    # initialize the figure
    scatter = ScatterPlot(title='my title', subtitle='my subtitle')

    # 2D
    scatter.plot(values=np.array([[1.0, 2.0, 1.0], [2.1, 1.4, 2.4]]))
    scatter.add(np.array([[1.2], [0.2]]), label='reference point', axline=True)
    scatter.add(np.array([[0.2, 0.1], [1.4, 3.5]]), label='reference front', color='y')
    scatter.show()

    # 3D
    scatter.plot(values=np.array([[1.0, 3.0], [2.1, 3.3], [2.4, 1.3]]))
    scatter.add(np.array([[1.2], [0.2], [3.2]]), label='reference point', axline=True)
    scatter.add(np.array([[0.2, 0.1], [1.4, 3.5], [1.2, 3.2]]), label='reference front', color='y')
    scatter.show()

    # save file
    #scatter.save('example', output_format='png')