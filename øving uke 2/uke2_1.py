import datetime as date

# Det ser ikke ut til at lengden på strengen har mye å si for tiden det tar å sammenligne to strenger,
# ved hjelp av ==
# Den alternative string-looper-funksjonen løper gjennom to strenger og sammenligner hver char.
# Loopen avbrytes hvis en char er ulik

def compare_str(x, y):
    print("String comparer:")
    start_time = date.datetime.now()
    x == y
    end_time = date.datetime.now()
    used_time = end_time - start_time
    print(used_time)


def string_looper(x, y):
    print("String looper:")
    start_time = date.datetime.now()
    for a, b in zip(x, y):
        print(a, b)
        if a != b:
            print("Break")
            break
    end_time = date.datetime.now()
    used_time = end_time - start_time
    print(used_time)


lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac tortor malesuada, tristique velit vel, ullamcorper purus. Sed dolor sapien."
ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac tortor malesuada, tristique velit vel, ullamcorper purus. Sed dolor sapien."
long_lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus vel iaculis eros. 
Proin aliquet, lorem nec porttitor euismod, neque massa dapibus magna, et vulputate enim felis in nulla. Integer in lacinia arcu. 
Phasellus quis vulputate tortor. Aliquam fermentum venenatis magna, eget vestibulum quam auctor nec. 
Etiam dictum justo tellus, vitae sagittis odio congue sit amet. Sed consequat leo non odio porttitor viverra nec ac urna. 
Morbi felis nunc, finibus quis sapien sit amet, eleifend molestie libero.
Fusce ut odio neque. Pellentesque vitae sodales mi. Ut viverra feugiat dui non rutrum. Phasellus feugiat nibh vel nisl porttitor accumsan. Donec bibendum, dolor."""
long_lorem2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus vel iaculis eros. Proin aliquet, lorem nec porttitor euismod, neque massa dapibus magna, et vulputate enim felis in nulla. Integer in lacinia arcu. Phasellus quis vulputate tortor. Aliquam fermentum venenatis magna, eget vestibulum quam auctor nec. Etiam dictum justo tellus, vitae sagittis odio congue sit amet. Sed consequat leo non odio porttitor viverra nec ac urna. Morbi felis nunc, finibus quis sapien sit amet, eleifend molestie libero. Fusce ut odio neque. Pellentesque vitae sodales mi. Ut viverra feugiat dui non rutrum. Phasellus feugiat nibh vel nisl porttitor accumsan. Donec bibendum, dolor."
complex_string = "123@123124lkø@asdk98##"
complex_string2 = "123@123124lkø@asdk98"

compare_str(lorem, ipsum)
compare_str(complex_string, complex_string2)
compare_str(long_lorem, lorem)
compare_str(long_lorem, long_lorem2)
compare_str("hello", "Hello")
compare_str("Hello", "Hella")

string_looper(lorem, ipsum)
string_looper(complex_string, complex_string2)
string_looper(long_lorem, lorem)
string_looper(long_lorem, long_lorem2)
string_looper("hello", "Hello")
string_looper("Hello", "Hella")