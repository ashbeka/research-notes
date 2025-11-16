# Senpais’ comments, really important:

- like why are we using the land-use and damage assessments? Why are we combining them? What do we really wanna achieve? Like for example helping with reconstruction efforts? What does that really mean? Like for example do you wanna look a place before and after it was damaged, and decide according to the damage that happened to it after a disaster what is the optimal way to build it so that it doesn’t get as dangerously destroyed before or to limit damage or to understand how to keep the infrastructure of the building more stable? And how would you do that exactly? What is really the benefit of all of this?. No, but really, what is the purpose of this research, what is it really you wanna achieve?

- it's like, why are you using these tasks? How would you really utilize them? Say you got the data from satellites to a certain place that got affected by a disaster, you got the data, did dimensionality reduction with SSC, did damage assessment to a certain area with U-Net, and land-use also with U-Net. What then? What is it you wanna do afterwards? What is it really proposed here? Its like there’s this missing piece. Its fine that you want to say disaster resilience, but what is it really you wanna do? Make things more clear.

- The task isn’t understandable from my perspective, is it to segment areas that are damaged, for example, from an input satellite image, is the task to return binary images where white color means damaged area, black is not damaged? Or classify the damage of an area? From the title, I think it's a little bit confusing. I think focusing on one part only is better, (this is me speaking, the focus is assessing damage in levels, like is the building 75% damaged? 56% damaged? Fully damaged? Partially damaged? So I think it's basically classifying the damage of an area. How would we work to clear the confusion my senpai mentioned)

- Second, I don't really get the idea of using sparse subspace clustering. Is this what sensei was proposing back then? And also, the second paragraph doesn't have a solution yet in this proposal. I thought that you wanted to propose something to address the limitation of deep learning methods.

- how to combine the land-use and damage assessment tasks? What is the method or methodology I would use for that? It's not clear. how to make sense of the combining of these tasks in a concrete way, not some vague general sentences that don’t explain the method or the why and the how properly.

- Do you think you wanna use LLMs? Maybe that's good, but I don’t know for sure.

- Clearly define the task, specifying whether it involves segmenting damaged areas (binary output) or classifying damage levels (e.g., percentage or categories).

- Articulate the objective and purpose of the research, explaining why land-use and damage assessments are combined and how the results will be utilized.

- Narrow the scope for better clarity and focus, potentially prioritizing damage classification by levels.

- Justify the use of Sparse Subspace Clustering (SSC) by explaining its role and contribution to addressing the limitations of deep learning, and clarify if it stems from a previous suggestion or offers a novel solution.

- Provide a detailed methodology for integrating land-use and damage assessment tasks, avoiding vague or general statements.

- Address the gap in the proposal by offering a specific solution to the computational inefficiency of deep learning models.

- Explain the post-assessment application, detailing how the outputs from satellite/UAV data, SSC, and U-Net will be used for actionable outcomes, such as reconstruction or disaster mitigation.

- Consider the inclusion of Large Language Models (LLMs) as a potential enhancement, though this requires further justification and alignment with the framework.

- Try vectotizing multiple images where each image is one vector and you vectorize them and you use ResNet60 for example, you could also utilize ResNet50 on image net, you can try aggregating multiple images in one subspace instead of one per subspace, like for example you could try making. subspace for the first 15 images (15 days) of the month for one place then the other 15 for end of month, or 6 images for 6 months of the year and 6 other images for the others 6 months of the year for example to see if there's some sort of change.