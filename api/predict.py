def handler(request):
    import json
    import hashlib
    
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
    
    if request.method != 'POST':
        return (json.dumps({"error": "Method not allowed"}), 405, headers)
    
    try:
        # Simple mock response for now
        response_data = {
            "success": True,
            "results": [],
            "message": "API funcionando - datos mock"
        }
        
        return (json.dumps(response_data), 200, headers)
        
    except Exception as e:
        error_response = {"success": False, "error": str(e)}
        return (json.dumps(error_response), 500, headers)