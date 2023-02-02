import autocatchments as ac
import matplotlib.pyplot as plt

"""Takes a DEM (cairngorms_topo.asc) and automatically subdivides it into subcatchments 
greater than 5e8 m2 in area. Outputs the identified sample sites and subcatchments 
to specified folder ('outputs') as 'optimal_sample_sites.csv' and 'optimal_area_IDs.asc' respectively."""

print("Loading in topographic data...")
path_to_topo = "inputs/cairngorms_topo.asc"
area_per_basin = 5e8
mg = ac.toolkit.load_topo(path_to_topo) # Can also load direct from a D8 file see 'load_d8'
ac.toolkit.viz_drainage_area(mg)
plt.show()

sample_nodes_catchments = ac.autosampler.get_sample_nodes_by_area(mg, area_per_basin)
localities, node_map = ac.autosampler.process_output_dict(sample_nodes_catchments, mg)
ac.autosampler.save_autosampler_results(localities, node_map, mg, "outputs")
ac.autosampler.viz_sample_site_results(localities, node_map, mg)
plt.show()