

# Predictive Big Data Analytics

In this repo I create a web-app which determines the price for a flat in Moscow using ML-model under the hood

## Installation 

Clone the repo, create vertual environment, activate and install dependencies:  

```sh
git clone https://github.com/Ezopik/pabd24
cd pabd24
python -m venv venv

#source venv/bin/activate  # mac or linux
.\venv\Scripts\activate   # windows

pip install -r requirements.txt
```

## Usage

### 1. Data collection
<li><strong><a href="https://github.com/Ezopik/pabd24/blob/main/src/parse_cian.py">parse_cian.py</a></strong> Script for parsing flats charachteristics (e.g. price, location, meters etc.).</li>

```sh
python src/parse_cian.py 
```  

### 2. Upload data to S3 storage
<li><strong><a href="https://github.com/Ezopik/pabd24/blob/main/src/upload_to_s3.py">upload_to_s3.py</a></strong> Script for uploading parsed files to S3 storage.</li> 
To access the storage, copy the file`.env` to the root of the project.  

```sh
python src/upload_to_s3.py -i data/raw/file.csv
```
i - is the argument we use in the function. In this case, the path to the file of our function is specified.
### 3.Download data to your local machine 
<li><strong><a href="https://github.com/Ezopik/pabd24/blob/main/src/download_from_s3.py">download_from_s3.py</a></strong> Script for downloading files from S3 storage to your local directory.</li> 

```sh
python src/download_from_s3.py
``` 
### 4. Data preprocessing 
<li><strong><a href="https://github.com/Ezopik/pabd24/blob/main/src/preprocess_data.py">preprocess_data.py</a></strong> Script for data preprocessing.</li> 

NOTE: this script prepares data for simple paired linear regression model, however, further I use multiple features models, thus, whole processing is included in train file (next step).

### 5. Model training
<li><strong><a href="https://github.com/Ezopik/pabd24/blob/main/src/train_model.py">train_model.py</a></strong> Script for data process and model training.</li> 
To design the features, data were used about the city district, district (12 in total) where the apartment is located. The file with the mapping is <a href="https://github.com/Ezopik/pabd24/blob/main/mapping/county.txt">here</a></li> 

### 6. Flask app launch

todo

### 7. Service usage through web-interface

For service usage use this file `web/index.html`.  


