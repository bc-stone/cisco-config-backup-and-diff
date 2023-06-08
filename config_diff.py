import difflib
import sys

file_1 = input("Enter a reference file: ")
file_2 = input("Enter a file to compare: ")
diff_file = input("Enter a filename for the HTML diff: ")


with open(file_1) as f:
    reference_file = f.readlines()

with open(file_2) as f:
    file_to_test = f.readlines()

compare_config = difflib.HtmlDiff(wrapcolumn=95).make_file(
    fromlines=reference_file,
    tolines=file_to_test,
    fromdesc=f"{file_1}",
    todesc=f"{file_2}",
)

with open(diff_file, "w") as f:
    f.write(compare_config)

choice = input(f"Open {diff_file} in the default browser? (Y|N): ")

match choice.lower():
    case "y":
        import webbrowser

        webbrowser.open(diff_file)
    case "n":
        print("Exiting...")
        sys.exit(0)
    case _:
        print("Invalid input...  Exiting...")
        sys.exit(1)
