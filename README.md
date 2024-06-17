# Predictive Big Data Analytics

This repository contains a web app that predicts flat prices in Moscow using a machine learning model.

## Installation

Clone the repository, create a virtual environment, activate it, and install the dependencies:

```sh
git clone https://github.com/Ezopik/pabd24
cd pabd24
python -m venv venv

# For macOS or Linux
# source venv/bin/activate 

# For Windows
.\venv\Scripts\activate

pip install -r requirements.txt
```

## Usage

### 1. Data Collection
Use the [parse_cian.py](https://github.com/Ezopik/pabd24/blob/main/src/parse_cian.py) script to gather flat characteristics (e.g., price, location, size).

```sh
python src/parse_cian.py 
```

### 2. Upload Data to S3 Storage
The [upload_to_s3.py](https://github.com/Ezopik/pabd24/blob/main/src/upload_to_s3.py) script uploads the parsed data files to S3 storage. Ensure the `.env` file is in the project's root directory.

```sh
python src/upload_to_s3.py -i data/raw/file.csv
```
The `-i` argument specifies the path to the file to be uploaded.

### 3. Download Data to Local Machine
The [download_from_s3.py](https://github.com/Ezopik/pabd24/blob/main/src/download_from_s3.py) script downloads files from S3 storage to your local machine.

```sh
python src/download_from_s3.py
```

### 4. Data Preprocessing
Use the [preprocess_data.py](https://github.com/Ezopik/pabd24/blob/main/src/preprocess_data.py) script to preprocess the data.

Note: This script prepares data for a simple paired linear regression model. For models using multiple features, preprocessing is included in the training script.

### 5. Model Training
The [train_model.py](https://github.com/Ezopik/pabd24/blob/main/src/train_model.py) script handles data processing and model training. It uses information about the city district and the specific district (12 in total) where the apartment is located. The mapping file is available [here](https://github.com/Ezopik/pabd24/blob/main/mapping/county.txt).

### 6. Launch the Flask App
```sh
python src/predict_app.py
```

### 7. Use the Service via Web Interface
To use the service, open `web/index.html`.

### 8. Docker
to run docker use
```sh
docker run -p 8000:8000 ezopik/pabd24:nm
```
 ### 9. Price_predict_address
Address for price prediction service, please use
```sh
http://192.144.12.9:8000
```