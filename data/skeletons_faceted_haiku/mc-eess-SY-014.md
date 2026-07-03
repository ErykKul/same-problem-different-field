MECHANISM: Generate area coverage paths in 3D terrain by computing adjacent parallel swaths maintaining constant lateral spacing and constant altitude above the terrain surface. For each coordinate along a reference path, compute the heading direction from consecutive points. Project the working height above the terrain using a local slope angle. Offset perpendicular to the path by the working width, adjusted for terrain slope to maintain constant height projection above the surface. Use a local search loop that iteratively adjusts the offset angle until the projection distance matches the target working height within a tolerance. Interpolate elevation data using Inverse Distance Weighting.
DOMAIN: Agricultural robotics and path planning
STRUCTURE: other: local search with geometric computation
DATA_OBJECT: grid or lattice
INFERENCE: deterministic or closed-form
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: not stated
