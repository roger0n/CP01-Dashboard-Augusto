
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

st.set_page_config(page_title="Perfil + Análise de Dados - CP1", layout="wide")

@st.cache_data
def load_data(default_path: str, uploaded_file):
    if uploaded_file is not None:
        return pd.read_csv(uploaded_file)
    else:
        return pd.read_csv(default_path)

def detect_columns(df: pd.DataFrame):
    cols = df.columns.str.lower()
    fraud_col = None
    for name in ["fraud_flag", "fraud", "is_fraud", "fraudulent", "label", "target"]:
        if name in cols.values:
            fraud_col = df.columns[cols.get_loc(name)]
            break

    amount_col = None
    for c in df.columns:
        lc = c.lower()
        if any(k in lc for k in ["amount", "value", "price"]):
            amount_col = c
            break

    date_col = None
    for c in df.columns:
        if "date" in c.lower():
            date_col = c
            break

    return fraud_col, amount_col, date_col

def ci_mean(x, confidence=0.95):
    x = pd.Series(x).dropna().astype(float)
    n = len(x)
    if n < 2:
        return np.nan, np.nan
    m = x.mean()
    se = stats.sem(x, nan_policy="omit")
    h = se * stats.t.ppf((1 + confidence) / 2., n-1)
    return m - h, m + h

st.sidebar.title("Configurações")
uploaded = st.sidebar.file_uploader("Carregue um CSV (opcional)", type=["csv"])
default_path = "luxury_cosmetics_fraud_analysis_2025.csv"

df = load_data(default_path, uploaded)
if df is None or df.empty:
    st.error("Não foi possível carregar dados. Verifique o CSV.")
    st.stop()

fraud_col, amount_col, date_col = detect_columns(df)

if date_col is not None:
    try:
        df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    except Exception:
        pass

with st.sidebar.expander("Filtros"):
    work = df.copy()
    if date_col is not None and pd.api.types.is_datetime64_any_dtype(work[date_col]):
        min_d, max_d = work[date_col].min(), work[date_col].max()
        if pd.notna(min_d) and pd.notna(max_d):
            start, end = st.date_input("Intervalo de datas", value=(min_d.date(), max_d.date()))
            if start and end:
                work = work[(work[date_col] >= pd.to_datetime(start)) & (work[date_col] <= pd.to_datetime(end))]

    cat_cols = [c for c in work.columns if work[c].dtype == "object" or pd.api.types.is_categorical_dtype(work[c])]
    for c in cat_cols[:5]:
        vals = ["(Todos)"] + sorted([str(v) for v in work[c].dropna().unique()])[:1000]
        choice = st.selectbox(f"{c}", options=vals, index=0)
        if choice != "(Todos)":
            work = work[work[c].astype(str) == choice]

    df_filtered = work

tabs = st.tabs(["Home", "Formação e Experiência", "Skills", "Análise de Dados", "Sobre os Dados"])

with tabs[0]:
    st.title("Augusto Ferreira Rogel de Souza - 20 anos")
    left, right = st.columns([1, 2], vertical_alignment="center")
    with left:
        try:
            st.image("Foto_augusto.jpeg", width=220)
        except Exception as e:
            st.warning("Não encontrei 'foto.jpg' na pasta do projeto. Coloque a imagem lá ou ajuste o nome do arquivo.")

    with right:
        st.subheader("Objetivo Profissional")
        st.write("""
        Busco atuar como **Programador Backend**, desenvolvendo soluções escaláveis e eficientes,
        com foco em **Python, Java e bancos de dados relacionais**. 
        Tenho interesse em boas práticas de arquitetura, APIs e otimização de performance.
        """)

        st.subheader("Contato")
        st.markdown(
            "- Telefone: (11)- 98817-4642\n"
            "- Email: gurogel@gmail.com\n"
            "- LinkedIn: https://acesse.one/Linkedin-Augusto-Ferreira\n"
            "- Local: Brasil"
        )
    st.write("""Bem-vindo(a)! Este dashboard reúne meu perfil profissional e uma análise de dados aplicada a um problema de detecção de fraude no varejo de cosméticos de luxo.""")


with tabs[1]:
    st.header("Formação e Experiência")
    st.write("""- **Formação**:\n\n**Colégio Adventista de Diadema** - ENSINO MÉDIO | 30/01/2020 - 18/12/2022 
    \n**Faculdade de Informática e Administração Paulista(FIAP)** - ENSINO SUPERIOR, ENGENHARIA DE SOFTWARE |
19/02/2024 até o presente momento  
- **Cursos/Certificações**:  \n\nGestão de Infraestrutura de TI\n\nFormação Social e Sustentabilidade\n\nDessign think- process""")

