from flask import Flask, render_template_string, request, redirect, send_file
import os

app = Flask(__name__)
BASE_DIR = os.getcwd()

HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>trhacknon - File Manager</title>
    <style>
        body { background: #111; color: #0f0; font-family: monospace; padding: 20px; }
        a { color: #0ff; text-decoration: none; }
        a:hover { text-decoration: underline; }
        input, textarea { width: 100%; background: #222; color: #0f0; border: 1px solid #0f0; padding: 5px; }
    </style>
</head>
<body>
    <h2>Répertoire : {{ path }}</h2>
    <ul>
        {% if parent %}
            <li><a href="/?path={{ parent }}">[..]</a></li>
        {% endif %}
        {% for f in files %}
            <li>
                {% if f.isdir %}
                    <a href="/?path={{ f.path }}">[{{ f.name }}/]</a>
                {% else %}
                    {{ f.name }} -
                    <a href="/view?file={{ f.path }}">Voir</a> |
                    <a href="/edit?file={{ f.path }}">Éditer</a> |
                    <a href="/download?file={{ f.path }}">Télécharger</a> |
                    <a href="/delete?file={{ f.path }}">Supprimer</a>
                {% endif %}
            </li>
        {% endfor %}
    </ul>

    <h3>Créer/Nouveau fichier</h3>
    <form method="POST" action="/save">
        <input name="file" placeholder="ex: monfichier.txt">
        <textarea name="content" rows="10" placeholder="Contenu..."></textarea>
        <button type="submit">Sauvegarder</button>
    </form>
</body>
</html>
"""

@app.route("/")
def index():
    path = request.args.get("path", BASE_DIR)
    path = os.path.abspath(path)

    parent = os.path.dirname(path) if path != BASE_DIR else None

    items = []
    for name in os.listdir(path):
        full_path = os.path.join(path, name)
        items.append({"name": name, "path": full_path, "isdir": os.path.isdir(full_path)})

    return render_template_string(HTML, path=path, files=items, parent=parent)

@app.route("/view")
def view_file():
    fpath = request.args.get("file")
    if not os.path.isfile(fpath):
        return "Fichier introuvable", 404
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    return f"<pre>{content}</pre><a href='/'>Retour</a>"

@app.route("/edit")
def edit_file():
    fpath = request.args.get("file")
    if not os.path.isfile(fpath):
        return "Fichier introuvable", 404
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    return f"""
    <form method="POST" action="/save">
        <input name="file" value="{fpath}">
        <textarea name="content" rows="20">{content}</textarea>
        <button type="submit">Sauvegarder</button>
    </form>
    """

@app.route("/save", methods=["POST"])
def save_file():
    fpath = request.form["file"]
    content = request.form["content"]
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    return redirect(f"/?path={os.path.dirname(fpath)}")

@app.route("/download")
def download():
    fpath = request.args.get("file")
    if os.path.isfile(fpath):
        return send_file(fpath, as_attachment=True)
    return "Fichier introuvable", 404

@app.route("/delete")
def delete():
    fpath = request.args.get("file")
    if os.path.isfile(fpath):
        os.remove(fpath)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=False, port=8080)
