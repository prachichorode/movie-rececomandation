# movie-rececomandation
# 🎬 CODSOFT Task 4: Movie Recommendation System

A simple **Movie Recommendation System** developed using **Python** as part of the **CODSOFT Python Programming Internship – Task 4**.

The system recommends movies based on the similarity between their genres.

## 📌 Features

* 🎬 Displays available movies
* 🔍 Allows the user to select a movie
* 🎭 Compares movie genres
* 🧮 Calculates a similarity score
* ⭐ Recommends the top 5 similar movies
* 📊 Sorts recommendations by similarity score
* ⚠️ Handles invalid movie names
* 💻 Runs in the terminal

## 🛠️ Technologies Used

* Python 3
* Dictionary
* Sets
* Functions
* Loops
* Conditional Statements
* Lambda Functions
* Sorting

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── movie_recommendation.py
└── README.md
```

## 🎥 Available Movies

* Inception
* Interstellar
* The Matrix
* Avengers
* Iron Man
* Titanic
* The Notebook
* Jurassic Park
* Avatar

## 🚀 How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
```

### Step 2: Open the Project

```bash
cd movie-recommendation-system
```

### Step 3: Run the Program

```bash
python movie_recommendation.py
```

## 💻 Example Output

```text
===== MOVIE RECOMMENDATION SYSTEM =====

Available Movies:
- Inception
- Interstellar
- The Matrix
- Avengers
- Iron Man
- Titanic
- The Notebook
- Jurassic Park
- Avatar

Enter a movie name: Inception

Recommended Movies:
The Matrix - Similarity Score: 3
Jurassic Park - Similarity Score: 2
Avatar - Similarity Score: 2
Interstellar - Similarity Score: 1
Avengers - Similarity Score: 1
```

## 🧠 How It Works

The system stores movie names and genres in a Python dictionary.

When the user selects a movie:

1. The genres of the selected movie are extracted.
2. Genres are converted into sets.
3. The selected movie's genres are compared with other movies.
4. Common genres are found using **set intersection**.
5. The number of common genres becomes the **Similarity Score**.
6. Movies are sorted according to their scores.
7. The top 5 movies are displayed as recommendations.

### Example

For **Inception**:

```text
Inception → Action, Sci-Fi, Thriller
The Matrix → Action, Sci-Fi, Thriller
```

Common genres:

```text
Action, Sci-Fi, Thriller
```

Similarity Score:

```text
3
```

## 🎯 Learning Objectives

This project helps to understand:

* Python dictionaries
* Functions
* Sets
* Set intersection
* Loops
* Conditional statements
* String manipulation
* Sorting
* Lambda functions
* Basic recommendation systems

## 🔮 Future Improvements

* ⭐ Add movie ratings
* 🎭 Add more genres
* 🎬 Add more movies
* 👤 Add user preferences
* 🖼️ Add movie posters
* 🌐 Create a web interface
* 🤖 Use Machine Learning for recommendations
* 📊 Use a larger movie dataset
* 🔎 Add movie search functionality

## 👩‍💻 Author

**Prachi**

## 📜 Internship

**CODSOFT Python Programming Internship**

**Task 4 – Movie Recommendation System**

## ⭐ Acknowledgement

Thanks to **CODSOFT** for providing the opportunity to develop practical Python projects.

## 📄 License

This project is created for educational purposes.
