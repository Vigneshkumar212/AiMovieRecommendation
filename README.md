# AiMovieRecommendation
An small ai which predicts movies you'll likely watch based on your recently or most liked movie.

# How to run
Download and unzip the project via this site or clone this git repo.

Once cloned unzip the data set from `tmdb_5000_credits` or download from kaggle

Then create an python virtual env via

```
python -m venv venv
```

Then activate the env by

```
venv\Scripts\activate
```

Then install the following via pip

```
pip install pandas
pip install scikit-learn
```

Once done, run

```
python main.py
```

you will be prompted asking you

```
Enter a movie youve watched :
```

Enter a movie that you've watched, make sure its already present in the dataset
Then it will show you a list of movies you might like to watch 

# An example
```
[Path removed]>venv\Scripts\activate
(venv) [Path removed]>python main.py
Enter a movie you've watched : Real Steel
951                 Into the Storm
37      Oz: The Great and Powerful
2960                           LOL
4401           The Helix... Loaded
4638      Amidst the Devil's Wings
1615                 Gridiron Gang
4734                      Echo Dr.
2020                    The Rookie
3361                    Alien Zone
2770        Resurrecting the Champ
Name: original_title, dtype: object
```

## Thanks for checking this project out!
