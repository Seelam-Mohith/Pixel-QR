from flask import Flask, render_template, request, send_file, session, redirect, url_for
import qrcode
import io
import base64
import os
from PIL import Image

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_generated = False
    qr_image = None
    if request.method == 'POST':
        url = request.form.get('url')
        action = request.form.get('action')
        if url and action == 'generate':
            qr = qrcode.QRCode(
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
            buffer = io.BytesIO()
            img.save(buffer, 'PNG')
            buffer.seek(0)
            # Store the image in session as base64
            img_b64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
            session['qr_image'] = img_b64
            qr_generated = True
            qr_image = f"data:image/png;base64,{img_b64}"
            return render_template('index.html', qr_generated=qr_generated, qr_image=qr_image)
    # For GET or after generation
    qr_generated = 'qr_image' in session
    qr_image = f"data:image/png;base64,{session['qr_image']}" if qr_generated else None
    return render_template('index.html', qr_generated=qr_generated, qr_image=qr_image)

@app.route('/download')
def download_qr():
    img_b64 = session.get('qr_image')
    if not img_b64:
        return redirect(url_for('index'))
    buffer = io.BytesIO(base64.b64decode(img_b64))
    buffer.seek(0)
    return send_file(buffer, mimetype='image/png', as_attachment=True, download_name='qrcode.png')

@app.route('/visitor-ip')
def visitor_ip():
    # Render passes the real IP in X-Forwarded-For
    visitor_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    print(f"Visitor IP: {visitor_ip}")
    return f"Visitor IP: {visitor_ip}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)