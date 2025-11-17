# My notes, really important

- To focus on damage progress change detection use: near IR, short wave IR (bands 11, 12), for BD, we still rely on bands 8, 11, 12 because they highlight how surfaces change when a building is damaged (they reflect light differently) (patterns, textures, shadows RGB)

- Focus on shadow accurate detection change more granular shadow details 

- PCA-diff change detection is a method used in remote sensing and image analysis to identify differences between two images of the same area taken at different times. It combines the use of Principal Component Analysis (PCA) with image differencing. 

- NEW: learning the patterns of disasters before they happen (time period undecided could be all the way from a previous disaster to a current one) where we use satellite images 13 bands (RGB, infrared, LiDAR, NVDI, others) to draw out principles components (meaningfully representing the trend/behavior of variables that could have led to a disaster), like did a house location/elevation change a little bit in the span of year? How and why? Could this have been a previous incident before/similar pattern to a certain disaster? Like earthquake or something?  F-DS and S-DS could be used to discover the general and granular details of timeseries along a certain span of time then we get some sort of change features that we can use for some processing/correlation to flag an indication of an event or a similarity to a previous incident data patterns (that we used CD to learn). Could be useful for vegetation patters discovery, forest fires, volcano activity (meh?)

- dictionary learning to extract features.

- Fermi data, sound from topography? Destruction? Building?

- NEW GOAL (Potential main research focus maybe or alternative?): understand how damage evolves over time (temporal dynamics), for that we can use DMD (dynamic mode decomposition)

- LASSO Standard method of sparse modeling, could be used for automatic feature selection

- We could use TorchGeo (library) for working with geospatial datasets and its few pre-trained models for feature extraction, classification and regression or other purposed (utilizing this library could prove useful).

- Auxiliary LULC (Land Use/Land Cover) datasets are additional, non-spectral data layers, like elevation and slope, used to improve the accuracy of land use and land cover mapping. Possible utilization?

- Random thought: Fourier Transform, Fourier analysis, Fourier on time series satellite data.

- Check if the dataset has referenced the Sentinel-2 tiles used to make the classification of a given pixel/patch for a given area(s). 

- xBD has no direct Sentinel-2 tile IDs. You can overlay onto Sentinel-2 by using the corrected GeoTIFFs and mapping to MGRS tiles yourself (what xBD-S12 essentially did).

- MultiSenGE / MultiSenNA has Sentinel-2 tile IDs alignment (I think, check please), each patch’s JSON label file includes a tile (S2 tile ID) and S2 acquisition dates, and filenames encode the tile as well. For a given pixel/patch, you can unambiguously say “this label came from S2 tile TxxYYY on dates D1…Dn”.

- WOW! Interesting thing happened, in August 5th 2025, I noted with my sensei through our discussion that I can try using xBD dataset metadata to get the same satellite images from Sentinel-2 online dataset which has other bands like LiDAR or infrared, the challenge with this approach is combining data from two different datasets, as I would need to do a lot of pre-processing for stuff like matching and alignment. And now it’s November 2025 and some people produced a research paper that makes that and they call it xBD-s12. 

- Track damage and how it progresses over time goals could be: urgent help, resource allocation, (possible main focus) long term planning to see how damage changes “patterns” to become better prepared next time.

- The hypothesized idea I'm thinking about is somewhere along the lines is temporal damage analysis in satellite images using first and second difference subspace, I guess it could be boiled down to a change detection method. The immediate thought is this is a damage assessment tool, falling under the logistics usefulness.

- Our research main aim could be to capture immediate post-disaster changes (first-difference) and track longer-term recovery or further degradation (Second-order difference) through SM.

- Maybe subspace based change detection could be better than pixel-wise segmentation when it comes to detection noise and small fluctuations.

- (IMPORTANT) regarding potential SSC use in the research:
    *　Strong unsupervised baseline: one of the main research objectives/gaps we want to show is: “Our method is better than simple baselines and strong classical baselines.” Since SSC is a well-known, principled unsupervised method for union-of-subspaces data. So it’s a good reference point: Difference Subspace (simple linear change model), SSC (more flexible, multi-subspace clustering of changes), U-Net (deep supervised segmentation) If my framework beats SSC, it’s a strong argument.
    * (IMPORTANT) Temporal behavior / recovery patterns (if multi-time): If you later extend to multiple time steps (t1, t2, t3, …): Each building has a trajectory in feature space. Buildings that recover quickly, never recover, or change slowly will form different subspaces/trajectories. SSC can cluster these trajectories into: “fast recovery”, “delayed recovery”, “no recovery”, “repeated damage” This directly connects to your “temporal damage analysis” goal.
    * Pseudo-labels & pre-processing for U-Net: You mentioned combining SSC with U-Net. SSC can: Provide pseudo-labels from unsupervised clusters  used to: pretrain a network, or guide what classes might exist. Give you a cleaner representation of change patterns that you can feed into U-Net as extra channels (e.g., cluster assignments, subspace coordinates). So pipeline example: Extract patch features / difference features. Run SSC  get cluster labels (types of change). Use these as: inputs to U-Net, or as auxiliary targets, or as a strong unsupervised baseline to compare your supervised model against.

