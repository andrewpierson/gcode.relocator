import sys
import re


def main():
    print("Processing inputs...")
    input_filename = "input.gcode"
    output_filename = "output.gcode"
    delta_x = 0
    delta_y = 0
    if len(sys.argv) > 1:
        input_filename = sys.argv[1]
    if len(sys.argv) > 2:
        output_filename = sys.argv[2]
    if len(sys.argv) > 3:
        delta_x = float(sys.argv[3])
    if len(sys.argv) > 4:
        delta_y = float(sys.argv[4])
    print("in={0} out={1} dx={2} dy={3}".format(
        input_filename, output_filename, str(delta_x), str(delta_y)))
    output_file = open(output_filename, 'w')
    with open(input_filename, 'r') as f:
        cull_prog = re.compile('G0 ')
        extract_prog = re.compile('^G0 X([0-9\.]*) Y([0-9\.]*) F0$')
        output_format = "G0 X{0:5.2f} Y{1:5.2f} F0\n"
        for line in f:
            m = cull_prog.match(line)
            if None == m:
                output_file.write(line)
                continue
            m = extract_prog.search(line)
            x = float(m.group(1)) + delta_x
            y = float(m.group(2)) + delta_y
            relocated_line = output_format.format(x, y)
            print("Replacing: " + line.strip())
            print("     with: " + relocated_line.strip())
            output_file.write(relocated_line)


if __name__ == "__main__":
    main()
