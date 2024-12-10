// Header file for input output functions
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <array>
#include <vector>
#include <tuple>
#include <unordered_set>
#include <unordered_map>

// main() function: where the execution of
// C++ program begins
bool test_outside_grid(uint16_t x_pos, uint16_t y_pos, size_t width, size_t height){

    return x_pos >= width || y_pos >= height;
}

struct hash_tuple { 
  
    template <class T1, class T2> 
  
    size_t operator()( 
        const std::tuple<T1, T2>& x) 
        const
    { 
        return std::get<0>(x)*53UL+std::get<1>(x); 
    } 
}; 

std::unordered_map<char, std::tuple<int64_t, int64_t>> directions=
{
    {'N', {-1, 0}},
    {'E', {0,1}},
    {'S', {1, 0}},
    {'W', {0, -1}}
};


std::unordered_set<std::tuple<uint64_t, uint64_t>, hash_tuple> go_uphill(uint16_t x_pos, uint16_t y_pos, char depth, std::string& path,  size_t width, size_t height,const std::vector<std::string>& input_lines){
    std::unordered_set<std::tuple<uint64_t, uint64_t>, hash_tuple> partial_tracks{} ;
    for (const auto& [cardinal, offsets] : directions){
        int16_t new_x = x_pos + std::get<0>(offsets);
        int16_t new_y = y_pos + std::get<1>(offsets);
        if(!test_outside_grid(new_x, new_y, width, height)){
            char entry = input_lines[new_x][new_y];
            if(depth == entry){
                if(depth == '9'){
                    partial_tracks.insert({new_x, new_y});
                } else{
                    path.push_back(cardinal);
                    partial_tracks.merge(go_uphill(new_x, new_y, depth+1, path, width, height, input_lines));
                }
            }
        }
    }
    return partial_tracks;
}

int main() {
  
    // This statement prints "Hello World"
    std::cout << "Hello World\n";
    std::ifstream t("input.txt");
    std::stringstream buffer;
    buffer << t.rdbuf();
    std::string input_data = buffer.str();
    auto width = input_data.find('\r');
    // std::cout << width;
    std::vector<std::string> input_lines;
    auto height = input_data.length()/(width+2);
    // std::cout << height;
    for(auto index = 0; index < height; index++){
        input_lines.push_back(input_data.substr(index*(width+2), width));
    }
    // for(auto index = 0; index < height; index++){
        // std::cout << input_lines[index];
        // std::cout << "\n";
    // }
    std::vector<std::tuple<uint64_t, uint64_t>> trailheads;
    for(auto row = 0; row<height;row++){
        for(auto column = 0; column<width;column++){
            if(input_lines[row][column]=='0'){
                trailheads.push_back({row, column});
                // std::cout << row << ' ' << column << '\n';

            }
        }
    }
    uint16_t num_of_trailheads = trailheads.size();
    uint16_t accumulator = 0;
    for (auto index=0; index<num_of_trailheads; index++){
        uint16_t x_pos = std::get<0>(trailheads[index]);
        uint16_t y_pos = std::get<1>(trailheads[index]);
        std::string path {};
        auto tracks = go_uphill(x_pos, y_pos, '1', path, width, height, input_lines);
        accumulator += tracks.size();
    }
    std::cout << "Trails:" << accumulator << '\n';
    std::cout << "Goodbye";
    return 0;
}