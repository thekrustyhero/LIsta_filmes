# Aplicativo para criar listas de filmes


import tkinter as tk
from datetime import date

class MovieListGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Lista de Filmes")
        self.root.geometry("400x400")

        self.movies_watched = []
        self.movies_to_watch = []

        self.create_widgets()

    def create_widgets(self):
        # Label para indicar a seção de filmes assistidos
        watched_label = tk.Label(self.root, text="Filmes Assistidos")
        watched_label.pack()

        # Lista para exibir os filmes assistidos
        self.watched_listbox = tk.Listbox(self.root)
        self.watched_listbox.pack()

        # Entry para adicionar filmes assistidos
        watched_entry = tk.Entry(self.root)
        watched_entry.pack()

        # Botão para adicionar filmes assistidos
        watched_button = tk.Button(self.root, text="Adicionar Filme Assistido",
                                   command=lambda: self.add_movie(watched_entry.get(), self.movies_watched))
        watched_button.pack()

        # Label para indicar a seção de filmes para assistir
        to_watch_label = tk.Label(self.root, text="Filmes para Assistir")
        to_watch_label.pack()

        # Lista para exibir os filmes para assistir
        self.to_watch_listbox = tk.Listbox(self.root)
        self.to_watch_listbox.pack()

        # Entry para adicionar filmes para assistir
        to_watch_entry = tk.Entry(self.root)
        to_watch_entry.pack()

        # Botão para adicionar filmes para assistir
        to_watch_button = tk.Button(self.root, text="Adicionar Filme para Assistir",
                                    command=lambda: self.add_movie(to_watch_entry.get(), self.movies_to_watch))
        to_watch_button.pack()

    def add_movie(self, movie_title, movie_list):
        # Verificar se o filme já foi adicionado a alguma lista
        if movie_title in self.movies_watched or movie_title in self.movies_to_watch:
            tk.messagebox.showwarning("Filme já adicionado", f"O filme '{movie_title}' já foi adicionado à lista em {self.get_movie_date(movie_title)}.")
        else:
            # Adicionar o filme à lista correspondente
            movie_list.append(movie_title)

            # Adicionar o filme à listabox correspondente
            if movie_list == self.movies_watched:
                self.watched_listbox.insert(tk.END, movie_title)
            else:
                self.to_watch_listbox.insert(tk.END, movie_title)

    def get_movie_date(self, movie_title):
        # Verificar em qual lista o filme foi adicionado
        if movie_title in self.movies_watched:
            movie_list = self.movies_watched
        else:
            movie_list = self.movies_to_watch

        # Obter a data em que o filme foi adicionado à lista
        movie_index = movie_list.index(movie_title)
        movie_date = date.today().strftime("%d/%m/%Y")

        return movie_date

    def run(self):
        self.root.mainloop()

# Criar a instância do GUI e executar
movie_list_gui = MovieListGUI()
movie_list_gui.run()


