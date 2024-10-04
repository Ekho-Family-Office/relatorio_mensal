
import requests

url = "https://www.comdinheiro.com.br/Clientes/API/EndPoint001.php"

querystring = {"code":"import_data"}

# payload = "username=ekho.fo&password=EKH%40fo2024&URL=ExtratoCarteira021.php%3F%26nome_portfolio%3D1001%26data_ini%3D29072024%26data_fim%3D19092024%26data_ini2%3Dmes_atual%26data_ini3%3Dano_atual%26layout%3D2%26classe%3DTIPO%26classe2%3DIF%26cot_tir%3Dcot%26cot_tir_ativo%3Dtir%26benchmarks%3DCDI%2BIBOV%26on_off%3Don%26colunas_adicionais%3D%26alias_colunas_adicionais%3D%26ret_classe%3D0%26mes%3DCDI%2Bpercent_CDI%7C0%7CV%7C%26aloc%3Dpesod%7Cb%7Canel%7Cl%7C4%7Cicl%7C0%7C0%7C2%26ordem_grandeza_grafico_rendimento%3D1000%26aloc_per_tipo%3Dbarra%26aloc_per_exibir%3Dvsb%26aloc_per_ordem_grandeza%3D1000%26aloc_per_periodo%3Dmes%26aloc_per_valores%3D12%26ret%3Dmes_atual%2Bano_atual%2B12m%2B24m%2Bperiodo%26movext%3D1%7C1%7C%7C1%26liq%3D0%2B2%2B6%2B31%7Ccorridos%7Cambos%7C0%7C1%7Cpos_liq%2Bper_pos_liq%7Ctabela%7C0%26liq_exibe%3D1%26infoAdd_primeiro_mes%3D0%26infoAdd_bench_IS%3DCDI%26infoAdd_bench%3DCDI%26ret2%3Dcor%2Bativo%2Bmes_atual%2Bano_atual%2B03m%2B06m%2B12m%2B24m%2B36m%2Bperiodo%2Bdata_aplicacao%26filtro_tipo_ativo%3Dtodos%26filtro_CV%3Dtodos%26linha_cart%3D0%26ret_nulos%3D1%26ret_bench_ativo%3D%26ord_ativo%3Dalfc%26ord_classe%3Dalfc%26mov_ext%3D1%26exibicao%3Ddefault%26num_casas%3D2%26valores%3D1%26graf_linha%3D1%7C1%7C%7C%26ret3%3Dativo%2Bmes_atual%2Bano_atual%2B12m%2B24m%26aloc_ordem2%3Dpesod%26aloc_saldo2%3DSB%26aloc_limit2%3D%26bench4%3DCDI%26classe3%3DIF%26aloc_ordem3%3Dpesod%26aloc_saldo3%3DSB%26aloc_limit3%3D%26fall_ordem%3D1%26fall_ordem_grand%3D1000%26fall_cor%3Dd3d3d3t%26exibir_commit%3D1%26cart_explodida%3D%26estilo_pdf%3Dazul0001%26num_pdf%3D2&format=json3"

