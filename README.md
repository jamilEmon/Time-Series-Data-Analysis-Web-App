# Time Series Data Analysis Web App

This project is a Flask-based web application designed for comprehensive time series data analysis. It provides a user-friendly interface for uploading CSV data, performing essential preprocessing steps, conducting exploratory data analysis (EDA) with interactive visualizations, and training a basic machine learning model for prediction.

## Features

*   **Data Upload:** Easily upload your time series data in CSV format. The application automatically parses the first column as dates and sets it as the DataFrame index.
*   **Data Preprocessing:**
    *   **Missing Value Imputation:** Numeric missing values are filled using the median of their respective columns.
    *   **Categorical Encoding:** Categorical features are converted into numerical representations using Label Encoding.
    *   **Feature Scaling:** Numeric features are scaled using `StandardScaler` to normalize their ranges.
*   **Exploratory Data Analysis (EDA):**
    *   **Time Series Plots:** Interactive line plots are generated for selected columns to visualize trends over time using Plotly.
    *   **Correlation Heatmaps:** A heatmap displays the correlation matrix of all numerical features, helping to identify relationships between variables.
*   **Machine Learning Model:**
    *   **Model Training:** A Linear Regression model is trained on the preprocessed data. Users select a target column, and the remaining numeric columns are used as features.
    *   **Prediction & Evaluation:** The model makes predictions on a test set, and performance metrics such as Mean Squared Error (MSE) and R² Score are calculated and displayed. An interactive plot shows actual vs. predicted values.
*   **Data Download:** Users can download the preprocessed dataset and the model's predictions as CSV files.

## Technology Stack

*   **Backend:** Python with Flask (web framework).
*   **Data Manipulation:** Pandas, NumPy.
*   **Machine Learning:** Scikit-learn (for preprocessing, model training, and evaluation).
*   **Interactive Visualizations:** Plotly Express.
*   **Web Server:** Gunicorn (for production deployment).
*   **Frontend:** HTML templates with Jinja2 for dynamic content, and CSS for styling.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-repo/Time-Series-Data-Analysis-Web-App.git
    cd Time-Series-Data-Analysis-Web-App
    ```
    *(Note: Replace `https://github.com/your-repo/Time-Series-Data-Analysis-Web-App.git` with the actual repository URL if available, or remove this step if the user already has the project locally.)*

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    *   **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the application:**
    ```bash
    python app.py
    ```

    The application will typically run on `http://127.0.0.1:5000/`. Open this URL in your web browser.

## Project Architecture Diagram

This diagram illustrates the architecture and data flow of the Time Series Data Analysis Web App.

```mermaid
graph TD
    subgraph User Interface
        A[index.html] -- Upload CSV --> B(Upload Endpoint /upload);
        B -- Display Raw Data --> C[preprocessing.html];
        C -- Submit for Preprocessing --> D(Preprocess Endpoint /preprocess);
        D -- Display Processed Data --> E[analysis.html];
        E -- Select Column for EDA --> F(EDA Endpoint /eda);
        F -- Display Plots & Download Processed CSV --> G[eda.html];
        G -- Select Target Column for ML --> H(Model Endpoint /model);
        H -- Display Model Results & Download Predictions CSV --> I[model.html];
        I -- Back to Home --> A;
    end

    subgraph Flask Backend (app.py)
        B -- Reads CSV, Sets Index --> J(Raw DataFrame `df`);
        D -- Fills Missing, Encodes Categorical, Scales Numeric --> K(Processed DataFrame `processed_df`);
        F -- Generates Time Series Plot & Correlation Heatmap --> L(Plotly Figures);
        H -- Splits Data, Trains Linear Regression, Predicts --> M(Predictions DataFrame `predictions_df`);
        H -- Calculates MSE, R2 Score --> N(Model Metrics);
    end

    subgraph Data Storage
        J
        K
        M
    end

    subgraph Libraries
        O[Pandas]
        P[Numpy]
        Q[Scikit-learn]
        R[Plotly Express]
    end

    B --> O;
    D --> O;
    D --> Q;
    F --> O;
    F --> R;
    H --> O;
    H --> Q;
    H --> R;

    J -- `df` --> K;
    K -- `processed_df` --> L;
    K -- `processed_df` --> M;
    M -- `predictions_df` --> I;

    G -- Download Processed CSV --> K;
    I -- Download Predictions CSV --> M;

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style C fill:#f9f,stroke:#333,stroke-width:2px
    style E fill:#f9f,stroke:#333,stroke-width:2px
    style G fill:#f9f,stroke:#333,stroke-width:2px
    style I fill:#f9f,stroke:#333,stroke-width:2px

    style B fill:#bbf,stroke:#333,stroke-width:2px
    style D fill:#bbf,stroke:#333,stroke-width:2px
    style F fill:#bbf,stroke:#333,stroke-width:2px
    style H fill:#bbf,stroke:#333,stroke-width:2px

    style J fill:#ccf,stroke:#333,stroke-width:2px
    style K fill:#ccf,stroke:#333,stroke-width:2px
    style M fill:#ccf,stroke:#333,stroke-width:2px
    style L fill:#cfc,stroke:#333,stroke-width:2px
    style N fill:#cfc,stroke:#333,stroke-width:2px

    style O fill:#ffc,stroke:#333,stroke-width:2px
    style P fill:#ffc,stroke:#333,stroke-width:2px
    style Q fill:#ffc,stroke:#333,stroke-width:2px
    style R fill:#ffc,stroke:#333,stroke-width:2px
