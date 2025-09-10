

MONTH_NAMES = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]


DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True if year is a leap year (Gregorian rules)."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in given month (1-12)."""
    if month == 2:
        return 29 if is_leap(year) else 28
    return DAYS_IN_MONTH[month - 1]

def weekday(year, month, day):
    """
    Return weekday index for given date:
      0 = Sunday, 1 = Monday, ..., 6 = Saturday
    Uses Sakamoto's algorithm (all integer ops).
    """
    y = year
    m = month
    if m < 3:
        y -= 1
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    w = (y + y//4 - y//100 + y//400 + t[m-1] + day) % 7
    return w

def format_month(year, month, start_on_monday=False):
    """
    Return string for one month calendar.
    start_on_monday: if True, weeks start Monday; otherwise Sunday.
    """
    title = f"{MONTH_NAMES[month-1]} {year}"
    width = 20  
    header = title.center(width) + "\n"
    if start_on_monday:
        days_header = "Mo Tu We Th Fr Sa Su\n"
        
 0=Sun..6=Sat -> shift so Monday=0
        shift = lambda w: (w - 1) % 7
    else:
        days_header = "Su Mo Tu We Th Fr Sa\n"
        shift = lambda w: w

    first_w = shift(weekday(year, month, 1))
    days = days_in_month(year, month)

   
    rows = []
    row = ["  "] * 7
    
    for i in range(first_w):
        row[i] = "  "
    cur = 1
    i = first_w
    while cur <= days:
        row[i] = f"{cur:2d}"
        cur += 1
        i += 1
        if i == 7:
            rows.append(" ".join(row))
            row = ["  "] * 7
            i = 0
    if any(cell.strip() for cell in row):
        rows.append(" ".join(row))

    body = "\n".join(rows)
    return header + days_header + body + "\n"

def print_month(year, month, start_on_monday=False):
    print(format_month(year, month, start_on_monday))

def print_year(year, start_on_monday=False):
   
  calendars
    for quarter_start in (1, 4, 7, 10):
        
        titles = []
        for m in range(quarter_start, quarter_start + 3):
            titles.append(f"{MONTH_NAMES[m-1]} {year}".center(20))
        print("  ".join(titles))
        
        if start_on_monday:
            hdr = "Mo Tu We Th Fr Sa Su"
        else:
            hdr = "Su Mo Tu We Th Fr Sa"
        print(f"{hdr}  {hdr}  {hdr}")

        
        month_lines = []
        max_lines = 0
        for m in range(quarter_start, quarter_start + 3):
            lines = format_month(year, m, start_on_monday).splitlines()[2:] 

            month_lines.append(lines)
            if len(lines) > max_lines:
                max_lines = len(lines)

        
        for r in range(max_lines):
            parts = []
            for lines in month_lines:
                if r < len(lines):
                    parts.append(lines[r])
                else:
                    parts.append(" " * 20) 
            print("  ".join(parts))
        print() 


if __name__ == "__main__":
    print_month(2025, 9)        
 (default, weeks starting Sunday)
