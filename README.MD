sistema web completo:

Usuario pesquisa por um molde no site (frontend react)
backend FastApi responde onde esta esse molde
Raspberry Pis monitoram a movimentação dos moldes(presença e ausencia) usando sensores
Leds e buzzers são usados para indicar localização ou alertar
tudo funcionando em tempo real


funcionalidades:

Raspberry Pi  -	Lê sensores, controla buzzer/LED, envia informações pro back-end ou executa comandos que vierem do back-end

FastAPI (Back-end) - CRUD de moldes, API para receber status das Raspberries, API para mandar comandos,armazena as informações do rasp no banco

React (Front-end) -	Tela para o usuário pesquisar moldes, ver status em tempo real, interagir com sistema

rodar projeto - uvicorn main:app --reload

Criar molde - POST/moldes/
Buscar moldes - GET/moldes/
Buscar molde por ID - GET/ moldes/{id}
Atualizar molde - PUT/moldes/{id}
Deletar molde - DELETE/moldes/{id}

depois que o banco de dados é atualizado 
testar a rota POST/moldes / para criar moldes
ver se o arquivo database.db é atualizado

importante : IP da maquina que esta rodando o FastApi,ip config

a porta deve estar aberta e o fastapi rodando :uvicorn app.main:app --host 0.0.0.0 --port 8000

Deixe a porta 8000 liberada no seu firewall (ou desativa firewall enquanto testa, com cuidado!).

instalar na rasp: pip install requests