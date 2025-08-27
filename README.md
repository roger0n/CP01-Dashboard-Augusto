
# CP1 - Dashboard Profissional + Análise de Dados (Streamlit)

## Como rodar (PyCharm ou terminal)
1. (Opcional) Crie e ative um virtualenv.
2. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Certifique-se de que `luxury_cosmetics_fraud_analysis_2025.csv` está na mesma pasta do `app.py`.
4. Rode o app:
   ```bash
   streamlit run app.py
   ```

## Abas
- **Home**: objetivo profissional e contato (edite com seus dados).
- **Formação e Experiência** e **Skills**: personalize seu perfil.
- **Análise de Dados** (obrigatória):
  - Preview do dataset e tipos das variáveis.
  - Medidas centrais, histograma de `Purchase_Amount` e matriz de correlação.
  - IC95% da média de `Purchase_Amount` por `Fraud_Flag`.
  - Teste t de Welch (fraude vs. não-fraude).
  - Boxplot por grupo.
- **Sobre os Dados**: missing values (%) e amostra aleatória.

Sinta-se livre para incluir novas hipóteses (ex.: qui-quadrado para proporções de fraude por `Payment_Method`).
