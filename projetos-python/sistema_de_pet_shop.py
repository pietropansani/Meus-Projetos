import tkinter as tk
from tkinter import messagebox, ttk

# --- LÓGICA E SESSÃO DE DADOS ---
agendamentos = []

def confirmar_agendamento():
    # Coleta de dados dos campos de texto da tela
    cliente = entry_cliente.get().strip()
    pet = entry_pet.get().strip()
    servico = combo_servico.get()
    data = entry_data.get().strip()
    horario = entry_horario.get().strip()

    # Validação simples para não deixar campos vazios
    if not cliente or not pet or not data or not horario:
        messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos antes de confirmar!")
        return

    # Tela de Confirmação visual (Popup)
    mensagem_confirmacao = f"Deseja confirmar o agendamento?\n\nCliente: {cliente}\nPet: {pet}\nServiço: {servico}\nHorário: {horario}"
    resposta = messagebox.askyesno("Confirmar Agendamento", mensagem_confirmacao)

    if resposta: # Se o usuário clicar em 'Sim'
        # Salva no banco de dados temporário (lista)
        novo_registro = {
            "cliente": cliente,
            "pet": pet,
            "servico": servico,
            "data": data,
            "horario": horario
        }
        agendamentos.append(novo_registro)
        
        # Atualiza os componentes visuais da tela
        atualizar_agenda_diaria()
        atualizar_resumo_servicos()
        
        # Limpa os campos de entrada para o próximo agendamento
        entry_cliente.delete(0, tk.END)
        entry_pet.delete(0, tk.END)
        entry_data.delete(0, tk.END)
        entry_horario.delete(0, tk.END)
        combo_servico.current(0)
        
        messagebox.showinfo("Sucesso", f"Agendamento do pet {pet} realizado!")

def atualizar_agenda_diaria():
    # Limpa a tabela visual para não duplicar dados
    for linha in tabela_agenda.get_children():
        tabela_agenda.delete(linha)
        
    # Ordena a lista por horário antes de exibir na tabela
    agendamentos_ordenados = sorted(agendamentos, key=lambda x: x['horario'])
    
    # Insere os dados ordenados na tabela visual
    for agend in agendamentos_ordenados:
        tabela_agenda.insert("", tk.END, values=(agend["horario"], agend["pet"], agend["cliente"], agend["servico"]))

def atualizar_resumo_servicos():
    # Zera os contadores
    banho = 0
    tosa = 0
    banho_e_tosa = 0
    
    # Recalcula com base na lista atualizada
    for agend in agendamentos:
        if agend["servico"] == "Banho":
            banho += 1
        elif agend["servico"] == "Tosa":
            tosa += 1
        elif agend["servico"] == "Banho e Tosa":
            banho_e_tosa += 1
            
    # Atualiza os textos dos labels na interface gráfica
    lbl_total_banho.config(text=f"Banhos: {banho}")
    lbl_total_tosa.config(text=f"Tosas: {tosa}")
    lbl_total_combo.config(text=f"Banhos e Tosas: {banho_e_tosa}")
    lbl_total_geral.config(text=f"Total de Pets no Dia: {len(agendamentos)}")


# --- CONSTRUÇÃO DA INTERFACE GRÁFICA (Tkinter) ---
janela = tk.Tk()
janela.title("PET SHOP AMIGO FIEL - Sistema de Gestão")
janela.geometry("750x550")
janela.resizable(False, False)

# Título Principal
lbl_titulo = tk.Label(janela, text="PET SHOP AMIGO FIEL", font=("Arial", 16, "bold"), fg="#1a5276")
lbl_titulo.pack(pady=10)

# --- CONTAINER superior: Formulario de Cadastro ---
# CORRIGIDO: Alterado para ttk.LabelFrame para aceitar a opção padding
frame_formulario = ttk.LabelFrame(janela, text=" [ Registrar Novo Agendamento ] ", padding=10)
frame_formulario.pack(fill="x", padx=15, pady=5)

