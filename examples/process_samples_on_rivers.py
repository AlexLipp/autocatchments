import autocatchments as ac
import matplotlib.pyplot as plt

"""Takes a D8 grid and a list of sample sites (samples_thames.csv) and aligns the sample sites
to nodes on the DEM which have a drainage network greater than given threshold. Can be a bit slow"""

path_to_d8 = "inputs/thames_d8.nc"
path_to_samples = "inputs/samples_thames.csv"
catchment_threshold = 1e7
print("Loading in topographic data...")
mg = ac.toolkit.load_d8(path_to_d8)

sample_names, sample_sites = ac.autosampler.load_sample_data(path_to_samples)
ac.toolkit.viz_drainage_area(mg)
plt.scatter(x=sample_sites[:,0],y=sample_sites[:,1],c='red')
plt.show()

print("Snapping to drainage")
snapped_localities = ac.autosampler.snap_to_drainage(mg, sample_sites, catchment_threshold)
target_nodes = ac.autosampler.coords_to_node_ids(mg, snapped_localities)
print("Getting unique subcatchments")
sub_catchment_dict = ac.autosampler.get_subcatchments(mg, target_nodes, sample_names)
catchment_map = ac.autosampler.get_subcatchment_map(mg, sub_catchment_dict)

ac.autosampler.save_subcatchments(mg, sub_catchment_dict, catchment_map, "outputs")

plt.title("Subcatchments: Samples aligned to drainage")
plt.imshow(catchment_map, cmap="nipy_spectral")
cb = plt.colorbar()
cb.set_label("Catchment ID")
plt.show()
