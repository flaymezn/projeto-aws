import json

def lambda_handler(event, context):
    """
    Esta é a função principal que a Amazon (AWS) vai executar 
    toda vez que alguém enviar uma mensagem para o nosso sistema.
    """
    try:
        # 1. Pegar o corpo da mensagem que chegou da internet
        corpo = json.loads(event.get('body', '{}'))
        
        # 2. Extrair o nome e a mensagem enviados pelo usuário
        nome_usuario = corpo.get('nome', 'Visitante Anônimo')
        mensagem_texto = corpo.get('mensagem', '')
        
        # 3. Criar uma resposta inteligente automatizada
        resposta_texto = f"Olá {nome_usuario}! Recebemos sua mensagem: '{mensagem_texto}'. Ela foi processada com sucesso na Nuvem da AWS!"
        
        # 4. Retornar um status de Sucesso (Código 200) para quem enviou
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*' # Permite que qualquer site use nossa API
            },
            'body': json.dumps({
                'status': 'Sucesso',
                'resposta': resposta_texto
            })
        }
        
    except Exception as e:
        # Se acontecer qualquer erro, avisa quem enviou (Código 500)
        return {
            'statusCode': 500,
            'body': json.dumps({'erro': str(e)})
        }