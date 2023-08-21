import webview

class API:
    def load_inputs(self):
        # Adicione aqui o código para carregar os inputs
        print('clicou')
        response = {
            'message': 'Load Inputs'
        }
        return response

    def generate_report(self):
        # Adicione aqui o código para gerar o relatório
        response = {
            'message': 'generate report'
        }
        return response

    def clear_all(self):
        # Adicione aqui o código para limpar tudo
        response = {
            'message': 'clear all'
        }
        return response

    def generate_log(self):
        # Adicione aqui o código para gerar o log
        response = {
            'message': 'generate log'
        }
        return response

    def printar(self, mensagem):
        '''
        Printar apenas para testes, informações vindas do HTML
        :param mensagem:
        :return:
        '''
        print(mensagem)

def main():
    with open('index.html', 'r') as file:
        html_content = file.read()
    api = API()
    window = webview.create_window(
        title="Sua Ferramenta",
        html=html_content,
        js_api=api,
        width=800,
        height=600
    )

    webview.start(debug=False)

if __name__ == '__main__':
    main()