- Potential goals for research: 
    * Automatically map damage and land-use classes (intact / light / heavy / rubble / land-use change, etc.) with higher accuracy and less manual labeling.
    * Capture different patterns of change/recovery over time (who recovers, who doesn’t, how fast). Turn this into fast, operational decision support: prioritize where to send help, resources, and reconstruction efforts right after a disaster.

- Learn what topographic data is. Topographic data: Digital Elevation Models (DEM), slope, and aspect are frequently used because topography strongly influences land cover and land use. SO we can utilize this in our research.

- (REALLY IMPORTANT) Major idea (transformation/connection of thoughts!): I Thought of this idea and sketched it out, it was sort of thoughtful, it could be important, look into it carefully but without bias and give honest objective consideration. The idea is that we can try to construct something similar to the xBD building damage dataset but with even more granular damage variety levels (or other features besides damage like structural integrity or color or whatever), how? We try to utilize First-Order DS and Second-Order DS to get some sort of change features/data that we can consolidate or flatten into 1D vector, we can use multiple bands with one big dataset where damage isn’t labeled yet (maybe from S2 or Planet org or use AI to automatically build the dataset based on dates of known disaster maybe?), after that we can use SSC for clustering since I’m hypothesizing we get similar looking change detection features output with different levels of damage and SSC tries to figure out the connection between polygons from different disasters in hope of grouping each granular level of damage (or other desirable features/trends) into its own category/class, THEN, we try to create labeled datasets based on First-Order DS and Second-Order DS and SSC from the massive amount of satellite data all over the web then we use it as pretext for deep learning training to create a model for fast damage-levels classification (I wanted to say damage recognition, could be a goal task, or we could outsource it to YOLO). Note: We could try reversing the order of the pipeline by using SSC first the FO/SO DS if it works better.
    * Potential pipeline example:
        + Extract patch features / difference features.
        + Run SSC → get cluster labels (types of change).
        + Use these as:
            - inputs to U-Net,
            - or as auxiliary targets,
            - or as a strong unsupervised baseline to compare your supervised model against.

- Maybe we could say: “Our method is better than simple baselines and strong classical baselines.”
- SSC is a well-known, principled unsupervised method for union-of-subspaces data, so it’s a good reference point:
    * Difference Subspace (simple linear change model)
    * SSC (more flexible, multi-subspace clustering of changes)
    * U-Net (deep supervised segmentation)

- If our framework beats SSC alone, it’s a strong argument. Such as “We use Sparse Subspace Clustering because our pre/post-disaster features are a mixture of different change patterns (intact, lightly damaged, collapsed, land-use transitions). SSC is designed exactly for data that lie in a union of low-dimensional subspaces, so it lets us unsupervisedly discover and cluster these types of change, providing both a strong baseline and useful pseudo-labels/structure for our U-Net–based damage and land-use mapping.”

- Potential map could be (not confirmed just hypothesis): Pre / Post Disaster Images  Feature Extraction (e.g., bands, diff, CNN)  Sparse Subspace Clustering (SSC) (sparse self-expression, spectral clustering)  Change-Type Clusters (e.g., no damage / mild / heavy / land-use change, etc.)
          ├──► Unsupervised damage map (baseline)
          ├──► Pseudo-labels for training U-Net
          └──► Extra input channels to U-Net

- Maybe SSC can be viewed as a label-free way to discover “types of change”, maybe we feed SSC with feature vectors (e.g., difference features for each patch/building), maybe SSC groups them into clusters where:
    * Points in the same cluster follow a similar change pattern (e.g., “no change”, “moderate darkening of roof”, “strong spectral change + texture loss”)
    * Each cluster corresponds to a subspace capturing that pattern. It could be that we don’t start with labels like “slightly damaged” / “collapsed”. SSC can discover natural groups of change:
        - Cluster 1 → mostly no change
        - Cluster 2 → bright → dark change (possible burnt / destroyed)
        - Cluster 3 → urban → green (clearing + vegetation)