# payload = "username=ekho.fo&password=EKH@fo2024&URL=ExtratoCarteira021.php?&nome_portfolio=1001&data_ini=29072024&data_fim=19092024&data_ini2=mes_atual&data_ini3=ano_atual&layout=2&classe=TIPO&classe2=IF&cot_tir=cot&cot_tir_ativo=tir&benchmarks=CDI+IBOV&on_off=on&colunas_adicionais=&alias_colunas_adicionais=&ret_classe=0&mes=CDI+percent_CDI|0|V|&aloc=pesod|b|anel|l|4|icl|0|0|2&ordem_grandeza_grafico_rendimento=1000&aloc_per_tipo=barra&aloc_per_exibir=vsb&aloc_per_ordem_grandeza=1000&aloc_per_periodo=mes&aloc_per_valores=12&ret=mes_atual+ano_atual+12m+24m+periodo&movext=1|1||1&liq=0+2+6+31|corridos|ambos|0|1|pos_liq+per_pos_liq|tabela|0&liq_exibe=1&infoAdd_primeiro_mes=0&infoAdd_bench_IS=CDI&infoAdd_bench=CDI&ret2=cor+ativo+mes_atual+ano_atual+03m+06m+12m+24m+36m+periodo+data_aplicacao&filtro_tipo_ativo=todos&filtro_CV=todos&linha_cart=0&ret_nulos=1&ret_bench_ativo=&ord_ativo=alfc&ord_classe=alfc&mov_ext=1&exibicao=default&num_casas=2&valores=1&graf_linha=1|1||&ret3=ativo+mes_atual+ano_atual+12m+24m&aloc_ordem2=pesod&aloc_saldo2=SB&aloc_limit2=&bench4=CDI&classe3=IF&aloc_ordem3=pesod&aloc_saldo3=SB&aloc_limit3=&fall_ordem=1&fall_ordem_grand=1000&fall_cor=d3d3d3t&exibir_commit=1&cart_explodida=&estilo_pdf=azul0001&num_pdf=2&format=json3"
payload = "username=ekho.fo&password=EKH%40fo2024&URL=ExtratoCarteira021.php%3F%26nome_portfolio%3D1001%26data_ini%3D29072024%26data_fim%3D19092024%26data_ini2%3Dmes_atual%26data_ini3%3Dano_atual%26layout%3D2%26classe%3DMV%28class_ekho%29%26classe2%3DIF%26cot_tir%3Dcot%26cot_tir_ativo%3Dtir%26benchmarks%3DCDI%2BIBOV%26on_off%3Don%26colunas_adicionais%3D%26alias_colunas_adicionais%3D%26ret_classe%3D0%26mes%3DCDI%2Bpercent_CDI%7C0%7CV%7C%26aloc%3Dpesod%7Cb%7Canel%7Cl%7C4%7Cicl%7C0%7C0%7C2%26ordem_grandeza_grafico_rendimento%3D1000%26aloc_per_tipo%3Dbarra%26aloc_per_exibir%3Dvsb%26aloc_per_ordem_grandeza%3D1000%26aloc_per_periodo%3Dmes%26aloc_per_valores%3D12%26ret%3Dmes_atual%2Bano_atual%2B12m%2B24m%2Bperiodo%26movext%3D1%7C1%7C%7C1%26liq%3D0%2B2%2B6%2B31%7Ccorridos%7Cambos%7C0%7C1%7Cpos_liq%2Bper_pos_liq%7Ctabela%7C0%26liq_exibe%3D1%26infoAdd_primeiro_mes%3D0%26infoAdd_bench_IS%3DCDI%26infoAdd_bench%3DCDI%26ret2%3Dcor%2Bativo%2Bmes_atual%2Bano_atual%2B03m%2B06m%2B12m%2B24m%2B36m%2Bperiodo%2Bdata_aplicacao%26filtro_tipo_ativo%3Dtodos%26filtro_CV%3Dtodos%26linha_cart%3D0%26ret_nulos%3D1%26ret_bench_ativo%3D%26ord_ativo%3Dalfc%26ord_classe%3Dalfc%26mov_ext%3D1%26exibicao%3Ddefault%26num_casas%3D2%26valores%3D1%26graf_linha%3D1%7C1%7C%7C%26ret3%3Dativo%2Bmes_atual%2Bano_atual%2B12m%2B24m%26aloc_ordem2%3Dpesod%26aloc_saldo2%3DSB%26aloc_limit2%3D%26bench4%3DCDI%26classe3%3DIF%26aloc_ordem3%3Dpesod%26aloc_saldo3%3DSB%26aloc_limit3%3D%26fall_ordem%3D1%26fall_ordem_grand%3D1000%26fall_cor%3Dd3d3d3t%26exibir_commit%3D1%26cart_explodida%3D%26estilo_pdf%3Dazul0001%26num_pdf%3D2&format=json3"

