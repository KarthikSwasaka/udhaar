import nltk
import wordcloud
from nltk.corpus import stopwords
from wordcloud import WordCloud

set(stopwords.words('english'))


def handle_uploaded_file(f):
    with open('myapp/static/upload/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            with open("myapp/static/upload/", "r") as f:
                words = f.read().split()
                data = dict()
                for word in words:
                    word = word.lower()
                    if word in stop_words:
                        continue

                    data[word] = data.get(word, 0) + 1
                    word_cloud = WordCloud(
                        background_color=background_color,
                        width=width,
                        height=height
                    )

                    word_cloud.generate_from_frequencies(data)
                    word_cloud.to_file('image.png')