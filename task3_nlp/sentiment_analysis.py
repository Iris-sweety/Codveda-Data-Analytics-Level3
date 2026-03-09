# LEVEL 3 - TASK 3 : NLP Sentiment Analysis
# Dataset : Social Media Sentiments

import matplotlib
matplotlib.use("Agg")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
from wordcloud import WordCloud
from collections import Counter
from matplotlib.patches import Patch
import warnings
warnings.filterwarnings("ignore")

print("✅ All libraries imported")

# LOAD DATASET
df = pd.read_csv("task3_nlp\\3) Sentiment dataset.csv")
df = df.drop(columns=["Unnamed: 0"], errors="ignore")
df["Sentiment"] = df["Sentiment"].str.strip()
df["Text"]      = df["Text"].astype(str).str.strip()

print(f"\nShape : {df.shape}")
print(f"Columns : {df.columns.tolist()}")
print(f"Unique sentiments : {df['Sentiment'].nunique()}")

# TEXT PREPROCESSING 
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    if pd.isna(text) or text == "":
        return ""
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    tokens = word_tokenize(text)
    tokens = [w for w in tokens
              if w not in stop_words and len(w) > 2]
    tokens = [lemmatizer.lemmatize(w) for w in tokens]
    return " ".join(tokens)

df["Text_clean"] = df["Text"].apply(preprocess_text)
print("\nText preprocessing done")
print(f"Original : {df['Text'].iloc[0]}")
print(f"Cleaned  : {df['Text_clean'].iloc[0]}")

# TEXTBLOB ANALYSIS
def get_polarity(text):
    return TextBlob(str(text)).sentiment.polarity

def get_subjectivity(text):
    return TextBlob(str(text)).sentiment.subjectivity

def polarity_to_label(polarity):
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

df["Polarity"]            = df["Text_clean"].apply(get_polarity)
df["Subjectivity"]        = df["Text_clean"].apply(get_subjectivity)
df["Sentiment_predicted"] = df["Polarity"].apply(polarity_to_label)

print("\nTextBlob analysis done")
print(df["Polarity"].describe().round(4))

#SENTIMENT MAPPING
positive_words = [
    "Positive", "Joy", "Happy", "Happiness", "Hopeful",
    "Gratitude", "Excitement", "Love", "Optimism", "Pride",
    "Amusement", "Relief", "Enjoyment", "Admiration",
    "Affection", "Awe", "Acceptance", "Adoration",
    "Calmness", "Kind"
]

negative_words = [
    "Negative", "Sad", "Sadness", "Anger", "Fear",
    "Disgust", "Frustration", "Anxiety", "Hate",
    "Regret", "Bad", "Embarrassed", "Mischievous",
    "Bitter", "Disappointed"
]

neutral_words = [
    "Neutral", "Curiosity", "Surprise",
    "Confusion", "Anticipation"
]

def assign_sentiment(row):
    label = row["Sentiment"]
    if label in positive_words:
        return "Positive"
    elif label in negative_words:
        return "Negative"
    elif label in neutral_words:
        return "Neutral"
    else:
        return row["Sentiment_predicted"]

df["Sentiment_final"] = df.apply(assign_sentiment, axis=1)

known    = positive_words + negative_words + neutral_words
direct   = df[df["Sentiment"].isin(known)].shape[0]
fallback = df[~df["Sentiment"].isin(known)].shape[0]

print(f"\nClassified from original label  : {direct}")
print(f"Classified by TextBlob fallback : {fallback}")
print(f"\nFinal distribution :")
print(df["Sentiment_final"].value_counts())

# COLOR PALETTE
colors = {
    "Positive": "#2ECC5D",
    "Negative": "#E74C3C",
    "Neutral" : "#3498DB"
}

#SENTIMENT DISTRIBUTION
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

df["Sentiment"].value_counts().head(15).plot(
    kind="bar", ax=axes[0],
    color="steelblue", edgecolor="white"
)
axes[0].set_title("Original Sentiment (Top 15)")
axes[0].set_xlabel("Sentiment")
axes[0].set_ylabel("Count")
axes[0].tick_params(axis="x", rotation=45)
axes[0].grid(True, alpha=0.3, axis="y")

grouped_counts = df["Sentiment_final"].value_counts()
grouped_counts.plot(
    kind="bar", ax=axes[1],
    color=[colors.get(s, "gray") for s in grouped_counts.index],
    edgecolor="white"
)
axes[1].set_title("Final Grouped Sentiment")
axes[1].set_xlabel("Sentiment")
axes[1].set_ylabel("Count")
axes[1].tick_params(axis="x", rotation=0)
axes[1].grid(True, alpha=0.3, axis="y")

