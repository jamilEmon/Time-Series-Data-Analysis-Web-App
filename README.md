```mermaid
graph TD
    subgraph User Interface
        A[index.html] -- Upload CSV --> B(Upload Endpoint /upload)
        B -- Display Raw Data --> C[preprocessing.html]
        C -- Submit for Preprocessing --> D(Preprocess Endpoint /preprocess)
        D -- Display Processed Data --> E[analysis.html]
        E -- Select Column for EDA --> F(EDA Endpoint /eda)
        F -- Display Plots & Download Processed CSV --> G[eda.html]
        G -- Select Target Column for ML --> H(Model Endpoint /model)
        H -- Display Model Results & Download Predictions CSV --> I[model.html]
        I -- Back to Home --> A
    end

    subgraph Flask Backend (app.py)
        B -- Reads CSV, Sets Index --> J(Raw DataFrame `df`)
        D -- Fills Missing, Encodes Categorical, Scales Numeric --> K(Processed DataFrame `processed_df`)
        F -- Generates Time Series Plot & Correlation Heatmap --> L(Plotly Figures)
        H -- Splits Data, Trains Linear Regression, Predicts --> M(Predictions DataFrame `predictions_df`)
        H -- Calculates MSE, R2 Score --> N(Model Metrics)
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

    B --> O
    D --> O
    D --> Q
    F --> O
    F --> R
    H --> O
    H --> Q
    H --> R

    J -- `df` --> K
    K -- `processed_df` --> L
    K -- `processed_df` --> M
    M -- `predictions_df` --> I

    G -- Download Processed CSV --> K
    I -- Download Predictions CSV --> M

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
