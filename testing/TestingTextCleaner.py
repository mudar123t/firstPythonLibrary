import pandas as pd
from dataMnp import TextCleaner


data = {
    'text': ["This is a sample text with stopwords and punctuation!",
             "It also contains different cases of letters, and needs lemmatization.",
             "Let's see how the text cleaner works to process this data."]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nDataFrame after removing stop words:")
df1 = TextCleaner.remove_stopwords(df.copy(), 'text')
print(df1)

df2 = TextCleaner.lowercase(df.copy(), 'text')
print("\nDataFrame after converting text to lowercase:")
print(df2)

df3 = TextCleaner.remove_punctuation(df.copy(), 'text')
print("\nDataFrame after removing punctuation:")
print(df3)

df4 = TextCleaner.lemmatize(df.copy(), 'text')
print("\nDataFrame after lemmatizing text:")
print(df4)
