# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Route pour la racine (/)
@app.route('/')
def index():
    return redirect(url_for('parureception'))

# Route pour la première page
@app.route('/parureception')
def parureception():
    return render_template('parureception.html')

# Route pour la deuxième page
@app.route('/paruconnexion')
def paruconnexion():
    return render_template('paruconnexion.html')

# Route pour la troisième page
@app.route('/paruinformations')
def paruinformations():
    return render_template('paruinformations.html')

# Route pour la quatrième page
@app.route('/parucard')
def parucard():
    return render_template('parucard.html')

# Route pour la cinquième page
@app.route('/parucompte')
def parucompte():
    return render_template('parucompte.html')

# Route pour la sixième page
@app.route('/paruvirement')
def paruvirement():
    return render_template('paruvirement.html')

# Redirections
@app.route('/next/<current_page>')
def next_page(current_page):
    if current_page == 'parureception':
        return redirect(url_for('paruconnexion'))
    elif current_page == 'paruconnexion':
        return redirect(url_for('paruinformations'))
    elif current_page == 'paruinformations':
        return redirect(url_for('parucard'))
    elif current_page == 'parucard':
        return redirect(url_for('parucompte'))
    elif current_page == 'parucompte':
        return redirect(url_for('paruvirement'))
    elif current_page == 'paruvirement':
        return redirect(url_for('parureception'))  # Retour à l'accueil

if __name__ == '__main__':
    app.run(debug=True)
