import autocatchments.toolkit as tk
from matplotlib.pyplot import show
# Load an ESRI D8 raster
mg = tk.load_d8("inputs/thames_d8.nc")
tk.viz_drainage_area(mg)
show()

# Load from arrays of ordered nodes. 
# Twice as fast but requires xy spacing
# and lower left to be manually specified

# mg = tk.load_from_node_arrays(
#     path_to_receiver_nodes="thames_receiver_nodes.txt",
#     path_to_ordered_nodes="thames_ordered_nodes.txt",
#     shape=(1001,1001),
#     xy_of_lower_left=(319975.0, 79975.0),
#     xy_spacing= (50,50)
# )
# tk.viz_drainage_area(mg)
# show()

# Load a DEM
mg = tk.load_topo("inputs/cairngorms_topo.asc")
tk.viz_drainage_area(mg)
show()
