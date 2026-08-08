# Plano de Planilhas e Formulários - Casa de Eventos Pão por Deus

## 1. Objetivo
- Definir a estrutura de planilhas necessárias para implementar os planos financeiro, operacional e de controle de clientes/eventos
- Identificar dados que devem ser coletados via Google Forms para reduzir trabalho manual
- Planejar integração entre formulários e planilhas para entrada direta de dados
- Preparar um modelo profissional antes de criar as planilhas no Google Sheets

## 2. Planilhas Necessárias
### 2.1 Planilha Financeira
Objetivo: controlar custos, receitas e precificação de eventos.
Abas propostas:
- `Resumo`: visão geral de receita, custos, lucro, margem e evento do mês
- `Custos Fixos`: lista de despesas mensais com valores, datas de vencimento e status
- `Custos Variáveis`: registro de despesas por evento (limpeza, decoração, energia, equipe extra, etc.)
- `Orçamentos`: cálculo de preço de cada evento com custo direto, custo alocado, margem e preço final
- `Receitas`: faturamento recebido por evento, pagamentos pendentes, forma de pagamento
- `Indicadores`: métricas como ponto de equilíbrio, custo médio por evento, margem bruta

### 2.2 Planilha Operacional
Objetivo: planejar e coordenar a execução de eventos e parcerias.
Abas propostas:
- `Eventos`: lista de eventos com data, tipo, cliente, status, serviços contratados e observações
- `Fornecedores`: cadastro de parceiros (limpeza, decoração, buffet, som, bar, segurança), contatos e notas
- `Checklist`: etapas de operação por evento (pré-evento, montagem, dia, desmontagem, pós-evento)
- `Logística`: necessidades do espaço, equipamentos, tempo de montagem e desmontagem, responsáveis
- `Agenda`: calendário de eventos e disponibilidade do espaço

### 2.3 Planilha Clientes / Eventos
Objetivo: armazenar dados de clientes, leads, histórico de contato e detalhes do evento.
Abas propostas:
- `Clientes`: cadastro de clientes com nome, e-mail, telefone, tipo de evento, data de cadastro
- `Leads`: origem do contato (WhatsApp, Instagram, Google Meu Negócio, formulário), interesse, status de negociação
- `Eventos Agendados`: informações detalhadas por evento, número de convidados, orçamento aprovado, serviços extras, status de pagamento
- `Histórico`: registros de reuniões, propostas enviadas, follow-up e resultados
- `Documentos`: links para contratos, fotos, orçamentos ou outros arquivos relevantes

## 3. Formulários Google Forms Recomendados
### 3.1 Formulário de Solicitação de Orçamento / Lead
Objetivo: captar dados dos clientes automaticamente.
Campos sugeridos:
- Nome completo
- E-mail
- Telefone / WhatsApp
- Tipo de evento (casamento, aniversário, bodas, formatura, outro)
- Data preferencial do evento
- Número estimado de convidados
- Serviço desejado (espaço, decoração, buffet, som, bar, limpeza, etc.)
- Orçamento aproximado ou faixa de valor
- Mensagem adicional / observações
- Como nos encontrou? (Instagram, WhatsApp, Google, indicação, outro)

### 3.2 Formulário de Contratação de Parceiro / Fornecedor
Objetivo: registrar dados de fornecedores e serviços terceirizados.
Campos sugeridos:
- Nome do fornecedor / empresa
- Categoria de serviço (limpeza, decoração, buffet, som, bar, segurança, outros)
- Contato principal
- Telefone / WhatsApp
- E-mail
- Condições de pagamento
- Observações sobre disponibilidade e exigências técnicas
- Rating ou avaliação inicial

### 3.3 Formulário de Briefing de Evento (opcional)
Objetivo: coletar detalhes aprofundados para cada evento.
Campos sugeridos:
- Nome do cliente
- Evento vinculado
- Preferências de decoração e tema
- Requisitos de buffet e menu
- Necessidades de som e iluminação
- Horário de início e fim do evento
- Quantidade de convidados
- Observações especiais

