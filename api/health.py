def handler(request):
    # Headers CORS para todas las respuestas
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': '*',
        'Content-Type': 'application/json'
    }
    
    # Manejar preflight request
    if request.method == 'OPTIONS':
        return ('', 200, headers)
    
    # Health check response
    response_data = {
        "status": "ok", 
        "message": "API funcionando correctamente"
    }
    
    import json
    return (json.dumps(response_data), 200, headers)