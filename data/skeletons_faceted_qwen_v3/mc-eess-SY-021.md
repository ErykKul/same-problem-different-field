MECHANISM: The paper computes a real-time monitoring system using sensor data and a pre-trained machine learning model to predict and control aquaculture parameters. Sensors collect time-series measurements of water quality metrics (e.g., pH, temperature, dissolved oxygen). These measurements are processed by a convolutional neural network (CNN) model, which forecasts future values of the metrics based on historical data. The model is trained to minimize the median absolute percentage error (MdAPE), which accounts for outliers and abrupt variations in the data. Predicted values are compared against predefined optimal ranges for each metric. If a predicted value falls outside the range, the system triggers alerts and activates corrective actions (e.g., adjusting water flow, notifying staff). The model is deployed on edge devices (Arduino microcontrollers) to enable low-latency, on-device computation without reliance on cloud infrastructure. The system continuously refines its predictions using real-time data collected from the aquaculture environment. The computational pipeline includes data acquisition, feature extraction, model inference, and decision-making based on forecasted outcomes. No explicit mathematical formulas are derived or solved; instead, the focus is on deploying a pre-trained model for real-time prediction and control.  
DOMAIN: aquaculture monitoring  
STRUCTURE: other: neural network-based processing  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
