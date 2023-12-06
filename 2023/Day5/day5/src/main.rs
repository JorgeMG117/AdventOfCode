use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;


//50 98 2
//52 50 48
//79 -> 81
//
//start = 98
//end = 99
//transform = 50 - 98 = -48
//
//
//39 0 15
//10 -> 49
//start = 0
//end = 15
//transform = 39 - 0 = 39

// Data types to store the information in the file
struct Description {
    start : u64,
    end : u64,
    transform : i64,
}

//Map is a list of descriptions
struct Map {
    descriptions: Vec<Description>,
}



fn process_file(reader: io::BufReader<File>) -> io::Result<()> {
    // Create a list of maps
    let mut maps: Vec<Map> = Vec::new();
    let mut index: usize = 0;

    // Vector to store the seeds
    let mut seeds: Vec<u64> = Vec::new();

    for line in reader.lines() {
        let line = line?;
        if line.trim().is_empty() {
            continue;
        }
        // Split the line into words
        let words: Vec<&str> = line.split_whitespace().collect();

        //println!("Line: {}", line);

        // Check the first word to determine the type of data
        match words[0] {
            "seeds:" => {
                // Process seeds data
                for seed in words[1..].iter() {
                    seeds.push(seed.parse().unwrap());
                    //println!("Seed: {}", seed);
                }
            }
            "seed-to-soil" => {
                // Process seed-to-soil map data
                maps.push(Map { descriptions: Vec::new() });
            }
            "soil-to-fertilizer" => {
                // Process soil-to-fertilizer map data
                maps.push(Map { descriptions: Vec::new() });
                index += 1;
            }
            "fertilizer-to-water" => {
                // Process fertilizer-to-water map data
                maps.push(Map { descriptions: Vec::new() });
                index += 1;
            }
            "water-to-light" => {
                // Process water-to-light map data
                maps.push(Map { descriptions: Vec::new() });
                index += 1;
            }
            "light-to-temperature" => {
                // Process light-to-temperature map data
                maps.push(Map { descriptions: Vec::new() });
                index += 1;
            }
            "temperature-to-humidity" => {
                // Process temperature-to-humidity map data
                maps.push(Map { descriptions: Vec::new() });
                index += 1;
            }
            "humidity-to-location" => {
                // Process humidity-to-location map data
                maps.push(Map { descriptions: Vec::new() });
                index += 1;
            }
            _ => {
                // Handle unknown lines or do nothing
                //
                // Read the following lines to get map descriptions
                let description_info: Vec<u64> = line
                    .split_whitespace()
                    .map(|s| s.parse().unwrap())
                    .collect();
                let description = Description {
                    start: description_info[1],
                    end: description_info[1] + description_info[2] - 1,
                    transform: description_info[0] as i64 - description_info[1] as i64,
                };

                maps[index].descriptions.push(description);
            }
        }
    }
    //Print the seeds
    /*
    println!("Seeds: {:?}", seeds);
    //Print maps using a loop
    for map in maps.iter() {
        for description in map.descriptions.iter() {
            println!("Start: {}, End: {}, Transform: {}", description.start, description.end, description.transform);
        }
    }
    */

    let mut min_value: u64 = 0;
    for seed in seeds.iter() {
        let mut value = *seed;
        for map in maps.iter() {
            for description in map.descriptions.iter() {
                if value >= description.start && value <= description.end {
                    value = (value as i64 + description.transform) as u64;
                    break;
                }
            }
        }
        if min_value == 0 || value < min_value {
            min_value = value;
        }

        println!("Seed: {}, Value: {}", seed, value);
    }
    println!("Min Value: {}", min_value);
    Ok(())
}


fn main() -> io::Result<()> {
    // Read firts line of the file and store in a list the seeds values
    
    // I want to have a list of maps
    // Each map gives the transformation to apply to the next map


    // Run each seed value through the maps safe the lowest value

    let path = Path::new("input.txt");
    let file = File::open(&path)?;

    // Read the file line by line
    let reader = io::BufReader::new(file);
    process_file(reader)?;

    Ok(())

}
