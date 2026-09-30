# 🚍 Pipeline de Dados e Monitorização de Mobilidade Urbana (Rio de Janeiro)

<p align="center">
  <b>Pipeline de Engenharia de Dados em tempo real para telemetria de autocarros do Rio de Janeiro, integrada com PostgreSQL via Docker e visualizada no Power BI.</b>
</p>

---

## 🛠️ Tecnologias e Ferramentas Utilizadas
* **Linguagem:** Python (ETL, automação e extração de dados)
* **Banco de Dados:** PostgreSQL (hospedado em contentor Docker)
* **Gestão e Consultas:** DBeaver / SQL (CTE, funções de janela e modelagem relacional)
* **Visualização de Dados:** Power BI Desktop (DAX, Mapas de GPS e Design de Dashboards)
* **Controlo de Versão:** Git & GitHub

---

## 🏗️ Arquitetura do Projeto
1. **Ingestão e ETL (Python):** Extração automatizada de dados de geolocalização e telemetria da frota de autocarros do Rio de Janeiro.
2. **Armazenamento (Docker & PostgreSQL):** Centralização dos dados num banco relacional robusto executado localmente através de contentores Docker (`rj_mobility_db`).
3. **Modelagem e Métricas (SQL & DAX):** Criação de tabelas dimensionais e métricas avançadas em DAX (como o cálculo de *Velocidade Média* por veículo).
4. **Data Viz (Power BI):** Construção de um painel executivo moderno com foco em experiência de utilizador (UI/UX limpo, cartões flutuantes, mapas geográficos e tabelas analíticas).

---

## 📊 Pré-visualização do Dashboard
*(Adicione aqui a captura de ecrã do Power BI que acabou de criar, por exemplo: `docs/dashboard_preview.png`)*

O painel está estruturado com:
* **Mapa Geográfico:** Monitorização espacial das coordenadas GPS dos veículos em circulação.
* **KPIs Executivos:** Cartão estilizado com a velocidade média global da frota.
* **Tabela de Detalhe por Veículo:** Listagem individualizada cruzando o identificador do autocarro (`veiculo_id`) com a sua respetiva velocidade média calculada.

---

## 🚀 Como Executar o Projeto
1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-utilizador/analise-dados-onibus-rj.git](https://github.com/seu-utilizador/analise-dados-onibus-rj.git)