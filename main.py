
import requests

url = "https://www.comdinheiro.com.br/Clientes/API/EndPoint001.php"

querystring = {"code":"export_data"}

payload = "username=ekho.fo&password=EKH%40fo2024&URL=ComprasVendas002--0-listar-0-&format=json&content=%5B%0A++++%7B%0A++++++++%22nome_portfolio%22%3A+%22CarteiraExemplo%22%2C%0A++++++++%22ativo%22%3A+%22PETR4%22%2C%0A++++++++%22tipo_ativo%22%3A+%22acao%22%2C%0A++++++++%22data_operacao%22%3A+%222015-02-02%22%2C%0A++++++++%22id%22%3A+69576961%2C%0A++++++++%22id2%22%3A+%22%22%2C%0A++++++++%22CV%22%3A+%22C%22%2C%0A++++++++%22data_cotizacao%22%3A+%22%22%2C%0A++++++++%22data_liquidacao%22%3A+%222015-02-05%22%2C%0A++++++++%22preco_unitario%22%3A+8.66%2C%0A++++++++%22quantidade%22%3A+1000%2C%0A++++++++%22total_bruto%22%3A+8660%2C%0A++++++++%22alt_caixa%22%3A+0%2C%0A++++++++%22data_vencimento%22%3A+%22%22%2C%0A++++++++%22custo_transacao%22%3A+0%2C%0A++++++++%22flag_tribut%22%3A+%22%22%2C%0A++++++++%22marcacao%22%3A+%22%22%2C%0A++++++++%22indexador%22%3A+%22%22%2C%0A++++++++%22percent%22%3A+%22%22%2C%0A++++++++%22taxa_pre%22%3A+%22%22%2C%0A++++++++%22gross_up%22%3A+%22%22%2C%0A++++++++%22taxa_cupom_pre%22%3A+%22%22%2C%0A++++++++%22instituicao_financeira%22%3A+%22%22%2C%0A++++++++%22banco%22%3A+%22%22%2C%0A++++++++%22flag_liquidez%22%3A+%22%22%2C%0A++++++++%22tempo_liquidez%22%3A+%22%22%2C%0A++++++++%22data_liquidez%22%3A+%22%22%2C%0A++++++++%22apelido%22%3A+%22%22%2C%0A++++++++%22flag_provisao%22%3A+%22%22%2C%0A++++++++%22IR%22%3A+%22%22%2C%0A++++++++%22IOF%22%3A+%22%22%2C%0A++++++++%22total_liquido%22%3A+%22%22%2C%0A++++++++%22campo_preciso%22%3A+%22quant%22%0A++++%7D%0A%5D&on_error=0&email_log=0"
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)

