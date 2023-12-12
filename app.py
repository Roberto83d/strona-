pip install Flask
from flask import Flask

# Tworzenie instancji aplikacji Flask
app = Flask(__name__)

# Definicja trasy - obsługa adresu głównego ('/')
@app.route('/')
def hello():
    return 'Witaj, Świecie!'

# Uruchomienie serwera Flask
if __name__ == '__main__':
    app.run(debug=True)
