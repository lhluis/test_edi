from flask import Flask, render_template, jsonify, request, redirect, url_for, send_file
import requests
import pandas as pd

app = Flask(__name__, static_folder='style')

link = "https://24e6f406-2f69-45ca-bd74-b88c3559e660-00-of1umc32ierk.kirk.replit.dev/estados"

requisicao = requests.get(link)
informacoes = requisicao.json()

nomes_estados = [estado['nome'] for estado in informacoes]

def criar_planilha_excel(dados_filtrados):
    df = pd.DataFrame({'Estado': dados_filtrados})
    nome_arquivo = 'planilha_estados.xlsx'
    df.to_excel(nome_arquivo, index=False)
    return nome_arquivo

@app.route("/", methods=['GET'])
def lista():
    return render_template("index.html", estados=nomes_estados)

@app.route("/filtrar_estados", methods=['GET'])
def filtrar_estados():
    regiao_selecionada = request.args.get('regiao')
    ordem = request.args.get('ordem')  
    if regiao_selecionada:
        estados_filtrados = [estado['nome'] for estado in informacoes if estado['regiao'] == regiao_selecionada]
    else:
        estados_filtrados = nomes_estados
    
    if ordem == 'decrescente':
        estados_filtrados = sorted(estados_filtrados, reverse=True)  
    return jsonify(estados_filtrados)

@app.route("/criar_planilha", methods=['POST'])
def criar_planilha():
    regiao_selecionada = request.form.get('regiao')
    if regiao_selecionada:
        estados_filtrados = [estado['nome'] for estado in informacoes if estado['regiao'] == regiao_selecionada]
    else:
        estados_filtrados = nomes_estados
    nome_arquivo = criar_planilha_excel(estados_filtrados)
    return redirect(url_for('download_planilha', nome_arquivo=nome_arquivo))

@app.route("/download_planilha/<nome_arquivo>")
def download_planilha(nome_arquivo):
    return send_file(nome_arquivo, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)