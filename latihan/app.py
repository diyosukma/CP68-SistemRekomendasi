from flask import Flask, render_template, request #url_for,redirect

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from rake_nltk import Rake
import nltk
nltk.download('stopwords')
import nltk
nltk.download('punkt')

app = Flask(__name__)

new_data = {'Nama':'', 'Gender':'', 'Jurusan':'', 'Teman Berpengaruh':'', 'Lama Pertemuan':'', 'Banyak Pertemuan':'', 'Minat Bakat':''}

@app.route('/', methods=['GET'])

def hello_word():
    return render_template('index.html')

@app.route('/', methods=['POST'])

def predict():
    input_val = [i for i in request.form.values()]
    input_val_minat = [i for i in request.form.getlist('minat')]

    new_data['Nama'] = input_val[0]
    new_data['Gender'] = input_val[1]
    new_data['Jurusan'] = input_val[2]    
    new_data['Teman Berpengaruh'] = input_val[3]
    new_data['Lama Pertemuan'] = input_val[4]
    new_data['Banyak Pertemuan'] = input_val[5]

    temp_minat_bakat = ", "
    new_data['Minat Bakat'] = temp_minat_bakat.join(input_val_minat)

    def get_siswa():
        df_eskul = pd.read_excel('data_ekstrakurikuler_clean.xlsx')
        df_eskul = df_eskul[['Nama', 'Gender', 'Jurusan', 'Teman Berpengaruh', 'Lama Pertemuan', 'Banyak Pertemuan', 'Minat Bakat']]
        df_eskul['Key_words'] = ""

        df_eskul = df_eskul.append(new_data, ignore_index=True)
        for index, row in df_eskul.iterrows():
            plot = row['Minat Bakat']

            r = Rake()
            r.extract_keywords_from_text(plot)

            key_words_dict_scores = r.get_word_degrees()
            

            row['Key_words'] = list(key_words_dict_scores.keys())


        # dropping the Plot column
        df_eskul.drop(columns = ['Minat Bakat'], inplace = True)

        df_eskul.set_index('Nama', inplace = True)

        df_eskul['bag_of_words'] = ''
        columns = df_eskul.columns
        for index, row in df_eskul.iterrows():
            words = ''
            for col in columns:
                if col == 'Key_words':
                        words = words + ' '.join(row[col])+ ' '
                else:
                        words = words + row[col]+ ' '
            row['bag_of_words'] = words
            
        df_eskul.drop(columns = [col for col in df_eskul.columns if col!= 'bag_of_words'], inplace = True)

        count = CountVectorizer()
        count_matrix = count.fit_transform(df_eskul['bag_of_words'])
        cosine_sim = cosine_similarity(count_matrix, count_matrix)

        indices = pd.Series(df_eskul.index)

        def recommendations(nama, cosine_sim = cosine_sim):
        
            recommended = []
                        
            idx = indices[indices == nama].index[0]
            
            score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)

            top_indexes = list(score_series.iloc[1:2].index)
            
            for i in top_indexes:
                recommended.append(list(df_eskul.index)[i])
            
            return recommended

        return recommendations(new_data['Nama'])

    def get_ekstra():
        df_eskul = pd.read_excel('data_ekstrakurikuler_clean.xlsx')
        df_eskul = df_eskul[['Nama', 'Bidang Ekstrakurikuler', 'Gender', 'Jurusan', 'Teman Berpengaruh', 'Lama Pertemuan', 'Banyak Pertemuan', 'Minat Bakat']]

        df_eskul['Key_words'] = ""

        for index, row in df_eskul.iterrows():
            plot = row['Minat Bakat']

            r = Rake()
            r.extract_keywords_from_text(plot)

            key_words_dict_scores = r.get_word_degrees()
            

            row['Key_words'] = list(key_words_dict_scores.keys())


        # dropping the Plot column
        df_eskul.drop(columns = ['Minat Bakat'], inplace = True)

        df_eskul.set_index('Nama', inplace = True)

        df_eskul['bag_of_words'] = ''
        columns = df_eskul.columns
        for index, row in df_eskul.iterrows():
            words = ''
            for col in columns:
                if col == 'Key_words':
                        words = words + ' '.join(row[col])+ ' '
                else:
                        words = words + row[col]+ ' '
            row['bag_of_words'] = words
            
        df_eskul.drop(columns = [col for col in df_eskul.columns if col!= 'bag_of_words'], inplace = True)

        count = CountVectorizer()
        count_matrix = count.fit_transform(df_eskul['bag_of_words'])
        cosine_sim = cosine_similarity(count_matrix, count_matrix)

        indices = pd.Series(df_eskul.index)

        def recommendations(nama, cosine_sim = cosine_sim):
        
            recommended = []
            
            # gettin the index that matches the nama
            idx = indices[indices == nama].index[0]

            # creating a Series with the similarity scores in descending order
            score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)

            top_indexes = list(score_series.iloc[1:2].index)
            
            for i in top_indexes:
                recommended.append(list(df_eskul['bag_of_words'])[i])
            
            return recommended

        name = ' '.join(get_siswa())

        get_result = recommendations(name)
        for i in get_result:
            result = i.split()[0]
            
        return result

    # return render_template('index.html', recommendation_ekstra=temp_minat_bakat, user_name=new_data['Nama'])
    return render_template('index.html', recommendation_ekstra=get_ekstra(), user_name=new_data['Nama'])


if __name__ == '__main__':
    app.run(port=3000, debug=True)

    
