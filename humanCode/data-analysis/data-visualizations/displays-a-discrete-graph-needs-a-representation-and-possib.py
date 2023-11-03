import networkx
import matplotlib

g = networkx.fast_gnp_random_graph(10, .3)
networkx.draw(g)

matplotlib.pyplot.show()
