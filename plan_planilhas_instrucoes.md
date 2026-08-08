# Instruções Passo a Passo para Montar Planilhas e Formulários no Google Sheets

## 1. Preparação Inicial
1. Abra o Google Drive e crie uma pasta chamada `Pão por Deus - Gestão`.
2. Dentro dessa pasta, crie um novo arquivo do Google Sheets chamado `Planejamento Pão por Deus`.
3. Crie um novo Google Form chamado `Formulário de Orçamento - Pão por Deus`.
4. Crie um novo Google Form chamado `Cadastro de Parceiros - Pão por Deus`.
5. Se desejar, crie um terceiro Google Form chamado `Briefing de Evento - Pão por Deus`.

## 2. Planilha Financeira (Google Sheets)
### 2.1 Criar abas
No mesmo arquivo `Planejamento Pão por Deus`, crie estas abas:
- `Resumo`
- `Custos Fixos`
- `Custos Variáveis`
- `Orçamentos`
- `Receitas`
- `Indicadores`

### 2.2 Campos da aba `Custos Fixos`
1. ID
2. Descrição
3. Categoria
4. Valor Mensal
5. Data de Vencimento
6. Forma de Pagamento
7. Status do Pagamento
8. Observações

### 2.3 Campos da aba `Custos Variáveis`
1. ID do Evento
2. Data
3. Descrição do Gasto
4. Categoria do Gasto
5. Valor
6. Fornecedor
7. Observações

### 2.4 Campos da aba `Orçamentos`
1. ID do Evento
2. Cliente
3. Data do Orçamento
4. Tipo de Evento
5. Custo Direto Estimado
6. Custo Fixo Alocado
7. Margem de Lucro (%)
8. Preço Sugerido
9. Preço Aprovado
10. Observações

### 2.5 Campos da aba `Receitas`
1. ID do Evento
2. Cliente
3. Data do Evento
4. Valor Total Recebido
5. Valor Recebido no Sinal
6. Valor Restante
7. Data de Recebimento
8. Forma de Pagamento
9. Observações

### 2.6 Campos da aba `Indicadores`
- Receita total mensal
- Custos fixos totais
- Custos variáveis totais
- Lucro bruto
- Margem de lucro média
- Eventos realizados no mês
- Ponto de equilíbrio

### 2.7 Campos da aba `Resumo`
- Total de receitas no mês
- Total de custos no mês
- Resultado financeiro do mês
- Eventos agendados
- Eventos confirmados
- Fluxo de caixa projetado

## 3. Planilha Operacional (Google Sheets)
### 3.1 Criar abas
No mesmo arquivo ou em um segundo arquivo, crie estas abas:
- `Eventos`
- `Fornecedores`
- `Checklist`
- `Agenda`
- `Logística`

### 3.2 Campos da aba `Eventos`
1. ID do Evento
2. Cliente
3. Data do Evento
4. Tipo de Evento
5. Local do Evento
6. Número Estimado de Convidados
7. Serviços Contratados
8. Status do Evento
9. Observações
10. Responsável Interno

### 3.3 Campos da aba `Fornecedores`
1. ID do Fornecedor
2. Nome da Empresa / Profissional
3. Categoria de Serviço
4. Contato Principal
5. Telefone / WhatsApp
6. E-mail
7. Condições de Pagamento
8. Disponibilidade
9. Avaliação
10. Observações

### 3.4 Campos da aba `Checklist`
1. ID do Evento
2. Item de Tarefa
3. Categoria (pré-evento, montagem, dia do evento, desmontagem, pós-evento)
4. Responsável
5. Data Prevista
6. Status (pendente, em andamento, concluído)
7. Observações

### 3.5 Campos da aba `Agenda`
1. Data
2. ID do Evento
3. Evento
4. Cliente
5. Horário de Início
6. Horário de Fim
7. Localização
8. Status

### 3.6 Campos da aba `Logística`
1. ID do Evento
2. Requisito/Item
3. Quantidade Necessária
4. Responsável
5. Prazo de Entrega
6. Observações

## 4. Planilha Clientes / Eventos (Google Sheets)
### 4.1 Criar abas
- `Clientes`
- `Leads`
- `Eventos Agendados`
- `Histórico`
- `Documentos`

### 4.2 Campos da aba `Clientes`
1. ID do Cliente
2. Nome Completo
3. E-mail
4. Telefone / WhatsApp
5. Tipo de Evento
6. Data de Cadastro
7. Origem do Contato
8. Status do Cliente
9. Observações

### 4.3 Campos da aba `Leads`
1. ID do Lead
2. Nome Completo
3. E-mail
4. Telefone / WhatsApp
5. Tipo de Evento Desejado
6. Data Preferencial
7. Número Estimado de Convidados
8. Serviço de Interesse
9. Como nos encontrou
10. Status do Lead
11. Próxima Ação

