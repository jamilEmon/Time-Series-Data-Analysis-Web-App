from flask import Flask, render_template, request, send_file
import pandas as pd
import numpy as np
import io
import plotly.express as px
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

app = Flask(__name__)
df = None
processed_df = None
predictions_df = None

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Upload CSV
@app.route('/upload', methods=['POST'])
def upload():
    global df
    file = request.files['file']
    df = pd.read_csv(file, parse_dates=[0])
    df.set_index(df.columns[0], inplace=True)
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    return render_template('preprocessing.html',
                           table=df.head().to_html(classes='table table-striped'),
                           numeric_cols=numeric_cols)

# Preprocessing
@app.route('/preprocess', methods=['POST'])
def preprocess():
    global df, processed_df
    processed_df = df.copy()

    # Fill numeric missing values
    for col in processed_df.select_dtypes(include=np.number).columns:
        processed_df[col].fillna(processed_df[col].median(), inplace=True)

    # Encode categorical columns
    for col in processed_df.select_dtypes(include='object').columns:
        processed_df[col] = LabelEncoder().fit_transform(processed_df[col])

    # Scale numeric columns
    scaler = StandardScaler()
    numeric_cols = processed_df.select_dtypes(include=np.number).columns
    processed_df[numeric_cols] = scaler.fit_transform(processed_df[numeric_cols])

    return render_template('analysis.html',
                           table=processed_df.head().to_html(classes='table table-striped'),
                           numeric_cols=numeric_cols)

# EDA
@app.route('/eda', methods=['POST'])
def eda():
    global processed_df
    column = request.form['column']
    numeric_cols = processed_df.select_dtypes(include=np.number).columns.tolist()

    # Time series plot
    fig_ts = px.line(processed_df, y=column, title=f'Time Series Plot: {column}')
    ts_html = fig_ts.to_html(full_html=False)

    # Correlation heatmap
    corr = processed_df.corr()
    fig_corr = px.imshow(corr, text_auto=True, title='Correlation Heatmap')
    corr_html = fig_corr.to_html(full_html=False)

    return render_template('eda.html',
                           ts_html=ts_html,
                           corr_html=corr_html,
                           table=processed_df.head().to_html(classes='table table-striped'),
                           numeric_cols=numeric_cols)

# ML Model
@app.route('/model', methods=['POST'])
def model():
    global processed_df, predictions_df
    target_col = request.form['target']
    feature_cols = [col for col in processed_df.select_dtypes(include=np.number).columns if col != target_col]

    X = processed_df[feature_cols]
    y = processed_df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    predictions_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

    fig_pred = px.line(predictions_df, y=['Actual','Predicted'], title='Actual vs Predicted')
    pred_html = fig_pred.to_html(full_html=False)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    return render_template('model.html',
                           pred_html=pred_html,
                           mse=mse,
                           r2=r2)

# Download processed CSV
@app.route('/download_processed')
def download_processed():
    global processed_df
    buf = io.BytesIO()
    processed_df.to_csv(buf)
    buf.seek(0)
    return send_file(buf, as_attachment=True, download_name="processed_data.csv", mimetype="text/csv")

# Download predictions CSV
@app.route('/download_predictions')
def download_predictions():
    global predictions_df
    buf = io.BytesIO()
    predictions_df.to_csv(buf)
    buf.seek(0)
    return send_file(buf, as_attachment=True, download_name="predictions.csv", mimetype="text/csv")

if __name__ == '__main__':
    app.run(debug=True)
