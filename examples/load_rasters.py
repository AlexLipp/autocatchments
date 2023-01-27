import autocatchments.toolkit as tk
from matplotlib.pyplot import show
# Load an ESRI D8 raster
mg = tk.load_d8("inputs/thames_d8.nc")
tk.viz_drainage_area(mg)
show()

# Load a DEM
mg = tk.load_topo("inputs/cairngorms_topo.asc")
tk.viz_drainage_area(mg)
show()