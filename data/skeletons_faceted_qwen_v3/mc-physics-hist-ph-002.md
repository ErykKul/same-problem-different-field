MECHANISM: The paper computes a sequence of integer values representing the age of an imaginary moon, derived from a recurrence relation with modular arithmetic. The recurrence adds 11 to the previous value, adjusted by periodic corrections based on a 19-year cycle and century rules. Corrections are applied when the year aligns with specific intervals, modifying the sequence to maintain alignment with astronomical observations. The initial value is set to 26 for the year 1582, and subsequent values are computed iteratively. An explicit formula is derived using a golden number (a 19-year cycle index) and century-based adjustments. The final value for a given year is obtained by combining these terms modulo 30. The moon age is then calculated as the computed value plus one. The algorithm ensures periodicity by adjusting for discrepancies between the 19-year lunar cycle and the solar year. Corrections for century years and specific intervals are encoded as conditional adjustments. The method avoids continuous variables, relying solely on integer arithmetic and discrete adjustments. The result is a deterministic sequence of values representing the moon's age for any year after 1582.  
DOMAIN: calendar computation  
STRUCTURE: other: recurrence with corrections  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: closed-form  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
