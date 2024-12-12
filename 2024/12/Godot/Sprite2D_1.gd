extends Sprite2D

const other_path = "user://save_game.dat"
#func load():
	#var file = File.new()
	#file.open("user://mytext.txt", File.READ)
	#var content = file.get_as_text()
	#file.close()
	#return content
	
func load_from_file(path):
	var file = FileAccess.open(path, FileAccess.READ)
	var content = file.get_as_text()
	return content

func test_outside_grid(x_pos, y_pos, height, width):
	return x_pos < 0 or x_pos > width-1 or y_pos < 0 or y_pos > height -1

func add_to_dict(entry, dict):
	if entry not in dict.keys():
		dict[entry] = 1
	else:
		dict[entry] +=1
	return dict

func explore_region(row, column, input_lines, width, height):
	var entry = input_lines[row][column]
	var belonging = [[column, row]]
	var new_plots = [[column, row]]
	var new_plots_found = true
	while new_plots_found:
		var newer_plots = []
		for plot in new_plots:
			var x_pos = plot[0]
			var y_pos = plot[1]
			# north
			if y_pos != 0:
				if input_lines[y_pos - 1][x_pos] == entry:
					var north_plot = [x_pos, y_pos -1]
					if north_plot not in belonging:
						belonging.append(north_plot)
						newer_plots.append(north_plot)
			# east
			if x_pos != width - 1:
				if input_lines[y_pos][x_pos + 1] == entry:
					var east_plot = [x_pos + 1, y_pos]
					if east_plot not in belonging:
						belonging.append(east_plot)
						newer_plots.append(east_plot)
			# south 
			if y_pos !=  height - 1:
				if input_lines[y_pos + 1][x_pos] == entry:
					var south_plot = [x_pos, y_pos +1]
					if south_plot not in belonging:
						belonging.append(south_plot)
						newer_plots.append(south_plot)
			# west
			if x_pos != 0:
				if input_lines[y_pos][x_pos - 1] == entry:
					var west_plot = [x_pos - 1, y_pos]
					if west_plot not in belonging:
						belonging.append(west_plot)
						newer_plots.append(west_plot)
		if newer_plots == []:
			new_plots_found = false
		new_plots = newer_plots
	return belonging

func _init():
	const path = "C:\\Code\\GithubRepos\\AdventOfCode\\2024\\12\\input.txt"
	var input_data = load_from_file(path)
	var input_lines = Array(input_data.split("\n"))
	input_lines.pop_back()
	print(len(input_lines))
	
	var width = len(input_lines[0]) - 1
	var height = len(input_lines)
	
	var my_dict = {}
	my_dict[[1,2]] = "3"
	#print(explore_region(0,0,input_lines,width,height))
	
	var belonging_region = {}
	
	for row in range(height):
		for column in range(width):
			if [column, row] not in belonging_region.keys():
				var current_new_region = explore_region(row, column, input_lines, width, height)
				var region_value = current_new_region[0]
				for region in current_new_region:
					belonging_region[region] = region_value
	
	var plants_area = {}
	var plants_perimeter = {}
	
	for row in range(height):
		for column in range(width):
			var entry = belonging_region[[column, row]]
			add_to_dict(entry, plants_area)
			if row == 0:
				add_to_dict(entry, plants_perimeter)
			if column == 0 :
				add_to_dict(entry, plants_perimeter)
			if row == height-1:
				add_to_dict(entry, plants_perimeter)
			else:
				var south_neighbour = belonging_region[[column, row+1]]
				if entry != south_neighbour:
					add_to_dict(entry, plants_perimeter)
					add_to_dict(south_neighbour, plants_perimeter)
			if column == width - 1:
				add_to_dict(entry, plants_perimeter)
			else:
				var east_neighbour = belonging_region[[column+1, row]]
				if entry != east_neighbour:
					add_to_dict(entry, plants_perimeter)
					add_to_dict(east_neighbour, plants_perimeter)
	var accumulator = 0
	#print(plants_area.keys())
	

	for plant in plants_area.keys():
		print(plant, " ",plants_perimeter[plant]* plants_area[plant])
		accumulator += plants_perimeter[plant]* plants_area[plant]
	print(accumulator)
	
	
