
# Grid = Dict{Tuple{Integer, Integer}, String}
Grid = Dict()
for row in -1:71
   for column in -1:71
      if (row == -1) | (row == 71) | (column == -1) | (column == 71)
         Grid[(string(row), string(column))] = "#"
      else
         Grid[(string(row), string(column))] = "."
      end
   end
end
open("input.txt") do f
   line = 0 
      while line < 1024     
      s = readline(f)          
      line += 1
      x_val, y_val = split(s, ",")
      Grid[(x_val, y_val)] = "#" 
   end
end
   
Directions = Dict()
Directions["N"] = (0,-1)
Directions["S"] = (0,1)
Directions["W"] = (-1,0)
Directions["E"] = (1,0)

for direction in keys(Directions)
   println(Directions[direction][2])
end

new_cells = Array{Tuple{Int, Int}}(undef, 0)

push!(new_cells, Tuple([0,0]))
end_not_found = true
println(new_cells)
rec_depth = 0
println(Grid[("0", "5")])
println(Grid[("-1", "5")])
println(Grid[("1", "5")])
println(Grid[("0", "4")])
println(Grid[("0", "6")])
# println(Directions["N"] == (0,0))
while end_not_found
   fresh_cells = Array{Tuple{Int, Int}}(undef, 0)
   global rec_depth +=1
   for cell in new_cells
      for directionals in keys(Directions)
         new_x = Directions[directionals][1] + cell[1]
         new_y = Directions[directionals][2] + cell[2]   
         if Grid[(string(new_x), string(new_y))] == "."
            push!(fresh_cells, Tuple([new_x,new_y]))
            Grid[(string(new_x), string(new_y))] = string(rec_depth)
            if (new_x, new_y) == (70, 70)
               global end_not_found = false
            end
         end
      end
   end
   global new_cells = fresh_cells
end

print(Grid[("70", "70")])