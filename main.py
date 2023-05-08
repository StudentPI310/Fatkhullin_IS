import tkinter as tk


class TaxCalculator:
	def __init__(self, master):
		self.master = master
		master.title("Налоговый калькулятор")

		# Создание виджетов
		self.income_label = tk.Label(master, text="Доход:", padx=10, pady=10, font=("Arial", 14))
		self.income_entry = tk.Entry(master, font=("Arial", 14))

		self.tax_type_label = tk.Label(master, text="Тип налога:", padx=10, pady=10, font=("Arial", 14))
		self.tax_type_var = tk.StringVar(value="НДФЛ")
		self.tax_type_radio1 = tk.Radiobutton(master, text="НДФЛ", variable=self.tax_type_var, value="НДФЛ",
											  font=("Arial", 14))
		self.tax_type_radio2 = tk.Radiobutton(master, text="НДС", variable=self.tax_type_var,
											  value="НДС", font=("Arial", 14))

		self.calculate_button = tk.Button(master, text="Рассчитать", command=self.calculate_tax, font=("Arial", 14))

		self.result_label = tk.Label(master, text="", padx=10, pady=10, font=("Arial", 14), anchor="w")

		# Размещение виджетов на экране
		self.income_label.grid(row=0, column=0)
		self.income_entry.grid(row=0, column=1)
		self.tax_type_label.grid(row=1, column=0)
		self.tax_type_radio1.grid(row=1, column=1, sticky="w")
		self.tax_type_radio2.grid(row=2, column=1, sticky="w")
		self.calculate_button.grid(row=3, column=1, pady=10)
		self.result_label.grid(row=4, column=0, columnspan=2, padx=10)

	def calculate_tax(self):
		income = float(self.income_entry.get())
		tax_type = self.tax_type_var.get()

		if tax_type == "НДФЛ":
			tax = income * 0.13
		else:
			tax = income * 0.2

		self.result_label.configure(text="Налог: {:.2f}".format(tax))


root = tk.Tk()
root.geometry("400x300")
my_gui = TaxCalculator(root)
root.mainloop()