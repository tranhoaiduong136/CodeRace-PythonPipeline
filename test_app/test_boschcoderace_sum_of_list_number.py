import sys
import atheris
with atheris.instrument_imports():
    from src.applications import boschcoderace_sum_of_list_number

@atheris.instrument_func  # Instrument 
def test_boschcoderace_sum_of_list_number():
    boschcoderace_sum_of_list_number(9)
    boschcoderace_sum_of_list_number(10)
    boschcoderace_sum_of_list_number(1)
    boschcoderace_sum_of_list_number(2)
    boschcoderace_sum_of_list_number(3)
    boschcoderace_sum_of_list_number(4)
    boschcoderace_sum_of_list_number(5.2)
    boschcoderace_sum_of_list_number(4)

@atheris.instrument_func
def my_function(boschcoderace_sum_of_list_number):
  print("Instrumented library")

if __name__ == '__main__':
    # atheris.Setup(sys.argv, test_boschcoderace_sum_of_list_number)
    # atheris.Fuzz()
    # atheris.instrument_func(boschcoderace_sum_of_list_number)
    test_boschcoderace_sum_of_list_number()
