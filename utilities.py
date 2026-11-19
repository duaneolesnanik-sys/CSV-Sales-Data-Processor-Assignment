
def validate_sale(sale):
    """Returns bool of if a sale is valid"""
    return ("" not in sale.values()) and sale["Qty"].isdigit() and int(sale["Qty"])>0 and sale["Price Total"].count(".") < 2 and sale["Price Total"].replace(".","").isdigit() and sale["Price Total"][-1] != "."

def find_error(sale):
    """Finds the error in an invslid sale"""
    if "" in sale.values():
        return "Missing " + list(sale.keys())[[ind for ind, val in enumerate(sale.values()) if val == ""][0]]
    elif not sale["Qty"].isdigit() or int(sale["Qty"])<1:
        return "Invalid Quantity"
    elif not(sale["Price Total"].count(".") < 2 and sale["Price Total"].replace(".","").isdigit() and sale["Price Total"][-1] != "."):
        return "Invalid Price Total"
    
def update_total(info, error=False, price=0):
    """Updates a given dictionary using given data"""
    if not error:
        info["Sales"] += 1
        info["Sum"] += float(price)
        info["Files"].add("sales_summary.csv")
    else:
        info["Errors"] += 1
        info["Files"].add("errors.log")

def console_output(info):
    """Prints the results of the programs"""
    print(f"Sales Processing Complete\n{"-"*25}\nTotal Items Sold: {info["Sales"]}\nSales Subtotal: ${info["Sum"]:.2f}\nInvalid Records: {info["Errors"]}\nFiles Created: {", ".join(info["Files"])}")

