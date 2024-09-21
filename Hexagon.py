def print_hexagon_pattern(rows, cols):
    top_line = " ___    "
    mid_top_line = "/   \\___"
    mid_bottom_line = "\\___/   "
    last_line = "\\___/   "
    end_pattern = "/   \\"
    if cols % 2 == 0:
      a = cols // 2
    else:
      a = cols // 2 + 1
    for row in range(rows):
        if row == 0:
           for col in range(a):
                print(top_line, end='')
           print()
        else:
           for col in range(a):
                print(last_line, end='')     
           print()
           
        if row==rows-1:
          break
        
        for col in range(a):
            if col == a - 1:
                print(end_pattern, end='')
            else:
                print(mid_top_line, end='')
        print()
        skip = False
        for i in range(2, rows):
         if row == rows - i:
            skip = True
            break
        if skip:
          continue
      
        for col in range(a):
                print(mid_bottom_line, end='')
        print()
        if row < rows - 1:
            for col in range(a):
                if col == a - 1:
                    print(end_pattern, end='')
                else:
                    print(mid_top_line, end='')
            print()
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
print_hexagon_pattern(rows, cols)