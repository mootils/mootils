from matplotlib import pyplot as plt


class Plot:

    def __init__(self,
                 title: str = '',
                 subtitle: str = '',
                 font: str = 'serif',
                 fontsize: int = 16,
                 default_color: str = '#236FA4',
                 **kwargs):
        """
        :param title: Title of the graph.
        :param subtitle: Subtitle of the graph.
        """
        self.title = title
        self.subtitle = subtitle

        self.font = font
        self.fontsize = fontsize
        self.default_color = default_color

        self.n_dim = 0

        # matplotlib classes
        self._figure = None

    def initialize(self):
        """ Creates an empty figure.
        """
        self._figure = plt.figure()
        self._figure.suptitle(self.title, fontsize=self.fontsize)

        # change the font of plots
        plt.rc('font', family=self.font)

    @property
    def fig(self):
        return self._figure