### 4.4 Campos da aba `Eventos Agendados`
1. ID do Evento
2. Cliente / ID do Cliente
3. Data do Evento
4. Tipo de Evento
5. Número de Convidados
6. Serviços Contratados
7. Valor do Orçamento
8. Valor Pago
9. Status de Pagamento
10. Status do Evento
11. Observações

### 4.5 Campos da aba `Histórico`
1. ID do Registro
2. Cliente / Lead
3. Data do Contato
4. Tipo de Contato
5. Resultado
6. Observações

### 4.6 Campos da aba `Documentos`
1. ID do Evento
2. Tipo de Documento
3. Link do Documento
4. Data de Envio
5. Observações

## 5. Formulários Google Forms e Campos Exatos
### 5.1 Formulário de Orçamento / Lead
Criar perguntas com as seguintes opções e tornar obrigatórias quando necessário:
1. Nome completo
2. E-mail
3. Telefone ou WhatsApp
4. Tipo de evento
   - Casamento
   - Aniversário
   - Bodas
   - Formatura
   - Outro
5. Data preferencial do evento
6. Número estimado de convidados
7. Serviços desejados
   - Espaço
   - Decoração
   - Buffet
   - DJ/Banda
   - Bar
   - Limpeza
   - Iluminação
   - Outros
8. Faixa de orçamento ou valor estimado
9. Observações adicionais
10. Como conheceu o espaço?
    - Instagram
    - WhatsApp
    - Google
    - Indicação
    - Outro

### 5.2 Formulário de Cadastro de Parceiros
1. Nome do fornecedor / empresa
2. Categoria de serviço
   - Limpeza
   - Decoração
   - Buffet
   - Som / Iluminação
   - Bar
   - Segurança
   - Outro
3. Contato principal
4. Telefone / WhatsApp
5. E-mail
6. Condições de pagamento
7. Disponibilidade para eventos
8. Observações
9. Avaliação inicial do parceiro

### 5.3 Formulário de Briefing de Evento (opcional)
1. Nome do cliente
2. ID do evento ou nome do evento
3. Tipo de evento
4. Data do evento
5. Número de convidados
6. Tema / estilo desejado
7. Requisitos de decoração
8. Requisitos de buffet / menu
9. Requisitos de som / iluminação
10. Horário de início e fim previstos
11. Observações adicionais

## 6. Como Conectar Formulários às Abas do Sheets
### 6.1 Exportar respostas para o Sheets
1. Abra o Google Form.
2. Clique em `Respostas`.
3. Clique no ícone de planilha verde `Criar planilha`.
4. Escolha `Selecionar uma planilha existente`.
5. Selecione o arquivo `Planejamento Pão por Deus`.
6. Crie ou escolha a aba correspondente.

### 6.2 Abas sugeridas de destino
- Respostas do formulário de orçamento → aba `Leads`
- Respostas do formulário de parceiros → aba `Fornecedores`
- Respostas do formulário de briefing → aba `Eventos Agendados`

### 6.3 Ajustes após conectar
- Alinhe as colunas das abas de destino com os campos do formulário.
- Utilize fórmulas para copiar ou formatar dados se os nomes de campos diferirem.
- Mantenha a primeira linha como cabeçalho e acrescente novas colunas na direita quando precisar de status ou observações internas.

## 7. Recomendações de Automação e Uso
1. Use validação de dados no Google Sheets para campos como `Tipo de Evento`, `Status`, `Categoria de Serviço`.
2. Crie listas suspensas nas abas para evitar variações de texto.
3. Use formatação condicional para destacar eventos próximos e pagamentos pendentes.
4. Conecte o Google Form com notificações por e-mail para saber quando um novo lead é captado.
5. Se precisar, crie uma aba `Configuração` com categorias e status padronizados.

## 8. Teste do Fluxo de Dados
1. Preencha o formulário de orçamento com dados fictícios.
2. Verifique se os dados chegam na aba `Leads`.
3. Preencha o formulário de parceiros e valide a aba `Fornecedores`.
4. Se usar o briefing, confirme a aba `Eventos Agendados`.
5. Ajuste colunas e cabeçalhos até garantir o fluxo correto.

## 9. Manutenção Contínua
- Atualize os formulários sempre que precisar coletar um novo campo.
- Revise o cabeçalho das abas no Sheets sempre que adicionar perguntas.
- Faça backup do arquivo periodicamente ou copie a planilha para um arquivo de controle.
- Documente dentro da planilha os campos obrigatórios e os responsáveis pela atualização.

## 10. Observação Final
Este roteiro foi desenhado para criar um sistema integrado de captura, controle e gestão de eventos com mínima digitação manual. Ele garante que os dados de clientes e fornecedores entrem diretamente via Google Forms e sejam armazenados automaticamente nas abas corretas do Google Sheets.