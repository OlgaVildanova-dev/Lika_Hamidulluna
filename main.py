    # --- Виджеты ---
    self.create_widgets()
    self.update_history_list()

def create_widgets(self):
    # Фильтр по типу
    ttk.Label(self.root, text="Фильтр по типу:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    self.filter_var = tk.StringVar(value="все")
    filter_options = ["все", "учёба", "спорт", "работа"]
    ttk.OptionMenu(self.root, self.filter_var, *filter_options, command=self.update_history_list).grid(
        row=0, column=1, padx=10, pady=5, sticky="w"
    )

    # Кнопка генерации
    ttk.Button(self.root, text="Сгенерировать задачу", command=self.generate_task).grid(
        row=1, column=0, columnspan=2, pady=10
    )

    # Поле результата
    self.result_label = ttk.Label(self.root, text="Ваша задача появится здесь", font=("Arial", 12))
    self.result_label.grid(row=2, column=0, columnspan=2, pady=10)

    # Список истории
    ttk.Label(self.root, text="История:").grid(row=3, column=0, columnspan=2, pady=(10, 0))
    self.history_listbox = tk.Listbox(self.root, width=50, height=10)
    self.history_listbox.grid(row=4, column=0, columnspan=2, padx=10)

def generate_task(self):
    task = random.choice(self.tasks)
    self.history.append(task)
    self.save_history()
    self.result_label.config(text=f"Задача: {task['name']} (тип: {task['type']})")
    self.update_history_list()

def update_history_list(self):
    self.history_listbox.delete(0, tk.END)
    filter_type = self.filter_var.get()
    for task in self.history:
        if filter_type == "все" or task["type"] == filter_type:
            self.history_listbox.insert(tk.END, f"{task['name']} ({task['type']})")

def load_history(self):
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить историю: {e}")
            return []
    return []

def save_history(self):
    try:
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить историю: {e}")
