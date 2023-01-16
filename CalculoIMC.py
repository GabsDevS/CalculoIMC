import PySimpleGUI as sg
from time import sleep

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkAmber')
        # Layout
        layout = [
            [sg.Text('Nome', size=(10, 0)), sg.Input(size=(20, 0), key='nome')],
            [sg.Text('Idade', size=(10, 0)), sg.Input(size=(5, 0), key='idade')],
            [sg.Text('Peso (KG)', size=(10, 0)), sg.Input(size=(5, 0), key='peso')],
            [sg.Text('Altura', size=(10, 0)), sg.Input(size=(5, 0), key='altura')],
            [sg.Text('Selecione o Sexo: ')],
            [sg.Radio('Homem','sexo', key='homem'), sg.Radio('Mulher', 'sexo', key='mulher')],
            [sg.Button('Calcular')],
            [sg.Output(size=(50, 50))]
        ]
        # Janela
        self.janela = sg.Window("Calculo de IMC", size=(350, 350)).layout(layout)



    def iniciar(self):
        imc = 0
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            homem = self.values['homem']
            mulher = self.values['mulher']
            peso = float(self.values['peso'])
            altura = float(self.values['altura'])

            imc = peso / (altura ** 2)
            print('Calculando...\n')
            sleep(3)

            if imc < 18.5:
                print('Você está abaixo do peso !')
                print('Precisa engordar um pouquinho em kkkk !')
            elif 18 <= imc < 24.9:
                print('Seu Peso está normal !')
                print('Parabéns seu peso está ótimo !')
            elif 25 <= imc < 29.9:
                print('Você está com Sobrepeso !')
                print('Vamos dar uma moderada ai meu filho !')
            elif 30 <= imc < 34.9:
                print('Você está com Obesidade Grau 1')
                print('Comece a fazer uma dieta, bolofote !')
            elif 35 <= imc < 39.9:
                print('Você está com Obesidade Grau 2')
                print('Procure um médico seu gordo !')
            else:
                print('Você está com Obseidade Grau 3')
                print('Meu Deus !!! você vai morrer !')

            print('Seu IMC é: {:.1f}kg/m2'.format(imc))


tela = TelaPython()
tela.iniciar()