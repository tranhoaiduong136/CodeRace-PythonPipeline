import atheris
with atheris.instrument_imports():
  import sys

# #Test 
# def test_boschcoderace_sum_of_list_number():
#     src.applications.boschcoderace_sum_of_list_number(9)
#     src.applications.boschcoderace_sum_of_list_number(10)
#     src.applications.boschcoderace_sum_of_list_number(1)
#     src.applications.boschcoderace_sum_of_list_number(2)
#     src.applications.boschcoderace_sum_of_list_number(3)
#     src.applications.boschcoderace_sum_of_list_number(4)
#     src.applications.boschcoderace_sum_of_list_number(5.2)
#     src.applications.boschcoderace_sum_of_list_number(4)


# def test_boschcoderace_validate_ip():
#     ip = src.applications.boschcoderace_validate_ip("9.1.2.3")

@atheris.instrument_func
def my_function(app,lib):
  print("Instrumented library")

if __name__ == '__main__':
    # atheris.Setup(sys.argv, test_boschcoderace_sum_of_list_number)
    # atheris.Fuzz()
    atheris.instrument_all()
