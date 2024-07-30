from flask import Flask, render_template, request, jsonify, send_file
from pytube import YouTube
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'success': False, 'error': 'No URL provided'}), 400

    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        output_path = 'downloads'
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        filepath = stream.download(output_path=output_path)
        filename = os.path.basename(filepath)
        return jsonify({'success': True, 'filename': filename}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join('downloads', filename), as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
