
# Dashboard de Vendas - AdventureWorks

Este projeto consiste em um mini painel de controle de vendas baseado nos dados do AdventureWorks, desenvolvido com Streamlit. O painel permite que os usuários filtrem e visualizem informações relevantes sobre vendas, como vendas por produto e vendas ao longo do tempo.

## Requisitos

- Python 3.8+
- SQL Server com banco de dados AdventureWorks instalado
- Dependências Python (listadas abaixo)

## Instalação

1. **Clone o repositório:**
   ```
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Instale as dependências:**
   ```
   pip install pandas plotly streamlit sqlalchemy pyodbc
   ```

3. **Configure a conexão ao banco de dados:**
   Edite o arquivo `dashboard.py` e atualize a string de conexão:
   ```python
   engine = create_engine('mssql+pyodbc://username:password@server/database?driver=SQL+Server')
   ```

4. **Configure o SQL Server:**
   Certifique-se de que a base de dados AdventureWorks está configurada e disponível para conexão.

## Execução

Para iniciar o dashboard, execute o comando:
```
streamlit run dashboard.py
```

## Funcionalidades do Painel

- **Filtros Interativos:** Selecione intervalos de datas, produtos e regiões para visualizar as vendas.
- **KPI:** Total de vendas no período filtrado.
- **Gráficos:** Visualizações de vendas por produto e vendas ao longo do tempo.

## Contribuição

Sinta-se à vontade para contribuir com melhorias para o projeto através de pull requests.
