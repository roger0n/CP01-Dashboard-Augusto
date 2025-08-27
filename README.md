# CP01 — Dashboard Profissional + Análise de Dados

[![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-ff4b4b?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3110/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

## Objetivo
Este projeto foi desenvolvido como parte da avaliação **CP1**, com os seguintes objetivos:
- Apresentar um **dashboard interativo** com meu perfil profissional.
- Realizar uma **análise de dados aplicada** ao problema de **fraudes em transações de cosméticos de luxo**.
- Aplicar conceitos de **estatística descritiva e inferencial**:
  - Medidas centrais (média, mediana, moda)  
  - Dispersão (desvio padrão, variância)  
  - Correlação  
  - Distribuições  
  - Intervalos de confiança  
  - Testes de hipótese (t de Welch)  

---

## Tecnologias Utilizadas
- [Python 3.11+](https://www.python.org/)  
- [Streamlit](https://streamlit.io/)  
- [Pandas](https://pandas.pydata.org/)  
- [NumPy](https://numpy.org/)  
- [SciPy](https://scipy.org/)  
- [Matplotlib](https://matplotlib.org/)  

---

## Estrutura do Projeto
- app.py # Arquivo principal do dashboard
- requirements.txt # Dependências
- README.md # Documentação
- luxury_cosmetics_fraud_analysis_2025.csv # Base de dados usada
- Foto_augusto.jpeg # Foto pessoal para a aba Home

---

## Como Rodar Localmente

# Clone este repositório
git clone https://github.com/roger0n/CP01-Dashboard-Augusto.git
cd CP01-Dashboard-Augusto

# (Opcional) Crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

# Instale as dependências
pip install -r requirements.txt

# Rode o dashboard
streamlit run app.py

# O app estará disponível em:
- http://localhost:8501

---

## Funcionalidades

- Home → Foto, objetivo profissional e contatos.

- Formação e Experiência → Histórico acadêmico e experiências relevantes.

- Skills → Habilidades técnicas e comportamentais.

- Análise de Dados

- - Classificação das variáveis (qualitativas/quantitativas)

- - Medidas centrais e dispersão

- - Distribuições (histogramas, boxplots)

- - Correlações

- - Intervalos de confiança

- - Teste de hipótese (t de Welch)

- Sobre os Dados → valores faltantes (%) e amostra aleatória.

---

## Deploy
- Este projeto foi deployado no Streamlit Community Cloud:
- - https://cp01-dashboard-augusto-dtkztisbhvquqplblpd6dg.streamlit.app/

---
## Autor

- Nome: Augusto Ferreira Rogel de Souza

- Objetivo Profissional: Programador Backend

- Contato: Email: gurogel@gmail.com | LinkedIn: https://acesse.one/Linkedin-Augusto-Ferreira | Telefone: (11)- 98817-4642
 
  
