from flask import Flask, request, jsonify

app = Flask(__name__)

# Fonction pour simuler un classement SEO
def get_seo_ranking(keyword):
    # Exemple de données fictives (remplace par une vraie logique)
    rankings = {
        "seo": 1,
        "google ranking": 5,
        "mots-clés": 3
    }
    return rankings.get(keyword.lower(), -1)  # -1 si non trouvé

@app.route('/ranking', methods=['GET'])
def ranking():
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({"error": "Veuillez fournir un mot-clé"}), 400
    
    rank = get_seo_ranking(keyword)
    return jsonify({"keyword": keyword, "rank": rank})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
