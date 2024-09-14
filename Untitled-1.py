class Episode:
    title = ""
    duration = 0
    num_ep = 0

    def __init__(self, inp_title, inp_duration, inp_num_ep):
        self.title = inp_title
        self.duration - inp_duration
        self.num_ep = inp_num_ep

class Serial:
    title = ""
    num_of_ep = 0
    rating = 0
    episodes = []

    def __init__(self, inp_title, inp_num_of_ep, inp_rating):
        self.title = inp_title
        self.num_of_ep = inp_num_of_ep
        self.rating = inp_rating

    def add_ep(self, Episode):
        self.episodes.append(Episode)