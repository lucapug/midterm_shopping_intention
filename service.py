import numpy as np

import bentoml
from bentoml.io import JSON

model_ref = bentoml.sklearn.get("shopper_intention:latest")
dv = model_ref.custom_objects['dictVectorizer']

model_runner = model_ref.to_runner()

svc = bentoml.Service("midterm_classifier", runners=[model_runner])


@svc.api(input=JSON(), output=JSON())
async def classify(application_data):
    vector = dv.transform(application_data)
    prediction = await model_runner.predict_proba.async_run(vector)
    print(prediction)
    result = prediction[:,1]

    if result >= 0.5:
        return {
            "status": "REVENUE GAINED"
        }
    else:
        return {
            "status": "LOSS OF REVENUE"
        }