import streamlit as st
import os
import PyPDF2
import docx
from openai import OpenAI
from dotenv import load_dotenv

# Verifica se está rodando no Streamlit Cloud ou localmente
if "OPENAI_API_KEY" in st.secrets:
    api_key = st.secrets["OPENAI_API_KEY"]  # No Streamlit Cloud
else:
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")  # No ambiente local

# Configuração da API da OpenAI
openai = OpenAI(api_key=api_key)

# Função para extrair texto de PDF
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Função para extrair texto de DOCX
def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

# Função para extrair texto de TXT
def extract_text_from_txt(file):
    return file.read().decode('utf-8')

# Função para gerar o resumo com a OpenAI
def generate_summary_with_openai(text):
    system_prompt = """
    Você é um assistente jurídico especializado em documentos legais. Seu objetivo é fornecer um resumo conciso de um documento jurídico, destacando cláusulas importantes, como prazos, valores monetários, e condições que possam ser relevantes para um contrato ou termo de uso.
    Responda de maneira clara e objetiva, removendo informações irrelevantes como cabeçalhos, rodapés e dados de navegação.
    """
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Resuma o seguinte documento jurídico:\n{text}"}
    ]
    response = openai.chat.completions.create(
        model="gpt-4o-mini",  # Ou use "gpt-3.5-turbo" se necessário
        messages=messages
    )
    return response.choices[0].message.content

# Configuração do layout do Streamlit
st.set_page_config(
    page_title="Resumo Jurídico Automatizado",
    page_icon="⚖️",
    layout="wide"
)

# CSS personalizado para melhorar o design
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f4f4f9;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stFileUploader>div>div>div>div {
        background-color: #ffffff;
        border-radius: 5px;
        padding: 20px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }
    .stMarkdown h1 {
        color: #2c3e50;
        text-align: center;
    }
    .stMarkdown h2 {
        color: #2c3e50;
    }
    .stExpander {
        background-color: #ffffff;
        border-radius: 5px;
        padding: 20px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título e descrição
st.title("⚖️ Resumo Jurídico Automatizado")
st.markdown("""
    <div style="text-align: center; color: #555;">
        Carregue seu documento e receba um resumo detalhado em segundos.
    </div>
    """, unsafe_allow_html=True)

# Upload do arquivo
uploaded_file = st.file_uploader("Escolha um arquivo (PDF, DOCX ou TXT)", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    # Extrai o texto do arquivo
    if uploaded_file.name.endswith('.pdf'):
        text = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.name.endswith('.docx'):
        text = extract_text_from_docx(uploaded_file)
    elif uploaded_file.name.endswith('.txt'):
        text = extract_text_from_txt(uploaded_file)
    else:
        st.error("Formato de arquivo não suportado.")
        st.stop()

    # Exibe o texto extraído (opcional)
    with st.expander("📄 Ver texto extraído"):
        st.write(text)

    # Gera o resumo
    if st.button("✨ Gerar Resumo"):
        with st.spinner("⏳ Gerando resumo..."):
            summary = generate_summary_with_openai(text)
            st.success("✅ Resumo gerado com sucesso!")
            st.markdown("### 📝 Resumo Gerado")
            st.write(summary)

            # Opção para exportar o resumo como TXT
            st.download_button(
                label="📥 Baixar Resumo (TXT)",
                data=summary,
                file_name="resumo.txt",
                mime="text/plain"
            )