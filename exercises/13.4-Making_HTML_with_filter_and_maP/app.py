all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

# Your code here

def filter_colors(data):
    return data["sexy"] == True

def generate_li(colour):
    return "<li>" + colour["label"] + "</li>"

filtered_list = list(map(generate_li, filter(filter_colors, all_colors)))

print(filtered_list)
