#  Level 3 - Task 3 : NLP Sentiment Analysis
**Internship** : Codveda Technologies — Data Analytics  
**Level** : 3 (Advanced)  
**Dataset** : Social Media Sentiments (732 posts)  
**Tools** : Python, nltk, TextBlob, pandas, matplotlib, wordcloud

---

## 🎯 Objective
Preprocess social media text data, classify posts into
Positive / Negative / Neutral sentiments using TextBlob,
and visualize sentiment distribution, word frequencies
and engagement patterns.


---

## 🛠️ Tools & Libraries
| Library | Usage |
|---------|-------|
| `pandas` | Data loading and manipulation |
| `nltk` | Tokenization, stopwords, lemmatization |
| `TextBlob` | Polarity and subjectivity scoring |
| `wordcloud` | Word cloud generation |
| `matplotlib` | All visualizations |
| `seaborn` | Statistical plots |

---

## ⚙️ Methodology

### Text Preprocessing Pipeline
| Step | Description |
|------|-------------|
| Lowercasing | Normalize text case |
| Remove URLs | Clean http links |
| Remove mentions | Remove @username |
| Remove hashtag symbol | Keep the word, remove # |
| Remove punctuation | Keep only words |
| Tokenization | Split text into words |
| Remove stopwords | Remove common words |
| Lemmatization | Reduce to base form |

### Sentiment Classification Strategy
The original dataset contains **191 unique sentiment labels**
(e.g. "Culinary Adventure", "Winter Magic") — far too granular
for standard 3-class classification.

Two-step approach used :
1. **Direct mapping** : known labels (Joy, Anger, Neutral...)
   mapped to Positive / Negative / Neutral
2. **TextBlob fallback** : unknown labels classified by
   polarity score (> 0.1 = Positive, < -0.1 = Negative)

---

## 📈 Results

### Sentiment Distribution
| Sentiment | Count | % |
|-----------|-------|---|
| **Positive** | 335 | 45.8% |
| **Neutral** | 284 | 38.8% |
| **Negative** | 113 | 15.4% |

The dataset is **predominantly positive** — typical of
curated social media content where users share
experiences and emotions.

**Top original labels :**
Positive (45) > Joy (44) > Excitement (37) >
Contentment (19) > Neutral (18) > Gratitude (16)

---

### Polarity & Subjectivity Analysis
- Most posts cluster around **polarity = 0** (neutral zone)
  due to short, ambiguous social media text
- **Positive posts** spread widely to the right (0.1 to 1.0)
- **Negative posts** are concentrated between -0.5 and 0
  → negative emotions are expressed more moderately
- High subjectivity (0.8-1.0) is present across all
  sentiments → social media text is generally opinion-based
- TextBlob struggles with very short or metaphorical text
  → large neutral cluster at polarity = 0

---

### Sentiment by Platform
| Platform | Positive | Neutral | Negative |
|----------|----------|---------|----------|
| Facebook | 107 | 91 | 31 |
| Instagram | 116 | 103 | 38 |
| Twitter | 61 | 46 | 21 |
| Twitter* | 50 | 44 | 21 |

*Two Twitter entries suggest slight data inconsistency
in platform naming (case or spacing difference)

**Instagram** has the highest volume of posts across
all sentiment categories — most active platform in
this dataset.

---

### Sentiment by Country
- **USA** dominates in volume across all sentiments
- **UK** and **Canada** follow as the most active countries
- **Positive** sentiment is the dominant category in
  every country — consistent global pattern
- **Australia** shows a relatively balanced distribution
  between Positive and Neutral

---

### Engagement Analysis
| Sentiment | Avg Likes | Avg Retweets |
|-----------|-----------|--------------|
| Negative | 37.2 | 18.5 |
| Neutral | 41.8 | 21.2 |
| Positive | 45.7 | 22.8 |

**Positive posts generate the most engagement** — both
likes and retweets increase progressively from
Negative → Neutral → Positive. Users are more likely
to interact with uplifting and joyful content.

---

### Word Frequency Analysis

**Top Positive words :**
`new`, `joy`, `life`, `laughter`, `friend`, `day`,
`time`, `art`, `moment`, `beauty`, `gratitude`
→ Themes of **social connection, celebration and beauty**

**Top Negative words :**
`feeling`, `day`, `grief`, `frustration`, `broken`,
`bad`, `regret`, `shattered`, `wandering`
→ Themes of **loss, frustration and emotional pain**

**Top Neutral words :**
`dream`, `life`, `like`, `moment`, `heart`, `curiosity`,
`whisper`, `journey`, `echo`
→ Themes of **reflection, introspection and uncertainty**

---

### Top Hashtags
| Rank | Hashtag | Count |
|------|---------|-------|
| 1 | #Serenity | 15 |
| 2 | #Gratitude | 13 |
| 3 | #Excitement | 13 |
| 4 | #Despair | 11 |
| 5 | #Nostalgia | 11 |
| 6 | #Contentment | 10 |
| 7 | #Curiosity | 10 |
| 8 | #Awe | 9 |
| 9 | #Grief | 9 |
| 10 | #Loneliness | 9 |

Hashtags reflect a mix of **positive emotions** (#Serenity,
#Gratitude, #Excitement) and **introspective/negative ones**
(#Despair, #Nostalgia, #Grief) — consistent with the
overall sentiment distribution.

---

## ✅ Conclusion

| Metric | Value |
|--------|-------|
| Total posts analyzed | 732 |
| Unique original sentiments | 191 |
| Final Positive | 335 (45.8%) |
| Final Neutral | 284 (38.8%) |
| Final Negative | 113 (15.4%) |
| Best engaging sentiment | Positive (45.7 avg likes) |
| Most used hashtag | #Serenity (15) |
| Most active platform | Instagram |
| Most active country | USA |

**Key findings :**
- Social media content in this dataset skews **positive**
  with 45.8% positive posts
- **Positive posts generate 23% more likes** than negative
  ones → positivity drives engagement
- **Instagram** is the most active platform for
  emotional expression
- The word `new` dominates positive posts → users share
  new experiences and discoveries
- `grief` and `feeling` dominate negative posts →
  emotional processing is a key driver of negative content
- TextBlob performs well on clear emotional text but
  assigns neutral polarity to short/metaphorical posts

**Limitations :**
- TextBlob is not optimized for social media slang
- 191 original labels required a hybrid classification
  approach — some ambiguity remains

**Next steps :**
- Use **VADER** (better for social media text)
- Train a supervised classifier (Logistic Regression, BERT)
- Topic modeling with **LDA** to extract themes
- Analyze sentiment trends by platform over time

---

## 🚀 How to Run

1. Install dependencies
```bash
pip install pandas numpy matplotlib seaborn nltk textblob wordcloud
```

2. Download NLTK resources
```bash
python download_nltk.py
```

3. Run sentiment analysis
```bash
python sentiment.py
```

---

*Codveda Technologies Internship — Data Analytics | 2026*