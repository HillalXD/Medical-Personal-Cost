# Medical personal cost forecast

This project use to predict insurance medical cost based on different variable, using linear regression technique this project are build for predict cost based on different variable

## Install

This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [streamlit](https://streamlit.io/)


## Usage

first, you can clone this git repository

```
git clone https://github.com/HillalXD/Medical-Personal-Cost.git
```

then navigate your command to this directory

```
cd Medical-Personal-Cost
```

after that run `app.py` to use streamlit app

```
streamlit run app.py
```


## Code 
- Template code is provided in the `linear.ipynb` notebook file.
- `insurance.csv` is provide data source for training model
- `app.py` is streamlit web application to user input features for model predicting insurance personal cost 
## Dataset features

for doing prediction you need to input this features:

| features  | explanation  | 
| :-------- | :------- | 
| age | user age |
| sex  | user gender |
| BMI  | user BMI number |
| children | user total child |
| smoker | is user smoker or not |
| region | user region |




