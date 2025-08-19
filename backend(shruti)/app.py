from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret_key_here"  # required for session management

# Temporary database (dictionary) – in real apps, use SQLite/MySQL
users = {}
mood_songs = {
    "Happy": [
        {"Mood": "Happy", "Quote": "Happiness is a journey, not a destination.", "Song": "love you zindagi - dear zindagi", "link": "https://youtu.be/bw7bVpI5VcM?si=xW9jR7TNb4e9GwvR"},
        {"Mood": "Happy", "Quote": "Smile, it’s free therapy.", "Song": "phir se udd chala - Rockstar", "link": "https://youtu.be/-3gQ6HIkRys?si=wrUlnIxo_QMuOtiU"},
        {"Mood": "Happy", "quote" : "One whose happiness is within … attains liberation.","Song":"Dil Dhadkane do - Zindagi na milegi dobara","link":"https://youtu.be/PyTaSNvflM0?si=BDvdssDCiwc5s4Cu"},
        {"Mood": "Happy", "Quote": "Detached from external contacts, he finds happiness in the Self.","song":"Man ki Lagan - Paap","link" :"https://youtu.be/tuxzfwUVSlE?si=Y_uThfWSsL5qvJUx"},
        {"Mood": "Happy", "Quote": "A day without laughter is a day wasted.", "Song": "Gallan goodiyan - dil dhadkane do", "link": "https://youtu.be/jCEdTq3j-0U?si=b1u1heCu7cUMGrC2"}
    ],
    "Sad": [
        {"Mood": "Sad",  "Quote": "Tears are words that the heart can’t express.", "Song": "Agar tum saath ho - Tamasha","link":"https://youtu.be/dhY8jRNELUc?si=qnAUN2uC7A6IhB6d"},
        {"Mood": "Sad",  "Quote": "Sometimes you just need a good cry.", "Song": "Ae dil hai mushkil - Ae dil hai mushkil","link":"https://youtu.be/6FURuLYrR_Q?si=mj46gzBAmj5Qomth" },
        {"Mood" : "Sad", "Quote": "Every storm runs out of rain.", "Song": "Raabta - agent vinod","link":"https://youtu.be/zAU_rsoS5ok?si=Dzh6ROOBNqdWKqOU" },
        {"Mood": "Sad",  "Quote":"For one who is born, death is certain… therefore you should not lament","song":"Zinda - lootera","link":"https://youtu.be/cgHLvt0rxmM?si=zBg79n47rWq9Vwxw"},
        {"Mood": "Sad",  "quote": "You grieve for what is not worthy of grief; the wise lament neither for the living nor the dead.","song":"Chale chalo - Lagan","link":"https://youtu.be/LQmHKl3oNu0?si=VVULvroUZ45Lr6Gt" }
    ],
    "Emotional": [
        {"Mood": "Emotional", "Quote": "Wherever the restless mind wanders, bring it back under the control of the Self.", "Song": "Kun Faya Kun - Rockstar","Link":"https://youtu.be/0RDI9CMilhk?si=iAvx-1pkxan-GQ_7"},
        {"Mood": "Emotional", "Quote": "Lift yourself by your own Self; the mind is one’s friend and enemy", "Song": "","link":""},
        {"Mood": "Emotional", "Quote": "Sometimes the heaviest burdens are the ones we carry silently, hidden behind a smile", "Song": "","link":""},
        {"Mood": "Emotional", "quotes":"The heart remembers what the mind tries to forget, and in that memory lies both pain and beauty","song":"","link":""},
        {"Mood": "Emotional", "Quotes":"Some scars are invisible, yet they shape us more than any wound ever could","song":"","link":""}
    ],
    "Neutral": [
        {"Mood": "Neutral", "Quote": "Be steadfast in yoga; perform your duty, abandoning attachment; equanimity is yoga", "Song": "","link":""},
        {"Mood": "Neutral", "Quote": "Cold and heat, pleasure and pain… endure them, O Arjuna", "Song": "","link":""},
        {"Mood": "Neutral", "Quote": "Every day is a page in the story of your life; some are quiet, some are loud, but each is worth reading.", "Song": "","link":""},
        {"Mood": "Neutral", "Quote": "Life flows like a river—sometimes calm, sometimes restless, but always moving forward", "Song": "","link":""},
        {"Mood": "Neutral", "Quote": "The mind finds clarity when we simply observe, without needing to change anything", "Song": "","link":""}
    ],
    "Angry": [
        {"Mood": "Angry", "Quote": "Speak when you are angry and you'll make the best speech you'll ever regret.", "Song": "Bulleya - Ae dil hai mushkil", "link": ""},
        {"Mood": "Angry", "Quote": "Anger is one letter short of danger.", "Song": "Bekhayali - kabir singh", "link": ""},
        {"Mood": "Angry",  "Quote":"From anger arises delusion… and one falls down from the spiritual platform","song":"", "link":""},
        {"Mood": "Angry",  "quote":"Anger is a storm; let it pass, or it will drown the calm within you.","Song":"","link":""},
        {"Mood": "Angry", "Quote": "Don't let anger control you, let it teach you.", "Song": "Jee karda - Badlapur", "link": ""}
    ],
    "Love": [
        {"Mood": "Love", "Quote": "You are my today and all of my tomorrows.", "Song": "tum mile - tum mile", "link": ""},
        {"Mood": "Love", "Quote": "Every love story is beautiful, but ours is my favorite.", "Song": "teri meri kahani - gabbar is back", "link": ""},
        {"Mood": "Love", "Quote": "Love is composed of a single soul inhabiting two bodies.", "Song": "janam janam - dilwale", "link": ""},
        {"Mood": "Love", "quote":"Always think of Me, be devoted to Me, worship Me…","song":"","link":""},
        {"Mood": "Love", "Quote":"Fix your mind on Me… you will come to Me; you are dear to Me","song":"","link":""}
    ],
    "Excited": [
        {"Mood": "Excited", "Quote": "Worker in goodness: free from attachment, fearless, enthusiastic (utsāha), and resolute.", "Song": "","Link":""},
        {"Mood": "Excited", "Quote": "Embrace the thrill—today is yours to conquer.", "Song": "","link":""},
        {"Mood": "Excited", "Quote": "Adventure begins the moment you decide to feel alive", "Song": "","link":""},
        {"Mood": "Excited", "quote":"Every heartbeat feels like a drum, and the world is ready for your dance","song":"","link":""},
        {"Mood": "Excited", "Quote":"When joy sparks in your chest, let it light up everything around you","Song":"","Link":""}
    ],
    "Relaxed": [
        {"Mood": "Relaxed", "Quote": "As rivers enter the full, unmoving ocean… such a person alone attains peace", "Song": "","link":""},
        {"Mood": "Relaxed", "Quote": "Self-controlled, moving among objects… attains tranquility; in tranquility all sorrows end", "Song": "","link":""},
        {"Mood": "Relaxed", "Quote": "Breathe deeply; even the quietest moments have their own melody.", "Song": "","link":""},
        {"Mood": "Relaxed", "Quote": "Let the world move around you while you find stillness within", "Song": "","link":""},
        {"Mood": "Relaxed", "Quote": "In the calm, we find clarity, and in clarity, we find ourselves", "Song": "","link":""}
    ],
    "Romantic": [
        {"Mood": "Romantic", "Quote": "Love isn’t just a feeling; it’s the quiet moments that make life magical", "Song": "","link":""},
        {"Mood": "Romantic", "Quote": "Every heartbeat whispers your name, even when we’re apart", "Song": "","Link":""},
        {"Mood": "Romantic", "Quote": "Some souls are meant to meet, and ours collided like a spark in the dark", "Song": "","link":""},
        {"Mood": "Romantic", "Quote": "In your eyes, I find the home my heart has always sought", "Song": "","link":""},
        {"Mood": "Romantic", "Quote": "To love you is to see the world in brighter colors and softer light", "Song": "","link":""}
    ]
}

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            return "⚠ User already exists! Try another username."
        
        users[username] = password
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return "❌ Invalid username or password!"
    return render_template("login.html")

@app.route("/welcome")
def welcome():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("welcome.html", moods=mood_songs.keys())

@app.route("/mood/<mood>")
def mood_page(mood):
    if "user" not in session:
        return redirect(url_for("login"))

    song = mood_songs.get(mood, "No song available for this mood.")
    return render_template("mood.html", mood=mood, song=song)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
