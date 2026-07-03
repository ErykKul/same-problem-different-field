MECHANISM: The paper computes a method to generate adjacent 3D paths that maintain a specified working width and height above terrain. The algorithm begins by defining a reference path as a sequence of 3D coordinates. For each segment of this path, it calculates the angle of the path segment and computes a midpoint. If this midpoint is already at the desired height above the terrain, it uses this point directly. Otherwise, it performs a local search to adjust the position vertically and horizontally to achieve the target height. The algorithm then computes a new adjacent path by offsetting the adjusted midpoint by the working width in the direction perpendicular to the path. This offset is corrected iteratively to ensure the new path remains at the target height, using a hyperparameter to adjust the angle of the boombar. The process repeats for each segment of the reference path, generating a sequence of adjacent paths. To handle elevation data, the method uses an inverse distance weighting (IDW) approach to interpolate terrain heights on a uniform grid, enabling efficient look-up during path generation. The algorithm also includes a stopping criterion based on convergence of the height adjustment iterations. The final paths are validated against the terrain to ensure they avoid gaps and overlaps while maintaining the specified working width and height. The method is deterministic and relies on geometric transformations and iterative corrections to achieve the desired path properties.

DOMAIN: agricultural robotics

STRUCTURE: other: geometric path planning

DATA_OBJECT: grid or lattice; point set

INFERENCE: deterministic or closed-form

PROBLEM_FORM: optimization

DISTRIBUTION: none

COMPLEXITY: not stated

DATA_AVAILABILITY: none

CODE_AVAILABILITY: none

PREREGISTRATION: none

EVIDENCE_BASIS: empirical-with-private-data
