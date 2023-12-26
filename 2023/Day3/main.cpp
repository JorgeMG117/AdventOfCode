#include <iostream>
#include <fstream>

using namespace std;


int read_number(ifstream& in, int& position, char c, int line_length) {
    line_length = line_length + 1;
    int number = 0;
    bool valid = false;
    do {
        //cout << "Char: " << c << endl;
        //cout << "Position: " << position << endl;
        //cout << "Position 2: " << in.tellg() << endl;
        
        //Check left
        if(position % line_length != 0) {
            char left;
            in.seekg (position - 1, in.beg);
            in.get(left);

            if (!isdigit(left) && left != '.') {
                cout << "Left: " << left << endl;
                valid = true;
            }
        }

        //Check right
        if(position % line_length != line_length - 1) {
            char right;
            in.seekg (position + 1, in.beg);
            in.get(right);

            if (!isdigit(right) && right != '.') {
                cout << "Right: " << right << endl;
                valid = true;
            }
        }

        //Check up
        if(position > line_length) {
            char up;
            in.seekg (position - line_length, in.beg);
            in.get(up);

            if (!isdigit(up) && up != '.') {
                cout << "Up: " << up << endl;
                valid = true;
            }
        }

        //Check down
        if(position < line_length * line_length - line_length) {
            char down;
            in.seekg (position + line_length, in.beg);
            in.get(down);

            if (!isdigit(down) && down != '.') {
                cout << "Down: " << down << endl;
                valid = true;
            }
        }

        //Check top left diagonal
        if(position > line_length && position % line_length != 0) {
            char top_left;
            in.seekg (position - line_length - 1, in.beg);
            in.get(top_left);

            if (!isdigit(top_left) && top_left != '.') {
                cout << "Top left: " << top_left << endl;
                valid = true;
            }
        }

        //Check top right diagonal
        if(position > line_length && position % line_length != line_length - 1) {
            char top_right;
            in.seekg (position - line_length + 1, in.beg);
            in.get(top_right);

            if (!isdigit(top_right) && top_right != '.') {
                cout << "Top right: " << top_right << endl;
                valid = true;
            }
        }

        //Check bottom left diagonal
        if(position < line_length * line_length - line_length && position % line_length != 0) {
            char bottom_left;
            in.seekg (position + line_length - 1, in.beg);
            in.get(bottom_left);

            if (!isdigit(bottom_left) && bottom_left != '.') {
                cout << "Bottom left: " << bottom_left << endl;
                valid = true;
            }
        }

        //Check bottom right diagonal
        if(position < line_length * line_length - line_length && position % line_length != line_length - 1) {
            char bottom_right;
            in.seekg (position + line_length + 1, in.beg);
            in.get(bottom_right);

            if (!isdigit(bottom_right) && bottom_right != '.') {
                cout << "Bottom right: " << bottom_right << endl;
                valid = true;
            }
        }

        number = number * 10 + (c - '0');
        position++;
        in.seekg (position, in.beg);
    } while (in.get(c) && isdigit(c));

    //cout << "Number: " << number << endl;

    if(valid) {
        cout << "Valid number: " << number << endl;
        return number;
    }
    return 0;
}


int main(int argc, char** argv) {
    int total_sum = 0;

    // Read file param
    string file;
    if (argc > 1) {
        file = argv[1];
    }

    // Read file
    ifstream in(file);
    if (!in) {
        cout << "Cannot open file.\n";
        return 1;
    }

    //Get line length
    string line;
    getline(in, line);

    cout << "Line lenght: " << line.length() << endl;

    in.seekg (0, in.beg);

    //Read char by char
    char c;
    int line_length = line.length();
    int position = 0;
    while (in.get(c)) {
        if(isdigit(c)) {
            total_sum += read_number(in, position, c, line_length);
        }
        position++;
    }

    cout << "Total sum: " << total_sum << endl;

    return 0;
}

