from flask import Flask, render_template, request, redirect, url_for
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('karaoke.db')
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db_connection()
conn.execute('''
    CREATE TABLE IF NOT EXISTS songs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        artist TEXT NOT NULL,
        joysound BOOLEAN NOT NULL DEFAULT 0,
        dam BOOLEAN NOT NULL DEFAULT 0,
        favorite BOOLEAN NOT NULL DEFAULT 0
    )
''')
conn.commit()
conn.close()

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    
    conn = get_db_connection()
    songs = conn.execute('SELECT * FROM songs').fetchall()
    conn.close()
    
    
    search_word = request.args.get('search', '')  # 検索ワードを取得（デフォルトは空文字）
    filter_type = request.args.get('filter', 'all')  # フィルターの種類を取得（デフォルトは'all'）
    filtered_songs = []
    
    if search_word:
        for song in songs:
            if search_word.lower() in song['title'].lower() or search_word.lower() in song['artist'].lower():
                filtered_songs.append(song)  # 曲名またはアーティスト名に検索ワードが含まれている場合はリストに追加
    else:
        filtered_songs = songs  # 検索ワードが空の場合は全ての曲を表示
        
    if filter_type == 'favorite':
        filtered_songs = [song for song in filtered_songs if song['favorite'] == 1]  # お気に入りのみ表示
            

    if request.method == "POST":
        action = request.form.get('action')  # フォームからアクションを取得（追加か削除か） 
        song_id = request.form.get('song_id')  # フォームから曲IDを取得（編集用）
        
        if action == 'toggle_favorite':
            conn = get_db_connection()
            conn.execute(
                'UPDATE songs SET favorite = CASE WHEN favorite = 1 THEN 0 ELSE 1 END WHERE id = ?',
                (song_id,)
            )
            conn.commit()
            conn.close()
        elif song_id:
            conn = get_db_connection()
            conn.execute('DELETE FROM songs WHERE id = ?', (song_id,))
            conn.commit()
            conn.close()
        else:
            song_title = request.form.get('song_title')
            artist = request.form.get('artist')
            joysound = request.form.get('joysound')  # joysoundのチェックボックスの値を取得
            dam = request.form.get('dam')  # damのチェックボックスの値を取得
            favorite = request.form.get('favorite')  # favoriteのチェックボックスの値を取得
            conn = get_db_connection()
            conn.execute(
                'INSERT INTO songs (title, artist, joysound, dam, favorite) VALUES (?, ?, ?, ?, ?)', 
                (
                    song_title, 
                    artist, 
                    1 if joysound == 'on' else 0,  # joysoundがチェックされている場合は1、そうでない場合は0
                    1 if dam == 'on' else 0,  # damがチェックされている場合は1、そうでない場合は0
                    1 if favorite == 'on' else 0  # favoriteがチェックされている場合は1、そうでない場合は0
                )
            )
            conn.commit()
            conn.close()
        return redirect(url_for('index'))  # 追加後にトップページへリダイレクト

    return render_template('index.html' , songs=filtered_songs, search_word=search_word)

if __name__ == '__main__':
    app.run(debug=True)
    
