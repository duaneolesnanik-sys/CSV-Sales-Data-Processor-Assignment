import csv 
import utilities as u

def main():
    info = {"Sales": 0, "Sum": 0, "Errors": 0, "Files": set()}
    with open("sales.csv", "r", newline="") as file:
        for num, sale in sorted(tuple(enumerate(csv.DictReader(file))),key = lambda x: (x[1]["Item"][0]) if x[1]["Item"] != "" else "a"):
            valid = u.validate_sale(sale)
            with open(("sales_summary.csv" if valid else "errors.log"), "a", newline = "") as file:
                csv.writer(file).writerow(sale.values()) if valid else file.write(f"Line {num} | {u.find_error(sale)} | {sale}\n")
            u.update_total(info, error=not valid, price=sale["Price Total"])
    u.console_output(info)

if __name__ == "__main__":
    main()
