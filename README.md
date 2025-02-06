# Resumo de Documentos Jurídicos com OpenAI

Este projeto é uma aplicação web que utiliza inteligência artificial para gerar resumos concisos de documentos jurídicos, como contratos, termos de uso e processos. A aplicação extrai o texto de arquivos (PDF, DOCX, TXT) e utiliza a API da OpenAI para gerar um resumo destacando cláusulas importantes, prazos, valores monetários e outras informações relevantes.

- **Web Site**: [Link](https://resumo-de-documentos-juridicos-com-openai-mybtsvbmkibvnkh6suya.streamlit.app/)


### **Objetivo**
O objetivo principal deste projeto é desenvolver uma aplicação que:
- Resuma documentos jurídicos de forma concisa, destacando as cláusulas mais relevantes, como prazos, valores monetários, obrigações, direitos e responsabilidades.
- Permita que advogados, profissionais de compliance ou qualquer outro usuário com necessidade de interpretar documentos legais de forma rápida e eficiente, utilizem o sistema para acelerar sua análise.
- Ofereça a possibilidade de identificar e destacar informações críticas, como **prazos** e **valores monetários**, que frequentemente exigem atenção especial em contratos e acordos.

### **Funcionalidades Principais**
Este protótipo implementa as seguintes funcionalidades:
 **Entrada de Documento:**
   - Suporte para documentos em formatos PDF, Word (.docx) ou texto simples (.txt).
   - Opção para o usuário carregar um documento ou colar texto diretamente na interface.
  
 **Processamento de Texto:**
   - Extração do texto do documento carregado.
   - Geração de um resumo conciso usando a API da OpenAI (GPT-4), com foco em cláusulas importantes e prazos.
   - Extração de informações específicas, como **prazos**, **valores monetários** e outras cláusulas críticas.
  
 **Exibição de Resultados:**
   - Exibição do resumo gerado de forma clara e objetiva.
   - Exibição de prazos e valores destacados, facilitando a análise e compreensão do conteúdo crítico.
   - Opção para exportar o resumo em formato PDF, para que o usuário possa salvar ou compartilhar os resumos gerados.

### **Justificativa**
A necessidade de ferramentas que ajudem na **análise e resumo de textos jurídicos** é crescente, especialmente em um ambiente jurídico que lida com grandes volumes de documentos e que exige precisão. Resumir textos de maneira automatizada não só melhora a eficiência, mas também permite que o profissional se concentre nas questões mais importantes do documento, economizando tempo e esforço.

Este projeto faz uso de **técnicas de Processamento de Linguagem Natural (NLP)** e **inteligência artificial** para analisar documentos complexos e gerar resumos relevantes de maneira rápida e eficaz.

## Funcionalidades

- **Geração de resumos** de documentos jurídicos.
- Extração de **informações importantes**, como prazos, valores monetários, cláusulas relevantes, entre outros.
- **Destaque em negrito** das palavras-chave importantes no resumo.
- **Interface web simples** com **Streamlit** para facilitar o upload e processamento de arquivos (PDF, DOCX).

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **OpenAI gpt-4o-mini**: API para processamento de linguagem natural e geração de resumos.
- **Streamlit**: Framework para criar a interface web interativa.
- **PyPDF2**: Para extrair texto de arquivos PDF.
- **python-docx**: Para extrair texto de arquivos DOCX.
- 

## Contribuições

Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, fique à vontade para abrir um **Pull Request** ou uma **Issue**.

### **Nota**:

- Este projeto foi feito para fins educacionais e pode ser expandido de várias formas, incluindo suporte para outros tipos de documentos jurídicos, integração com bancos de dados, ou melhoria na interface de usuário.
- Se você encontrar algum erro ou tiver alguma dúvida sobre como usar a aplicação, sinta-se à vontade para abrir uma **issue**.

---

### **Conclusão**:

Com esse README, qualquer pessoa poderá entender rapidamente o propósito do projeto, como configurá-lo e usá-lo. Se precisar de mais ajustes ou detalhes adicionais, é só avisar! 😊
