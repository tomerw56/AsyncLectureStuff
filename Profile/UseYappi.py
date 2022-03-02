import yappi
import TestClass

example=TestClass.TesClass(heavy_second_function=False)
yappi.set_clock_type("cpu") # Use set_clock_type("wall") for wall time
yappi.start()
example.RunMe()
yappi.get_func_stats().print_all()
yappi.get_thread_stats().print_all()