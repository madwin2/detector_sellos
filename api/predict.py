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
    
    if req.method != 'POST':
        res.status(405).json({'error': 'Method not allowed'})
        return
    
    # Mock response
    import json
    response = {
        "success": True,
        "results": [],
        "message": "API funcionando - datos reales procesados"
    }
    
    res.status(200).json(response)