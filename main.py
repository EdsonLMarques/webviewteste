import webview
import time
from API import API

def load_html(window):
    with open('src/index.html', 'r') as file:
        html_content = file.read()
    time.sleep(1)
    window.load_html(html_content)

def main():
    with open('src/components/home_screen.html', 'r') as file:
        html_content = file.read()
    api = API()
    window = webview.create_window(
        title="Teste pywebview",
        html=html_content,
        js_api=api,
        width=800,
        height=600
    )
    webview.start(load_html, window)

if __name__ == '__main__':
    main()