# payload = "username=ekho.fo&password=EKH%40fo2024&URL=ExtratoCarteira021.php?&nome_portfolio=1001&data_ini=05082024&data_fim=26092024&data_ini2=mes_atual&data_ini3=ano_atual&layout=2&classe=MV(class_ekho)&classe2=IF&cot_tir=cot&cot_tir_ativo=tir&benchmarks=CDI+IBOV&on_off=on&colunas_adicionais=&alias_colunas_adicionais=&ret_classe=0&mes=CDI+percent_CDI|0|V|&aloc=pesod|b|anel|l|4|icl|0|0|2&ordem_grandeza_grafico_rendimento=1000&aloc_per_tipo=barra&aloc_per_exibir=vsb&aloc_per_ordem_grandeza=1000&aloc_per_periodo=mes&aloc_per_valores=12&ret=mes_atual+ano_atual+12m+24m+periodo&movext=1|1||1&liq=0+2+6+31|corridos|ambos|0|1|pos_liq+per_pos_liq|tabela|0&liq_exibe=1&infoAdd_primeiro_mes=0&infoAdd_bench_IS=CDI&infoAdd_bench=CDI&ret2=cor+ativo+mes_atual+ano_atual+03m+06m+12m+24m+36m+periodo+data_aplicacao&filtro_tipo_ativo=todos&filtro_CV=todos&linha_cart=0&ret_nulos=1&ret_bench_ativo=&ord_ativo=alfc&ord_classe=alfc&mov_ext=1&exibicao=default&num_casas=2&valores=1&graf_linha=1|1||&ret3=ativo+mes_atual+ano_atual+12m+24m&aloc_ordem2=pesod&aloc_saldo2=SB&aloc_limit2=&bench4=CDI&classe3=IF&aloc_ordem3=pesod&aloc_saldo3=SB&aloc_limit3=&fall_ordem=1&fall_ordem_grand=1000&fall_cor=d3d3d3t&exibir_commit=1&cart_explodida=&estilo_pdf=azul0001&num_pdf=2
# payload = "username%3Dekho.fo%26password%3DEKH%2540fo2024%26URL%3DExtratoCarteira021.php%3F%26nome_portfolio%3D1001%26data_ini%3D05082024%26data_fim%3D26092024%26data_ini2%3Dmes_atual%26data_ini3%3Dano_atual%26layout%3D2%26classe%3DMV%28class_ekho%29%26classe2%3DIF%26cot_tir%3Dcot%26cot_tir_ativo%3Dtir%26benchmarks%3DCDI%2BIBOV%26on_off%3Don%26colunas_adicionais%3D%26alias_colunas_adicionais%3D%26ret_classe%3D0%26mes%3DCDI%2Bpercent_CDI%7C0%7CV%7C%26aloc%3Dpesod%7Cb%7Canel%7Cl%7C4%7Cicl%7C0%7C0%7C2%26ordem_grandeza_grafico_rendimento%3D1000%26aloc_per_tipo%3Dbarra%26aloc_per_exibir%3Dvsb%26aloc_per_ordem_grandeza%3D1000%26aloc_per_periodo%3Dmes%26aloc_per_valores%3D12%26ret%3Dmes_atual%2Bano_atual%2B12m%2B24m%2Bperiodo%26movext%3D1%7C1%7C%7C1%26liq%3D0%2B2%2B6%2B31%7Ccorridos%7Cambos%7C0%7C1%7Cpos_liq%2Bper_pos_liq%7Ctabela%7C0%26liq_exibe%3D1%26infoAdd_primeiro_mes%3D0%26infoAdd_bench_IS%3DCDI%26infoAdd_bench%3DCDI%26ret2%3Dcor%2Bativo%2Bmes_atual%2Bano_atual%2B03m%2B06m%2B12m%2B24m%2B36m%2Bperiodo%2Bdata_aplicacao%26filtro_tipo_ativo%3Dtodos%26filtro_CV%3Dtodos%26linha_cart%3D0%26ret_nulos%3D1%26ret_bench_ativo%3D%26ord_ativo%3Dalfc%26ord_classe%3Dalfc%26mov_ext%3D1%26exibicao%3Ddefault%26num_casas%3D2%26valores%3D1%26graf_linha%3D1%7C1%7C%7C%26ret3%3Dativo%2Bmes_atual%2Bano_atual%2B12m%2B24m%26aloc_ordem2%3Dpesod%26aloc_saldo2%3DSB%26aloc_limit2%3D%26bench4%3DCDI%26classe3%3DIF%26aloc_ordem3%3Dpesod%26aloc_saldo3%3DSB%26aloc_limit3%3D%26fall_ordem%3D1%26fall_ordem_grand%3D1000%26fall_cor%3Dd3d3d3t%26exibir_commit%3D1%26cart_explodida%3D%26estilo_pdf%3Dazul0001%26num_pdf%3D2%3Dformat=json3"

headers = {'Content-Type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)


# Write the response to a file
with open('response_output_new.txt', 'w') as file:
    file.write(response.text)


print(response.text)