tk.Label(frame_formulario, text="Nome do Cliente:").grid(row=0, column=0, sticky="w", pady=2)
entry_cliente = tk.Entry(frame_formulario, width=30)
entry_cliente.grid(row=0, column=1, pady=2, padx=5)

tk.Label(frame_formulario, text="Nome do Pet:").grid(row=0, column=2, sticky="w", pady=2)
entry_pet = tk.Entry(frame_formulario, width=25)
entry_pet.grid(row=0, column=3, pady=2, padx=5)

tk.Label(frame_formulario, text="Serviço:").grid(row=1, column=0, sticky="w", pady=5)
combo_servico = ttk.Combobox(frame_formulario, values=["Banho", "Tosa", "Banho e Tosa"], state="readonly", width=27)
combo_servico.current(0)
combo_servico.grid(row=1, column=1, pady=5, padx=5)

tk.Label(frame_formulario, text="Data (DD/MM):").grid(row=1, column=2, sticky="w", pady=5)
entry_data = tk.Entry(frame_formulario, width=10)
entry_data.grid(row=1, column=3, sticky="w", pady=5, padx=5)

tk.Label(frame_formulario, text="Horário (HH:MM):").grid(row=1, column=3, sticky="e", pady=5)
entry_horario = tk.Entry(frame_formulario, width=8)
entry_horario.grid(row=1, column=4, sticky="w", pady=5, padx=5)

# Botão de confirmação
btn_confirmar = tk.Button(frame_formulario, text="[ Confirmar Agendamento ]", bg="#27ae60", fg="white", font=("Arial", 10, "bold"), command=confirmar_agendamento)
btn_confirmar.grid(row=2, column=0, columnspan=5, pady=10)


# --- CONTAINER do meio: Consulta da Agenda Diária ---
# CORRIGIDO: Alterado para ttk.LabelFrame para aceitar a opção padding
frame_agenda = ttk.LabelFrame(janela, text=" [ Consultar Agenda Diária ] ", padding=10)
frame_agenda.pack(fill="both", expand=True, padx=15, pady=5)

# Criação de uma tabela real (Treeview) para listar a agenda
colunas = ("horario", "pet", "cliente", "servico")
tabela_agenda = ttk.Treeview(frame_agenda, columns=colunas, show="headings", height=6)
tabela_agenda.heading("horario", text="Horário")
tabela_agenda.heading("pet", text="Nome do Pet")
tabela_agenda.heading("cliente", text="Cliente")
tabela_agenda.heading("servico", text="Serviço Definido")

# Ajuste da largura das colunas
tabela_agenda.column("horario", width=70, anchor="center")
tabela_agenda.column("pet", width=120)
tabela_agenda.column("cliente", width=150)
tabela_agenda.column("servico", width=150)
tabela_agenda.pack(fill="both", expand=True)


# --- CONTAINER inferior: Visualizar Serviços Marcados (Resumo) ---
# CORRIGIDO: Alterado para ttk.LabelFrame para aceitar a opção padding
frame_resumo = ttk.LabelFrame(janela, text=" [ Visualizar Serviços Marcados ] ", padding=10)
frame_resumo.pack(fill="x", padx=15, pady=10)

lbl_total_banho = tk.Label(frame_resumo, text="Banhos: 0", font=("Arial", 10, "bold"))
lbl_total_banho.pack(side="left", padx=20)

lbl_total_tosa = tk.Label(frame_resumo, text="Tosas: 0", font=("Arial", 10, "bold"))
lbl_total_tosa.pack(side="left", padx=20)

lbl_total_combo = tk.Label(frame_resumo, text="Banhos e Tosas: 0", font=("Arial", 10, "bold"))
lbl_total_combo.pack(side="left", padx=20)

lbl_total_geral = tk.Label(frame_resumo, text="Total de Pets no Dia: 0", font=("Arial", 10, "bold"), fg="#1a5276")
lbl_total_geral.pack(side="right", padx=20)


# Inicia a janela do aplicativo
janela.mainloop()