## 4. Integração entre Formulários e Planilhas
- Cada formulário deve ser conectado a uma aba correspondente no Google Sheets
- O formulário de orçamento deve alimentar automaticamente `Clientes` ou `Leads`
- O formulário de parceiro deve alimentar `Fornecedores`
- O briefing de evento deve alimentar `Eventos Agendados`
- Utilizar fórmulas para vincular dados do `Leads` ao `Eventos Agendados` quando um orçamento evoluir para fechamento

## 5. Estrutura de Dados e Relacionamentos
- `Leads` são potenciais clientes; quando o interesse é confirmado, gerar um registro em `Clientes` e `Eventos Agendados`
- `Eventos Agendados` deve referenciar `Clientes` e `Fornecedores` utilizados
- `Custos Variáveis` e `Receitas` devem referenciar o código ou nome do evento para análise consolidada
- `Checklist` deve ser atualizado por evento, com status de tarefas e responsáveis
- `Resumo` deve consolidar informações das demais abas para gerar indicadores em uma visão única

## 6. Campos-chave para cada aba
### 6.1 Clientes / Leads
- ID
- Nome completo
- Contato (telefone, WhatsApp, e-mail)
- Origem do contato
- Tipo de evento
- Data desejada
- Status (novo, em negociação, aprovado, cancelado)
- Próxima ação / follow-up

### 6.2 Eventos Agendados
- ID do evento
- Cliente (nome ou ID)
- Data do evento
- Tipo de evento
- Convidados previstos
- Serviços contratados
- Valor do orçamento
- Status do evento
- Pagamento inicial / sinal
- Observações

### 6.3 Custos Fixos
- Categoria do custo
- Valor mensal
- Vencimento
- Status do pagamento
- Observações

### 6.4 Custos Variáveis
- ID do evento
- Descrição do gasto
- Categoria do gasto
- Valor
- Fornecedor
- Data
- Observações

### 6.5 Orçamentos / Receita
- ID do evento
- Custo direto estimado
- Custo fixo alocado
- Margem desejada
- Preço sugerido
- Preço aprovado
- Receita recebida
- Data de pagamento

### 6.6 Fornecedores
- Nome do fornecedor
- Serviço oferecido
- Contato
- Condições comerciais
- Comentários sobre desempenho

## 7. Painéis e Automação
- Criar um painel de controle (`Resumo`) com gráficos simples de receita, inscrição de clientes e eventos agendados
- Utilizar formatação condicional para destacar eventos próximos e status de pagamento
- Adicionar fórmulas de soma e média para custos por evento, margem e fluxo de caixa
- Usar validação de dados para garantir tipos de eventos e categorias padronizadas

## 8. Prioridades de Implementação
1. Criar o modelo de `Clientes / Eventos` com formulário de orçamento conectado
2. Criar a planilha financeira com abas de `Custos Fixos`, `Custos Variáveis`, `Orçamentos` e `Resumo`
3. Criar a planilha operacional com `Eventos`, `Fornecedores`, `Checklist` e `Agenda`
4. Conectar Google Forms a planilhas para coleta automática de dados
5. Testar o fluxo com entradas simuladas e ajustar campos necessários
6. Definir como os dados serão atualizados e quem terá acesso

## 9. Observações Importantes
- O Google Forms deve ser usado sempre que possível para captar dados de clientes e fornecedores sem preenchimento manual
- Manter nomes de campos coerentes entre formulários e abas do Sheets
- Documentar no próprio Google Sheets como os campos são usados para cada processo
- O formulário deve ser acessível via link compartilhado em canais de divulgação ou enviado diretamente para o cliente

## 10. Próximos Passos
- Validar quais dados obrigatórios são necessários antes de iniciar a planilha
- Preparar o layout das abas e nomes de campos no Google Sheets
- Criar os formulários e conectar às planilhas
- Definir uma rotina de manutenção semanal das planilhas e dos dados coletados
