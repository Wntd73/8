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
import csv
import matplotlib.pyplot as plt
from collections import Counter

class EmploymentContract:
    def __init__(self):
        self.contracts = []

    def load_contracts(self, file_path):
        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) == 3:
                        self.contracts.append({
                            'company_name': row[0],
                            'profession': row[1],
                            'contract_date': row[2]
                        })
                    else:
                        raise ValueError("Неверный формат данных в файле.")
            messagebox.showinfo("Успех", "Данные загружены успешно.")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

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
    def __init__(self, root, file_path):
        self.root = root
        self.root.title("Договоры на трудоустройство")
        self.contract_manager = EmploymentContract()
        self.contract_manager.load_contracts(file_path)

        self.segment_company_button = tk.Button(root, text="Сегментация по компаниям", command=self.segment_by_company)
        self.segment_company_button.pack(pady=10)

        self.segment_profession_button = tk.Button(root, text="Сегментация по профессиям", command=self.segment_by_profession)
        self.segment_profession_button.pack(pady=10)

    def segment_by_company(self):
        data = self.contract_manager.segment_by_company()
        self.contract_manager.visualize(data, "Сегментация по компаниям")

    def segment_by_profession(self):
        data = self.contract_manager.segment_by_profession()
        self.contract_manager.visualize(data, "Сегментация по профессиям")

root = tk.Tk()

file_path = 'input.csv'  
app = App(root, file_path)
root.mainloop()