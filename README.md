# Diabetis-Risk Prediction APP

![diabetis_image](diabetis_image.png) <small><small>\
*Image courtesy: aok-erleben.de*</small>

This project contains the implementation of a machine-learning based diabetis-risk prediction flask-app running in docker, involving the following steps:

**step #1 - "diabetes_dataprep.ipynb":** exploratory data analysis and data preparation. To smoothly run this notebook in google colab, the repository folder must be linked to the "My Storage" area in google drive. To run this notebook locally the paths must be adopted.

**step #2 - "diabetes_modeling.ipynb":** data modeling and model evaluation; the speciality here is that a custom loss scoring function was implemented to considere also monetary aspects of true or false model predictions rather than just e.g. accuracy-scores or f1-scores To smoothly run this notebook in google colab, the repository folder must be linked to the "My Storage" area in google drive. To run this notebook locally the paths must be adopted.

**step #3 - "diabetes_pipeline.ipynb":** a comprehensive data processing and data modeling sklearn pipeline was implemented, trained and locally saved to be later used for the final diabetes risk app. To smoothly run this notebook in google colab, the repository folder must be linked to the "My Storage" area in google drive. To run this notebook locally the paths must be adopted.

**step #4 - "model_explainability.ipynb":** model explainability is an increasingly important issue. here the shap-package in combination with the explainerdashboard-package to analyse global feature importance and also to analyse feature importances in single model decisions. To smoothly run this notebook in google colab, the repository folder must be linked to the "My Storage" area in google drive. To run this notebook locally the paths must be adopted.

**step #5 - "model_fairness.ipynb":** model fairness is an increasingly important issue in the context of responsible ai. Here the fair-learn-package was used to analyse and mitigate unfair model behavior with "age" being defined as the sensitive feature. To smoothly run this notebook in google colab, the repository folder must be linked to the "My Storage" area in google drive. To run this notebook locally the paths must be adopted.