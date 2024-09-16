class Serial:
    title = ""
    num_of_ep = 0
    rating = 0

#-----------------------------------------------

    def __init__(self, inp_title, inp_num_of_ep, inp_rating) -> None:
        self.title = inp_title
        self.num_of_ep = inp_num_of_ep
        self.rating = inp_rating
        pass

    def set_title(self) -> None:
        self.title = input("Введите название сериала: ")
        pass
  
    def set_rating(self) -> None:
        while True:
            try:
                rating = float(input("Введите рейтинг фильма: "))
                if rating < 0 or rating > 5:
                    print("Рейтинг фильма может быть только от 0 до 5")
                else:
                    self.rating = rating
                    break
            except ValueError:
                print("Рейтинг фильма может быть только вещественным числом")
        pass

    def set_num_of_ep(self) -> None:
        while True:
            try:
                eps = int(input("Введите количество серий в сериале: "))
                if eps <= 0:
                    print("Количество серий должно быть положительным")
                else:
                    self.num_of_ep = eps
                    break
            except ValueError:
                print("Количество серий может быть только целым числом")
        pass

#-----------------------------------------------

    def get_title(self) -> str:
        return self.title

    def get_num_of_ep(self) -> int:
        return self.num_of_ep
    
    def get_rating(self) -> float:
        return self.rating

class Film:
    title = ""
    duration = 0
    rating = 0

#-----------------------------------------------

    def __init__(self, inp_title, inp_duratoin, inp_rating) -> None:
        self.title = inp_title
        self.duration = inp_duratoin
        self.rating = inp_rating
        pass

    def set_title(self) -> None:
        self.title = input("Введите название фильма: ")
        pass

    def set_duration(self) -> None:
        while True:
            try:
                duration = int(input("Введите хронометраж фильма в минутах: "))
                if duration <= 0:
                    print("Хронометраж должно быть быть положительным")
                else:
                    self.duration = duration
                    break
            except ValueError:
                print("Хронометраж фильма может быть только целым числом")
        pass

    def set_rating(self) -> None:

        while True:
            try:
                rating = float(input("Введите рейтинг фильма: "))
                if rating < 0 or rating > 5:
                    print("Рейтинг фильма может быть только от 0 до 5")
                else:
                    self.rating = rating
                    break
            except ValueError:
                print("Рейтинг фильма может быть только вещественным числом")
        pass

#-----------------------------------------------

    def get_title(self) -> str:
        return self.title

    def get_duration(self) -> int:
        return self.duration
    
    def get_rating(self) -> float:
        return self.rating
    


