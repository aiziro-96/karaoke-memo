from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    
    songs = [{'title':'怪物', 'artist': 'YOASOBI'}, {'title':'夜に駆ける', 'artist': 'YOASOBI'}, {'title':'群青', 'artist': 'YOASOBI'}]
    
    search_word = request.args.get('search', '')  # 検索ワードを取得（デフォルトは空文字）
    filtered_songs = []
    
    if search_word:
        for song in songs:
            if search_word.lower() in song['title'].lower() or search_word.lower() in song['artist'].lower():
                filtered_songs.append(song)  # 曲名またはアーティスト名に検索ワードが含まれている場合はリストに追加
    else:
        filtered_songs = songs  # 検索ワードが空の場合は全ての曲を表示
            
    return render_template('index.html' , songs=filtered_songs, search_word=search_word)


if __name__ == '__main__':
    app.run(debug=True)
    
