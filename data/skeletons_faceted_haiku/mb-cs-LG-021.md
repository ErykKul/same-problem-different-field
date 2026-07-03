MECHANISM: Represent traffic patterns in three stages. First, embed raw input data, temporal indicators (hour of day, day of week), and spatial structure via three components: feature embedding (fully connected), temporal embedding (learnable lookup tables), and dynamic weighted graph structure embedding (learn time-varying edge weights using self-attention over input). Second, model spatial dependencies using self-attention on compressed node representations. Third, model temporal dependencies by transforming time-series to frequency domain via FFT, processing real and imaginary components with separate MLPs in a cross-computation manner, then transforming back via IFFT. Finally, apply regression to produce time-series forecast.
DOMAIN: Time-series forecasting, traffic prediction, spatial-temporal learning, graph neural networks
STRUCTURE: spectral or transform
DATA_OBJECT: grid or lattice
INFERENCE: frequentist point estimate
PROBLEM_FORM: prediction or classification
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
