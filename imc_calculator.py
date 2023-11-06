import tkinter as tk
from tkinter import messagebox

# Função calcular IMC
def calcular_imc():
    try:
        peso = float(peso_entry.get())
        altura = float(altura_entry.get()) / 100  # Converter altura de cm para m
        imc = peso / (altura ** 2)
        resultado_label.config(text=f"IMC: {imc:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Certifique-se de que os valores de peso e altura sejam numéricos.")

# Função limpar campos
def limpar_campos():
    nome_entry.delete(0, 'end')
    endereco_entry.delete(0, 'end')
    altura_entry.delete(0, 'end')
    peso_entry.delete(0, 'end')
    resultado_label.config(text="IMC:")

# Função para aplicativo
def sair():
    janela.quit()

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")

# campos de entrada
nome_label = tk.Label(janela, text="Nome do Paciente:")
nome_label.pack()
nome_entry = tk.Entry(janela)
nome_entry.pack()

endereco_label = tk.Label(janela, text="Endereço Completo:")
endereco_label.pack()
endereco_entry = tk.Entry(janela)
endereco_entry.pack()

altura_label = tk.Label(janela, text="Altura (cm):")
altura_label.pack()
altura_entry = tk.Entry(janela)
altura_entry.pack()

peso_label = tk.Label(janela, text="Peso (kg):")
peso_label.pack()
peso_entry = tk.Entry(janela)
peso_entry.pack()

resultado_label = tk.Label(janela, text="IMC:")
resultado_label.pack()

# Botões
calcular_button = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
calcular_button.pack()

limpar_button = tk.Button(janela, text="Reiniciar", command=limpar_campos)
limpar_button.pack()

sair_button = tk.Button(janela, text="Sair", command=sair)
sair_button.pack()

# Iniciar interface gráfica
janela.mainloop()
