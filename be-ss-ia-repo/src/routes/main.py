from flask import Blueprint, render_template_string

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Mini-plantilla HTML integrada
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FESC-IA Backend Status</title>
        <style>
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                display: flex; justify-content: center; align-items: center; 
                height: 100vh; margin: 0; background-color: #f0f8ff; 
            }
            .card { 
                background: white; padding: 2rem; border-radius: 12px; 
                box-shadow: 0 4px 15px rgba(0,0,0,0.1); text-align: center;
                border-top: 5px solid #1867C0;
            }
            h1 { color: #333; margin-bottom: 0.5rem; }
            p { color: #666; }
            .status-badge { 
                background-color: #4CAF50; color: white; padding: 5px 15px; 
                border-radius: 20px; font-size: 0.9rem; font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>FESC-IA Backend</h1>
            <p>El servidor Flask está operando correctamente.</p>
            <p>Estructura de <b>Blueprints</b>: <span class="status-badge">ACTIVA</span></p>
            <hr style="border: 0; border-top: 1px solid #eee; margin: 1.5rem 0;">
            <p style="font-size: 0.8rem; color: #999;">Ready for Frontend Connection</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)