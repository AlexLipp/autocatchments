import autocatchments as ac
import matplotlib.pyplot as plt
import pandas as pd

"""Takes a D8 grid and a list of sample sites (samples_thames.csv) and aligns the sample sites
to nodes on the DEM which have a drainage network greater than given threshold. These fitted localities
are then saved to "outputs/samples_thames_fitted.csv". 

Next, we extract the unique subcatchment corresponding to each of these subsamples (can be slow! sorry!).
Each of these subcatchments are given a unique 'AreaID' integer. A map of these subcatchments 
(ESRI ASCII format) is saved to file as: `area_IDs.asc`. A key matching each areaID to the samples is 
given in `subcatch_area_IDs.csv`. """

path_to_d8 = "inputs/thames_d8.nc"
path_to_samples = "inputs/samples_thames.csv"
catchment_threshold = 1e7
print("Loading in topographic data...")
mg = ac.toolkit.load_d8(path_to_d8)

sample_names, sample_sites = ac.autosampler.load_sample_data(path_to_samples)
print("Snapping to drainage")
snapped_sites_model_xy = ac.autosampler.snap_to_drainage(mg, sample_sites, catchment_threshold)
snapped_x, snapped_y = ac.toolkit.model_xy_to_geographic_coords(
    (snapped_sites_model_xy[:, 0], snapped_sites_model_xy[:, 1]), mg
)

ac.toolkit.viz_drainage_area(mg)
plt.scatter(x=sample_sites[:, 0], y=sample_sites[:, 1], c="red", marker="x")
plt.scatter(x=snapped_x, y=snapped_y, c="green", marker="x")
plt.legend(["Input sites", "Snapped sites"])
plt.title("Observed and fitted localities")
plt.show()

outdf = pd.DataFrame({"SampleName": sample_names, "fitted_x": snapped_x, "fitted_y": snapped_y})
outdf.to_csv("outputs/samples_thames_fitted.csv", index=False)

print("Getting unique subcatchments")
target_nodes = ac.autosampler.coords_to_node_ids(mg, snapped_sites_model_xy)
sub_catchment_dict = ac.autosampler.get_subcatchments(mg, target_nodes, sample_names)
catchment_map = ac.autosampler.get_subcatchment_map(mg, sub_catchment_dict)
ac.autosampler.save_subcatchments(mg, sub_catchment_dict, catchment_map, "outputs")
