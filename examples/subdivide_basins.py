import autocatchments as ac
import matplotlib.pyplot as plt

"""Takes a DEM (cairngorms_topo.asc) and automatically subdivides it into subcatchments 
greater than 5e8 m2 in area. Outputs the sample sites and subcatchments to specified folder"""

print("Loading in topographic data...")
path_to_topo = "inputs/cairngorms_topo.asc"
path_to_d8 = "inputs/thames_d8.nc"
area_per_basin = 5e8
mg = ac.toolkit.load_topo(path_to_topo) 
# mg = ac.toolkit.load_d8(path_to_d8) # Can also use a D8 file
ac.toolkit.viz_drainage_area(mg)
plt.show()
sample_nodes_catchments = ac.autosampler.get_sample_nodes_by_area(mg, area_per_basin)
localities, node_map = ac.autosampler.process_output_dict(sample_nodes_catchments, mg)
ac.autosampler.save_autosampler_results(localities, node_map, mg, "outputs")
ac.autosampler.viz_sample_site_results(localities, node_map, mg)
plt.show()