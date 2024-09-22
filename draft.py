#-----------------------------------------------

def load_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
    except FileNotFoundError:
        return {"movies": [], "tvseries": []}

    data = {"movies": [], "tvseries": []}
    
    for movie in root.find('movies'):
        movie_data = {}
        for child in movie:
            movie_data[child.tag] = child.text
        data['movies'].append(movie_data)

    for series in root.find('tvseries'):
        series_data = {}
        for child in series:
            series_data[child.tag] = child.text
        data['tvseries'].append(series_data)

    return data

def add_movie(data, movie):
    data['movies'].append(movie.to_dict())

def add_tvseries(data, tvseries):
    data['tvseries'].append(tvseries.to_dict())
