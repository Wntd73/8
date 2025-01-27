'''Требуется написать ООП с графическим интерфейсом в соответствии со своим вариантом. 
Должны быть реализованы минимум один класс, три атрибута, четыре метода (функции). 
Ввод данных из файла с контролем правильности ввода. 
Базы данных не использовать. При необходимости сохранять информацию в файлах, разделяя значения запятыми (CSV файлы) или пробелами. Для GUI и визуализации использовать библиотеку tkinter.
Объекты – договоры на трудоустройство
Функции:	сегментация полного списка договоров по компаниям, обратившимся за специалистами
визуализация предыдущей функции в форме круговой диаграммы
сегментация полного списка договоров по профессиям
визуализация предыдущей функции в форме круговой диаграммы
'''

import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from collections import Counter

class EmploymentContract:
    def __init__(self):
        self.contracts = []

    def add_contract(self, company_name, profession, contract_date):
        if company_name and profession and contract_date:
            self.contracts.append({
                'company_name': company_name,
                'profession': profession,
                'contract_date': contract_date
            })
            messagebox.showinfo("Успех", "Договор добавлен успешно.")
        else:
            messagebox.showerror("Ошибка", "Все поля должны быть заполнены.")

    def segment_by_company(self):
        return Counter(contract['company_name'] for contract in self.contracts)

    def segment_by_profession(self):
        return Counter(contract['profession'] for contract in self.contracts)

    def visualize(self, data, title):
        labels = data.keys()
        sizes = data.values()
        plt.figure(figsize=(8, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title(title)
        plt.axis('equal')
        plt.show()

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Договоры на трудоустройство")
        self.root.geometry("300x300")
        self.contract_manager = EmploymentContract()

        self.company_name_entry = tk.Entry(root, width=30)
        self.company_name_entry.pack(pady=5)
        self.company_name_entry.insert(0, "Название компании")

        self.profession_entry = tk.Entry(root, width=30)
        self.profession_entry.pack(pady=5)
        self.profession_entry.insert(0, "Профессия")

        self.contract_date_entry = tk.Entry(root, width=30)
        self.contract_date_entry.pack(pady=5)
        self.contract_date_entry.insert(0, "Дата контракта (ДД.ММ.ГГГГ)")

        self.add_contract_button = tk.Button(root, text="Добавить договор", command=self.add_contract)
        self.add_contract_button.pack(pady=10)

        self.segment_company_button = tk.Button(root, text="Сегментация по компаниям", command=self.segment_by_company)
        self.segment_company_button.pack(pady=10)

        self.segment_profession_button = tk.Button(root, text="Сегментация по профессиям", command=self.segment_by_profession)
        self.segment_profession_button.pack(pady=10)

    def add_contract(self):
        company_name = self.company_name_entry.get()
        profession = self.profession_entry.get()
        contract_date = self.contract_date_entry.get()
        self.contract_manager.add_contract(company_name, profession, contract_date)

    def segment_by_company(self):
        data = self.contract_manager.segment_by_company()
        self.contract_manager.visualize(data, "Сегментация по компаниям")

    def segment_by_profession(self):
        data = self.contract_manager.segment_by_profession()
        self.contract_manager.visualize(data, "Сегментация по профессиям")

root = tk.Tk()
app = App(root)
root.mainloop()