MECHANISM: A three-stage pipeline identifies and removes unwanted elements from a collection of geometric primitives (3D Gaussians). Stage 1 whitelist-filters primitives by projecting them to masked regions in a sparse set of views; stage 2 validates the retained primitives using depth buffering and color matching against expected values; stage 3 removes outliers using spatial distance statistics and k-nearest-neighbor distances. The method operates on an already-trained model by analyzing geometric positions and optical properties.
DOMAIN: 3D scene reconstruction, computer vision
STRUCTURE: map-reduce or embarrassingly-parallel
DATA_OBJECT: point set
INFERENCE: deterministic or closed-form
PROBLEM_FORM: filtering or removal
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