plt.suptitle("Sentiment Distribution", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig("task3_nlp\\results\\sentiment_distribution.png", dpi=150, bbox_inches="tight")
plt.close()
print("sentiment_distribution.png saved")

#POLARITY & SUBJECTIVITY
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for sentiment, color in colors.items():
    subset = df[df["Sentiment_final"] == sentiment]["Polarity"]
    axes[0].hist(subset, bins=30, alpha=0.6,
                 color=color, label=sentiment, edgecolor="white")

axes[0].axvline(0, color="black", linestyle="--", lw=1.5)
axes[0].set_title("Polarity Distribution by Sentiment")
axes[0].set_xlabel("Polarity Score")
axes[0].set_ylabel("Count")
axes[0].legend()
axes[0].grid(True, alpha=0.3)

scatter_colors = df["Sentiment_final"].map(colors)
axes[1].scatter(df["Polarity"], df["Subjectivity"],
                c=scatter_colors, alpha=0.4, s=20)
axes[1].axvline(0, color="black", linestyle="--", lw=1)
axes[1].set_title("Polarity vs Subjectivity")
axes[1].set_xlabel("Polarity")
axes[1].set_ylabel("Subjectivity")
axes[1].grid(True, alpha=0.3)

legend_elements = [Patch(facecolor=c, label=s)
                   for s, c in colors.items()]
axes[1].legend(handles=legend_elements)

plt.tight_layout()
plt.savefig("task3_nlp\\results\\polarity_subjectivity.png", dpi=150, bbox_inches="tight")
plt.close()
print("polarity_subjectivity.png saved")

#SENTIMENT BY PLATFORM & COUNTRY
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

platform_sentiment = df.groupby(
    ["Platform", "Sentiment_final"]
).size().unstack(fill_value=0)

platform_sentiment.plot(
    kind="bar", ax=axes[0],
    color=[colors.get(c, "gray")
           for c in platform_sentiment.columns],
    edgecolor="white"
)
axes[0].set_title("Sentiment by Platform")
axes[0].set_xlabel("Platform")
axes[0].set_ylabel("Count")
axes[0].tick_params(axis="x", rotation=45)
axes[0].legend(title="Sentiment")
axes[0].grid(True, alpha=0.3, axis="y")

top_countries = df["Country"].value_counts().head(10).index
country_data  = df[df["Country"].isin(top_countries)]
country_sent  = country_data.groupby(
    ["Country", "Sentiment_final"]
).size().unstack(fill_value=0)

country_sent.plot(
    kind="bar", ax=axes[1],
    color=[colors.get(c, "gray")
           for c in country_sent.columns],
    edgecolor="white"
)
axes[1].set_title("Sentiment by Top 10 Countries")
axes[1].set_xlabel("Country")
axes[1].set_ylabel("Count")
axes[1].tick_params(axis="x", rotation=45)
axes[1].legend(title="Sentiment")
axes[1].grid(True, alpha=0.3, axis="y")

plt.tight_layout()
plt.savefig("task3_nlp\\results\\sentiment_platform_country.png",
            dpi=150, bbox_inches="tight")
plt.close()
print("sentiment_platform_country.png saved")

#SENTIMENT OVER TIME 
monthly = df.groupby(
    ["Year", "Month", "Sentiment_final"]
).size().unstack(fill_value=0)

plt.figure(figsize=(14, 5))
for sentiment, color in colors.items():
    if sentiment in monthly.columns:
        plt.plot(range(len(monthly)),
                 monthly[sentiment],
                 label=sentiment, color=color,
                 lw=2, marker="o", markersize=4)

plt.title("Sentiment Trend Over Time")
plt.xlabel("Time Period (Year-Month)")
plt.ylabel("Count")
plt.xticks(
    range(len(monthly)),
    [f"{y}-{m:02d}" for y, m in monthly.index],
    rotation=45, ha="right"
)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("task3_nlp\\results\\sentiment_over_time.png", dpi=150, bbox_inches="tight")
plt.close()
print("sentiment_over_time.png saved")

#ENGAGEMENT ANALYSIS 
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

df.groupby("Sentiment_final")["Likes"].mean().plot(
    kind="bar", ax=axes[0],
    color=[colors.get(s, "gray")
           for s in df.groupby("Sentiment_final")["Likes"].mean().index],
    edgecolor="white"
)
axes[0].set_title("Average Likes by Sentiment")
axes[0].set_xlabel("Sentiment")
axes[0].set_ylabel("Avg Likes")
axes[0].tick_params(axis="x", rotation=0)
axes[0].grid(True, alpha=0.3, axis="y")

df.groupby("Sentiment_final")["Retweets"].mean().plot(
    kind="bar", ax=axes[1],
    color=[colors.get(s, "gray")
           for s in df.groupby("Sentiment_final")["Retweets"].mean().index],
    edgecolor="white"
)
axes[1].set_title("Average Retweets by Sentiment")
axes[1].set_xlabel("Sentiment")
axes[1].set_ylabel("Avg Retweets")
axes[1].tick_params(axis="x", rotation=0)
axes[1].grid(True, alpha=0.3, axis="y")

plt.tight_layout()
plt.savefig("task3_nlp\\results\\engagement_by_sentiment.png",
            dpi=150, bbox_inches="tight")
plt.close()
print("engagement_by_sentiment.png saved")

print("\nEngagement Stats :")
print(df.groupby("Sentiment_final")[
    ["Likes", "Retweets"]].mean().round(2))

#WORD CLOUDS
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

colormaps = {
    "Positive": "Greens",
    "Negative": "Reds",
    "Neutral" : "Blues"
}

for ax, sentiment in zip(axes, ["Positive", "Negative", "Neutral"]):
    text = " ".join(
        df[df["Sentiment_final"] == sentiment]["Text_clean"].dropna()
    )
    if len(text.strip()) == 0:
        ax.set_title(f"{sentiment} — No data")
        ax.axis("off")
        continue

    wc = WordCloud(
        width=600, height=400,
        background_color="white",
        colormap=colormaps[sentiment],
        max_words=100,
        collocations=False
    ).generate(text)

    ax.imshow(wc, interpolation="bilinear")
    ax.set_title(f"{sentiment} Sentiment",
                 fontsize=13, fontweight="bold")
    ax.axis("off")

plt.suptitle("Word Clouds by Sentiment",
             fontsize=15, fontweight="bold")
plt.tight_layout()
plt.savefig("task3_nlp\\results\\wordclouds.png", dpi=150, bbox_inches="tight")
plt.close()
print(" wordclouds.png saved")

#WORD FREQUENCY 
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

for ax, (sentiment, color) in zip(
    axes, [("Positive", "#2ECC71"),
           ("Negative", "#E74C3C"),
           ("Neutral",  "#3498DB")]
):
    text = " ".join(
        df[df["Sentiment_final"] == sentiment]["Text_clean"].dropna()
    )
    word_freq = Counter(text.split()).most_common(15)
    words  = [w[0] for w in word_freq]
    counts = [w[1] for w in word_freq]

    ax.barh(words[::-1], counts[::-1],
            color=color, edgecolor="white")
    ax.set_title(f"Top 15 Words — {sentiment}",
                 fontweight="bold")
    ax.set_xlabel("Frequency")
    ax.grid(True, alpha=0.3, axis="x")

plt.suptitle("Most Frequent Words by Sentiment",
             fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("task3_nlp\\results\\word_frequency.png", dpi=150, bbox_inches="tight")
plt.close()
print("word_frequency.png saved")

#  HASHTAG ANALYSIS
try:
    all_hashtags = df["Hashtags"].dropna().str.strip()
    all_hashtags = all_hashtags[all_hashtags != ""]
    all_hashtags = all_hashtags.str.split().explode()
    top_hashtags = all_hashtags.value_counts().head(15)

    plt.figure(figsize=(10, 5))
    top_hashtags.plot(
        kind="barh", color="steelblue", edgecolor="white"
    )
    plt.title("Top 15 Most Used Hashtags")
    plt.xlabel("Count")
    plt.gca().invert_yaxis()
    plt.grid(True, alpha=0.3, axis="x")
    plt.tight_layout()
    plt.savefig("task3_nlp\\results\\top_hashtags.png", dpi=150, bbox_inches="tight")
    plt.close()
    print(" top_hashtags.png saved")
except Exception as e:
    print(f"⚠️ Hashtag analysis skipped : {e}")

#FINAL SUMMARY 
print("📊 FINAL SUMMARY")
print("="*50)
print(f"Total posts analyzed     : {len(df):,}")
print(f"Unique original sentiments: {df['Sentiment'].nunique()}")
print(f"\nFinal Sentiment Distribution :")
print(df["Sentiment_final"].value_counts())
print(f"\nAvg Polarity  : {df['Polarity'].mean():.4f}")
print(f"Avg Subjectivity : {df['Subjectivity'].mean():.4f}")
print(f"\nEngagement by Sentiment :")
print(df.groupby("Sentiment_final")[
    ["Likes", "Retweets"]].mean().round(2))
print("\n✅ All outputs saved successfully !")
