import pandas as pd
import re
from nltk.stem import PorterStemmer
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# -----------------------------------------
# CREATE STEMMER
# -----------------------------------------

ps = PorterStemmer()

# -----------------------------------------
# SELECT CSV FILE
# -----------------------------------------

Tk().withdraw()

print("Select your BBC News CSV file...")

file_path = askopenfilename(
    title="Select BBC News Dataset",
    filetypes=[("CSV Files", "*.csv")]
)

if file_path == "":
    print("No file selected.")
    exit()

print("\nSelected file:")
print(file_path)

# -----------------------------------------
# READ DATASET
# -----------------------------------------

data = pd.read_csv(file_path)

print("\nDataset loaded successfully!")
print("Columns:", data.columns.tolist())
print("Number of rows:", len(data))

# -----------------------------------------
# FIND TEXT COLUMN
# -----------------------------------------

possible_columns = [
    "Text",
    "text",
    "Article",
    "article",
    "Content",
    "content",
    "Description",
    "description"
]

text_column = None

for column in possible_columns:
    if column in data.columns:
        text_column = column
        break

if text_column is None:

    print("\nERROR: Text column was not found.")

    print("Your columns are:")
    print(data.columns.tolist())

    exit()

print("\nText column selected:", text_column)

# -----------------------------------------
# STEMMING FUNCTION
# -----------------------------------------

def stem_text(text):

    text = str(text).lower()

    words = re.findall(r"[a-z]+", text)

    stems = []

    for word in words:
        stems.append(ps.stem(word))

    return " ".join(stems)

# -----------------------------------------
# APPLY PORTER STEMMER
# -----------------------------------------

data["Processed"] = data[text_column].apply(stem_text)

# -----------------------------------------
# ORIGINAL VS STEMMED
# -----------------------------------------

print("\n")
print("=" * 70)
print("ORIGINAL VS STEMMED")
print("=" * 70)

for i in range(min(5, len(data))):

    print("\nARTICLE", i + 1)

    print("\nOriginal:")
    print(str(data[text_column].iloc[i])[:300])

    print("\nStemmed:")
    print(data["Processed"].iloc[i][:300])

    print("\n" + "-" * 70)

# -----------------------------------------
# 20 STEMMING CASES
# -----------------------------------------

words = [
    "organization",
    "organizer",
    "organizing",
    "organized",
    "government",
    "governments",
    "national",
    "nationality",
    "nationalize",
    "connection",
    "connected",
    "connecting",
    "development",
    "developing",
    "developed",
    "players",
    "playing",
    "happiness",
    "unbelievable"
]

print("\n")
print("=" * 70)
print("20 STEMMING ERROR CASES")
print("=" * 70)

print(
    "{:<20} {:<20} {:<20}".format(
        "WORD",
        "STEM",
        "TYPE"
    )
)

print("-" * 70)

for word in words:

    stem = ps.stem(word)

    # Morphological classification
    if word in [
        "organizing",
        "organized",
        "governments",
        "connected",
        "connecting",
        "developing",
        "developed",
        "players",
        "playing"
    ]:
        morphology = "Inflectional"
    else:
        morphology = "Derivational"

    print(
        "{:<20} {:<20} {:<20}".format(
            word,
            stem,
            morphology
        )
    )

# -----------------------------------------
# SAVE OUTPUT
# -----------------------------------------

output_file = file_path.replace(
    ".csv",
    "_Stemmed.csv"
)

data.to_csv(
    output_file,
    index=False
)

# -----------------------------------------
# FINAL OUTPUT
# -----------------------------------------

print("\n")
print("=" * 70)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 70)

print("Input file:")
print(file_path)

print("\nOutput file:")
print(output_file)

print("\nTotal articles:", len(data))
