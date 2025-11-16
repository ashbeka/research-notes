# Old notes, not as important as sensei, senpai and my notes, but still pretty relevent, don't forget it.

•	Combine LiDAR data, SAR and InSAR data, and other sensors to infer knowledge?
•	captures structural patterns in large datasets. 
•	Clearly define the task, specifying whether it involves segmenting damaged areas (binary output) or classifying damage levels (e.g., percentage or categories).
•	Articulate the objective and purpose of the research, explaining why land-use and damage assessments are combined and how the results will be utilized.
•	Task in not clearly defined, what do I wanna do? There’s a missing piece
•	Combining Land use and damage assessment, Methods to combine between both maybe..?
•	lightweight deployment to edge devices? on-the-ground application in post-disaster scenarios and urban planning efforts  (UAVs?)
•	Explain the post-assessment application, detailing how the outputs from satellite/UAV data, SSC, and U-Net will be used for actionable outcomes, such as reconstruction or disaster mitigation.
•	More detailed methodology? Maybe?
•	Offer a specific solution to the computational inefficiency of deep learning models, subspace methods on UAV?
•	How will the outputs from satellite/UAV data, SSC, and U-Net be used for actionable outcomes? More details are needed, vagueness makes no sense
•	The Damage Assessment information and the Land-use information, will it be a heatmap? Grid numbers? How will we present that information?
•	Will we use SSC to compress data?
•	Explain more what xBD does, xBD used to Damage assessment
•	“Sell your fish”, maybe deployment on UAV as the main focus? Maybe running on drones is a good reason
•	SSC -> drones, U-Net -> computer
•	Current post-disaster assessment models often rely on Deep Learning methods, what do these models do, for example identifying..
•	How do we give insights from two heatmaps? Will Insights = heatmap Output -> ?
•	This is a mixed interfeild
•	focus on Drones images UAV maybe? (senpai advised me this)
•	Processing images in drone (resource constraints)
•	Maps for multiple infrastructures (schools, hospitals, etc..)? a way to construct the maps, A method to build maps?
•	Maybe we can use Multi-criteria decision analysis (MCDA), Multi criteria analysis, MCDM?
•	Built a heatmap for MCA, made subspaces for each year 2011, 2012, 2013 for example, compare subspaces and see similarity
•	Multi criteria analysis using satellite images for Disaster Resillience
•	“processing satellite imaging remote sensing computer vision to determine civil engineering infrastructure route”?
•	Try to create from satellite images a perspective of a city and ask a generative model to create a perspective of the city depending on where you are and where you are looking.
•	Using subspaces and remote sensing to determine the optimum placement for urgent infrastructure(hospitals, evacuation centers)
•	processing satellite imaging remote sensing computer vision to determine civil engineering infrastructure route.
•	An AI model that processes satellites images for a certain region, it looks at its contours, terrain, climate, and other general factors, in order to determine what is the best way to build such a region, as in, Urban and architectural planning. Homes, hospitals, other facilities, determine where and how and what.
•	Do you remember the news about the lab that built the mushroom thing that detects the best route to train metro-lines in Tokyo, maybe we can get inspiration form that? see how the ants build their homes/colonies, make OpenCV datasets from that, maybe it could be useful, apply the research idea on ant colonies and extract wisdom.
•	Also, hospitals, utilizing best routes for evacuation of patients, transporting and stuff neighborhood
•	Damage analysis information as heatmaps?
•	Damage analysis -> heatmaps
•	LU -> grid numbers
•	SSC to compress data
•	Xbd explain more, we use xbd for damage analysis
•	Sell my fish, deployment on UAV could be a unique unexlored region 
•	Running on drones is a good reason
•	SSC on drone, U-Net on computers
•	Current post-disaster assessment models often rely on Deep Learning methods, what do these models, for example identifying
•	How do we give insights from two heatmaps?
•	Insights = heatmap Output -> ?
•	Multi criteria analysis
•	Multi criteria decision analysis
•	mix interfield
•	MCDM
•	Multi criteria analysis using satellite images for Disaster resillience
•	Maybe extract wisdom from the Multi criteria analysis using satellite images for GIS Saudi Arania groundwater mapping paper?
•	Using subspace methods to calculate similarly 
•	Zero shot learning (could be a great idea, important)
•	You could focus on Drones images UAV for the research, could be a unique idea.
•	Processing images in drone (resource constraints)
•	Landslide detection
•	Automation of detection of landslides
•	Landslide satellite images
•	Maps for multiple infrastcures (schools, hospitals, etc..)? a way to construct the maps, 
•	A method to build maps 
•	Maybe we could built destruction maps using drones.
•	Built a heatmap for MCA, made subspaces for each year 2011, 2012, 2013 for example, compare subspaces and see similarity.
•	What is the task really about? What is the objective? What is accomplished or the thing to be accomplished? And specify it, not some general sentences that are vague.
•	Satellite image disaster resilience evacuation routes?
•	Delta encoder, could be useful, sounds important
•	Critical infrastructure analysis assessment
•	Tracking refugees movement
•	Depth, lidar data 3d info, shape of change and angle of change, visual changes, shapes and shifts in space
•	SAR data cloud, hidden data
•	Combine all data
•	Idea human mobile phone on-presence using pictures or videos to capture building structural damage.  
•	There’s a missing piece of combining Land use and damage assessment
•	Methods to combine.
•	processing satellite imaging remote sensing computer vision to determine civil engineering infrastructure route
•	Remote sensing survey infrastructure 
•	Using subspaces and remote sensing to determine the optimum placement for urgent infrastructure (hospitals, evacuation centers)
•	An AI model that processes satellites images for a certain region, it looks at this contours, climate, topography, terrain, enviroment, and other general factors, to determine what is the best way to build such region, as in civil/urban/infrastructure engineering. Homes, hospitals, other facilities, determine where and how and what.
•	processing satellite imaging remote sensing computer vision to determine civil engineering infrastructure route, The lab that built the mushroom thing that detects best route to train metro-lines in Tokyo, utalize that, see how the ants build their homes/colones, make OpenCV datasets from that, maybe it could be useful, apply the research idea on ant colonies and extract wisdom.
•	Also, hospitals, utilizing best routed for evacuation or patients transporting and stuff neighborhood 
•	increased frequency of natural and man-made disasters requires the need for post-event damage assessment and land-use analysis for disaster resilience purposes, including the reconstruction phase
•	urban/disaster resilience: refers to the ability of cities to effectively analyze, respond and recover from disasters, hence that efficient and fast recovery requires rapid and precise insights into land-use patterns and structural damage 
•	Focus is land-use and damage classification
•	Aiming to offer insights for urban planners, deployable tools to improve disaster resilience, scalable tools for urban planners in both developed and developing regions, to enhance urban planning and resilience against recurring disasters
•	Japan, disaster-prone place for earthquakes and tsunamis, similarly, war-torn regions, where infrastructure is decimated, demeaning scalable tools to assist in reconstruction
•	DL techniques, while accurate, are computationally expensive and less practical in resource-constrained environments
•	Why combine the independent tasks of damage assessment and land-use? Damage assessment identifies the impact on infrastructure, while land-use analysis helps understand the spatial distribution of resources and human activity. Together, they provide a comprehensive view of the affected areas, enabling more targeted and efficient recovery strategies, optimal resource allocation, and better urban resilience.
•	a hybrid framework combining subspace and deep learning methods
•	UAV-acquired imagery
•	Datasets such as: Sentinel-2, EuroSAT, xView2, and xBD (most important), publicly accessible, annotated datasets are important
•	Sentinel-2 first for training to classify land-use features (e.g., urban, rural, vegetation) across high-resolution images, xBD secondly, since it has high-resolution satellite imagery specifically annotated for pre- and post-disaster damage assessment, we use part of it for a second round of training, and the other part of testing and validation, then validate and test on combination of both and other datasets
•	For datasets, perform augmentation, applying transformations like rotation, flipping, scaling, or brightness adjustment to input images like destroyed building. It helps the model generalize better and accurately describe the damage percentage.
•	We’ll use Sparse Subspace Clustering (SSC), it effectively reduces the dimensionality of high-resolution satellite data while preserving important features, captures structural patterns in large datasets 
•	CNNs (NO, U-Nets? SenNet? Hmmmm, seems like no) for extracting spatial features, SM complementing deep learning models by improving computational efficiency and interpretability 
•	captures structural patterns in large datasets. 
•	Compare against baseline models (e.g., standalone CNNs, traditional classifiers) on benchmark datasets
•	lightweight deployment to edge devices (UAVs?) using PyTorch
•	F1-score and IoU as metrics against other approaches
•	on-the-ground application in post-disaster scenarios and urban planning efforts (UAVs)?
•	Enhance the framework with real-time data from drones or IoT sensors for dynamic infrastructure planning
•	Expand collaborations to include government agencies, NGOs, and international research institutions to scale the impact of the research.
•	Adapt the methodology for use in other domains, such as climate change monitoring, deforestation analysis, and smart city planning
•	Enhanced urban planning and resilience against recurring disasters
•	Providing tools for rapid infrastructure planning in both conflict-affected and disaster-prone regions
•	cost-efficient AI tools
•	disaster preparedness and response in resource-constrained settings.
•	Contribute to Japan's disaster resilience efforts and post-conflict recovery in war-torn regions globally
•	Urban infrastructure planning aid with insights, optimal infrastructure placement, stuff like that

