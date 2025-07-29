def handler(req, res):
    # Set CORS headers
    res.setHeader('Access-Control-Allow-Origin', '*')
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    res.setHeader('Access-Control-Allow-Headers', '*')
    res.setHeader('Content-Type', 'application/json')
    
    # Handle preflight
    if req.method == 'OPTIONS':
        res.status(200).end()
        return
    
    response = {"status": "ok", "message": "API funcionando correctamente"}
    res.status(200).json(response)