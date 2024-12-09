// use ferris_says::say;
// use std::io::{stdout, BufWriter};
use std::fs;

fn get_id(index: u16) -> u16 {
    if index % 2 == 0 {
        return index/2;
    } else {
        panic!{"BAD PARITY FOR ID"}
    }
}

fn get_next_backwalker_skips(backwalker: u16, input_lines: String) -> u16 {
    if backwalker % 2 == 0{
        let backwalker_index: usize = usize::from(backwalker);
        let skips_as_str: &str = &input_lines[backwalker_index-1..backwalker_index];
        let return_value: u16 = skips_as_str.parse().unwrap();
        return return_value
    } else {
        panic!{"BAD PARITY BACKWALKER"}
    }
}

fn get_next_backwalker(backwalker: u16, input_lines: String) -> Vec<String>{
    if backwalker % 2 == 0 {
        let backwalker_index: usize = usize::from(backwalker);
        let multiplicity: u8 = input_lines[backwalker_index..backwalker_index+1].parse().unwrap();
        let mut buffer: Vec<String> = vec![];
        let current_id: u16 = get_id(backwalker);
        for n in 0..multiplicity {
            buffer.insert(n.into(), current_id.to_string());
        }
        return buffer
    } else {
        panic!{"BAD PARITY BACKWALKER"}
    }
}

fn get_next_block_length(index: u16, input_lines:String)-> u16{
    let index: usize = usize::from(index);
    return input_lines[index..index+1].parse().unwrap()
}

fn main() {
    let filename: &str = "input_small.txt";
    let data_terminated = fs::read_to_string(filename).expect("Can't read lol");
    let final_index = data_terminated.chars().count() - 2;
    println!("{}", final_index);
    let input_lines: &str = &data_terminated[0..final_index];
    let input_bytes: &[u8] = input_lines.as_bytes();
    // Two end characters, need to be removed "/" and "n" possibly
    let total_length: usize = input_lines.chars().count();
    let total_length_u16 = u16::try_from(total_length).ok().unwrap();
    println!("{}", total_length);
    println!("{}", input_lines);
    println!("{}", get_id(12));
    let checksum: u128 = 0;
    let backwalker: u16 = total_length_u16 - 1;
    let mut backwalker_buffer: Vec<String> = vec![];
    let map_position: i16 = -1;
    let current_block_length: u8 = 0;
    let block_position: u32 = 0;
    let mut backwalker_block: i16 = -1;
    // for index in 0..total_length_u16{
    //     let mut index_usize: usize = usize::from(index);
    //     backwalker_block += input_bytes[index];
    // }
    
    // let stdout = stdout();
    // let message = String::from("Hello fellow Rustaceans!");
    // let width = message.chars().count();
    
    // let mut writer = BufWriter::new(stdout.lock());
    // say(&message, width, &mut writer).unwrap();
    // println!("Hello, world!");

}