Some Scattered ideas I got from asking AI to generate keywords too:
“Urban Infrastructure Planning Using AI | Feature Extraction for Urban Land Use Classification from Satellite Imagery | AI-Assisted Urban Reconstruction and Infrastructure Planning | Land-Use Classification for Post-Conflict Reconstruction Using Satellite Imagery and Lightweight Machine Learning Models | AI-Driven Infrastructure Planning for Disaster Resilience and Urban Development | AI-driven system for infrastructure planning and land-use optimization | land-use classification and AI-assisted planning | AI-Assisted Urban Reconstruction and Infrastructure Planning: Integrating Lightweight Machine Learning and Deep Learning for Post-Conflict and Disaster-Resilient Development | AI-Assisted Land-Use Classification and Damage Detection for Post-Conflict and Disaster-Prone Urban Planning | developing an efficient, scalable framework for automated land-use classification and infrastructure damage detection
Develop a machine learning model to analyze satellite images for key urban features (e.g., roads, buildings, vegetation). The model could predict optimal placements for new infrastructure like hospitals, schools, and evacuation centers, accounting for terrain, climate, and population density. Use satellite imagery and computer vision techniques to map and classify land use dynamically, identifying areas suitable for residential, commercial, and industrial purposes. Identifying and classifying specific land-use types (e.g., residential, industrial, green spaces) within urban settings from high-resolution satellite images, This task is critical for urban planning but is often computationally intensive when using deep learning for large-scale images.”
