# Music Recommender System

## Overview

The **Music Recommender System** is a Python-based application that leverages natural language processing (NLP) and machine learning techniques to suggest songs similar to a user-selected track based on their lyrical content. The app uses **Spotify’s API** to fetch album artwork for the recommended songs and displays the recommendations in a visually appealing format using **Streamlit**.

---

## Features

- **Lyrical Similarity-Based Recommendations**: Suggests songs based on the similarity of their lyrics using a **cosine similarity matrix**.
- **Spotify Integration**: Retrieves album artwork for recommended songs via the Spotify API.
- **Interactive Interface**: Provides an intuitive user interface for selecting songs and viewing recommendations.
- **Serialized Models for Efficiency**: Uses precomputed similarity matrices and preprocessed data stored as pickle files for faster loading and processing.

---
