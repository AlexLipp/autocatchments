# Autocatchments

This is a series of python scripts I made to make my life easier analysing drainage networks. This was designed strictly for personal purposes only so I strongly recommend benchmarking results. Nonetheless, it may be useful if you are interested in: hydrology, fluvial geomorphology, or anything else to do with rivers. 

## Installation 

- Clone this repository into any location 
- Navigate into a conda environment if desired
- Run `pip install .`
- The `autocatchments` package can be imported the normal way (e.g., `import autocatchments as ac`)

## Usage 

Some examples of use are given in the `examples/` subdirectory. 

### 1. Identifying 'optimal' sampling sites to equally subdivide a drainage network 

![autocatchments_output](https://user-images.githubusercontent.com/10188895/216290943-1c5dee11-f71f-4e68-a027-1a6093c92d9c.png)

In `subdivide_basins.py` I show an algorithm that, given a DEM and a target sub-catchment area, identifies N sample sites on a drainage network that sub-divide it into N sub-catchments which have an area greater than the given target area. This algorithm could be useful for designing sample-campaigns we ensure equal _area_ coverage across drainage basins for [geochemical exploration](https://doi.org/10.1016/0375-6742(87)90081-1), and [ecological/environmental monitoring](https://www.biorxiv.org/content/10.1101/2022.01.25.475970v1.abstract). I briefly detail how the algorithm works here but the code is well commented. I don't know if this has been done before (a very brief search found nothing) or whether there is a faster way of doing it (there probably is). Example output is shown below. I make no claim that this is novel or even the best way of solving the problem... but hopefully it is useful. Boris Gailleton helped work out the most efficient approach. 

1. Process input DEM/D8 data (fill sinks and route drainage across DEM using `LandLab` functions). 
2. Create a list of 'unvisited' nodes in topological order from downstream to upstream.
3. Identify sink nodes which have area smaller than the target area.
4. Remove these sinks and all their upstream nodes from the unvisited nodes list as these cannot be sampled.
5. Loop through all nodes from upstream to downstream 
6. For each node, calculate the number of unvisited nodes (and thus area) uniquely upstream of that point. 
7. If this area is greater than the threshold we add it to the list of sample sites and remove its upstream basin from the list of unvisited nodes.
8. Repeat until all nodes have been visited. 

An example DEM from [North East Scotland, UK ](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2021GC009838) is provided for testing purposes. The above image shows the output from subdividing this DEM into sub-catchments greater than 500 km2 in size. 

### 2. Aligning sample sites to drainage networks and getting subcatchments 

![snapped_to_drainage](https://user-images.githubusercontent.com/10188895/216292704-55f08d5c-69f5-4515-8611-aaa582843365.png)

`process_samples_on_rivers.py` shows how to automatically align sample sites to the nearest node with a drainage area greater than a specified threshold. Next, it calculates the unique sub-catchment corresponding to each of these sample sites. This is useful if you have made real observations on a river network but the coordinates of the sample sites [do not precisely align](https://onlinelibrary.wiley.com/doi/abs/10.1029/2007WR006507) with nodes on a model grid. An example of the output is shown above.

## Feedback 

Any feedback or suggestions are welcome via email, twitter, GitHub issue, carrier pigeon. My contact details are easily located :) 

## Cite

If you use this and find it useful please cite it as:
`Lipp, Alex. 2022. AutoCatchments. Software. doi:  10.5281/zenodo.7311352`. 

Please also acknowledge: `Barnhart et al. 2020. doi: 10.5194/esurf-8-379-2020` and `Barnes et al. 2014. doi: 10.1016/j.cageo.2013.04.024`.