with tabs[2]:
    st.header("Skills")
    st.write("""**Técnicas**: \n
- Python \n
- Java \n
- HTML \n
- CSS \n
- JavaScript \n
- SQL \n
- Estatística\n  
**Soft Skills**: \n
- Boa Comunicação \n
- Colaboração \n
- Pensamento Analítico \n
- Curiosidade \n
- Raciocínio Lógico \n
- Organizado \n
- Meticuloso \n
- Senso de Responsabilidade \n
- Sei lidar sob pressão""")

with tabs[3]:
    st.header("Análise de Dados")
    st.caption("Todos os cálculos abaixo se ajustam ao dataset filtrado na barra lateral.")

    st.subheader("1) Apresentação dos dados e tipos de variáveis")
    st.write(f"Linhas: **{len(df_filtered)}** | Colunas: **{df_filtered.shape[1]}**")
    st.dataframe(df_filtered.head(20))
    st.subheader("Classificação Estatística das Variáveis")

    tipo_estatistico = {
        "Transaction_ID": "Qualitativa Nominal",
        "Customer_ID": "Qualitativa Nominal",
        "Transaction_Date": "Qualitativa Ordinal",
        "Transaction_Time": "Qualitativa Ordinal",
        "Store_ID": "Qualitativa Nominal",
        "Product_SKU": "Qualitativa Nominal",
        "IP_Address": "Qualitativa Nominal",
        "Customer_Age": "Quantitativa Discreta",
        "Customer_Loyalty_Tier": "Qualitativa Ordinal",
        "Location": "Qualitativa Nominal",
        "Payment_Method": "Qualitativa Nominal",
        "Device_Type": "Qualitativa Nominal",
        "Product_Category": "Qualitativa Nominal",
        "Purchase_Amount": "Quantitativa Contínua",
        "Footfall_Count": "Quantitativa Discreta",
        "Fraud_Flag": "Qualitativa Nominal (binária)"
    }

    colunas_validas = [c for c in tipo_estatistico.keys() if c in df_filtered.columns]

    tabela_classificacao = pd.DataFrame({
        "Coluna": colunas_validas,
        "Tipo Estatístico": [tipo_estatistico[c] for c in colunas_validas]
    })

    st.dataframe(tabela_classificacao, use_container_width=True)

    st.write("**Perguntas de análise:**")
    st.markdown("""
    - Há diferença no **valor médio de compra** entre transações **fraudulentas vs. não fraudulentas**?
    - Quais variáveis apresentam **correlação** com o valor de compra?
    - As distribuições de **Purchase_Amount** indicam outliers ou caudas longas?
    - Determinados **métodos de pagamento** estão mais associados a fraudes?
    - O **tipo de dispositivo** (desktop vs. mobile) influencia na ocorrência de fraude?
    - Clientes de certas **faixas etárias** apresentam maior propensão a fraude?
    - O nível de **fidelidade do cliente** (loyalty tier) está relacionado à fraude?
    """)

    st.subheader("2) Medidas Centrais, Dispersão, Correlação e Distribuições")


    num_cols = [c for c in df_filtered.columns if pd.api.types.is_numeric_dtype(df_filtered[c])]

    if num_cols:

        resumo = pd.DataFrame({
            "Média": df_filtered[num_cols].mean(numeric_only=True),
            "Mediana": df_filtered[num_cols].median(numeric_only=True),
            "Moda": [
                (df_filtered[c].mode().iloc[0] if not df_filtered[c].mode().empty else None)
                for c in num_cols
            ],
            "Desvio Padrão": df_filtered[num_cols].std(numeric_only=True),
            "Variância": df_filtered[num_cols].var(numeric_only=True),
        })
        st.dataframe(resumo)


        if "Purchase_Amount" in df_filtered.columns:
            fig = plt.figure()
            plt.hist(df_filtered["Purchase_Amount"].dropna(), bins=30, density=True, alpha=0.6)
            plt.title("Distribuição de Purchase_Amount")
            plt.xlabel("Purchase_Amount");
            plt.ylabel("Densidade")
            st.pyplot(fig)


        if len(num_cols) > 1:
            st.markdown("**Matriz de correlação (Pearson) — variáveis numéricas**")
            corr = df_filtered[num_cols].corr(numeric_only=True)
            st.dataframe(corr)

            fig = plt.figure()
            plt.imshow(corr, aspect="auto")
            plt.xticks(range(len(num_cols)), num_cols, rotation=90)
            plt.yticks(range(len(num_cols)), num_cols)
            plt.colorbar()
            plt.title("Matriz de Correlação (Pearson)")
            st.pyplot(fig)
    else:
        st.warning("Não foram encontradas colunas numéricas para calcular medidas centrais.")


    st.subheader("Interpretação — Medidas Centrais, Dispersão e Correlação")


    if "Purchase_Amount" in df_filtered.columns:
        pa = df_filtered["Purchase_Amount"].dropna().astype(float)
        if len(pa) >= 3:
            media = pa.mean()
            mediana = pa.median()
            moda = (pa.mode().iloc[0] if not pa.mode().empty else None)
            desvio = pa.std(ddof=1)
            variancia = pa.var(ddof=1)
            skew = pa.skew()  # >0 cauda à direita, <0 cauda à esquerda
            kurt = pa.kurt()  # ~0 ~normal, >0 caudas mais pesadas

            tendencia = "à direita (cauda longa)" if skew > 0 else ("à esquerda" if skew < 0 else "simétrica")
            curtose_txt = (
                "caudas mais pesadas que a normal" if kurt > 0
                else ("caudas mais leves que a normal" if kurt < 0 else "semelhante à normal")
            )

            st.markdown(f"""
            **Purchase_Amount**  
            • Média = **{media:.2f}**, Mediana = **{mediana:.2f}**, Moda = **{moda}**  
            • Desvio padrão = **{desvio:.2f}**, Variância = **{variancia:.2f}**  
            • Assimetria (skewness) ≈ **{skew:.2f}** → distribuição {tendencia}.  
            • Curtose ≈ **{kurt:.2f}** → {curtose_txt}.

            **Leitura:** quando a média se afasta da mediana e a assimetria é positiva, há indícios de **cauda à direita** (algumas compras muito altas). 
            O desvio padrão quantifica a **dispersão**; valores maiores indicam maior variabilidade do ticket.
            """)


    num_cols_validas = [c for c in df_filtered.columns if pd.api.types.is_numeric_dtype(df_filtered[c])]
    if "Purchase_Amount" in df_filtered.columns and len(num_cols_validas) > 1:
        corr = df_filtered[num_cols_validas].corr(numeric_only=True)["Purchase_Amount"].drop(labels=["Purchase_Amount"],
                                                                                             errors="ignore")
        if not corr.empty:
            corr_abs_ordenado = corr.abs().sort_values(ascending=False).head(5)
            linhas = [f"- `{idx}`: correlação = **{corr[idx]:.2f}**" for idx in corr_abs_ordenado.index]
            st.markdown("**Variáveis mais correlacionadas com `Purchase_Amount`:**\n" + "\n".join(linhas))
            st.caption(
                "Correlação não implica causalidade; use como sinal para explorar relações e potenciais drivers do ticket.")

    st.markdown("""
    **Resumo da seção 2:**  
    - **Média/Mediana**: tendência central e assimetrias.  
    - **Desvio/Variância**: medem a **dispersão**.  
    - **Distribuição**: histogramas revelam **caudas** e **outliers**.  
    - **Correlação**: aponta variáveis que se movem juntas (positiva) ou em sentidos opostos (negativa).
    """)

    st.subheader("3) Intervalos de Confiança e Testes de Hipótese")

    if fraud_col is None or amount_col is None:
        st.warning("Não foi possível detectar automaticamente colunas de 'fraude' e 'valor'.")
    else:
        st.markdown(f"**Parâmetro escolhido:** média de `{amount_col}` por grupo de `{fraud_col}`.  \n"
                    f"**Teste:** t de **Welch** (médias de dois grupos com variâncias/tamanhos possivelmente diferentes).  \n"
                    f"**IC:** 95% para a média em cada grupo.")


        if df_filtered[fraud_col].dtype == "object":
            mapv = {str(v): i for i, v in enumerate(df_filtered[fraud_col].astype(str).unique())}
            y = df_filtered[fraud_col].astype(str).map(mapv)
        else:
            y = df_filtered[fraud_col]

        g0 = df_filtered[y == 0][amount_col].dropna().astype(float)  # Não fraude
        g1 = df_filtered[y == 1][amount_col].dropna().astype(float)  # Fraude
        n0, n1 = len(g0), len(g1)



        def ci_t(series, conf=0.95):
            series = series.dropna().astype(float)
            n = len(series)
            if n < 2:
                return (np.nan, np.nan)
            m = series.mean()
            se = stats.sem(series, nan_policy="omit")
            h = se * stats.t.ppf((1 + conf) / 2.0, n - 1)
            return (m - h, m + h)


        colA, colB = st.columns(2)
        with colA:
            lo0, hi0 = ci_t(g0, conf=0.95)
            st.write(f"**Não Fraude (0)** — n={n0}, média={g0.mean():.2f}, desvio={g0.std(ddof=1):.2f}")
            st.write(f"IC95% da média: [{lo0:.2f}, {hi0:.2f}]")
        with colB:
            lo1, hi1 = ci_t(g1, conf=0.95)
            st.write(f"**Fraude (1)** — n={n1}, média={g1.mean():.2f}, desvio={g1.std(ddof=1):.2f}")
            st.write(f"IC95% da média: [{lo1:.2f}, {hi1:.2f}]")


        if n0 >= 2 and n1 >= 2:
            tstat, pval = stats.ttest_ind(g1, g0, equal_var=False, nan_policy="omit")
            st.markdown(f"**Teste t de Welch**: t = **{tstat:.3f}**, p-valor = **{pval:.5f}**")
            if pval < 0.05:
                st.success("Resultado: diferença **estatisticamente significativa** ao nível de 5%.")
            else:
                st.info("Resultado: **não significativa** ao nível de 5%.")


        fig2 = plt.figure()
        plt.boxplot([g0.values, g1.values], labels=["Não Fraude (0)", "Fraude (1)"])
        plt.title(f"Boxplot de {amount_col} por {fraud_col}")
        st.pyplot(fig2)


        st.subheader("Interpretação — Intervalos de Confiança e Teste de Hipótese")

        if n0 >= 2 and n1 >= 2:
            m0, s0 = g0.mean(), g0.std(ddof=1)
            m1, s1 = g1.mean(), g1.std(ddof=1)

            st.markdown(f"""
            **IC95% (`{amount_col}`):**  
            - Não Fraude (0): média = **{m0:.2f}** | IC95% = **[{lo0:.2f}, {hi0:.2f}]**  
            - Fraude (1): média = **{m1:.2f}** | IC95% = **[{lo1:.2f}, {hi1:.2f}]**

            **Leitura:** ICs com **pouca sobreposição** sugerem diferença entre os grupos.  
            **Teste t de Welch:** p-valor = **{pval:.5f}** — interpreta-se com α = 0,05.  
            """)


            pooled_sd = np.sqrt((s0 ** 2 + s1 ** 2) / 2) if (s0 > 0 and s1 > 0) else np.nan
            d = (m1 - m0) / pooled_sd if pooled_sd and not np.isnan(pooled_sd) else np.nan
            if not np.isnan(d):
                if abs(d) < 0.2:
                    mag = "muito pequeno"
                elif abs(d) < 0.5:
                    mag = "pequeno"
                elif abs(d) < 0.8:
                    mag = "médio"
                else:
                    mag = "grande"
                st.markdown(f"**Tamanho de efeito (Cohen’s d)** ≈ **{d:.2f}** → efeito **{mag}**.")

            direcao = "maior" if m1 > m0 else "menor"
            st.markdown(f"""
            **Interpretação prática:** em média, transações **Fraude (1)** apresentam valor de compra **{direcao}** do que **Não Fraude (0)** 
            (diferença ≈ **{(m1 - m0):.2f}** em `{amount_col}`).
            """)
        else:
            st.info("Amostra insuficiente para interpretar ICs e teste com segurança.")

with tabs[4]:
    st.header("Sobre os Dados")
    st.write("""
    Este dataset contém transações de um **varejo de cosméticos de luxo**, incluindo variáveis sobre clientes, produtos e
    um indicador de fraude (`Fraud_Flag`).
    Ele permite analisar o comportamento das compras e identificar diferenças entre transações legítimas e fraudulentas.
    """)

    miss = df_filtered.isna().mean().sort_values(ascending=False).rename("percent_missing").to_frame()
    st.subheader("Valores faltantes (%)")
    st.dataframe((miss*100).round(2))
    st.subheader("Amostra")
    st.dataframe(df_filtered.sample(min(10, len(df_filtered)), random_state=42))

st.sidebar.success("Use `streamlit run app.py` para rodar o dashboard.")
