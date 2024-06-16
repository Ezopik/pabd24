# syntax=docker/dockerfile:1

FROM python:3.9
WORKDIR /app
COPY src/predict_app.py src/predict_app.py
COPY ./.env ./.env
COPY models/linear_regression_v01.joblib models/linear_regression_v01.joblib
RUN pip3 install flask flask-cors scikit-learn python-dotenv joblib flask_httpauth
CMD ["python3", "src/predict_app.py"]
EXPOSE 5000

#RUN pip3 install gunicorn
#CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "src.predict_app:app"]
#EXPOSE 8000