- Could be combining SSC with U-Net. SSC can (as we said before) provide pseudo-labels from unsupervised clusters  used to:
    * Pretrain a network
    * Guide what classes might exist.
    * Give you a cleaner representation of change patterns that you can feed into U-Net as extra channels (e.g., cluster assignments, subspace coordinates).

- What are hoping to achieve? We could achieve/aim to After SSC + U-Net (options are just hypothesis):
    * Automatically map damage and land-use classes (intact / light / heavy / rubble / land-use change, etc.) with higher accuracy and less manual labeling.
    * Capture different patterns of change/recovery over time (who recovers, who doesn’t, how fast).
    * Turn this into fast, operational decision support: prioritize where to send help, resources, and reconstruction efforts right after a disaster.

- We could do something like feeding SSC our feature vectors (e.g., difference features for each patch/building) to get granular types of change. Points in the same cluster could follow a similar change pattern (e.g., “no change”, “moderate darkening of roof”, “strong spectral change + texture loss”) Each cluster corresponds to a subspace capturing that pattern.

- A hypothetical (not decided) pipeline example could be:
    * Extract patch features / difference features.
    * Run SSC → get cluster labels (types of change).
    * Use these as: inputs to U-Net, or as auxiliary targets, or as a strong unsupervised baseline to compare your supervised model against.

- Research could be orientated around Temporal behavior / recovery patterns (multi-time) we might need to implement multiple time steps (t1, t2, t3, …) to adhere to First-order and Second-order DS proper methodology:
    * Each building has a trajectory in feature space.
    * Buildings that recover quickly, never recover, or change slowly will form different subspaces/trajectories.
    * SSC can cluster these trajectories into: “fast recovery”, “delayed recovery”, “no recovery”, “repeated damage”

- Previous point directly connects to our “temporal damage analysis” goal.

- I thought about per-cluster models, where I can train light weight models so each region’s model learns context-specific cues, then compute per-cluster feature importances like which spectral bands or pre/post-disaster differences matter most to guide interpretable response planning. It’s an interesting use case for sure.

- I also thought about potential use in my research which is my current research focuses on disaster resilience from satellite imagery (damage assessment and land-use mapping). Using clustering strategy can improve my research, for region grouping, I can use spectral clustering on remote sensing features (multispectral indices, texture, built-up density) to partition a city into homogeneous region clusters like coastal vs. inland, high vs. low-density, old vs. new build). Another use is to handle rare severe damage, severe-damage pixel tiles are a minority. Within each region cluster, I can apply oversampling or class balanced losses so the model treats extreme damage more fairly.

- (Me speaking about incentive for research, could provide personal insights): I want to contribute to reconstruction efforts in Gaza, the reason why I’m now interested in damage assessments (change detection) is because I want to learn how to provide useful data for civil or infrastructure engineers to help speed up reconstruction efforts. My initial idea was very big, basically generating optimal infrastructure placement techniques through computer vision, but it big and vague that’s why I’m starting small with damage detection and incrementally going into more advanced tasks that could help with reconstruction.

- The “informative structure or most important patterns that we might get might be damage patterns, urban texture shifts, or vegetation change. PCA/SVD/First-order DS/Second-Order DS/RTW or other methods could helps isolate the core variation patterns across time or space. It lets us discard irrelevant information (e.g. sensor noise, lighting changes) and focus on change signals.

- A good way to imagine what satellite data look like in our case and how we want to process them “What the data “looks like” geometrically”: In our setting you have (for each patch / building): Pre-disaster features (multi-band, maybe deep features), Post-disaster features, Possibly difference or “change” features (from Difference Subspace, etc.), In reality, these points come from a mix of different “behaviors”: Intact buildings (no damage), Lightly damaged buildings, Heavily damaged / collapsed, Vegetation  urban, Urban  rubble / open space, etc. Each of these behaviors tends to live in its own low-dimensional pattern in feature space  i.e., a subspace. The data could be imagines like: “A union of several subspaces”. This could be the scenario DS with some sort of unsupervised clustering (label free way preferably since we have a ton of data) is built for.

- Some ideas/keywords that I thought about and wondered if they are of any use to our research or benefit:
    * based semantic change detection framework
    * initial and rapid assessment occurs at the scene (sometimes in a dangerous area) 
    * Disaster mapping.
    * Disaster Damage Mapping as a Service (maybe?)
    * Geodesics generalize straight lines to curved surfaces/spaces.
