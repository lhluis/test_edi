fazer ajuste nessa parte para fazer o dowload da planilha corretamente


def criar_planilha_excel(dados_filtrados):
    df = pd.DataFrame({'Estado': dados_filtrados})
    nome_arquivo = 'planilha_estados.xlsx' 
    df.to_excel(nome_arquivo, index=False)
    return nome_arquivo

 em "nome_arquivo" colocar um caminho ex: 'c:\\Users\\Cristina\\Desktop\\test_edi-main\\test_edi-main\\consultas\\planilha_estados.xlsx'
