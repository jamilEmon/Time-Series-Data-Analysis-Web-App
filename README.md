This project is a web application designed for time series data analysis, built using the Flask framework. It provides a user-friendly interface for uploading CSV data, performing essential preprocessing steps, conducting exploratory data analysis (EDA) with interactive visualizations, and training a basic machine learning model for prediction.

Here's a breakdown of its components and workflow:

__Core Functionality:__

1. __Data Upload:__ Users can upload their time series data in CSV format. The application automatically parses the first column as dates and sets it as the DataFrame index.

2. __Data Preprocessing:__

   - __Missing Value Imputation:__ Numeric missing values are filled using the median of their respective columns.
   - __Categorical Encoding:__ Categorical features are converted into numerical representations using Label Encoding.
   - __Feature Scaling:__ Numeric features are scaled using `StandardScaler` to normalize their ranges.

3. __Exploratory Data Analysis (EDA):__

   - __Time Series Plots:__ Interactive line plots are generated for selected columns to visualize trends over time using Plotly.
   - __Correlation Heatmaps:__ A heatmap displays the correlation matrix of all numerical features, helping to identify relationships between variables.

4. __Machine Learning Model:__

   - __Model Training:__ A Linear Regression model is trained on the preprocessed data. Users select a target column, and the remaining numeric columns are used as features.
   - __Prediction & Evaluation:__ The model makes predictions on a test set, and performance metrics such as Mean Squared Error (MSE) and R² Score are calculated and displayed. An interactive plot shows actual vs. predicted values.

5. __Data Download:__ Users can download the preprocessed dataset and the model's predictions as CSV files.

__Technology Stack:__

- __Backend:__ Python with Flask (web framework).
- __Data Manipulation:__ Pandas, NumPy.
- __Machine Learning:__ Scikit-learn (for preprocessing, model training, and evaluation).
- __Interactive Visualizations:__ Plotly Express.
- __Web Server:__ Gunicorn (for production deployment).
- __Frontend:__ HTML templates with Jinja2 for dynamic content, and CSS for styling.

__Project Diagram:__

graph TD A[User] --> B{Web Browser}; B -- Upload CSV (index.html) --> C[Flask App (app.py)]; C -- Store Raw Data (df) --> D[Data Preprocessing]; D -- Render Preprocessing Page (preprocessing.html) --> B; B -- Trigger Preprocessing --> C; C -- Fill Missing Values, Encode Categorical, Scale Numeric --> E[Processed Data (processed_df)]; E -- Render Analysis Page (analysis.html) --> B; B -- Select Column for EDA --> C; C -- Generate Time Series Plot & Correlation Heatmap --> F[EDA Results]; F -- Render EDA Page (eda.html) --> B; B -- Download Processed CSV --> C; B -- Select Target Column for ML --> C; C -- Split Data, Train Linear Regression Model, Predict --> G[ML Model Results]; G -- Render Model Page (model.html) --> B; B -- Download Predictions CSV --> C; B -- Back to Home --> A; subgraph Flask Application C D E F G end subgraph Frontend B end style A fill:#f9f,stroke:#333,stroke-width:2px style B fill:#bbf,stroke:#333,stroke-width:2px style C fill:#ccf,stroke:#333,stroke-width:2px style D fill:#cfc,stroke:#333,stroke-width:2px style E fill:#ffc,stroke:#333,stroke-width:2px style F fill:#fcc,stroke:#333,stroke-width:2px style G fill:#cff,stroke:#333,stroke-width:2px

