# Boston House Predictor

## Description

The Boston House Price Predictor is a Python application deployed on Heroku for predicting house prices in Boston. This application can be accessesd via

## Tools/Libraries required

* [Python 3.9](https://python.org) : Base programming language for development. The latest version of python.
* sklearn
* pickle
* requests
* flask

## Usage

Post request should be made to the endpoint using a list of 13 features.

```python

import json

url = "https://boston-house-price-predict.herokuapp.com/predict"
data = {"inputs": [[11.8123, 0.0, 18.1, 0.0, 0.718, 6.824,76.5, 1.794, 24.0, 666.0, 20.2, 48.45, 22.74],
            [5.82115, 0.0, 18.1, 0.0, 0.713, 6.513, 89.9, 2.8016, 24.0, 666.0, 20.2, 393.82, 10.29]]}

post_data = json.dumps(data)
response = requests.post(url, data=post_data)
print(response.status_code, response.content)

```

## Contribution

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

The MIT License - Copyright (c) 2021 - Adeyinka J. Oresanya

[MIT](https://choosealicense.com/licenses/mit/)
