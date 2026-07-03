MECHANISM: The PINOCCHIO code for dark matter halo simulation is ported from CPU to GPUs using OpenMP target directives. The collapse-time computation kernel (an embarrassingly parallel stage) is benchmarked on two HPC platforms (NVIDIA-based KAROLINA and AMD-based SETONIX). A newly developed parallel Power Measurement Toolkit (PMT) profiles CPU and GPU energy consumption via RAPL counters and hardware monitoring libraries. Strong and weak scaling experiments measure time-to-solution and energy-to-solution. Energy-Delay Product and Green Productivity metrics are computed to evaluate efficiency.
DOMAIN: High-performance computing; scientific computing; energy efficiency
STRUCTURE: map-reduce or embarrassingly-parallel
DATA_OBJECT: dense matrix or tensor
INFERENCE: deterministic or closed-form
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: not stated
