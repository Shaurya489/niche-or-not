# Niche or Not

A classification tool that determines the popularity and "niche-ness" of movies, anime, artists, and other media content using machine learning and data from multiple APIs.

## Overview

**Niche or Not** helps you understand whether a piece of media is mainstream or niche by analyzing various classification parameters. Whether you're curious about a movie's market penetration, an anime's fanbase size, or an artist's reach, this tool provides data-driven insights.

## Features

- Movie Classification - Analyze movie popularity using TMDB API
- Anime Analysis - Classify anime content using Jikan API
- Artist Insights - Determine artist reach and fanbase size
- Multiple Parameters - Uses relevant classification metrics for each content type
- Machine Learning - Intelligent classification algorithms to determine niche vs mainstream

## Tech Stack

- **TMDB API** - Movie database and statistics
- **Jikan API** - Anime data and information
- Additional APIs for artist/music data (configurable)

## Installation

```bash
# Clone the repository
git clone https://github.com/Shaurya489/niche-or-not.git
cd niche-or-not

# Install dependencies
pip install -r requirements.txt

# Set up API keys
# Add your TMDB and Jikan API keys to .env file
```

## Configuration

Create a `.env` file in the root directory:

```
TMDB_API_KEY=your_tmdb_api_key_here
JIKAN_API_KEY=your_jikan_api_key_here
```

## Usage

```python
from niche_or_not import NicheClassifier

classifier = NicheClassifier()

# Classify a movie
movie_result = classifier.classify_movie("Movie Title")
print(movie_result)

# Classify an anime
anime_result = classifier.classify_anime("Anime Title")
print(anime_result)

# Classify an artist
artist_result = classifier.classify_artist("Artist Name")
print(artist_result)
```

## How It Works

The classifier analyzes various parameters for each content type:

- **Popularity Score** - Raw popularity metric from the API
- **User Ratings** - Average ratings from the community
- **Number of Reviews** - Volume of user engagement
- **Release Date** - Temporal factors affecting mainstream appeal
- **Genre/Tags** - Content categorization
- **Social Metrics** - Engagement and reach indicators

Using these parameters, the model classifies content as:
- **Mainstream** - Widely known and popular
- **Semi-Niche** - Growing audience with some recognition
- **Niche** - Specialized audience, limited mainstream appeal

## Project Structure

```
niche-or-not/
├── README.md
├── requirements.txt
├── .env.example
├── niche_or_not/
│   ├── __init__.py
│   ├── classifier.py
│   ├── api/
│   │   ├── tmdb.py
│   │   ├── jikan.py
│   │   └── base.py
│   └── models/
│       ├── classifier_model.py
│       └── utils.py
└── tests/
    └── test_classifier.py
```

## API References

- [TMDB API Documentation](https://www.themoviedb.org/settings/api)
- [Jikan API Documentation](https://docs.api.jikan.moe/)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Shaurya489**

## Support

If you encounter any issues or have suggestions, please open an issue on the [GitHub repository](https://github.com/Shaurya489/niche-or-not/issues).

---

Made with care by Shaurya489
